import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());tic='25320385';m=json.loads((B/tic/'measurements.json').read_text());P=m['period_days'];epoch=m['reference_epoch_btjd'];out=[];panels=[]
def model(x,b,s,d,c,w,k):return b+s*x-d*np.clip((w/2-abs(x-c))/k,0,1)
for r in D[tic]['target']['file_receipts']:
 if r['sector'] not in (8,9,62,89,99):continue
 with fits.open(r['path']) as h:a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
 for n in range(int((t.min()-epoch)/P)-1,int((t.max()-epoch)/P)+1):
  pred=epoch+(n+.5)*P;x=t[abs(t-pred)<.8]-pred;y=f[abs(t-pred)<.8];oot=abs(x)>.42
  if sum(abs(x)<.15)<3 or sum(oot&(x<0))<4 or sum(oot&(x>0))<4:continue
  y=y/np.median(y[oot]);noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-5)
  try:
   p,c=curve_fit(model,x,y,p0=[1,0,.007,0,.55,.22],bounds=([.9,-.1,0,-.2,.1,.02],[1.1,.1,.05,.2,1.2,.5]),maxfev=20000)
   e=dict(sector=r['sector'],cycle=n+.5,mid_btjd=float(pred+p[3]),central_loss_ppt=float(p[2]*min(1,p[4]/2/p[5])*1000),duration_days=float(p[4]),scatter_ppt=noise*1000);out.append(e);panels.append((e,x,y,model(x,*p)))
  except Exception:pass
(B/tic/'opposite-eclipse-kind.json').write_text(json.dumps(dict(period_tested_days=P,events=out,note='Half-phase independently fitted raw events; compares eclipse kinds, not assumed same-kind recurrence. Sector99 primary and secondary visibility changes must not be treated as clean orbital nulls.'),indent=2)+'\n')
fig,axs=plt.subplots(min(6,len(panels)),1,figsize=(9,12),squeeze=False)
for ax,(e,x,y,z) in zip(axs[:,0],panels):ax.plot(x,y,'.',ms=3);ax.plot(x,z,'r-');ax.set_title(str(e),fontsize=7)
fig.tight_layout();fig.savefig(B/tic/'opposite-eclipse-kind.png',dpi=110)
print(out)
