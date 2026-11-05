"""Fit four same-kind T026 events found in raw SAP, then a linear clock."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='341688154';m=json.loads((B/tic/'lead-numeric.json').read_text())
def shape(x,base,slope,depth,center,width,edge):
    return base+slope*x-depth*np.clip((width/2-np.abs(x-center))/edge,0,1)
spec=[(14,1703.347,0),(21,1877.821,3),(48,2633.874,16),(74,3331.769,28)]
events=[];fig,axs=plt.subplots(4,1,figsize=(9,10))
for ax,(sector,seed,cycle) in zip(axs,spec):
    src=next(s for s in m['sources'] if s['sector']==sector);fp=Path(src['path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==src['sha256']
    with fits.open(fp,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int);names=d.names
        alt=np.asarray(d['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in names else None
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(np.abs(t-seed)<.55);x=t[ok]-seed;y=f[ok];side=np.abs(x)>.25;scale=np.median(y[side]);yn=y/scale
    p,cov=curve_fit(shape,x,yn,p0=[1,0,.007,0,.13,.04],bounds=([.95,-.05,0,-.08,.04,.01],[1.05,.05,.04,.08,.25,.15]),maxfev=30000)
    center=seed+p[3];err=float(np.sqrt(cov[3,3])) if cov[3,3]>0 else None
    resid=yn-shape(x,*p);noise=float(1.4826*np.median(np.abs(resid-np.median(resid))))
    rec=dict(sector=sector,cycle=cycle,seed_btjd=seed,mid_btjd=center,formal_mid_error_days=err,depth_ppt=1000*p[2]*min(1,p[4]/(2*p[5])),duration_days=p[4],edge_days=p[5],residual_scatter_ppt=1000*noise,n_quality0=len(x),source_sha256=src['sha256'])
    if alt is not None:
        aa=alt[ok];good=np.isfinite(aa)&(aa>0);core=np.abs(x)<.065;bl=(np.abs(x)>.18)&(np.abs(x)<.4);rec['alt_core_deficit_ppt']=1000*(1-np.median(aa[core&good])/np.median(aa[bl&good]))
    events.append(rec);ax.plot(x,yn,'.',ms=2);xx=np.linspace(-.5,.5,500);ax.plot(xx,shape(xx,*p),'r');ax.set_title(f's{sector} cycle {cycle} mid {center:.5f} depth {rec["depth_ppt"]:.2f} ppt');ax.set_ylabel('SAP / side')
T=np.array([e['mid_btjd'] for e in events]);C=np.array([e['cycle'] for e in events]);E=np.array([e['formal_mid_error_days'] for e in events]);floor=np.array([.01,.01,.006,.006]);W=1/np.maximum(E,floor)**2;X=np.stack((np.ones_like(C),C),axis=1);cov=np.linalg.inv((X.T*W)@X);coef=cov@((X.T*W)@T);res=T-X@coef;chi=float(np.sum(W*res**2));scale=max(1,(chi/(len(T)-2))**.5);sigma=np.sqrt(np.diag(cov))*scale
result=dict(events=events,epoch_btjd=float(coef[0]),period_days=float(coef[1]),epoch_error_days=float(sigma[0]),period_error_days=float(sigma[1]),residuals_days=list(map(float,res)),weighted_chi2=chi,scatter_inflation=scale,weight_floor_days=list(map(float,floor)),method='Local q0 raw SAP trapezoids; weighted line over same-kind cycle 0,3,16,28. Weights floor formal timing errors at stated values; multiply covariance errors by sqrt(reduced chi2) if >1. Alias coverage separate. QLP KSPSAP (same photons) is alternate reduction when available.')
(B/tic/'lead-timing.json').write_text(json.dumps(result,indent=2)+'\n')
axs[-1].set_xlabel('days from seed');fig.tight_layout();fig.savefig(B/tic/'lead-timing.png',dpi=130)
print(json.dumps(result,indent=2))
