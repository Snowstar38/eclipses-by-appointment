"""Animate the original sector 83 images alongside the QLP brightening they produced."""
import argparse
from io import BytesIO
from pathlib import Path

from astropy.io import fits
from astropy.time import Time
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from frames import HERE, rows


def main(cache,qlp):
    star=next(r for r in rows(HERE.parent/'roster.csv') if r['tic']=='137785497')
    epoch=3582.86556
    with fits.open(qlp/'137785497_s083.fits') as h:
        z=h[1].data
        good=(z['QUALITY']==0)&np.isfinite(z['SAP_FLUX'])&(abs(z['TIME']-epoch)<.14)
        tq=z['TIME'][good]
        flux=z['SAP_FLUX'][good]
        curve=100*(flux/np.median(flux[abs(tq-epoch)>.07])-1)
    with fits.open(cache/'137785497-83.fits') as h:
        d=h[1].data
        t=d['TIME']
        good=(d['QUALITY']==0)&np.isfinite(t)
        ref=np.nanmedian(d['FLUX'][good&(abs(t-epoch)>.13)&(abs(t-epoch)<.25)],axis=0)
        use=good&(abs(t-epoch)<.056)
        stamp=d['FLUX'][use].astype(float)-ref
        times=t[use]
        utc=Time(times-d['TIMECORR'][use]+2457000,format='jd',scale='tdb').utc.isot
        wcs=WCS(h[2].header)
        x,y=wcs.world_to_pixel_values(float(star['ra_deg']),float(star['dec_deg']))
    fig,(ax,bx)=plt.subplots(1,2,figsize=(8.6,3.8),gridspec_kw=dict(width_ratios=[1,1.4]),layout='constrained')
    image=ax.imshow(stamp[0],cmap='inferno',origin='lower',vmin=0,vmax=15000,interpolation='nearest')
    ax.scatter(x,y,facecolor='none',edgecolor='#66dce4',s=110,lw=1.3)
    ax.set(xticks=[],yticks=[],title='TESS difference image')
    ax.set_xlabel('Cyan circle marks the nominated star')
    bx.plot((tq-epoch)*1440,curve,color='#25567e',marker='.',ms=3,lw=1)
    cursor=bx.axvline(0,color='#bc5619',lw=2)
    bx.set(xlim=(-85,85),ylim=(-4,57),xlabel='Minutes from the measured flux peak',
           ylabel='Change in aperture flux (%)',title='Light recorded in the aperture')
    title=fig.suptitle('')
    frames=[]
    for s,time,timestamp in zip(stamp,times,utc):
        image.set_data(s)
        cursor.set_xdata([(time-epoch)*1440]*2)
        title.set_text(f'(1036) Ganymed crossing the TIC 137785497 field   |   {timestamp[:10]}  {timestamp[11:19]} UTC')
        buf=BytesIO()
        fig.savefig(buf,format='png',dpi=100)
        buf.seek(0)
        with Image.open(buf) as im:frames.append(im.convert('P',palette=Image.Palette.ADAPTIVE,colors=128))
    frames[0].save(HERE/'ganymed.gif',save_all=True,append_images=frames[1:],loop=0,
                   duration=[130]*(len(frames)-1)+[850],disposal=2)
    plt.close(fig)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cache',type=Path)
    ap.add_argument('qlp',type=Path)
    args=ap.parse_args()
    main(args.cache,args.qlp)
