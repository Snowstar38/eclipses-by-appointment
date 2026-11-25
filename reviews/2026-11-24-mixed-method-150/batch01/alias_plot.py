"""Compare a full clock with its subdivisions using original FITS products."""
import argparse
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits

p=argparse.ArgumentParser()
p.add_argument("batch_dir",type=Path)
p.add_argument("tic")
p.add_argument("period",type=float)
p.add_argument("epoch",type=float)
p.add_argument("divisors",type=int,nargs="+")
p.add_argument("--fits-dir",type=Path,default=(HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")/"sky/data/qlp-sb-p20-60")
a=p.parse_args()
with (a.batch_dir/"files.csv").open(encoding="utf-8-sig",newline="") as f:
    files=[r for r in csv.DictReader(f) if r["tic"]==a.tic]
fig, axes = plt.subplots(len(a.divisors),4,figsize=(13,2.7*len(a.divisors)),layout="constrained",squeeze=False)
for div,axs in zip(a.divisors,axes):
    for i,f in enumerate(files):
        path=a.fits_dir/f["file"]
        with fits.open(path) as h:
            z=h[1].data
            good = (z["QUALITY"]==0)&np.isfinite(z["TIME"])
            phase = ((z["TIME"][good]-a.epoch)*div/a.period+.5)%1-.5
            for ax,key in zip(axs,("SAP_FLUX",f["corrected_column"],"SAP_X","SAP_BKG")):
                y=np.asarray(z[key][good],float)
                y=y-np.nanmedian(y)
                if key in ("SAP_FLUX",f["corrected_column"]):
                    y*=1000/np.nanmedian(z[key][good])
                else:
                    scale=np.nanmedian(abs(y))
                    if scale:
                        y/=1.4826*scale
                edges=np.linspace(-.5,.5,81)
                groups=np.digitize(phase,edges)-1
                medians=[np.nanmedian(y[groups==j]) if sum(groups==j)>2 else np.nan for j in range(len(edges)-1)]
                ax.plot((edges[:-1]+edges[1:])/2,medians,lw=.9,color=f"C{i%10}",alpha=.7)
    axs[0].set_ylabel(f"P={a.period/div:.6f} d")
    for ax in axs:
        ax.axvline(0,lw=.6,color="gray")
        ax.set_xlim(-.5,.5)
for ax,label in zip(axes[0],("Raw SAP (ppt)","Corrected (ppt)","SAP X (robust units)","Sky background (robust units)")):
    ax.set_title(label)
fig.suptitle(f"TIC {a.tic}, phase profiles of the clock and tested subdivisions")
fig.savefig(a.batch_dir/"plots"/f"{a.tic}-alias-comparison.png",dpi=140)
