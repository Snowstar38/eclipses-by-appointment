import numpy as np,json
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
from pathlib import Path
B=Path(__file__).resolve().parent;tic='449012335';h=B/'helper-pixels'/tic;g=json.loads((B/'SOURCE-SNAPSHOT.json').read_text())[tic]['target']['gaia']
with fits.open(h/'tesscut.fits',memmap=False) as f: t=np.array(f[1].data['TIME'],float);v=np.array(f[1].data['FLUX'],float);q=np.array(f[1].data['QUALITY']);w=WCS(f[2].header)
tx,ty=w.all_world2pix(float(g['ra']),float(g['dec']),0);ix=round(float(tx));iy=round(float(ty));ok=np.isfinite(t)&(q==0)&np.isfinite(v).all(axis=(1,2))&(t>4083.4)&(t<4086.8);t=t[ok];v=v[ok];v-=np.median(np.sort(v.reshape(len(v),-1),axis=1)[:,:48],axis=1)[:,None,None]; result={}
for r in (0,1,2):
 y=v[:,iy-r:iy+r+1,ix-r:ix+r+1].sum(axis=(1,2));base=np.median(y);y/=base
 def fun(p):
  c,d,width,ingress,b,s=p;z=np.maximum(0,np.minimum(1,(width/2-np.abs(t-c))/ingress));return b+s*(t-4085.2)-d*z-y
 fit=least_squares(fun,[4085.2,.04,1.5,.18,1.,0.],bounds=([4084.8,0,.7,.02,.8,-.2],[4085.6,.2,2.5,.7,1.2,.2])); cov=np.linalg.pinv(fit.jac.T@fit.jac)*(np.sum(fit.fun**2)/(len(t)-len(fit.x))); formal=float(np.sqrt(cov[0,0])); result[f'{2*r+1}x{2*r+1}']={'mid_btjd':float(fit.x[0]),'formal_center_error_days':formal,'central_loss_fraction':float(fit.x[1]/fit.x[4]),'duration_days':float(fit.x[2]),'ingress_days':float(fit.x[3]),'samples':len(t),'note':'Unweighted iid least-squares covariance formal error; correlated noise, detrending, aperture and model systematics omitted; same photons.'}
print(json.dumps(result,indent=2)); (h/'custom-local-fit.json').write_text(json.dumps(result,indent=2)+'\n')
