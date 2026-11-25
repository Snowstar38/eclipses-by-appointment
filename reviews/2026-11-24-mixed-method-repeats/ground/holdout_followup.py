"""Test the single positive ASAS-SN holdout against contemporaneous TESS predictions."""
import argparse
import csv
from pathlib import Path

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE=Path(__file__).resolve().parent


def run(cache, qlp):
    tic="253463221"
    trial, = [r for r in csv.DictReader((HERE/"ground-holdout.csv").open())
              if r["tic"]==tic and r["passes"]=="True"]
    period,epoch,half=[float(trial[k]) for k in ("period_d","selected_epoch","halfwidth_d")]
    mag=pd.read_csv(cache/f"asassn-{tic}.csv.gz")
    mag=mag[(mag.quality=="G") & (mag.mag_err>0) & (mag.mag_err<.2)].copy()
    mag["residual"]=mag.mag-mag.groupby("camera").mag.transform("median")
    mag["dt"]=((mag.jd-2457000-epoch+period/2)%period)-period/2
    fig,axes=plt.subplots(2,1,figsize=(9,6),layout="constrained")
    for cam,group in mag.groupby("camera"):
        axes[0].scatter(group.dt,group.residual,s=4,label=cam)
    axes[0].invert_yaxis()
    axes[0].set(ylabel="Camera-relative g magnitude",xlabel="Days from ASAS-SN prediction")
    axes[0].legend(ncols=3,fontsize=8)
    rows=[]
    for path in sorted(qlp.glob(f"{tic}_s*.fits")):
        with fits.open(path) as h:
            z=h[1].data
            sector=h[0].header["SECTOR"]
            good=(z["QUALITY"]==0)&np.isfinite(z["TIME"])&np.isfinite(z["SAP_FLUX"])
            t=z["TIME"][good]
            raw=z["SAP_FLUX"][good]
            cadence=np.median(np.diff(t))
            for n in range(int(np.ceil((min(t)-epoch)/period)),int(np.floor((max(t)-epoch)/period))+1):
                dt=t-epoch-period*n
                core=abs(dt)<half
                left=(dt>=-4*half)&(dt<=-2*half)
                right=(dt>=2*half)&(dt<=4*half)
                if min(m.sum()*cadence/(2*half) for m in (core,left,right))<.65:
                    continue
                base=np.interp(dt,[np.median(dt[m]) for m in (left,right)],
                               [np.median(raw[m]) for m in (left,right)])
                flux=(raw/base-1)*1000
                rows.append(dict(sector=sector,cycle=n,btjd=epoch+n*period,core_n=int(core.sum()),
                                 raw_tess_depth_ppt=-float(np.median(flux[core]))))
                m=abs(dt)<=4*half
                axes[1].plot(dt[m],flux[m],".",ms=2,label=f"S{sector}, cycle {n}")
    for ax in axes:
        ax.axvspan(-half,half,alpha=.1,color="black")
    axes[1].set(ylabel="Local TESS SAP residual (ppt)",xlabel="Days from ASAS-SN prediction")
    axes[1].legend(ncols=3,fontsize=7)
    fig.suptitle("TIC 253463221   |   ground-selected phase and covered TESS windows")
    fig.savefig(HERE/"holdout-253463221.png",dpi=130)
    with (HERE/"holdout-253463221.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,rows[0],lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("cache",type=Path)
    p.add_argument("qlp",type=Path)
    a=p.parse_args()
    run(a.cache,a.qlp)
