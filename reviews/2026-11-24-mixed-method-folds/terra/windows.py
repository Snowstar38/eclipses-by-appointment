import argparse, os
import numpy as np,pandas as pd,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
from pathlib import Path
D=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(); parser.add_argument('--cache', default=os.environ.get('MIXED_FOLD_CACHE', str(D.parent/'sol'/'cadences'))); cache=Path(parser.parse_args().cache)
if not cache.is_dir(): raise FileNotFoundError(f'Cadence cache not found: {cache}')
clocks=pd.read_csv(D.parent/'ground'/'archived-clocks.csv').set_index('tic'); rows=[]
for _,r in pd.read_csv(D.parent/'batch.csv').iterrows():
 tic=int(r.tic); q=clocks.loc[tic]; P=q['period_d']; t0=q['epoch_btjd'];dur=q['duration_d'];ev=[]
 for f in sorted(cache.glob(f'{tic}-*.npz'),key=lambda p:int(p.stem.split('-')[-1])):
  z=np.load(f); t=z['t'];p=z['pdc'].astype(float);s=z['sap'].astype(float);ok=np.isfinite(t)&np.isfinite(p)&np.isfinite(s)&(p>0)&(s>0);t,p,s=t[ok],p[ok],s[ok];ix=np.argsort(t);t,p,s=t[ix],p[ix],s[ix]
  if len(t)<30:continue
  w=min(max(11,int(2/np.median(np.diff(t)))//2*2+1),len(t)//2*2-1);p=p/median_filter(p,w,mode='nearest')-1;s=s/median_filter(s,w,mode='nearest')-1
  for k in range(int(np.floor((t.min()-t0)/P))-1,int(np.ceil((t.max()-t0)/P))+2):
   c=t0+k*P;m=np.abs(t-c)<.7
   if m.sum()>=3:ev.append((t[m]-c,p[m],s[m],f.stem.split('-')[-1],c))
 if not ev:continue
 cols=3; nr=int(np.ceil(len(ev)/cols));fig,axs=plt.subplots(nr,cols,figsize=(14,2.5*nr),squeeze=False,layout='constrained')
 for ax,(t,p,s,sec,c) in zip(axs.flat,ev):
  ax.scatter(t,p*1000,s=5,c='black',alpha=.65);ax.scatter(t,s*1000,s=5,c='blue',alpha=.35);ax.axvspan(-dur/2,dur/2,color='red',alpha=.12);ax.axhline(0,c='gray',lw=.5);ax.set_title(f'S{sec}, BTJD {c:.3f}',fontsize=9);ax.set_xlabel('days from prediction');ax.set_ylabel('ppt');lim=np.percentile(np.r_[p,s],[1,99])*1300;ax.set_ylim(min(-5,lim[0]),max(5,lim[1]))
 for ax in list(axs.flat)[len(ev):]:ax.axis('off')
 fig.suptitle(f'TIC {tic} original P={P:.5f} t0={t0:.4f} dur={dur:.3f} d; black corrected blue SAP',fontsize=12);fig.savefig(D/f'{tic}-windows.png',dpi=100);plt.close(fig)
 rows.append((tic,P,t0,dur,len(ev)))
pd.DataFrame(rows,columns=['tic','period','epoch','duration','windows']).to_csv(D/'archived_clocks.csv',index=False)
