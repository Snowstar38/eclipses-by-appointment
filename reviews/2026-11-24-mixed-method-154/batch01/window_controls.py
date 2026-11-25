"""Compare alternating event windows in original QLP FITS data."""
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
p.add_argument("--fits-dir",type=Path,default=(HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")/"sky/data/qlp-sb-p20-60")
p.add_argument("--mask",type=Path,default=(HERE.parent/"inputs/exposure-guard.csv" if (HERE.parent/"inputs/exposure-guard.csv").is_file() else HERE.parents[2]/"sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv"))
a=p.parse_args()
flagged={}
with a.mask.open(encoding="utf-8-sig",newline="") as f:
    for r in csv.DictReader(f):
        if r["screen_flag"].lower()=="true" and r["pipeline"]=="QLP":
            key=(r["sector"],r["camera"],r["flux_column"])
            flagged.setdefault(key,set()).add(int(r["cadenceno"]))
period=a.period
epoch=a.epoch
width=a.width
radius=max(.22,2.5*width)
target=a.batch_dir/a.tic
(target/"plots").mkdir(parents=True,exist_ok=True)
out=[]
profiles={}
with (a.batch_dir/"files.csv").open(encoding="utf-8-sig",newline="") as f:
    files=[r for r in csv.DictReader(f) if r["tic"]==a.tic]
for r in files:
    if not (a.fits_dir/r["file"]).is_file():
        continue
    with fits.open(a.fits_dir/r["file"]) as h:
        z=h[1].data
        t=z["TIME"]
        dt=float(r["cadence"])
        for subcycle in range(int(np.ceil(2*(float(r["start"])-epoch)/period)),
                              int(np.floor(2*(float(r["end"])-epoch)/period))+1):
            time=epoch+subcycle*period/2
            ix=abs(t-time)<radius
            x=np.asarray(t[ix]-time,float)
            quality=z["QUALITY"][ix]==0
            camera_key=(r["sector"],r["camera"],r["corrected_column"])
            bad=np.isin(z["CADENCENO"][ix],list(flagged.get(camera_key,())))
            good=quality&~bad
            cols=("SAP_FLUX",r["corrected_column"],"SAP_X","SAP_Y","SAP_BKG")
            y=np.asarray([z[k][ix] for k in cols],float).T
            good &= np.isfinite(y[:,:2]).all(axis=1)
            core=abs(x)<=width/2
            before=(x>=-1.75*width)&(x<-.65*width)
            after=(x>.65*width)&(x<=1.75*width)
            counts=[np.sum(good & win) for win in (core,before,after)]
            frac=min(c*dt/size for c,size in zip(counts,(width,1.1*width,1.1*width)))
            nearest=int(z["CADENCENO"][np.nanargmin(abs(t-time))])
            row=dict(sector=r["sector"],camera=r["camera"],ccd=r["ccd"],half_period_index=subcycle,
                     center_btjd=time,cadenceno=nearest,core_quality_zero=counts[0],
                     core_quality_nonzero=int(sum(core & ~quality)),guard_masked=int(sum(core&quality&bad)),coverage=frac,support="insufficient")
            for k in cols:
                row[k+"_core_residual"]=np.nan
            if min(counts)>=2 and frac>=.55:
                row["support"]="measured"
                side=good & (before|after)
                shape=np.full_like(y,np.nan)
                for j,k in enumerate(cols):
                    usable=side & np.isfinite(y[:,j])
                    if min(sum(usable&before),sum(usable&after))<2:
                        continue
                    left,right=usable&before,usable&after
                    x0,x1=np.median(x[left]),np.median(x[right])
                    f0,f1=np.median(y[left,j]),np.median(y[right,j])
                    baseline=f0+(x-x0)*(f1-f0)/(x1-x0)
                    residual=y[:,j]-baseline
                    if j<2:
                        residual=1000*residual/baseline
                    shape[:,j]=residual
                    row[k+"_core_residual"]=float(np.nanmedian(residual[good&core]))
                profiles.setdefault(subcycle%2,[]).append((r["sector"],x[good],shape[good]))
            out.append(row)
keys=list(dict.fromkeys(k for row in out for k in row))
with (target/"refined-windows.csv").open("w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,keys)
    writer.writeheader()
    writer.writerows(out)
fig, axes=plt.subplots(2,5,figsize=(15,5.6),layout="constrained",sharex=True)
extent=max(.20,2.5*width)
edges=np.linspace(-extent,extent,41)
for parity,axrow in enumerate(axes):
    for k,ax in enumerate(axrow):
        if parity not in profiles:
            continue
        for name,x,profile in profiles[parity]:
            ax.scatter(x,profile[:,k],s=3,alpha=.14,color=f"C{int(name)%10}")
        x=np.concatenate([x for _,x,y in profiles[parity]])
        y=np.concatenate([y[:,k] for _,x,y in profiles[parity]])
        bins=np.digitize(x,edges)-1
        median=[np.nanmedian(y[bins==i]) if sum(bins==i)>2 else np.nan for i in range(len(edges)-1)]
        ax.plot((edges[1:]+edges[:-1])/2,median,color="black",lw=1)
        ax.axvspan(-width/2,width/2,alpha=.12,color="tab:orange")
        ax.set_xlim(-extent,extent)
        central=y[abs(x)<extent]
        finite=central[np.isfinite(central)]
        if finite.size:
            lo,hi=np.percentile(finite,[1,99])
            if hi>lo:
                ax.set_ylim(lo,hi)
ax=axes[0]
for panel,label in zip(ax,("Raw SAP (ppt)","Corrected (ppt)","Centroid X (px)","Centroid Y (px)","Sky background")):
    panel.set_title(label)
axes[0,0].set_ylabel("Predicted losses")
axes[1,0].set_ylabel("Interleaved half-cycles")
for ax in axes[1]:
    ax.set_xlabel("Days from prediction")
fig.suptitle(f"TIC {a.tic} | original QLP apertures folded at {period:.9f} d")
fig.savefig(target/"plots/local-control.png",dpi=145)

