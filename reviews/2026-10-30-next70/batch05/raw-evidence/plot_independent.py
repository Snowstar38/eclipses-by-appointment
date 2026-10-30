import json,pathlib,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits
R=pathlib.Path(__file__).parent;raw=json.load(open(R/'raw-events.json'));res=json.load(open(R/'independent-results.json'));fig,axes=plt.subplots(10,1,figsize=(10,25))
for ax,z in zip(axes,res):
 tic=z['tic'];r=raw[tic];ep=r['representative_ephemeris'];dur=np.median([e['duration_d'] for e in r['events'] if 'tc'in e and not e['edge']]);x,y=z['identity']['target_xy'];ix,iy=round(x),round(y)
 with fits.open(z['source_path']) as h:
  a=h[1].data;t=np.array(a['TIME']);F=np.array(a['FLUX']);q=np.array(a['QUALITY']);m=np.isfinite(t)&np.all(np.isfinite(F.reshape(len(t),-1)),axis=1)&(q==0);t=t[m];F=F[m];bg=np.median(np.sort(F.reshape(len(t),-1),axis=1)[:,:int(.4*F.shape[1]*F.shape[2])],axis=1);f=F[:,iy-1:iy+2,ix-1:ix+2].sum(axis=(1,2))-9*bg
 for row in z['measurements']:
  dt=t-row['tc'];m=abs(dt)<2*dur; base=(np.median(f[(dt<-.75*dur)&(dt>-1.75*dur)])+np.median(f[(dt>.75*dur)&(dt<1.75*dur)]))/2;ax.scatter(dt[m],f[m]/base,s=3,alpha=.4)
 ax.set_title(f'TIC {tic} sector {z["sector"]}, independent 3x3 aperture',fontsize=9);ax.axvline(0,color='red',alpha=.4);ax.grid(alpha=.2);ax.set_ylabel('relative flux')
fig.tight_layout();fig.savefig(R/'independent-panels.png',dpi=140)
