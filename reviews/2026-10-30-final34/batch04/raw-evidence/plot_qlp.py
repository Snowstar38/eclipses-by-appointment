import pathlib,json,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
R=pathlib.Path(__file__).parent;raw=json.load(open(R/'raw-events.json'));qlp=json.load(open(R/'qlp-results.json'));fig,axes=plt.subplots(4,2,figsize=(13,10),constrained_layout=True)
for i,(tic,v) in enumerate(raw.items()):
 q=qlp[tic]; f=R/tic/('qlp_s%03d.fits'%v['sector']);
 with fits.open(f) as h:
  a=h[1].data;t=np.array(a['TIME'],float);y=np.array(a['SAP_FLUX'],float);quality=np.array(a['QUALITY']);good=np.isfinite(t)&np.isfinite(y)&(y>0)&(quality==0);t=t[good];y=y[good]
 for j,ax in enumerate(axes[i]):
  if j>=len(q['events']):ax.axis('off');continue
  e=q['events'][j];tc=e['tc'];D=e['duration_d'];w=max(.6,3*D);m=abs(t-tc)<w;x=(t[m]-tc)*24;z=y[m]/np.median(y[m]);ax.plot(x,z,'.',ms=2.4,alpha=.65,color='#1d4f86');ax.axvline(0,c='#c04440',lw=.8);ax.set_title(f'TIC {tic}  S{v["sector"]}  cycle {e["cycle"]}  BTJD {tc:.5f}',fontsize=8);ax.set_xlabel('Hours from measured mid-event',fontsize=7);ax.set_ylabel('Normalized SAP flux',fontsize=7);ax.tick_params(labelsize=7);ax.grid(alpha=.18)
fig.suptitle('QLP SAP: two representative individual raw-flux eclipses per target (QUALITY=0)',fontsize=13);fig.savefig(R/'qlp-raw-event-panels.png',dpi=140);plt.close(fig)

