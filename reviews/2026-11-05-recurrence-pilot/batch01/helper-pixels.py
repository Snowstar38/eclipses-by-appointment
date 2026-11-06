from pathlib import Path
import numpy as np,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent
jobs=[('147413927',37,163.21764583099278,-47.70130734349548,2317.923),('147413927',90,163.21764583099278,-47.70130734349548,3750.813),('265066551',17,347.36321314194146,68.42988151080459,1770.93)]
out=[]
for tic,sec,ra,dec,c in jobs:
 p=B/tic/f'helper-tesscut-s{sec:03}.fits'
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['FLUX'],float);q=np.array(a['QUALITY'],int);w=WCS(h[2].header)
 x,y=w.world_to_pixel_values(ra,dec); x,y=float(x),float(y); ix,iy=int(round(x)),int(round(y)); ok=np.isfinite(t)&(q==0)&np.all(np.isfinite(f),axis=(1,2));
 if tic=='147413927':
  lo=ok&(abs(t-c)<.13);hi=ok&(abs(t-c)>.48)&(abs(t-c)<.95)
 else:
  near=ok&(abs(t-c)<1.5); series=np.sum(f[:,iy-1:iy+2,ix-1:ix+2],axis=(1,2)); q1,q3=np.quantile(series[near],[.2,.8]);lo=near&(series<=q1);hi=near&(series>=q3)
 baseline=np.median(f[hi],axis=0);low=np.median(f[lo],axis=0);d=baseline-low
 yy,xx=np.indices(d.shape); mask=(xx-x)**2+(yy-y)**2<9; wt=np.maximum(d,0)*mask; cx=float(np.sum(wt*xx)/np.sum(wt));cy=float(np.sum(wt*yy)/np.sum(wt)); peak=np.unravel_index(np.argmax(d),d.shape)
 sky=float(np.median(baseline[[0,0,-1,-1],[0,-1,0,-1]])); val=float(baseline[iy,ix]);
 rec=dict(tic=tic,sector=sec,center=c,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),target_xy=[float(x),float(y)],peak_yx=list(map(int,peak)),centroid_xy=[cx,cy],centroid_offset_px=float(np.hypot(cx-x,cy-y)),n_low=int(lo.sum()),n_high=int(hi.sum()),baseline_target_pixel=val,corner_median_sky=sky,target_above_sky=val-sky,method='V007 core +/-0.13d and side 0.48-0.95d; V002 top/bottom quintiles of target-centered 3x3 flux within +/-1.5d')
 out.append(rec)
 fig,ax=plt.subplots(1,2,figsize=(9,4));ax[0].imshow(baseline,origin='lower');ax[1].imshow(d,origin='lower',cmap='RdBu_r');
 for a in ax:a.plot(x,y,'rx',ms=9);a.plot(cx,cy,'c+',ms=9)
 ax[0].set_title('baseline; red target');ax[1].set_title('baseline minus low; cyan centroid');fig.suptitle(f'{tic} S{sec}');fig.tight_layout();fig.savefig(B/tic/f'helper-difference-s{sec:03}.png',dpi=140);plt.close(fig)
print(json.dumps(out,indent=2));(B/'helper-pixels.json').write_text(json.dumps(out,indent=2)+'\n')

