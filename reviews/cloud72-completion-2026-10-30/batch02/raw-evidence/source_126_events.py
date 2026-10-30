from pathlib import Path
import json, numpy as np, hashlib
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import least_squares
from scipy.special import erf
R=Path(__file__).parent; target=json.load(open(R.parent/'targets-selected.json'))['126363604']; raw=json.load(open(R/'raw-events.json'))['126363604']; DL=json.load(open(R/'tesscut-downloads.json')); out=[]
for d in DL:
 if d['tic']!='126363604':continue
 sec=d['sector']; p=R/d['tic']/d['members'][0]
 with fits.open(p,memmap=False) as h:
  a=h[1].data;t=np.array(a['TIME'],float);F=np.array(a['FLUX'],float);q=np.array(a['QUALITY']);tx,ty=WCS(h[2].header).all_world2pix(target['ra'],target['dec'],0)
 ok=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0);t=t[ok];F=F[ok];F-=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:48],axis=1)[:,None,None]
 for e in [x for x in raw['events'] if x['sector']==sec and not x['edge']]:
  x=t-e['tc']; D=e['duration_d']; i=abs(x)<.3*D; pre=(x<-.75*D)&(x>-1.75*D);post=(x>.75*D)&(x<1.75*D)
  if min(i.sum(),pre.sum(),post.sum())<2:continue
  O=(np.median(F[pre],axis=0)+np.median(F[post],axis=0))/2; Z=O-np.median(F[i],axis=0); yy,xx=np.mgrid[:11,:11];mask=(abs(xx-tx)<3.5)&(abs(yy-ty)<3.5);X=xx[mask];Y=yy[mask];z=Z[mask];scale=max(np.max(abs(z)),1)
  def model(a):
   amp,cx,cy,sx,sy,bg=a; return amp*(erf((X+.5-cx)/(2**.5*sx))-erf((X-.5-cx)/(2**.5*sx)))*(erf((Y+.5-cy)/(2**.5*sy))-erf((Y-.5-cy)/(2**.5*sy)))/4+bg
  fit=least_squares(lambda a:(model(a)-z)/scale,[max(z)*5,tx,ty,.7,.7,0],bounds=([0,tx-2,ty-2,.3,.3,-scale],[scale*200,tx+2,ty+2,2,2,scale]));a=fit.x
  fname=f'126_event_s{sec:03d}_{e["cycle"]}.npz';np.savez_compressed(R/'126363604'/fname,out=O,deficit=Z)
  out.append(dict(sector=sec,cycle=e['cycle'],tc=e['tc'],counts=[int(i.sum()),int(pre.sum()),int(post.sum())],target_px=[float(tx),float(ty)],gaussian_px=a[1:3].tolist(),offset_arcsec=float(np.hypot(a[1]-tx,a[2]-ty)*21),sigma_px=a[3:5].tolist(),residual_rms=float(np.std(model(a)-z)),array=fname,array_sha256=hashlib.sha256((R/'126363604'/fname).read_bytes()).hexdigest(),fits_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
json.dump(out,open(R/'126-event-source.json','w'),indent=2);print(out)
