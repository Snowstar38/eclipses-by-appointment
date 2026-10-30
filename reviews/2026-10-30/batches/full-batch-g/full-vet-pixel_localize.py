import json,csv,hashlib,sys
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from fit_batch import trap,linear
D=Path(__file__).parent;tic=sys.argv[1];sec=int(sys.argv[2]);fn=Path('C:/Home/sky/data/sb1-scale-c3')/('vet'+tic)/f'tesscut_s{sec:03}.fits';r=json.load(open(D/tic/'fit-results.json'));ep=r['ephemeris'];sh=r['shape'];T=sh['T14'];fr=sh['fr']
with fits.open(fn,memmap=False) as h:
 assert h[0].header['SECTOR']==sec
 a=h[1].data;t=np.array(a['TIME'],float);cube=np.array(a['FLUX'],float);q=np.array(a['QUALITY'],int);wcs=WCS(h[2].header)
good=np.isfinite(t)&(q==0)&np.all(np.isfinite(cube),axis=(1,2));t=t[good];cube=cube[good];cad=float(np.median(np.diff(t)));ny,nx=cube.shape[1:];yy,xx=np.mgrid[:ny,:nx];flat=cube.reshape(len(t),-1);depth=[];var=[];events=[];aperture=[]
stars=list(csv.DictReader(open(D/(tic+'_neighbors_ari.csv'))));pos=np.array([wcs.all_world2pix(float(s['ra']),float(s['dec']),0) for s in stars]); assert float(stars[0]['sep'])<.01
X=xx.ravel();Y=yy.ravel();ap=((X-pos[0,0])**2+(Y-pos[0,1])**2)<2.25;bg=((X-pos[0,0])**2+(Y-pos[0,1])**2)>25;af=flat[:,ap].sum(axis=1)-np.median(flat[:,bg],axis=1)*sum(ap)
for n in range(int(np.ceil((min(t)-ep['T0'])/ep['P'])),int(np.floor((max(t)-ep['T0'])/ep['P']))+1):
 tc=ep['T0']+n*ep['P'];w=max(.4,3*T);sel=abs(t-tc)<w;x=t[sel]-tc
 if sum(abs(x)<T/2)<4 or sum(x<-.65*T)<5 or sum(x>.65*T)<5:continue
 template=trap(x,T,fr,cad);A=np.column_stack([np.ones(len(x)),x/w,(x/w)**2,-template]);vals=flat[sel];coef=np.linalg.lstsq(A,vals,rcond=None)[0];res=vals-A@coef;v=np.sum(res*res,axis=0)/max(len(x)-4,1)*np.linalg.pinv(A.T@A)[-1,-1];depth.append(coef[-1]);var.append(v);events.append(float(tc))
 y=af[sel];y=y/np.median(y);fits1=[]
 for deg in [1,2]:
  z=linear(x/w,y,template,deg);fits1.append(dict(degree=deg,depth=float(z[1][-1]),formal_error=float(np.sqrt(max(z[3][-1,-1],0)))))
 aperture.append(dict(tc=float(tc),fits=fits1,n_core=int(sum(abs(x)<T/2))))
depth=np.array(depth);var=np.array(var);weight=1/np.maximum(var,1e-8);image=np.sum(weight*depth,axis=0)/np.sum(weight,axis=0);error=np.sqrt(1/np.sum(weight,axis=0));phase=(t-ep['T0']+ep['P']/2)%ep['P']-ep['P']/2;oot=np.median(cube[abs(phase)>max(.15,T)],axis=0).ravel()
def psf(px,py,sig):
 ans=np.zeros((ny,nx))
 for dx in (-.33,0,.33):
  for dy in (-.33,0,.33):ans+=np.exp(-((xx+dx-px)**2+(yy+dy-py)**2)/(2*sig*sig))/9
 return ans.ravel()
best=None
for sig in np.arange(.45,1.51,.1):
 for dx in np.arange(-.5,.501,.1):
  for dy in np.arange(-.5,.501,.1):
   calpos=list(pos); A=np.column_stack([psf(p[0]+dx,p[1]+dy,sig) for p in calpos]+[np.ones(nx*ny),X,Y]);c=np.linalg.lstsq(A,oot,rcond=None)[0];score=np.sum((oot-A@c)**2)
   if best is None or score<best[0]:best=(score,sig,dx,dy)
_,sig,dx,dy=best
def evalpos(p,im=image,err=error):
 A=np.column_stack([psf(p[0]+dx,p[1]+dy,sig),np.ones(nx*ny),X,Y]);c=np.linalg.lstsq(A/err[:,None],im/err,rcond=None)[0];return float(np.sum(((im-A@c)/err)**2)),float(c[0]),float(np.linalg.norm(im-A@c)/np.linalg.norm(im))
fixed=[dict(source_id=s['source_id'],sep_arcsec=float(s['sep']),G=float(s['phot_g_mean_mag']),chi2=evalpos(p)[0],amplitude=evalpos(p)[1],fractional_residual=evalpos(p)[2]) for s,p in zip(stars,pos)]
free=None
for px in np.arange(pos[0,0]-2,pos[0,0]+2.001,.1):
 for py in np.arange(pos[0,1]-2,pos[0,1]+2.001,.1):
  score,amp,resid=evalpos([px,py])
  if free is None or score<free[0]:free=(score,px,py,amp,resid)
jack=[]
for i in range(len(events)):
 im=depth[i];err=np.sqrt(np.maximum(var[i],1e-8));scores=[evalpos(p,im,err)[0] for p in pos];jack.append(dict(tc=events[i],best_source=stars[int(np.argmin(scores))]['source_id'],delta_chi2_neighbor_minus_target=[float(v-scores[0]) for v in scores]))
out=dict(source_path=str(fn),sha256=hashlib.sha256(fn.read_bytes()).hexdigest(),sector=sec,gaia_target=stars[0],target_wcs_pixel=pos[0].tolist(),gaia_positions=pos.tolist(),events=events,calibration=dict(sigma_pixels=float(sig),dx_pixels=float(dx),dy_pixels=float(dy)),fixed_fits=fixed,free_best=dict(chi2=free[0],pixel_x=free[1],pixel_y=free[2],distance_from_target_arcsec=float(np.linalg.norm(np.array(free[1:3])-pos[0])*21),fractional_residual=free[4]),event_source_comparisons=jack,aperture_photometry=aperture,calibration_note='Approximate Gaussian PSFs at own Gaia cone positions; no extra empirical source.',caution='Same TESS pixels as QLP, independent aperture reduction. Approximate circular Gaussian PSF calibrated to multi-star out-of-eclipse image; formal chi2 excludes PSF mismatch, correlated pixels/time and sector-level systematics. No formal significance from delta-chi2; compare event repeatability and residuals. Aperture depth errors are white-noise conditional only; degree comparison probes baseline sensitivity.')
json.dump(out,open(D/tic/'pixel-localization.json','w'),indent=2,allow_nan=False);print(tic,json.dumps(dict(events=len(events),cal=out['calibration'],fixed=fixed,free=out['free_best'],jack=jack),indent=2))


