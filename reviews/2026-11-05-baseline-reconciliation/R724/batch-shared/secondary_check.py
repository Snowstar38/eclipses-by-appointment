import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());tic='421331604';m=json.loads((B/tic/'measurements.json').read_text());P=m['period_days'];epoch=m['reference_epoch_btjd'];out=[];panels=[]
def model(x,b,s,d,c,w,k):return b+s*x-d*np.clip((w/2-abs(x-c))/k,0,1)
for r in D[tic]['target']['file_receipts']:
 if r['sector'] not in (14,54,76,83):continue
 with fits.open(r['path']) as h:a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
 for n in range(math.ceil((t.min()-epoch)/P-.286),math.floor((t.max()-epoch)/P-.286)+1):
  pred=epoch+(n+.286)*P;ix=abs(t-pred)<.8;x=t[ix]-pred;y=f[ix];oot=abs(x)>.35
  if sum(abs(x)<.12)<3 or sum(oot&(x<0))<4 or sum(oot&(x>0))<4:continue
  y=y/np.median(y[oot]);noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-5)
  try:
   p,c=curve_fit(model,x,y,p0=[1,0,.01,0,.23,.08],bounds=([.9,-.05,0,-.15,.08,.01],[1.1,.05,.03,.15,.5,.3]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=20000)
   er=float(np.sqrt(c[3,3]));e=dict(sector=r['sector'],orbital_cycle=n,mid_btjd=float(pred+p[3]),phase=float(((pred+p[3]-epoch)/P)%1),formal_center_error_days=er,central_loss_ppt=float(p[2]*min(1,p[4]/2/p[5])*1000),duration_days=float(p[4]),scatter_ppt=noise*1000);out.append(e);panels.append((e,x,y,model(x,*p)))
  except Exception:pass
(B/tic/'opposite-eclipse-kind.json').write_text(json.dumps(dict(period_tested_days=P,events=out,note='Separately fitted shallower conjunction near phase0.286; these are other-kind eclipses and excluded from selected-kind ephemeris. Formal center errors only; raw SAP and local linear baseline.'),indent=2)+'\n')
fig,axs=plt.subplots(len(panels),1,figsize=(9,2.2*len(panels)),squeeze=False)
for ax,(e,x,y,z) in zip(axs[:,0],panels):ax.plot(x,y,'.',ms=2);ax.plot(x,z,'r-');ax.set_title(f"s{e['sector']} secondary phase {e['phase']:.5f}, loss {e['central_loss_ppt']:.2f}ppt",fontsize=9)
fig.tight_layout();fig.savefig(B/tic/'opposite-eclipse-kind.png',dpi=110)
print(out)
