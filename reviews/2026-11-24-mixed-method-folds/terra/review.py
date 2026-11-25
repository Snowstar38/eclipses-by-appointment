import argparse, os
import numpy as np,pandas as pd,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
from pathlib import Path
D=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(); parser.add_argument('--cache', default=os.environ.get('MIXED_FOLD_CACHE', str(D.parent/'sol'/'cadences'))); cache=Path(parser.parse_args().cache)
if not cache.is_dir(): raise FileNotFoundError(f'Cadence cache not found: {cache}')
clocks=pd.read_csv(D.parent/'ground'/'archived-clocks.csv').set_index('tic')
for _,r in pd.read_csv(D.parent/'batch.csv').iterrows():
 chunks=[]
 for f in sorted(cache.glob(f'{int(r.tic)}-*.npz'), key=lambda p:int(p.stem.split('-')[-1])):
  z=np.load(f);t=z['t']; p=z['pdc'].astype(float);s=z['sap'].astype(float); m=np.isfinite(t)&np.isfinite(p)&np.isfinite(s)&(p>0)&(s>0);t,p,s=t[m],p[m],s[m]; ix=np.argsort(t);t,p,s=t[ix],p[ix],s[ix]
  if len(t)<30:continue
  cad=np.median(np.diff(t));w=min(max(11,int(2/cad)//2*2+1),len(t)//2*2-1);p=p/median_filter(p,size=w,mode='nearest')-1;s=s/median_filter(s,size=w,mode='nearest')-1
  chunks.append((t,p,s,f.stem.split('-')[-1]))
 if not chunks:continue
 fig,axs=plt.subplots(len(chunks)+1,1,figsize=(14,2*(len(chunks)+1)),layout='constrained',squeeze=False); axs=axs[:,0]
 for ax,(t,p,s,sec) in zip(axs,chunks):
  ax.scatter(t,p*1000,s=1,c='black',alpha=.6);ax.scatter(t,s*1000,s=1,c='blue',alpha=.25);ax.set_ylabel('ppt');ax.set_title('Sector '+sec,loc='left');lim=np.nanpercentile(p,[.3,99.7])*1400;ax.set_ylim(min(lim[0],-8),max(lim[1],8));ax.axhline(0,color='gray',lw=.4)
 t=np.concatenate([c[0] for c in chunks]);p=np.concatenate([c[1] for c in chunks]);s=np.concatenate([c[2] for c in chunks]);P=clocks.loc[int(r.tic),'period_d'];ph=(t/P)%1;ax=axs[-1];ax.scatter(ph,p*1000,s=1,c='black',alpha=.2);ax.scatter(ph,s*1000,s=1,c='blue',alpha=.08);bins=np.linspace(0,1,201);ids=np.digitize(ph,bins);x=[];y=[]
 for k in range(1,len(bins)):
  if sum(ids==k)>3:x.append((bins[k-1]+bins[k])/2);y.append(np.median(p[ids==k])*1000)
 ax.plot(x,y,c='red');lim=np.nanpercentile(p,[.3,99.7])*1400;ax.set_ylim(min(lim[0],-8),max(lim[1],8));ax.set_title(f'Screening period {P:.6f} d; arbitrary phase origin');ax.set_xlabel('phase');fig.suptitle(f'TIC {int(r.tic)} | black corrected, blue SAP | 2 d running median',fontsize=14);fig.savefig(D/f'{int(r.tic)}.png',dpi=100);plt.close(fig)
