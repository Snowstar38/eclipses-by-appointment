from pathlib import Path
import json,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
from scipy.optimize import curve_fit
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(__file__).parent;t='154652154';m=json.load(open(b/t/'measurements.json'));d=json.load(open(b/t/'fresh-pixels/diff_fresh.json'));g=json.load(open(b/t/'fresh-pixels/gaia.json'))['src'][0];p=Path('local-source/sky/data/sb1-scale-c3/vet154652154/tesscut_s057.fits')
with fits.open(p) as h:
 a=h[1].data;tm=np.array(a['TIME']);F=np.array(a['FLUX']);q=np.array(a['QUALITY']);w=WCS(h[2].header)
ok=np.isfinite(tm)&np.all(np.isfinite(F.reshape(len(tm),-1)),1)&(q==0);tm=tm[ok];F=F[ok];flat=F.reshape(len(tm),-1);bg=np.median(np.sort(flat)[:,:int(.4*flat.shape[1])],axis=1);F-=bg[:,None,None];x,y=w.all_world2pix(float(g['ra']),float(g['dec']),0);ix,iy=round(float(x)),round(float(y));f=F[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2));dur=np.median([e['duration_days'] for e in m['events']]);events=[];fig,axs=plt.subplots(3,1,figsize=(9,7))
def mod(x,b,s,d,c,w,k):return b+s*x-d*np.clip((w/2-abs(x-c))/k,0,1)
for ax,e in zip(axs,d['events']):
 pred=e['t'];sel=abs(tm-pred)<3*dur;xx=tm[sel]-pred;yy=f[sel];oot=abs(xx)>dur;yy/=np.median(yy[oot]);noise=1.4826*np.median(abs(yy[oot]-np.median(yy[oot])));v,c=curve_fit(mod,xx,yy,p0=[1,0,.08,0,dur,.2*dur],bounds=([.7,-1,0,-dur,.3*dur,.01*dur],[1.3,1,1,dur,3*dur,dur]),sigma=np.full(len(xx),noise),absolute_sigma=True,maxfev=20000);events.append(dict(cycle=e['cycle'],mid_btjd=pred+v[3],formal_center_error_days=float(np.sqrt(c[3,3])),depth_ppt=v[2]*1000));ax.plot(xx,yy,'.',ms=2);ax.plot(xx,mod(xx,*v),'r-');ax.set_title(str(events[-1]))
fig.tight_layout();fig.savefig(b/t/'cutout-s57-events.png',dpi=120);json.dump(dict(tic=t,sector=57,events=events,consecutive_separation_days=events[2]['mid_btjd']-events[1]['mid_btjd'],note='Free-center custom3x3 aperture timing on independent sector57 TESS photons. Supports same-kind cycle count; not added to quoted QLP ephemeris. Formal covariance errors uncalibrated.'),open(b/t/'cutout-s57-timing.json','w'),indent=2)
