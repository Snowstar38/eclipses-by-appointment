import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;S=B.parent.parent/'fresh-band'/'data'
def trap(x,b,s,d,c,w,ing):return b+s*x-d*np.clip((w/2-np.abs(x-c))/ing,0,1)
out=[];fig,axs=plt.subplots(3,1,figsize=(9,8))
for ax,(sec,pred,kind) in zip(axs,[(98,4038.52,'QLP raw SAP'),(106,4247.117,'TESSCut centered 3x3'),(108,4299.259,'TESSCut centered 3x3')]):
 if sec==98:
  with fits.open(S/f'768070_s{sec:03d}.fits') as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 else:
  with fits.open(B/f'lead-extra-s{sec}.fits') as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['FLUX'],float);q=np.asarray(a['QUALITY'],int)
   sky=np.nanmedian(f[:,[0,0,4,4],[0,4,0,4]],axis=1);y=np.nansum(f[:,1:4,1:4],axis=(1,2))-9*sky
 ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0)&(np.abs(t-pred)<.48);x=t[ok]-pred;v=y[ok]
 oot=np.abs(x)>.13;baseline=float(np.median(v[oot]));z=v/baseline
 noise=max(.0002,float(1.4826*np.median(np.abs(z[oot]-np.median(z[oot])))))
 p,cov=curve_fit(trap,x,z,p0=[1,0,.05,0,.17,.05],bounds=([.8,-.5,0,-.1,.04,.005],[1.2,.5,.5,.1,.4,.16]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000)
 fit=trap(x,*p);err=float(np.sqrt(cov[3,3]));out.append(dict(sector=sec,kind=kind,center_btjd=float(pred+p[3]),formal_center_error_d=err,depth_ppt=float(p[2]*1000),duration_d=float(p[4]),n=len(x),cadence_d=float(np.median(np.diff(t[ok]))),first_btjd=float(t[ok].min()),last_btjd=float(t[ok].max()),noise_ppt=noise*1000,resid_rms_ppt=float(np.std(z-fit)*1000),model_params=p.tolist()))
 ax.plot(x,z,'.',ms=2);ax.plot(x,fit,'r-',lw=1);ax.set_title(f'S{sec} {kind} center {pred+p[3]:.6f} depth {p[2]*1000:.1f} ppt');ax.set_ylabel('local normalized flux');ax.grid(alpha=.2)
axs[-1].set_xlabel('days from provisional center');fig.tight_layout();fig.savefig(B/'lead-s98-s106-s108-zooms.png',dpi=140)
for e in out:print(e['sector'],e['center_btjd'],e['depth_ppt'],e['duration_d'],e['formal_center_error_d'])
(B/'lead-new-clock.json').write_text(json.dumps(out,indent=2),encoding='utf8')
