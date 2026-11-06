from pathlib import Path
import json,numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(__file__).resolve().parent;t=np.load(b/'48099288/extra-s107.npz')['time'];y=np.load(b/'48099288/extra-s107.npz')['flux'];pred=4275.58;ok=abs(t-pred)<.5;x=t[ok]-pred;z=y[ok];base=abs(x)>.2;scale=np.median(z[base]);z/=scale
def trap(x,b,s,d,c,w,ing):
 z=np.abs(x-c);return b+s*x-d*np.clip((w/2-z)/(w*ing),0,1)
p,cv=curve_fit(trap,x,z,p0=[1,0,.01,0,.15,.3],bounds=([.9,-.1,0,-.2,.03,.05],[1.1,.1,.1,.2,.5,.49]),maxfev=20000);err=np.sqrt(cv[3,3]);ev=dict(sector=107,screen_btjd=pred,kind='kindA',center_btjd=float(pred+p[3]),center_formal_error_d=float(err),depth_ppt=float(1000*p[2]),duration_d=float(p[4]),cadence_d=float(np.median(np.diff(x))),fit_usable=bool(err>0 and err<.03),source='extra-s107.fits',note='custom3x3 same-photon extraction; local fit and independent PSF attribution required')
(b/'48099288/lead-extra107-timing.json').write_text(json.dumps(ev,indent=2));print(ev)
fig,ax=plt.subplots(figsize=(10,3));ax.plot(x,z,'.',ms=2);ax.plot(x,trap(x,*p));ax.grid(alpha=.2);ax.set_title(str(ev));fig.tight_layout();fig.savefig(b/'48099288/extra-repeat107-fit.png',dpi=100)
