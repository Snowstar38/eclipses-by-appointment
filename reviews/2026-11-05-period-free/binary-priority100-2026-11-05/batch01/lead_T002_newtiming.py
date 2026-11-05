"""Measure newly available T002 pixel-light-curve events and the P/2 null."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;tic='92234103';rr=json.loads((B/'lead-newsector-fetch.json').read_text());q=next(x for x in json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())['queue_row'].items() if x[0]=='ra_deg')
ra=float(dict(json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())['queue_row'])['ra_deg']);dec=float(dict(json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())['queue_row'])['dec_deg'])
def model(x,b,s,d,c,w,e):return b+s*x-d*np.clip((w/2-np.abs(x-c))/e,0,1)
data={};results=[];fig,axs=plt.subplots(3,1,figsize=(9,7))
for ax,(sector,seed) in zip(axs,[(105,4217.19),(108,4291.05),(108,4315.67)]):
 r=next(x for x in rr if x['tic']==tic and x['sector']==sector);p=Path(r['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==r['fits_sha256']
 if sector not in data:
  with fits.open(p,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);cube=np.asarray(a['FLUX'],float);qual=np.asarray(a['QUALITY'],int);w=WCS(h[2].header)
  valid=np.isfinite(t)&(qual==0);t=t[valid];cube=cube[valid];tx,ty=map(float,w.all_world2pix(ra,dec,0));yy,xx=np.indices(cube.shape[1:]);mask=(abs(xx-round(tx))<=1)&(abs(yy-round(ty))<=1);bg=np.nanmedian(np.sort(cube.reshape(len(cube),-1),axis=1)[:,:40],axis=1);f=np.nansum(cube[:,mask],axis=1)-bg*np.isfinite(cube[:,mask]).sum(axis=1);data[sector]=(t,f,[tx,ty],r['fits_sha256'])
 t,f,xy,sha=data[sector];local=np.abs(t-seed)<.7;x=t[local]-seed;y=f[local];side=np.abs(x)>.22;base=float(np.median(y[side]));yn=y/base;cad=float(np.median(np.diff(t)))
 rec=dict(sector=sector,seed_btjd=seed,source_sha256=sha,target_pixel=xy,ap3_baseline=base,cadence_days=cad,local_n=int(sum(local)),local_first_btjd=float(t[local].min()),local_last_btjd=float(t[local].max()),local_max_gap_days=float(np.max(np.diff(t[local]))))
 try:
  par,cov=curve_fit(model,x,yn,p0=[1,0,.1,0,.24,.06],bounds=([.7,-.2,0,-.25,.05,.005],[1.3,.2,.5,.25,.6,.3]),maxfev=20000)
  rec.update(center_btjd=float(seed+par[3]),center_formal_error_days=float(np.sqrt(cov[3,3])) if cov[3,3]>0 else None,depth_ppt=float(1000*par[2]*min(1,par[4]/(2*par[5]))),duration_days=float(par[4]));fit=model(x,*par)
 except Exception as e:rec['error']=repr(e);fit=None
 results.append(rec);ax.plot(x,yn,'.',ms=2);ax.plot(x,fit,'r-',lw=1) if fit is not None else None;ax.set_title(f's{sector} near {seed}, center {rec.get("center_btjd")}, depth {rec.get("depth_ppt")}');ax.set_ylabel('AP3 / side')
fig.tight_layout();fig.savefig(B/tic/'lead-new-events.png',dpi=130);plt.close(fig)
# P/2 alias predicts a deep event halfway between two full S108 occasions.
t,f,xy,sha=data[108];pred=4315.67-24.620857/2;dt=t-pred;core=np.abs(dt)<.12;left=(dt>-.6)&(dt<-.25);right=(dt>.25)&(dt<.6);base=float(np.median(np.r_[f[left],f[right]]));ct=t[core]
null=dict(predicted_btjd=pred,period_alias_days=24.620857/2,source_sha256=sha,target_pixel=xy,ap3_baseline=base,quality0_core_n=int(sum(core)),expected_core_n=.24/np.median(np.diff(t)),quality0_left_n=int(sum(left)),quality0_right_n=int(sum(right)),core_first_btjd=float(ct.min()),core_last_btjd=float(ct.max()),core_max_gap_days=float(np.max(np.diff(ct))),core_median_deficit_ppt=float((1-np.median(f[core])/base)*1000),side_scatter_ppt=float(1.4826*np.median(abs(np.r_[f[left],f[right]]/base-1))*1000))
(B/tic/'lead-new-timing.json').write_text(json.dumps(dict(events=results,half_period_null=null),indent=2)+'\n')
print(json.dumps(dict(events=results,half_period_null=null),indent=2))
