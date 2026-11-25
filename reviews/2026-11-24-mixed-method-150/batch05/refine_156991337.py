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
p.add_argument("--fits-dir",type=Path,default=(HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace")/"sky/data/qlp-sb-p20-60")
a=p.parse_args()
period=6.90559082635
epoch=1474.3898810774872
width=.080
radius=.22
out=[]
profiles={}
with (HERE/"156991337/files.csv").open(encoding="utf-8-sig",newline="") as f:
    files=list(csv.DictReader(f))
for r in files:
    with fits.open(a.fits_dir/r["file"]) as h:
        z=h[1].data
        t=z["TIME"]
        dt=float(r["cadence"])
        for subcycle in range(int(np.ceil(2*(float(r["start"])-epoch)/period)),
                              int(np.floor(2*(float(r["end"])-epoch)/period))+1):
            time=epoch+subcycle*period/2
            ix=abs(t-time)<radius
            x=np.asarray(t[ix]-time,float)
            good=z["QUALITY"][ix]==0
            cols=("SAP_FLUX",r["corrected_column"],"SAP_X","SAP_Y","SAP_BKG")
            y=np.asarray([z[k][ix] for k in cols],float).T
            good &= np.isfinite(y[:,:2]).all(axis=1)
            core=abs(x)<=width/2
            before=(x>=-.14)&(x<-.052)
            after=(x>.052)&(x<=.14)
            counts=[np.sum(good & win) for win in (core,before,after)]
            frac=min(c*dt/size for c,size in zip(counts,(.080,.088,.088)))
            nearest=int(z["CADENCENO"][np.nanargmin(abs(t-time))])
            row=dict(sector=r["sector"],camera=r["camera"],ccd=r["ccd"],half_period_index=subcycle,
                     center_btjd=time,cadenceno=nearest,core_quality_zero=counts[0],
                     core_quality_nonzero=int(sum(core & ~good)),coverage=frac,support="insufficient")
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
with (HERE/"156991337/refined-windows.csv").open("w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,keys)
    writer.writeheader()
    writer.writerows(out)
fig, axes=plt.subplots(2,5,figsize=(15,5.6),layout="constrained",sharex=True)
edges=np.linspace(-.20,.20,41)
for parity,axrow in enumerate(axes):
    for k,ax in enumerate(axrow):
        for name,x,profile in profiles[parity]:
            ax.scatter(x,profile[:,k],s=3,alpha=.14,color=f"C{int(name)%10}")
        x=np.concatenate([x for _,x,y in profiles[parity]])
        y=np.concatenate([y[:,k] for _,x,y in profiles[parity]])
        bins=np.digitize(x,edges)-1
        median=[np.nanmedian(y[bins==i]) if sum(bins==i)>2 else np.nan for i in range(len(edges)-1)]
        ax.plot((edges[1:]+edges[:-1])/2,median,color="black",lw=1)
        ax.axvspan(-width/2,width/2,alpha=.12,color="tab:orange")
        ax.set_xlim(-.20,.20)
        central=y[abs(x)<.2]
        finite=central[np.isfinite(central)]
        if finite.size:
            lo,hi=np.percentile(finite,[1,99])
            if hi>lo:
                ax.set_ylim(lo,hi)
ax=axes[0]
for a,label in zip(ax,("Raw SAP (ppt)","Corrected (ppt)","Centroid X (px)","Centroid Y (px)","Sky background")):
    a.set_title(label)
axes[0,0].set_ylabel("Predicted losses")
axes[1,0].set_ylabel("Interleaved half-cycles")
for ax in axes[1]:
    ax.set_xlabel("Days from prediction")
fig.suptitle("TIC 156991337 | original QLP apertures folded at 6.90559082635 d")
fig.savefig(HERE/"156991337/plots/local-control.png",dpi=145)
