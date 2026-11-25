"""Plot the independent split-sample clock from original QLP apertures."""
import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument("batch_dir",type=Path,nargs="?",default=HERE)
p.add_argument("--fits-dir",type=Path,default=(HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")/"sky/data/qlp-sb-p20-60")
p.add_argument("--clock-dir",type=Path,default=HERE.parent/"independent/trials")
p.add_argument("--mask",type=Path,default=HERE.parent/"inputs/exposure-guard.csv")
a = p.parse_args()


def read(path):
    with path.open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))


masked={}
for r in read(a.mask):
    if r["screen_flag"].lower()=="true" and r["pipeline"]=="QLP":
        k=(int(r["sector"]),int(r["camera"]),r["flux_column"])
        masked.setdefault(k,set()).add(int(r["cadenceno"]))

targets = read(a.batch_dir/"batch.csv")
files = read(a.batch_dir/"files.csv")
out = []
fig, axes = plt.subplots(len(targets),2,figsize=(12,1.53*len(targets)),layout="constrained")
for r, axs in zip(targets,axes):
    tic = r["tic"]
    j=a.clock_dir/f"{tic}.json"
    if not j.is_file():
        axs[0].set_ylabel(tic)
        axs[1].text(.5,.5,"No independent clock file",ha="center")
        continue
    candidates=json.loads(j.read_text()).get("clocks",[])
    candidates=[c for c in candidates if c["sign"]=="dip"]
    if not candidates:
        continue
    clock=max(candidates,key=lambda c:(c["test_hit_sectors"],c["test_hits"],c["train_hits"]))
    per,c,w=[clock[key] for key in ("period_d","epoch_btjd","width_d")]
    out.append(dict(tic=tic,**clock))
    for i,f in enumerate(v for v in files if v["tic"]==tic):
        path=a.fits_dir/f["file"]
        if not path.is_file():
            continue
        with fits.open(path) as h:
            z=h[1].data
            fs=["SAP_FLUX",f["corrected_column"]]
            good = (z["QUALITY"]==0)&np.isfinite(z["TIME"])
            good &= ~np.isin(z["CADENCENO"],list(masked.get((int(f["sector"]),int(f["camera"]),fs[1]),())))
            phase=(z["TIME"][good]-c+per/2)%per/per-.5
            for ax,col in zip(axs,fs):
                y=np.asarray(z[col][good],float)
                y=y/np.nanmedian(y)-1
                edges=np.linspace(-.5,.5,81 if per<7 else 61)
                k=np.digitize(phase,edges)-1
                b=np.array([np.nanmedian(y[k==j]) if sum(k==j)>1 else np.nan for j in range(len(edges)-1)])
                ax.plot((edges[1:]+edges[:-1])/2,b*1000,lw=.8,color=f"C{i%10}",alpha=.70)
    for ax in axs:
        ax.axvline(0,lw=.7,color="black")
        ax.set_xlim(-.5,.5)
        ax.tick_params(labelsize=7)
    axs[0].set_ylabel(f"{tic}\nP={per:.6f} d",fontsize=8)
    axs[1].text(.98,.87,f'{clock["test_hits"]}/{clock["test_covered"]} late hits',transform=axs[1].transAxes,ha="right",fontsize=7)
axes[0,0].set_title("Raw SAP, phase-binned by sector")
axes[0,1].set_title("Pipeline corrected, phase-binned by sector")
axes[-1,0].set_xlabel("Phase (relative flux in ppt)")
axes[-1,1].set_xlabel("Phase (relative flux in ppt)")
fig.savefig(a.batch_dir/"plots"/"independent-morphology.png",dpi=135)
plt.close(fig)
if out:
    keys=list(dict.fromkeys(k for item in out for k in item))
    with (a.batch_dir/"independent-clocks.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,keys)
        writer.writeheader()
        writer.writerows(out)
