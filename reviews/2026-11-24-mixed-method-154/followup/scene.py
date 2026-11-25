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
