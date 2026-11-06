import json,numpy as np
from pathlib import Path
from astropy.io import fits
from scipy.optimize import least_squares
B=Path(r'[workspace]/Astra/made/final-night-2026-11-05/fresh500/batch03');rng=np.random.default_rng(20261105);out={}
for tic in ['399027834','451669009','382672776']:
 p=B/tic;l=json.loads((p/'helper-localization.json').read_text());neighbors=json.loads((p/'lead-neighbors.json').read_text())['neighbors'];x,y=l['target_xy'];c=l['event']['center_btjd'];dur=l['event']['duration_d'];
 with fits.open(p/'helper-tesscut.fits') as h:
  a=h[1].data;t=np.array(a['TIME']);q=np.array(a['QUALITY']);cube=np.array(a['FLUX'])
 good=(q==0)&np.isfinite(t);core=cube[good&(abs(t-c)<dur*.25)];side=cube[good&(abs(t-c)>dur*.75)&(abs(t-c)<dur*2)];yy,xx=np.indices(cube.shape[1:]);mask=np.hypot(xx-x,yy-y)<3.4
 def fit(im):
  def fun(v):
   amp,cx,cy,sx,sy,angle,b,gx,gy=v;ca=np.cos(angle);sa=np.sin(angle);dx=xx-cx;dy=yy-cy;u=ca*dx+sa*dy;w=-sa*dx+ca*dy;mod=amp*np.exp(-.5*((u/sx)**2+(w/sy)**2))+b+gx*dx+gy*dy;return (mod-im)[mask]
  amp=max(float(np.nanmax(im)-np.nanmedian(im)),.001);v=[amp,x,y,.8,.8,0,0,0,0];lo=[0,x-2,y-2,.3,.3,-np.pi,-np.inf,-np.inf,-np.inf];hi=[np.inf,x+2,y+2,3,3,np.pi,np.inf,np.inf,np.inf];z=least_squares(fun,v,bounds=(lo,hi),max_nfev=500);return z.x, float(np.sqrt(np.mean(z.fun**2)))
 im=np.nanmedian(side,axis=0)-np.nanmedian(core,axis=0);par,rms=fit(im);samples=[]
 for _ in range(250):
  try:
   im1=np.nanmedian(side[rng.integers(0,len(side),len(side))],axis=0)-np.nanmedian(core[rng.integers(0,len(core),len(core))],axis=0);a,_=fit(im1);samples.append(a[1:3])
  except Exception:pass
 samples=np.array(samples); ns=[]
 for n in neighbors:
  if n.get('relative_G_flux') is None:continue
  nx,ny=n['pixel_xy'];dist=float(np.hypot(nx-x,ny-y))
  if .05<dist<3 and (n['relative_G_flux']>.005 or tic=='382672776'):ns.append({'id':n['source_id'],'xy':[nx,ny],'distance_px':dist,'G_ratio':n['relative_G_flux'],'distance_from_fit_px':float(np.hypot(nx-par[1],ny-par[2]))})
 ns=sorted(ns,key=lambda a:a['distance_px'])[:12];out[tic]={'target_xy':[x,y],'fit_center_xy':par[1:3].tolist(),'target_fit_distance_px':float(np.hypot(par[1]-x,par[2]-y)),'width_xy':par[3:5].tolist(),'fit_rms':rms,'bootstrap_n':len(samples),'bootstrap_xy_q025_q50_q975':np.quantile(samples,[.025,.5,.975],axis=0).tolist(),'neighbors':ns,'caveat':'Gaussian plus plane is a proxy, bootstrap samples temporal scatter only; PRF, WCS and systematics are uncalibrated.'}
(B/'audit-spatial-gaussian.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
