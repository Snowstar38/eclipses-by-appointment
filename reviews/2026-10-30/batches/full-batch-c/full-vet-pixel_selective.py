"""Selective TIC362610608 localization from existing s63 TESScut.
Per-pixel quadratic plus integrated eclipse template; global OOT WCS/PSF
calibration against both Gaia stars, then fixed-position deficit fits.
"""
import json,csv,hashlib,sys
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from fit_batch import trap
ROOT=Path(__file__).parent
tic=sys.argv[1]; fn=next((Path('C:/Home/sky/data/sb1-scale-c3')/('vet'+tic)).glob('*.fits'))
r=json.load(open(ROOT/tic/'fit-results.json'));ep=r['ephemeris'];sh=r['shape']
with fits.open(fn,memmap=False) as h:
    d=h[1].data;t=np.array(d['TIME'],float);cube=np.array(d['FLUX'],float);q=np.array(d['QUALITY'],int);wcs=WCS(h[2].header)
good=np.isfinite(t)&(q==0)&np.all(np.isfinite(cube),axis=(1,2));t=t[good];cube=cube[good];cad=float(np.median(np.diff(t)))
ny,nx=cube.shape[1:];yy,xx=np.mgrid[:ny,:nx];flat=cube.reshape(len(t),-1)
depth=[];var=[];events=[]
for n in range(int(np.ceil((min(t)-ep['T0'])/ep['P'])),int(np.floor((max(t)-ep['T0'])/ep['P']))+1):
    tc=ep['T0']+n*ep['P'];sel=abs(t-tc)<max(.40,3*sh['T14']);x=t[sel]-tc
    if sum(abs(x)<sh['T14']/2)<5:continue
    template=trap(x,sh['T14'],sh['fr'],cad);A=np.column_stack([np.ones(len(x)),x,x*x,-template]);Y=flat[sel]
    coef=np.linalg.lstsq(A,Y,rcond=None)[0];res=Y-A@coef;v=np.sum(res*res,axis=0)/(len(x)-4)*np.linalg.pinv(A.T@A)[-1,-1]
    depth.append(coef[-1]);var.append(v);events.append(tc)
depth=np.array(depth);var=np.array(var);weight=1/np.maximum(var,1e-8);image=np.sum(weight*depth,axis=0)/np.sum(weight,axis=0);error=np.sqrt(1/np.sum(weight,axis=0))
phase=(t-ep['T0']+ep['P']/2)%ep['P']-ep['P']/2;oot=np.median(cube[abs(phase)>.15],axis=0).ravel()
stars=list(csv.DictReader(open(ROOT/(tic+'_neighbors_ari.csv'))));pos=np.array([wcs.all_world2pix(float(s['ra']),float(s['dec']),0) for s in stars])
def psf(px,py,sigma):
    # Pixel-integrated circular Gaussian, 5x5 quadrature.
    ans=np.zeros((ny,nx))
    for dx in np.linspace(-.4,.4,5):
      for dy in np.linspace(-.4,.4,5):ans+=np.exp(-((xx+dx-px)**2+(yy+dy-py)**2)/(2*sigma*sigma))/25
    return ans.ravel()
best=None
for sig in np.arange(.35,1.801,.05):
 for dx in np.arange(-.8,.801,.08):
  for dy in np.arange(-.8,.801,.08):
    A=np.column_stack([psf(p[0]+dx,p[1]+dy,sig) for p in pos]+[np.ones(nx*ny),xx.ravel(),yy.ravel()]);c=np.linalg.lstsq(A,oot,rcond=None)[0];chi=np.sum((oot-A@c)**2)
    if best is None or chi<best[0]:best=(chi,sig,dx,dy)
_,sig,dx,dy=best;fits_out=[]
for star,p in zip(stars,pos):
    A=np.column_stack([psf(p[0]+dx,p[1]+dy,sig),np.ones(nx*ny),xx.ravel(),yy.ravel()]);aw=A/error[:,None];c=np.linalg.lstsq(aw,image/error,rcond=None)[0];chi=float(np.sum(((image-A@c)/error)**2));fits_out.append(dict(source_id=star['source_id'],chi2=chi,amplitude=float(c[0])))
free=None
for px in np.arange(pos[0,0]-1,pos[0,0]+1.001,.04):
 for py in np.arange(pos[0,1]-1,pos[0,1]+1.001,.04):
    A=np.column_stack([psf(px+dx,py+dy,sig),np.ones(nx*ny),xx.ravel(),yy.ravel()]);aw=A/error[:,None];c=np.linalg.lstsq(aw,image/error,rcond=None)[0];chi=float(np.sum(((image-A@c)/error)**2))
    if free is None or chi<free[0]:free=(chi,px,py)
out=dict(source_path=str(fn),sha256=hashlib.sha256(fn.read_bytes()).hexdigest(),events=events,gaia_positions=pos.tolist(),calibration=dict(sigma=sig,dx=dx,dy=dy),fixed_fits=fits_out,free_best=dict(chi2=free[0],x=free[1],y=free[2],target_distance_arcsec=float(np.linalg.norm(np.array(free[1:])-pos[0])*21)),caution='Gaussian PSF approximate; formal pixel chi2 excludes PSF systematic covariance. Relative source discrimination, not precise astrometry.')
json.dump(out,open(ROOT/tic/'pixel-localization.json','w'),indent=2);print(tic,json.dumps(out,indent=2))

