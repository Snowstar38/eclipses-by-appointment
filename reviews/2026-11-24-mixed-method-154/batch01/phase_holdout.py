"""Measure offsets from a proposed trial ephemeris in separate observing eras."""
import argparse
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument("batch_dir",type=Path)
p.add_argument("tic")
p.add_argument("period",type=float)
p.add_argument("epoch",type=float)
p.add_argument("width",type=float)
p.add_argument("split",type=float)
p.add_argument("--exclude",type=int,action="append",default=[])
p.add_argument("--fits-dir",type=Path,default=(HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")/"sky/data/qlp-sb-p20-60")
p.add_argument("--mask",type=Path,default=(HERE.parent/"inputs/exposure-guard.csv" if (HERE.parent/"inputs/exposure-guard.csv").is_file() else HERE.parents[2]/"sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"))
a=p.parse_args()


def read(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))


masked={}
for r in read(a.mask):
    if r["screen_flag"].lower()=="true" and r["pipeline"]=="QLP":
        key=(int(r["sector"]),int(r["camera"]),r["flux_column"])
        masked.setdefault(key,set()).add(int(r["cadenceno"]))

records=[]
fits_windows=[]
for r in read(a.batch_dir/"files.csv"):
    if r["tic"]!=a.tic or int(r["sector"]) in a.exclude:
        continue
    with fits.open(a.fits_dir/r["file"]) as h:
        z=h[1].data
        t=z["TIME"]
        dt=float(r["cadence"])
        camera_key=(int(r["sector"]),int(r["camera"]),r["corrected_column"])
        good=(z["QUALITY"]==0)&np.isfinite(t)
        good &= ~np.isin(z["CADENCENO"],list(masked.get(camera_key,())))
        cycle_lo=int(np.ceil((float(r["start"])-a.epoch)/a.period))
        cycle_hi=int(np.floor((float(r["end"])-a.epoch)/a.period))
        for cycle in range(cycle_lo,cycle_hi+1):
            c=a.epoch+cycle*a.period
            take=good & (abs(t-c)<5*a.width)
            if not take.any():
                continue
            flux=np.stack([np.asarray(z[col][take],float) for col in ("SAP_FLUX",r["corrected_column"])])
            x=np.asarray(t[take]-c,float)
            ok=np.isfinite(flux).all(axis=0)
            fits_windows.append((c,dt,x[ok],flux[:,ok]))

offsets=np.linspace(-3*a.width,3*a.width,61)
for shift in offsets:
    groups={"early":[],"late":[]}
    for c,dt,x,flux in fits_windows:
        d=x-shift
        core=abs(d)<=a.width/2
        left=(d>=-1.75*a.width)&(d<-.65*a.width)
        right=(d>.65*a.width)&(d<=1.75*a.width)
        counts=[m.sum() for m in (core,left,right)]
        if min(counts)<2 or min(counts)*dt/a.width<.55:
            continue
        t0,t1=np.median(d[left]),np.median(d[right])
        f0,f1=np.median(flux[:,left],axis=1),np.median(flux[:,right],axis=1)
        baseline=f0[:,None]+(d[core]-t0)*(f1-f0)[:,None]/(t1-t0)
        depths=1000*np.median(1-flux[:,core]/baseline,axis=1)
        groups["early" if c<a.split else "late"].append(depths)
    for era,depth in groups.items():
        record=dict(tic=a.tic,era=era,offset_d=shift,n=len(depth),median_raw=np.nan,median_corrected=np.nan,n_positive_both=0)
        if depth:
            record["median_raw"],record["median_corrected"]=np.median(depth,axis=0)
            record["n_positive_both"]=int(np.sum(np.min(depth,axis=1)>0))
        records.append(record)

out=a.batch_dir/a.tic
(out/"plots").mkdir(parents=True,exist_ok=True)
with (out/"phase-holdout.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,records[0].keys())
    w.writeheader()
    w.writerows(records)

fig,axs=plt.subplots(2,1,sharex=True,figsize=(9,5.4),layout="constrained")
for ax,era in zip(axs,("early","late")):
    group=[r for r in records if r["era"]==era]
    for key in ("median_raw","median_corrected"):
        ax.plot(offsets,[r[key] for r in group],label=key.replace("median_",""))
    ax.axvline(0,c="gray",lw=.8)
    ax.set_ylabel(f"{era} depth (ppt)")
    ax.legend(loc="lower right")
    ax2=ax.twinx()
    ax2.plot(offsets,[r["n"] for r in group],c="gray",ls=":",alpha=.55)
    ax2.set_ylabel("Measured")
axs[-1].set_xlabel("Trial epoch offset (d)")
fig.suptitle(f"TIC {a.tic} | P={a.period:.8f} d | split at BTJD {a.split:.2f} | excluded S{a.exclude}")
fig.savefig(out/"plots"/"phase-holdout.png",dpi=130)
