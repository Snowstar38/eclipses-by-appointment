import json, math
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit

B=Path(__file__).resolve().parent
D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text())
tic='280950412'; s=D[tic]; P=s['screen']['P']['P']; t0=s['screen']['P']['t0']
def model(x,b,m,d,c,w):
    return b+m*x-d*np.clip((w/2-np.abs(x-c))/.06,0,1)
out=[]
for r in s['target']['file_receipts']:
    with fits.open(r['path']) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
    for n in range(math.ceil((t.min()-t0)/P),math.floor((t.max()-t0)/P)+1):
        p=t0+n*P;x=t-p;ix=np.abs(x)<1.2;x=x[ix];y=f[ix]
        if len(x)<30:continue
        oot=np.abs(x)>.6
        if sum(oot&(x<0))<6 or sum(oot&(x>0))<6:continue
        y=y/np.median(y[oot]); noise=1.4826*np.median(abs(y[oot]-np.median(y[oot])))
        z=np.abs(x)<.2
        if sum(z)<3:continue
        deficit=1-np.median(y[z]); low=1-np.median(np.sort(y[z])[:max(2,sum(z)//3)])
        try:
            pars,cov=curve_fit(model,x,y,p0=[1,0,max(low,.0002),0,.35],bounds=([.9,-.1,0,-.3,.08],[1.1,.1,.2,.3,1.]),maxfev=20000)
            rec=dict(sector=r['sector'],cycle=n,predicted_btjd=p,center_btjd=p+pars[3],depth_ppt=pars[2]*1000,width_days=pars[4],formal_center_error_days=np.sqrt(cov[3,3]) if cov[3,3]>0 else None,core_median_ppt=deficit*1000,core_low_ppt=low*1000,oot_scatter_ppt=noise*1000,n=len(x))
        except Exception as exc:rec=dict(sector=r['sector'],cycle=n,error=str(exc))
        out.append(rec)
(B/'weak-events-280950412.json').write_text(json.dumps(out,indent=2)+'\n')
for e in out:print(e)
