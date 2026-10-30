import json, numpy as np
from pathlib import Path
from astropy.io import fits
from fit_batch import trap,linear
D=Path(__file__).parent
for tic in ['119301005','377656542','365181558']:
 p=D/tic;pix=json.load(open(p/'pixel-localization.json'));r=json.load(open(p/'fit-results.json'));sec=json.load(open(p/'secondary-fit.json'));ep=r['ephemeris'];sh=r['shape'];ss=json.load(open(p/'secondary-shape.json'))
 with fits.open(pix['source_path']) as h:
  a=h[1].data;t=np.array(a['TIME'],float);cube=np.array(a['FLUX'],float);q=np.array(a['QUALITY'],int)
 good=np.isfinite(t)&(q==0)&np.all(np.isfinite(cube),axis=(1,2));t=t[good];cube=cube[good];cad=float(np.median(np.diff(t)));ny,nx=cube.shape[1:];yy,xx=np.mgrid[:ny,:nx];x0,y0=pix['target_wcs_pixel'];ap=(xx-x0)**2+(yy-y0)**2<2.25;bg=(xx-x0)**2+(yy-y0)**2>25;flux=cube[:,ap].sum(axis=1)-np.median(cube[:,bg],axis=1)*sum(ap.ravel());out=[]
 for kind in ('primary','secondary'):
  phase=0 if kind=='primary' else sec['profile_phase']; shape=sh if kind=='primary' else ss;T=shape['T14'];fr=shape['fr'];
  for n in range(int(np.ceil((t.min()-ep['T0'])/ep['P']-phase)),int(np.floor((t.max()-ep['T0'])/ep['P']-phase))+1):
   tc=ep['T0']+(n+phase)*ep['P']
   for factor in ([2,3,4] if tic=='119301005' and kind=='primary' else [3]):
    w=max(.4,factor*T);m=abs(t-tc)<w;x=t[m]-tc;y=flux[m];
    if sum(abs(x)<T/2)<4 or sum(x<-.65*T)<5 or sum(x>.65*T)<5:continue
    y=y/np.median(y);temp=trap(x,T,fr,cad)
    for deg in (1,2):
     z=linear(x/w,y,temp,deg);res=z[2];beta=1.
     for mins in (20,40,60):
      bins=max(2,int(mins/1440/cad));nb=len(res)//bins
      if nb>=3:beta=max(beta,float(np.std(res[:nb*bins].reshape(nb,bins).mean(1),ddof=1)/(max(np.std(res,ddof=1),1e-12)/np.sqrt(bins))))
     error=float(np.sqrt(max(z[3][-1,-1],0))*beta);out.append(dict(kind=kind,tc=tc,window_halfwidth=w,degree=deg,depth=float(z[1][-1]),error=error,beta=beta,n_core=int(sum(abs(x)<T/2)),n_before=int(sum(x<-.65*T)),n_after=int(sum(x>.65*T))))
 json.dump(dict(source=pix['source_path'],source_sha256=pix['sha256'],secondary_phase=sec['profile_phase'],measurements=out,note='Same TESS pixels, separate background-subtracted aperture; fixed QLP template/ephemeris; beta-inflated errors conditional on baseline, not independent observatory.'),open(p/'targeted-aperture.json','w'),indent=2)
 print(tic,json.dumps(out))
