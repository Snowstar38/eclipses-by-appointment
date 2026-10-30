import json,pathlib,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
R=pathlib.Path(__file__).parent;data=json.load(open(R/'raw-events.json'))
fig,axes=plt.subplots(10,2,figsize=(12,23),squeeze=False)
for row,(tic,r) in enumerate(data.items()):
 ev=[e for e in r['events'] if 'tc'in e and not e['edge']]; chosen=[ev[0],ev[-1]] if len(ev)>1 else ev
 for j,ax in enumerate(axes[row]):
  if j>=len(chosen):ax.axis('off');continue
  e=chosen[j];f=R/tic/('qlp_s%03d.fits'%e['sector']);T=e['duration_d'];tc=e['tc'];w=min(.3*r['search_period'],max(.45,4*T))
  with fits.open(f) as h:
   d=h[1].data;t=np.asarray(d['TIME'],float);y=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY']); m=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[m];y=y[m];y/=np.median(y)
  m=abs(t-tc)<w;x=t[m]-tc;z=y[m];shape=np.clip((T/2-abs(x))/(T*e['ingress_fraction']),0,1);A=np.column_stack((np.ones(len(x)),x,x*x));base=np.linalg.lstsq(A,z+e['depth']*shape,rcond=None)[0];xx=np.linspace(-w,w,600);sh=np.clip((T/2-abs(xx))/(T*e['ingress_fraction']),0,1); yy=base[0]+base[1]*xx+base[2]*xx**2-e['depth']*sh
  ax.scatter(x,z,s=3,alpha=.5,color='#1e5277',rasterized=True);ax.plot(xx,yy,color='#d44c33',lw=1.5);ax.set_title(f'TIC {tic} | S{e["sector"]} | cycle {e["cycle"]} | depth {e["depth"]*100:.2f}%',fontsize=9);ax.set_xlabel('days from fitted center');ax.set_ylabel('normalized SAP flux');ax.grid(alpha=.15)
fig.tight_layout();fig.savefig(R/'raw-event-panels.png',dpi=140);plt.close(fig)
