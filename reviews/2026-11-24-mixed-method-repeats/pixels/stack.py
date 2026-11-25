"""Stack bracketing full-frame difference images at the two short TESS clocks."""
import argparse
import csv
import hashlib
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from astropy.io import fits
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import numpy as np
import requests

from measure import HERE, gaia_field, fit_scene, locate


def evaluate(s, c, sector, cache):
    tic=s["tic"]
    path=cache/f"{tic}-{sector}.fits"
    params=dict(ra=s["ra_deg"],dec=s["dec_deg"],sector=sector,x=15,y=15)
    url=requests.Request("GET","https://mast.stsci.edu/tesscut/api/v0.1/astrocut",params=params).prepare().url
    if not path.exists():
        response=requests.get(url,timeout=100)
        response.raise_for_status()
        with ZipFile(BytesIO(response.content)) as z:
            name,=[n for n in z.namelist() if n.endswith(".fits")]
            path.write_bytes(z.read(name))
    with fits.open(path) as h:
        assert h[0].header["SECTOR"]==sector
        raw=h[1].data
        t=raw["TIME"]
        valid=(raw["QUALITY"]==0)&np.isfinite(t)
        dt=np.median(np.diff(t[valid]))
        wcs=WCS(h[2].header)
        p,ep,w=[float(c[k]) for k in ("period_d","epoch_btjd","duration_d")]
        frames=[]
        for n in range(int(np.ceil((min(t[valid])-ep)/p)),int(np.floor((max(t[valid])-ep)/p))+1):
            u=(t-ep-n*p)/w
            masks=[valid&(u>=-2)&(u<=-1),valid&(abs(u)<.35),valid&(u>=1)&(u<=2)]
            if any(m.sum()<max(3,.65*w*f/dt) for m,f in zip(masks,[1,.7,1])):
                continue
            left,core,right=[np.nanmedian(raw["FLUX"][m],axis=0) for m in masks]
            frames.append([.5*(left+right),left-core,right-core])
    if len(frames)<3:
        raise ValueError(f"Insufficient covered events in sector {sector}")
    arr=np.asarray(frames)
    oot,l,r=np.nanmedian(arr,axis=0)
    img=(l+r)/2
    row=dict(**s,btjd=np.nanmedian(t[valid]))
    x,y,rel,ids,i=gaia_field(row,wcs,img.shape)
    sigma,dx,dy=fit_scene(oot,x,y,rel)
    x,y=x+dx,y+dy
    center=locate(img,sigma)
    scale=3600*np.sqrt(abs(np.linalg.det(wcs.pixel_scale_matrix)))
    dist=np.hypot(x-center[0],y-center[1])*scale
    # Show field sources brighter than one thousandth of the target in the Gaia proxy band.
    alternatives=[j for j in range(len(x)) if j!=i and rel[j]>.001 and np.hypot(x[j]-x[i],y[j]-y[i])*scale<110]
    nearest=min(alternatives,key=lambda j:dist[j]) if alternatives else None
    split=np.linalg.norm(locate(l,sigma)-locate(r,sigma))*scale
    halves=[np.nanmedian(np.mean(a[:,1:],axis=1),axis=0) for a in np.array_split(arr,2)]
    temporal=np.linalg.norm(locate(halves[0],sigma)-locate(halves[1],sigma))*scale
    rec=dict(tic=tic,sector=sector,events=len(frames),fit_dx=dx,fit_dy=dy,target_arcsec=dist[i],
             closest_other_id=ids[nearest] if nearest is not None else "",
             closest_other_arcsec=dist[nearest] if nearest is not None else "",left_right_shift_arcsec=split,
             early_late_shift_arcsec=temporal,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),url=url)
    return rec,(img,center,(x[i],y[i]),[(x[j],y[j]) for j in alternatives])


if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cache",type=Path)
    args=ap.parse_args()
    args.cache.mkdir(parents=True,exist_ok=True)
    roster={r["tic"]:r for r in csv.DictReader((HERE.parent/"batch.csv").open())}
    clocks={r["tic"]:r for r in csv.DictReader((HERE.parent/"ground/reviewer-clocks.csv").open())}
    records=[]
    for tic,sectors in [("170337570",[66,93,100]),("410900361",[61,62,89])]:
        fig,axes=plt.subplots(1,3,figsize=(10,3.5),layout="constrained")
        for sector,ax in zip(sectors,axes):
            rec,(img,center,target,neighbors)=evaluate(roster[tic],clocks[tic],sector,args.cache)
            records.append(rec)
            limit=max(abs(np.nanpercentile(img,[1,99])))
            ax.imshow(img,origin="lower",cmap="coolwarm",vmin=-limit,vmax=limit)
            if neighbors:
                ax.scatter(*np.transpose(neighbors),marker=".",s=10,c="gray")
            ax.scatter(*target,facecolors="none",edgecolors="yellow",s=115)
            ax.scatter(*center,marker="+",c="black",s=70)
            ax.set(title=f"Sector {sector}   |   {rec['events']} events",xlim=(-.5,14.5),ylim=(-.5,14.5))
        fig.suptitle(f"TIC {tic}   |   stacked light loss\nTarget: yellow circle   /   fitted loss: black cross")
        fig.savefig(HERE/f"stack-{tic}.png",dpi=140)
        plt.close(fig)
    with (HERE/"stack.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,records[0],lineterminator="\n");w.writeheader();w.writerows(records)
