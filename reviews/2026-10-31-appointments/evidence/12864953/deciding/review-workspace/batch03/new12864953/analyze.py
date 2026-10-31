from pathlib import Path
import sys,json
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
sys.path.insert(0,'[local path omitted] 5.1/made/appointments/vet12864953')
from vetlib import fit_trap,t0_error,model,trap
out=Path(__file__).parent
with fits.open(out/'tesscut_s107.fits') as h:
 z=h[1].data;t=np.array(z['TIME'],float);F=np.array(z['FLUX'],float);q=np.array(z['QUALITY']);wcs=WCS(h[2].header)
xy=wcs.all_world2pix([[4.338553687696893,-17.680976867536586]],0)[0];ix,iy=np.rint(xy).astype(int)
bk=np.nanmedian(np.sort(F.reshape(len(t),-1),axis=1)[:,:32],axis=1);F=F-bk[:,None,None]
good=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0)
rows=[];fig,axs=plt.subplots(2,3,figsize=(13,7))
for row,(kind,guess,old,old_err,dep0) in enumerate([('B',4271.33338,3196.0997,.0017,.0108),('A',4279.33528,3204.1016,.001,.01724)]):
 for col,radius in enumerate([0,1,2]):
  f=F[:,iy-radius:iy+radius+1,ix-radius:ix+radius+1].sum(axis=(1,2))
  k=good&(abs(t-guess)<1.5)&(f>0);x=t[k];y=f[k]/np.median(f[k])
  if not np.any(abs(x-guess)<.4):
   rows.append(dict(kind=kind,aperture_side=2*radius+1,status='flagged: predicted A window has no quality-zero data',n=int(k.sum())))
   axs[row,col].plot(x,y,'.',ms=2);axs[row,col].set_title(f'{kind}: predicted window quality2048');continue
  tr=guess
  init=[guess+.3,dep0,.25,.09,1.,0.,0.]
  fit=least_squares(lambda p:(y-model(p,x,tr)),init,bounds=([guess-.6,0,.1,.01,.8,-1,-1],[guess+.6,.04,.5,.12,1.2,1,1]),xtol=1e-12,ftol=1e-12,gtol=1e-12)
  b=fit.x;chi=np.sum(fit.fun**2);s=np.std(fit.fun)
  residual=y-model(b,x,tr)
  bins=np.floor((x-x.min())*24).astype(int)
  means=np.array([residual[bins==j].mean() for j in np.unique(bins) if (bins==j).sum()>5])
  nbin=np.median([(bins==j).sum() for j in np.unique(bins) if (bins==j).sum()>5])
  beta=max(1.,float(means.std()/s*np.sqrt(nbin)))
  et=max(.001,t0_error(x,y,b,tr,s,half=.02,n=401)*beta)
  p=(float(b[0])-old)/34;ep=np.hypot(float(et),old_err)/34
  result=dict(kind=kind,aperture_side=2*radius+1,target_pixel=xy.tolist(),n=int(k.sum()),t0=float(b[0]),t0_error_days=float(et),beta=float(beta),depth_ppt=float(b[1])*1000,T14_h=float(b[2])*24,T12_h=float(b[3])*24,period_days=p,period_error_days=float(ep),cycles=34)
  rows.append(result);ax=axs[row,col];ax.plot(x,y,'.',ms=2);ax.plot(x,model(b,x,tr));ax.set_title(f'{kind} {2*radius+1}x{2*radius+1}: {b[0]:.5f}, {b[1]*1000:.2f} ppt');ax.set_xlabel('BTJD')
fig.tight_layout();fig.savefig(out/'events.png',dpi=150)
(out/'measurements.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
r=rows[1];k=good&(abs(t-r['t0'])<1.5);x=t[k]-r['t0'];template=1-trap(t[k],r['t0'],1,r['T14_h']/24,r['T12_h']/24)
design=np.c_[np.ones(len(x)),x,x*x,-template];coef=np.linalg.lstsq(design,F[k].reshape(len(x),-1),rcond=None)[0];amp=coef[3].reshape(9,9);base=coef[0].reshape(9,9)
yy,xx=np.indices((9,9));sel=(abs(xx-xy[0])<2.5)&(abs(yy-xy[1])<2.5);weights=np.where(sel,np.maximum(amp,0),0);cen=[float((weights*xx).sum()/weights.sum()),float((weights*yy).sum()/weights.sum())]
pix=dict(target_pixel=xy.tolist(),deficit_centroid=cen,offset_arcsec=float(np.linalg.norm(np.array(cen)-xy)*21),central_depth_ppt=float(amp[iy,ix]/base[iy,ix]*1000),method='quadratic time trend plus fixed unit B trapezoid; positive 5x5 centroid; descriptive offset, not calibrated exclusion radius')
(out/'pixels.json').write_text(json.dumps(pix,indent=2)+'\n')
fig,axs=plt.subplots(1,3,figsize=(11,3));
for ax,z,title in zip(axs,[base,amp,np.divide(amp,base)],['baseline','flux deficit','fractional depth']):
 ax.imshow(z,origin='lower');ax.plot(*xy,'r+');ax.plot(*cen,'ro',fillstyle='none');ax.set_title(title)
fig.tight_layout();fig.savefig(out/'pixels.png',dpi=150);print(json.dumps(pix))

