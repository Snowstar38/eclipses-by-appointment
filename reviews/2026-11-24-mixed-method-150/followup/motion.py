"""Measure the moving point in sector 83 and compare with a TESS-centered Horizons prediction."""
import argparse
import csv
import io
from pathlib import Path

from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.optimize import least_squares

from frames import HERE, save


def measure(cache):
    with fits.open(cache/'137785497-83.fits') as h:
        d=h[1].data
        t=d['TIME']
        good=(d['QUALITY']==0)&np.isfinite(t)
        delta=t-3582.86556
        reference=np.nanmedian(d['FLUX'][good&(abs(delta)>.13)&(abs(delta)<.25)],axis=0)
        ix=np.flatnonzero(good&(abs(delta)<.023))
        wcs=WCS(h[2].header)
        rows=[]
        images=[]
        yy,xx=np.indices(reference.shape)
        for j in ix:
            im=d['FLUX'][j]-reference
            y,x=np.unravel_index(np.nanargmax(im),im.shape)
            use=np.isfinite(im)&(np.hypot(xx-x,yy-y)<=3.5)
            def residual(pars):
                amp,cx,cy,sigma,level=pars
                return (amp*np.exp(-.5*((xx-cx)**2+(yy-cy)**2)/sigma**2)+level-im)[use]
            fit=least_squares(residual,[im[y,x],x,y,.8,0],bounds=([0,x-1.5,y-1.5,.3,-np.inf],
                              [np.inf,x+1.5,y+1.5,2.5,np.inf]))
            cx,cy=fit.x[1:3]
            ra,dec=wcs.pixel_to_world_values(cx,cy)
            tm=Time(t[j]-d['TIMECORR'][j]+h[1].header['BJDREFI']+h[1].header['BJDREFF'],
                    format='jd',scale='tdb').utc
            rows.append(dict(utc=tm.isot,jd_utc=tm.jd,btjd=t[j],x=cx,y=cy,ra_deg=float(ra),dec_deg=float(dec),
                             width_px=fit.x[3],ffi=d['FFI_FILE'][j]))
            images.append(im)
    return rows,images


def ephemeris(rows):
    params=dict(format='json',COMMAND="'1036;'",CENTER="'500@-95'",EPHEM_TYPE='OBSERVER',
                QUANTITIES="'1,3,9'",CSV_FORMAT='YES',ANG_FORMAT='DEG',EXTRA_PREC='YES',
                CAL_FORMAT='BOTH',TIME_TYPE='UT',TLIST="'"+','.join(f"{r['jd_utc']:.8f}" for r in rows)+"'")
    response=requests.get('https://ssd.jpl.nasa.gov/api/horizons.api',params=params,timeout=60)
    response.raise_for_status()
    raw=response.json()['result']
    assert 'Ganymed' in raw and 'TESS' in raw and '$$SOE' in raw
    (HERE/'horizons-1036.txt').write_text(raw,encoding='utf8')
    header=next(l for l in raw.splitlines() if 'Date__(UT)' in l and 'R.A.' in l)
    names=[k.strip() for k in header.split(',')]
    raidx=next(i for i,k in enumerate(names) if k.startswith('R.A.'))
    decidx=next(i for i,k in enumerate(names) if k.startswith('DEC'))
    values=list(csv.reader(io.StringIO(raw.split('$$SOE')[1].split('$$EOE')[0].strip())))
    for r in rows:
        obs=min(values,key=lambda v:abs(float(v[1])-r['jd_utc']))
        assert abs(float(obs[1])-r['jd_utc'])<1e-6
        ra,dec=float(obs[raidx]),float(obs[decidx])
        s=SkyCoord(ra,dec,unit='deg').separation(SkyCoord(r['ra_deg'],r['dec_deg'],unit='deg')).arcsec
        r.update(predicted_ra_deg=ra,predicted_dec_deg=dec,separation_arcsec=round(s,3))


def main(cache):
    rows,images=measure(cache)
    ephemeris(rows)
    save(HERE/'track-137785497.csv',rows)
    fig,axes=plt.subplots(1,5,figsize=(12.5,3.5),layout='constrained')
    for ax,j in zip(axes,np.linspace(0,len(rows)-1,5).round().astype(int)):
        obj=rows[j]
        ax.imshow(images[j],origin='lower',cmap='inferno',vmin=0,vmax=15000)
        ax.scatter(obj['x'],obj['y'],marker='+',c='cyan',s=100)
        ax.set(xticks=[],yticks=[],title=obj['utc'][11:19]+' UTC',
               xlabel=f"{obj['separation_arcsec']:.1f} arcsec from prediction")
    fig.suptitle('The moving source near TIC 137785497 on 29 September 2024\nTESS sector 83   |   observed position and separation from the orbit of (1036) Ganymed')
    fig.savefig(HERE/'track-137785497.png',dpi=145)
    print(len(rows),'exposures:',min(r['separation_arcsec'] for r in rows),max(r['separation_arcsec'] for r in rows))


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cache',type=Path)
    main(ap.parse_args().cache)
