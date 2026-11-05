"""Inspect the unflagged third predicted T042 occasion in sector 66."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent/'255912894'
d=json.loads((B/'lead-numeric.json').read_text())
pred=4142.786 # fold prediction; the epoch is same kind as S13/S66/S100
a=json.loads((B/'lead-fold-windows.json').read_text())
o=[o for o in a['windows'] if o['sector']==102 and abs(o['pred_btjd']-pred)<1][0]
pred=o['pred_btjd'];path=[s['path'] for s in d['sources'] if s['sector']==102][0]
with fits.open(path,memmap=False) as h:
    x=h[1].data;t=np.asarray(x['TIME'],float);f=np.asarray(x['SAP_FLUX'],float);q=np.asarray(x['QUALITY'],int)
    alt=np.asarray(x['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in x.names else None
ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-pred)<.7);t=t[ok];f=f[ok]
if alt is not None:alt=alt[ok]
outer=(abs(t-pred)>.2)&(abs(t-pred)<.6)
fn=f/np.median(f[outer]);an=alt/np.median(alt[outer]) if alt is not None else None
def trap(z,b,s,dep,cen,width,edge):return b+s*z-dep*np.clip((width/2-abs(z-cen))/edge,0,1)
z=t-pred
p,cov=curve_fit(trap,z,fn,p0=[1,0,.003,0,.13,.02],bounds=([.97,-.1,0,-.1,.03,.005],[1.03,.1,.05,.1,.3,.1]),maxfev=20000)
error=float(np.sqrt(cov[3,3])) if cov[3,3]>0 else None
fig,ax=plt.subplots(figsize=(9,3));ax.plot(z,fn,'.',ms=2,label='QLP raw SAP');ax.plot(z,trap(z,*p),'r-',label='trapezoid');
if an is not None:ax.plot(z,an,'.',ms=1,alpha=.4,label='KSPSAP')
ax.legend();ax.set(xlabel='days from predicted center',ylabel='relative flux',title=f'T042 S102 predicted {pred:.5f}; raw center {pred+p[3]:.5f}')
fig.tight_layout();fig.savefig(B/'lead-fourth.png',dpi=140)
(B/'lead-fourth.json').write_text(json.dumps(dict(predicted_btjd=pred,fit_center_btjd=float(pred+p[3]),formal_error_days=error,depth_ppt=float(1000*p[2]*min(1,p[4]/(2*p[5]))),width_days=float(p[4]),side_n=int(sum(outer)),core_n=int(sum(abs(z)<.08)),source_path=path),indent=2)+'\n')
print((B/'lead-fourth.json').read_text())

