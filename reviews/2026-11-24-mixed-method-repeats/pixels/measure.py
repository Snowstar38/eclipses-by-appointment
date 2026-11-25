"""Locate the lost light in a supplied TESS-SPOC eclipse window."""
import argparse
import csv
from pathlib import Path

from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent


def gaia_field(row, wcs, shape):
    records=list(csv.DictReader((HERE/f"gaia-{row['tic']}.csv").open()))
    cols=lambda name: np.array([float(r[name]) if r[name] else np.nan for r in records])
    dt=Time(float(row["btjd"])+2457000,format="jd",scale="tdb").jyear-cols("ref_epoch")
    dec=cols("dec")
    ra=cols("ra")+dt*np.nan_to_num(cols("pmra"))/(3.6e6*np.cos(np.deg2rad(dec)))
    dec=dec+dt*np.nan_to_num(cols("pmdec"))/3.6e6
    x,y=wcs.world_to_pixel_values(ra,dec)
    g=cols("g")
    rp=cols("rp")
    mag=np.where(np.isfinite(rp),rp,g)
    ids=np.array([r["source_id"] for r in records])
    good=(x>-3)&(y>-3)&(x<shape[1]+2)&(y<shape[0]+2)&np.isfinite(mag)
    x,y,mag,ids=x[good],y[good],mag[good],ids[good]
    idx,=np.flatnonzero(ids==row["gaia_dr3"])
    return x,y,10**(-.4*(mag-mag[idx])),ids,idx


def locate(image, sigma):
    valid=np.isfinite(image)
    y,x=np.indices(image.shape)
    j,i=np.unravel_index(np.nanargmax(image),image.shape)
    def resid(p):
        amp,cx,cy,floor=p
        return (amp*np.exp(-.5*((x-cx)**2+(y-cy)**2)/sigma**2)+floor-image)[valid]
    sol=least_squares(resid,[max(.001,image[j,i]-np.nanmedian(image)),i,j,np.nanmedian(image)],
                      bounds=([0,-1,-1,-np.inf],[np.inf,image.shape[1],image.shape[0],np.inf]))
    return sol.x[1:3]


def fit_scene(oot, x, y, rel):
    yy,xx=np.indices(oot.shape)
    valid=np.isfinite(oot)
    good=rel>max(rel)*1.e-5
    dx=xx[:,:,None]-x[good]
    dy=yy[:,:,None]-y[good]
    def residual(p):
        scale,width,sx,sy,sky=p
        model=scale*(np.exp(-.5*((dx-sx)**2+(dy-sy)**2)/width**2)@rel[good])+sky
        return (model-oot)[valid]
    flux=np.nanmax(oot)-np.nanmin(oot)
    fit=least_squares(residual,[flux/max(rel),.9,0,0,np.nanmedian(oot)],
                      bounds=([0,.45,-1.25,-1.25,-np.inf],[np.inf,2.6,1.25,1.25,np.inf]),
                      loss="soft_l1",f_scale=max(1,flux*.02))
    return fit.x[1:4]


def median_cube(cube, mask):
    return np.nanmedian(cube[mask],axis=0)


def measure(cache,r):
    tic,sector=r["tic"],r["sector"]
    with fits.open(cache/f"{tic}-{sector}.fits",memmap=True) as hd:
        assert str(hd[0].header["TICID"])==tic and str(hd[0].header["SECTOR"])==sector
        raw=hd[1].data
        t=raw["TIME"]
        ok=(raw["QUALITY"]==0)&np.isfinite(t)
        dt=t-float(r["btjd"])
        width=float(r["core_h"])/24
        inner=ok&(abs(dt)<width*.5)
        left=ok&(dt>-2.7*width)&(dt<-1.35*width)
        right=ok&(dt>1.35*width)&(dt<2.7*width)
        sizes=[int(np.sum(v)) for v in (inner,left,right)]
        if min(sizes)<3:
            raise ValueError(f"insufficient core/left/right exposures {sizes}")
        key=inner|left|right
        f=raw["FLUX"][key].astype(float)
        b=raw["FLUX_BKG"][key].astype(float)
        wcs=WCS(hd[2].header)
        mask=(hd[2].data&2)>0
    inner,left,right=inner[key],left[key],right[key]
    dtime=dt[key]
    weight=(np.median(dtime[inner])-np.median(dtime[left]))/(np.median(dtime[right])-np.median(dtime[left]))
    def images(cube):
        l=median_cube(cube,left)
        u=median_cube(cube,right)
        i=median_cube(cube,inner)
        oot=l*(1-weight)+u*weight
        return oot,oot-i,l-i,u-i
    oot,loss,ls,rs=images(f)
    _,restored,_,_=images(f+b)
    sx,sy,rel,ids,i=gaia_field(r,wcs,loss.shape)
    width_px,dx,dy=fit_scene(oot,sx,sy,rel)
    cx,cy=sx+dx,sy+dy
    center=locate(loss,width_px)
    restored_center=locate(restored,width_px)
    yy,xx=np.indices(loss.shape)
    field=(np.hypot(xx-cx[i],yy-cy[i])>3.5)&~mask
    raw_ap=float(np.nansum(restored[mask]))
    relative_ap=raw_ap-np.count_nonzero(mask)*float(np.nanmedian(restored[field]))
    scale=3600*np.sqrt(np.abs(np.linalg.det(wcs.pixel_scale_matrix)))
    split_as=max(np.linalg.norm(locate(side,width_px)-center)*scale for side in (ls,rs))
    distance=scale*np.hypot(cx-center[0],cy-center[1])
    pdepth=float(r["depth_ppt"])/1000
    # Include neighbours four times fainter than the undiluted depth bound, allowing
    # for passband and aperture-fraction differences. This is an advisory screen.
    capable=(rel>=.25*pdepth/(1-pdepth)) & (scale*np.hypot(sx-sx[i],sy-sy[i])<90)
    others=np.flatnonzero(capable&(np.arange(len(sx))!=i))
    near=min(others,key=lambda j:distance[j]) if len(others) else None
    farthest_allowed=8
    if split_as>8 or np.linalg.norm(center-restored_center)*scale>8:
        grade="unstable"
    elif max(abs(dx),abs(dy))>=1.24:
        grade="registration_limit"
    elif distance[i]<=farthest_allowed and (near is None or distance[near]-distance[i]>8):
        grade="favors_target"
    elif near is not None and distance[near]<=8 and distance[i]-distance[near]>8:
        grade="favors_neighbor"
    else:
        grade="unresolved"
    result=dict(tic=tic,sector=sector,btjd=r["btjd"],family=r["family"],gaia_dr3=ids[i],
                core_n=sizes[0],left_n=sizes[1],right_n=sizes[2],target_offset_as=round(distance[i],3),
                nearest_plausible_neighbor=(ids[near] if near is not None else ""),
                neighbor_offset_as=(round(distance[near],3) if near is not None else ""),
                shoulder_shift_as=round(split_as,3),restored_shift_as=round(np.linalg.norm(center-restored_center)*scale,3),
                sector_registration_dx=round(dx,4),sector_registration_dy=round(dy,4),sigma_px=round(width_px,4),
                loss_e_s=round(np.nansum(loss[mask]),2),restored_loss_e_s=round(raw_ap,2),
                restored_local_loss_e_s=round(relative_ap,2),
                assessment=grade)
    return result,(loss,(cx[i],cy[i]),center,np.array([cx[others],cy[others]]),mask)


def draw(tic,results):
    fig,axes=plt.subplots(1,len(results),figsize=(max(5.6,3.25*len(results)),3.7),squeeze=False,layout="constrained")
    for ax,(r,(im,target,center,others,mask)) in zip(axes.flat,results):
        lim=max(.001,np.nanmax(abs(im)))
        ax.imshow(im,cmap="RdBu_r",origin="lower",vmin=-lim,vmax=lim)
        ax.contour(mask,levels=[.5],colors="#cfcfcf",linewidths=.6)
        ax.plot(*target,"+",color="black",markersize=13,mew=1.3)
        ax.plot(*center,"o",mfc="none",mec="#00a892",markersize=10)
        ax.plot(*others,"x",color="orange",markersize=5)
        ax.set(xlim=(-.5,im.shape[1]-.5),ylim=(-.5,im.shape[0]-.5),xticks=[],yticks=[])
        ax.set_title(f"S{r['sector']}  {r['family']}\nBTJD {float(r['btjd']):.3f}",fontsize=9)
        ax.set_xlabel(f"Target offset {r['target_offset_as']:.1f} arcsec")
    fig.suptitle(f"TIC {tic}   |   event difference images\nRed: lost flux   + target   O fitted loss   x field stars",fontsize=11)
    fig.savefig(HERE/f"{tic}.png",dpi=135)
    plt.close(fig)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("cache",type=Path)
    a=p.parse_args()
    windows=list(csv.DictReader((HERE/"windows.csv").open()))
    rows=[]
    for tic in dict.fromkeys(r["tic"] for r in windows):
        results=[]
        for r in (v for v in windows if v["tic"]==tic):
            try:
                record,figdata=measure(a.cache,r)
                results.append((record,figdata))
                rows.append(record)
            except (OSError,ValueError) as exc:
                rows.append(dict(tic=tic,sector=r["sector"],btjd=r["btjd"],family=r["family"],assessment="unavailable",error=str(exc)))
        if results:draw(tic,results)
        print(tic,[(r["assessment"],r.get("target_offset_as")) for r in rows if r["tic"]==tic],flush=True)
    with (HERE/"fits.csv").open("w",newline="",encoding="utf8") as f:
        w=csv.DictWriter(f,dict.fromkeys(k for r in rows for k in r),lineterminator="\n")
        w.writeheader();w.writerows(rows)
