"""Bounded same-photon TESS-SPOC target-pixel deficit check for two sectors."""
import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
H=Path(__file__).parent
s=json.load(open(H/'sap-measurements.json'));P=s['screening_period_days'];T0=s['screening_epoch_btjd'];dur=s['screening_width_days']
ns=json.load(open(H/'gaia-neighbors.json'))['neighbours']
from astropy.io.votable import parse_single_table
phot=parse_single_table(H/'gaia-photometry-source.xml').to_table();pos={str(x['datalinkID']):(float(x['ra']),float(x['dec'])) for x in phot}
fig,axs=plt.subplots(2,3,figsize=(13,8),layout='constrained');out=[]
for i,sec in enumerate((56,84)):
    ep=T0+({56:53,84:90}[sec])*P
    with fits.open(H/f'tess-spoc-s{sec:03d}-tp.fits',memmap=True) as h:
        assert h[0].header['TICID']==412639100 and h[0].header['SECTOR']==sec
        d=h[1].data;t=np.array(d['TIME'],float);q=np.array(d['QUALITY'],int);F=np.array(d['FLUX'],float)
        w=WCS(h[2].header);ap=np.array(h[2].data)
    x=t-ep
    m=np.isfinite(x)&(q==0)&np.isfinite(F).all(axis=(1,2))
    t=t[m];x=x[m];F=F[m]
    core=abs(x)<dur/2;pre=(x<-.35)&(x>-.8);post=(x>.35)&(x<.8)
    assert core.sum()>30 and pre.sum()>30 and post.sum()>30
    inner=np.median(F[core],axis=0);outer=.5*(np.median(F[pre],axis=0)+np.median(F[post],axis=0));D=outer-inner
    tx,ty=w.all_world2pix(329.7472812178442,61.66216426711785,0);tx=float(tx);ty=float(ty)
    yy,xx=np.mgrid[:D.shape[0],:D.shape[1]]
    bg=np.median(outer[(xx<3)|(xx>8)|(yy<3)|(yy>8)])
    template=np.clip(outer-bg,0,None)
    mask=(abs(xx-tx)<3)&(abs(yy-ty)<3)
    a=float(np.sum(D[mask]*template[mask])/np.sum(template[mask]**2))
    resid=D-a*template
    signal=np.clip(D,0,None)*mask
    cx=float(np.sum(signal*xx)/np.sum(signal)) if signal.sum()>0 else None
    cy=float(np.sum(signal*yy)/np.sum(signal)) if signal.sum()>0 else None
    closest=[]
    for n in ns:
        if n['required_intrinsic_fraction_for_300ppm_blended_loss']>2.5:continue
        ra,dec=pos[n['source_id']];px,py=w.all_world2pix(ra,dec,0)
        closest.append(dict(source_id=n['source_id'],G=n['G'],sep_arcsec=n['sep_arcsec'],pixel=[float(px),float(py)],required_intrinsic_fraction_for_120ppm=n['required_intrinsic_fraction_for_300ppm_blended_loss']*.4))
    out.append(dict(sector=sec,ephemeris_source='QLP BLS screening prediction',predicted_btjd=ep,n_core=int(core.sum()),n_pre=int(pre.sum()),n_post=int(post.sum()),target_pixel=[tx,ty],aperture_pixels=int(np.sum((ap&2)>0)),deficit_centroid_positive_3pix=[cx,cy],deficit_minus_target_px=[cx-tx,cy-ty] if cx is not None else None,deficit_psf_scale=a,deficit_psf_residual_rms=float(np.sqrt(np.mean(resid[mask]**2))),neighbors_capable_120ppm_optimistic=closest,note='Difference is broad trough core minus symmetric shoulders, not established eclipse. Positive-clipped deficit centroid is not reliable if deficit image lacks coherent target PSF.'))
    for j,img in enumerate((outer,D,resid)):
        ax=axs[i,j];v=None if j==0 else np.nanpercentile(abs(img),99)
        ax.imshow(img,origin='lower',cmap='viridis' if j==0 else 'coolwarm',vmin=-v if v else None,vmax=v if v else None)
        ax.plot(tx,ty,'r+',ms=14,mew=2)
        if j==1 and cx is not None:ax.plot(cx,cy,'mo',mfc='none',ms=12)
        for n in closest:
            px,py=n['pixel'];
            if 0<=px<12 and 0<=py<12:ax.plot(px,py,'wx',ms=5)
        ax.set_title(f's{sec} '+('outer' if j==0 else 'outer-core' if j==1 else 'residual after target PSF'),fontsize=9)
fig.savefig(H/'pixel-check.png',dpi=150);plt.close(fig)
(H/'pixel-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2)[:5000])
