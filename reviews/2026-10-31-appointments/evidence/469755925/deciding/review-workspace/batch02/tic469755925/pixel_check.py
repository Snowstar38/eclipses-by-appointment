import json,numpy as np,pathlib,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
out=pathlib.Path(__file__).parent
src=pathlib.Path('[local path omitted] 5.1/made/appointments/vet469755925')
g=json.loads((src/'gaia.json').read_text());star=g['src'][0]
with fits.open(out/'tesscut_s013.fits') as h:
 d=h[1].data;t=np.array(d['TIME']);f=np.array(d['FLUX'],float);q=np.array(d['QUALITY']);w=WCS(h[2].header)
results=[]
for kind,tc,dur,ing in [('A',1675.7384,7.55,1.55),('B',1663.2814,7.94,1.55)]:
 ok=np.isfinite(t)&(q==0)&(abs(t-tc)<0.8)&np.all(np.isfinite(f),axis=(1,2));tt=t[ok];ff=f[ok];x=tt-tc
 # Exposure-integrated trapezoid, quadratic local trend, per-cadence corner-background subtraction.
 off=np.linspace(-.0104,.0104,21);z=abs(x[:,None]+off);D=np.clip((dur/48-z)/(ing/24),0,1).mean(axis=1)
 bg=np.median(np.sort(ff.reshape(len(ff),-1),axis=1)[:,:40],axis=1);ff=ff-bg[:,None,None]
 A=np.array([np.ones(len(x)),x,x*x,-D]).T;c=np.linalg.lstsq(A,ff.reshape(len(ff),-1),rcond=None)[0];base=c[0].reshape(11,11);amp=c[3].reshape(11,11)
 res=ff.reshape(len(ff),-1)-A@c;err=(res.std(axis=0)*np.sqrt(np.linalg.inv(A.T@A)[3,3])).reshape(11,11)
 tx,ty=w.all_world2pix(float(star['ra']),float(star['dec']),0);ix,iy=round(float(tx)),round(float(ty));yy,xx=np.mgrid[:11,:11];m=(abs(xx-ix)<=2)&(abs(yy-iy)<=2);v=np.clip(amp,0,None)*m;cx=(v*xx).sum()/v.sum();cy=(v*yy).sum()/v.sum()
 r=dict(kind=kind,n=len(tt),n_in=int(sum(D>.5)),target=[float(tx),float(ty)],deficit=[cx,cy],offset_arcsec=float(np.hypot(cx-tx,cy-ty)*21),target_depth=float(amp[iy,ix]/base[iy,ix]),target_depth_err=float(err[iy,ix]/base[iy,ix]),neighbors=[])
 for nb in g['nb']:
  if float(nb.get('phot_g_mean_mag') or 99)>16:continue
  nx,ny=w.all_world2pix(float(nb['ra']),float(nb['dec']),0);jx,jy=round(float(nx)),round(float(ny))
  if 0<=jx<11 and 0<=jy<11:r['neighbors'].append(dict(G=nb['phot_g_mean_mag'],sep=nb.get('sep'),pixel=[float(nx),float(ny)],depth=float(amp[jy,jx]/base[jy,jx])))
 fig,ax=plt.subplots(1,3,figsize=(12,4))
 for a,img,title in zip(ax,[base,amp,amp/err],['Baseline','Eclipse flux deficit','Deficit S/N']):a.imshow(img,origin='lower');a.plot(tx,ty,'r+');a.set_title(title)
 ax[1].plot(cx,cy,'wo',mfc='none');fig.suptitle(f'TIC 469755925 sector 13 {kind}');fig.tight_layout();fig.savefig(out/f'pixel_{kind}.png');plt.close(fig);results.append(r)
(out/'pixel_results.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
