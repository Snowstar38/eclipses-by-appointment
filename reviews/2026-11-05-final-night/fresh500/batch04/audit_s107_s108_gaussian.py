import json,numpy as np
from pathlib import Path
from scipy.optimize import least_squares
from astropy.io import fits
from astropy.wcs import WCS
b=Path(__file__).resolve().parent;d=b/'48099288';ctx=json.loads((d/'lead-context.json').read_text());h=ctx['sectors'][0]['header'];ra,dec=h['RA_OBJ'],h['DEC_OBJ'];ng=json.loads((d/'lead-neighbors.json').read_text())['neighbors']; ids=['2925011408780139520','2925011477499610496'];rng=np.random.default_rng(9813); result={}
for sec,c,dur in [(107,4275.577562,.12753),(108,4313.440381,.13524)]:
 with fits.open(d/f'extra-s{sec}.fits') as f:
  t=np.array(f[1].data['TIME']);q=np.array(f[1].data['QUALITY']);cube=np.array(f[1].data['FLUX']);w=WCS(f[2].header);x,y=map(float,w.world_to_pixel_values(ra,dec))
 z=t-c;core=(q==0)&np.isfinite(t)&(abs(z)<dur*.25);side=(q==0)&np.isfinite(t)&(abs(z)>dur*.75)&(abs(z)<.4);p=np.polyfit(z[side],cube[side].reshape(side.sum(),-1),1);res=cube.reshape(len(t),-1)-(z[:,None]*p[0]+p[1]);a=res[core];s=res[side];yy,xx=np.indices(cube.shape[1:]);xx=xx.ravel();yy=yy.ravel();neighbors=[tuple(map(float,w.world_to_pixel_values(float(n['ra']),float(n['dec'])))) for n in ng if n['source_id'] in ids]
 def fit(v,start=None):
  v=v.ravel();amp=max(v.max()-np.median(v),1e-3)
  def fun(k):
   A,cx,cy,sig,b0,bx,by=k; return A*np.exp(-((xx-cx)**2+(yy-cy)**2)/(2*sig**2))+b0+bx*(xx-2)+by*(yy-2)-v
  r=least_squares(fun,[amp,x,y,.8,np.median(v),0,0] if start is None else start,bounds=([0,0,0,.35,-np.inf,-np.inf,-np.inf],[np.inf,4,4,2,np.inf,np.inf,np.inf]),max_nfev=300);return r.x
 base=np.median(s,axis=0)-np.median(a,axis=0);k=fit(base);samples=[]
 for i in range(200):
  v=np.median(s[rng.integers(len(s),size=len(s))],axis=0)-np.median(a[rng.integers(len(a),size=len(a))],axis=0);samples.append(fit(v,k)[1:3])
 sam=np.array(samples);ds=np.linalg.norm(sam-np.array([x,y]),axis=1); dn=[np.linalg.norm(sam-n,axis=1) for n in neighbors];result[str(sec)]=dict(target=[x,y],neighbor_xy=neighbors,fit=k.tolist(),bootstrap_target_preference=[float(np.mean(ds<v)) for v in dn],bootstrap_xy_quantiles=np.quantile(sam,[.025,.5,.975],axis=0).tolist())
(d/'audit-s107-s108-gaussian.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
