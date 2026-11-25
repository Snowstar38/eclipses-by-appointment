"""Align the TESS ingress of WHAT236 5760 across 48 cycles and check independent ASAS-SN seasons."""
import argparse
import csv
import sys
from pathlib import Path

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.optimize import least_squares

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"ground"))
from sampling import observations


def main(qlp,ground):
    tic="298262982"
    fig,axes=plt.subplots(1,2,figsize=(11,4.2),layout="constrained")
    curves={}
    for sec,a,b in [(24,1969.35,1972.12),(78,3448.56,3449.49)]:
        with fits.open(qlp/f"{tic}_s{sec:03}.fits") as h:
            d=h[1].data
            keep=(d["QUALITY"]==0)&(d["TIME"]>a)&(d["TIME"]<b)&np.isfinite(d["SAP_FLUX"])
            ts,ys=d["TIME"][keep],d["SAP_FLUX"][keep]
            curves[sec]=(ts,ys/np.quantile(ys,.95))
    t,y=curves[24]
    interp=PchipInterpolator(t,y)
    tb,yb=curves[78]
    def resid(par):
        period,ratio,offset=par
        return offset+ratio*(interp(tb-48*period)-1)-yb
    model=least_squares(resid,[30.80,1,1],bounds=([30.775,.4,.90],[30.82,1.6,1.08]),loss="soft_l1",f_scale=.002)
    period,ratio,offset=model.x
    half=(np.quantile(y,.95)+np.quantile(y,.15))/2
    down=t[:-1][(y[:-1]>half)&(y[1:]<=half)]
    up=t[:-1][(y[:-1]<half)&(y[1:]>=half)]
    center=(down[0]+up[-1])/2+np.median(np.diff(t))/2
    axes[0].plot(t-center,100*(y-1),".-",lw=.9,label="Sector 24")
    axes[0].plot(tb-48*period-center,100*(yb-offset)/ratio,".",ms=2,label="Sector 78, 48 cycles later")
    axes[0].set(xlabel="Days from eclipse center",ylabel="Raw aperture flux change (%)",title="Complete eclipse and later ingress")
    axes[0].legend()
    target_ground=list(observations(tic,ground))
    out=[]
    for band,marker in [("g","."),("V","+")]:
        sub=[s for s in target_ground if s[0]["band"]==band]
        if not sub:
            continue
        times,y=np.hstack([v[1] for v in sub]),np.hstack([v[2] for v in sub])
        phase=((times-center+.5*period)%period)-.5*period
        sel=abs(phase)<2.5
        axes[1].scatter(phase[sel],y[sel],s=15,marker=marker,alpha=.55,label=band+" band")
        sel=abs(phase)<.32
        cyc=np.rint((times-center)/period).astype(int)
        vals=[np.median(y[sel&(cyc==i)]) for i in np.unique(cyc[sel])]
        out.append(dict(band=band,reference_btjd=center,tess_ingress_period_d=period,ingress_cycles=48,
                        core_cycles=len(vals),median_core_loss_mag=np.median(vals) if vals else ""))
    axes[1].invert_yaxis()
    axes[1].set(xlabel="Days from TESS prediction",ylabel="ASAS-SN magnitude relative to baseline",title="Ground data at the TESS clock")
    axes[1].legend()
    fig.suptitle("WHAT236 5760  |  TIC 298262982")
    fig.savefig(HERE/"298262982-eclipse.png",dpi=145)
    plt.close(fig)
    with (HERE/"298262982-ephemeris.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,out[0],lineterminator="\n")
        w.writeheader()
        w.writerows(out)


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("qlp",type=Path)
    ap.add_argument("ground",type=Path)
    a=ap.parse_args()
    main(a.qlp,a.ground)
