"""Measure the two sector 16 eclipses of TIC 120239458 in 2-minute SPOC photometry."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.optimize import least_squares

HERE=Path(__file__).resolve().parent


def main(cache):
    products=json.loads((HERE.parent/"followup/products-120239458.json").read_text())
    product=next(p for p in products if p["productFilename"].endswith("s_lc.fits"))
    path=cache/product["productFilename"]
    url="https://mast.stsci.edu/api/v0.1/Download/file"
    if not path.exists():
        response=requests.get(url,params={"uri":product["dataURI"]},timeout=90)
        response.raise_for_status()
        cache.mkdir(parents=True,exist_ok=True)
        path.write_bytes(response.content)
    fig,axes=plt.subplots(1,2,figsize=(10,4),layout="constrained")
    out=[]
    with fits.open(path) as h:
        d=h[1].data
        for ax,estimate,name in zip(axes,[1741.14,1747.89],["Primary","Secondary"]):
            for key,color in [("SAP_FLUX","#34688f"),("PDCSAP_FLUX","#ad5539")]:
                t,y=d["TIME"],d[key]
                sel=(d["QUALITY"]==0)&np.isfinite(y)&np.isfinite(t)&(abs(t-estimate)<.46)
                t,y=t[sel]-estimate,y[sel]
                y=1000*(y/np.median(y[abs(t)>.22])-1)
                def profile(par,x):
                    offset,slope,depth,center,half,shape=par
                    return offset+slope*x-depth*np.exp(-np.log(2)*(abs(x-center)/half)**shape)
                fit=least_squares(lambda p:profile(p,t)-y,[0,0,-np.quantile(y,.05),0,.07,2],
                                  bounds=([-30,-80,0,-.1,.01,1],[30,80,500,.1,.20,12]),loss="soft_l1",f_scale=2)
                offset,slope,depth,center,half,shape=fit.x
                pointmask=abs(t-center)<.02
                out.append(dict(eclipse=name,product=key,points=len(t),center_btjd=estimate+center,
                                fitted_depth_ppt=depth,central_median_loss_ppt=np.median((offset+slope*t-y)[pointmask]),
                                fwhm_days=2*half,continuum_mad_ppt=np.median(abs(y[abs(t)>.22])),
                                input_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
                ax.scatter(t*24,y,s=5,color=color,alpha=.22)
                smooth=np.linspace(t.min(),t.max(),350)
                ax.plot(smooth*24,profile(fit.x,smooth),color=color,label=key)
            ax.set(title=f"{name} eclipse",xlabel=f"Hours from BTJD {estimate:.2f}",ylabel="Flux relative to local baseline (ppt)")
            ax.legend()
    fig.suptitle("TIC 120239458  |  two-minute TESS observations")
    fig.savefig(HERE/"120239458-two-eclipses.png",dpi=145)
    plt.close(fig)
    with (HERE/"120239458-eclipses.csv").open("w",newline="") as stream:
        w=csv.DictWriter(stream,out[0],lineterminator="\n")
        w.writeheader()
        w.writerows(out)


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cache",type=Path)
    main(ap.parse_args().cache)
