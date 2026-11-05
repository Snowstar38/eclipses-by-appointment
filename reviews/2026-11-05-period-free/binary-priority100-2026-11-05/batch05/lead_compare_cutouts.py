"""Compare simultaneous QLP SAP and target-centered TESSCut apertures."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
for tic,sector,center,core_half,side_outer in [('319604640',67,3147.36205335,.16,.6),('142119008',26,2011.75778664,.06,.3)]:
    out=B/tic;cp=out/f'lead-s{sector:03d}-tesscut.fits';qp=Path(r'[local-path-redacted]')/f'{tic}_s{sector:03d}.fits'
    with fits.open(cp,memmap=False) as h:
        a=h[1].data;ct=np.asarray(a['TIME'],float);cf=np.asarray(a['FLUX'],float);cq=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
    with fits.open(qp,memmap=False) as h:
        a=h[1].data;qt=np.asarray(a['TIME'],float);qf=np.asarray(a['SAP_FLUX'],float);qq=np.asarray(a['QUALITY'],int)
    rec=json.loads((out/'lead-cutout.json').read_text());x,y=rec['target_pixel'];yy,xx=np.indices(cf.shape[1:]);mask=(abs(xx-round(x))<=1)&(abs(yy-round(y))<=1);outer=np.hypot(xx-x,yy-y)>4
    cs=np.nansum(cf[:,mask],axis=1);bg=np.nanmedian(cf[:,outer],axis=1);cb=cs-9*bg
    good=np.isfinite(ct)&(cq==0);core=good&(abs(ct-center)<core_half);side=good&(abs(ct-center)>core_half*1.8)&(abs(ct-center)<side_outer)
    qgood=np.isfinite(qt)&np.isfinite(qf)&(qq==0);qcore=qgood&(abs(qt-center)<core_half);qside=qgood&(abs(qt-center)>core_half*1.8)&(abs(qt-center)<side_outer)
    def deficit(v,co,si):return float(1000*(1-np.median(v[co])/np.median(v[si])))
    rec.update(qlp_core_n=int(qcore.sum()),qlp_side_n=int(qside.sum()),qlp_core_deficit_ppt=deficit(qf,qcore,qside),cutout_bg_sub_side_median=float(np.median(cb[side])),cutout_bg_sub_core_deficit_ppt=deficit(cb,core,side),outer_pixel_zero_fraction=float(np.mean(cf[:,outer]==0)),outer_pixel_finite_fraction=float(np.mean(np.isfinite(cf[:,outer]))),background_zero_fraction=float(np.mean(bg==0)),background_finite_fraction=float(np.mean(np.isfinite(bg))))
    (out/'lead-cutout.json').write_text(json.dumps(rec,indent=2)+'\n')
    fig,ax=plt.subplots(figsize=(9,4));qwin=qgood&(abs(qt-center)<side_outer);cwin=good&(abs(ct-center)<side_outer)
    ax.plot(qt[qwin]-center,qf[qwin]/np.median(qf[qside]),'.',ms=4,label='QLP SAP');ax.plot(ct[cwin]-center,cs[cwin]/np.median(cs[side]),'.',ms=3,label='TESSCut target 3x3 raw');ax.plot(ct[cwin]-center,cb[cwin]/np.median(cb[side]),'.',ms=2,alpha=.6,label='TESSCut 3x3 outer-bg')
    ax.axvspan(-core_half,core_half,alpha=.12,color='red');ax.set(xlabel='days from screen seed',ylabel='relative flux',title=f'TIC {tic} S{sector}: same-photon reduction comparison');ax.legend();fig.tight_layout();fig.savefig(out/'lead-qlp-cutout-compare.png',dpi=140);plt.close(fig)
    print(tic,{k:rec[k] for k in ['qlp_core_deficit_ppt','target_aperture_loss_ppt','cutout_bg_sub_core_deficit_ppt','outer_pixel_zero_fraction','background_zero_fraction']},flush=True)
