import numpy as np,glob,json,hashlib
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import curve_fit
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
from pathlib import Path
out=Path('[local path omitted]');p=glob.glob(str(out/'tesscut156/*fits'))[0]
with fits.open(p) as h:
 a=h[1].data;t=np.array(a['TIME']);im=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header);print('target pixel',w.world_to_pixel_values(178.479860179752,20.9177208594718))
fig,axs=plt.subplots(2,3,figsize=(13,8));centers=[1908.162,1918.1039741459824];diffs=[];results=[]
for i,c in enumerate(centers):
 mask=np.isfinite(t)&(q==0);inside=mask&(abs(t-c)<.027);outside=mask&(abs(t-c)>.065)&(abs(t-c)<.17);diff=np.nanmean(im[outside],axis=0)-np.nanmean(im[inside],axis=0);diffs.append(diff)
 for ax,dat,title in zip(axs[i,:2],[np.nanmean(im[outside],axis=0),diff],['out-of-eclipse','out minus in']):
  ax.imshow(dat,origin='lower');ax.scatter([7.796909],[7.723260],marker='+',color='red');ax.set_title(title)
 ap=np.nansum(im[:,6:9,6:9],axis=(1,2));sel=mask&(abs(t-c)<.2);bas=np.median(ap[outside]);axs[i,2].plot(t[sel]-c,ap[sel]/bas,'.-');axs[i,2].set_title('3x3 aperture normalized, same photons');axs[i,2].axvline(0,color='orange')
 # local quadratic trough from QLP SAP, center and conservative cadence/2
 f=out.parent.parent/'shared-qlp/156985493_s022.fits'
 with fits.open(f) as h:
  a=h[1].data;tt=np.array(a['TIME']);ff=np.array(a['SAP_FLUX']);qq=np.array(a['QUALITY']);sel=(abs(tt-c)<.04)&(qq==0)&np.isfinite(ff);co=np.polyfit(tt[sel]-c,ff[sel],2);mid=c-co[1]/(2*co[0]);results.append({'predicted':c,'measured_btjd':float(mid),'nfit':int(sum(sel)),'half_cadence_days':float(np.median(np.diff(tt[np.isfinite(tt)]))/2),'depth_ppt':float((1-np.min(ff[sel])/np.nanmedian(ff[(abs(tt-c)>.07)&(abs(tt-c)<.17)]))*1000)})
fig.tight_layout();fig.savefig(out/'156-cutout-difference.png',dpi=150)
d=np.mean(diffs,axis=0);yy,xx=np.indices(d.shape);mask=(xx>=5)&(xx<=9)&(yy>=5)&(yy<=9);v=np.clip(d,0,None)*mask;cent=[float((v*xx).sum()/v.sum()),float((v*yy).sum()/v.sum())];print('centroid',cent,'events',results,'period',results[1]['measured_btjd']-results[0]['measured_btjd']);json.dump({'events':results,'period_two_adjacent_days':results[1]['measured_btjd']-results[0]['measured_btjd'],'period_error_halfcad_quadrature':np.hypot(*[r['half_cadence_days'] for r in results]),'centroid_xy_5x5_positive':cent,'tesscut_sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),'caution':'quadratic estimates only 3-4 cadences; half cadence is coarse allowance; timing shape systematics and integer aliases not included'},open(out/'156-independent.json','w'),indent=2)


