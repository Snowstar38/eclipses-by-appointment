import pandas as pd,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
from pathlib import Path
from PIL import Image
from paths import cadence_cache
o=Path(__file__).resolve().parent;b=o.parent;d=cadence_cache(); events=pd.read_csv(o/'event_candidates.csv'); batch=pd.read_csv(b/'batch.csv')
for _,r in batch.iterrows():
 ev=events[events.tic==r.tic]; fig,ax=plt.subplots(figsize=(9,3));
 for _,e in ev.iterrows():
  p=d/f'{int(r.tic)}-{int(e.sector)}.npz';z=np.load(p);t=z['t'];y=z['pdc'].astype(float);s=z['sap'].astype(float);m=np.isfinite(t)&np.isfinite(y)&np.isfinite(s)&(y>0)&(s>0);t=t[m];y=y[m];s=s[m];ix=np.argsort(t);t=t[ix];y=y[ix];s=s[ix];cad=np.median(np.diff(t));win=min(max(11,int(2/cad)//2*2+1),len(y)//2*2-1);y=y/median_filter(y,size=win,mode='nearest')-1;s=s/median_filter(s,size=win,mode='nearest')-1;m=np.abs(t-e.center_btjd)<.6
  ax.plot(t[m]-e.center_btjd,1000*y[m],lw=.7,alpha=.65);ax.scatter(t[m]-e.center_btjd,1000*s[m],s=1,c='black',alpha=.1)
 ax.axhline(0,c='gray',lw=.5);ax.axvline(0,c='gray',lw=.5);ax.set(title=f'TIC {int(r.tic)} | {len(ev)} candidate events | PDC lines; SAP black',xlabel='Days from candidate minimum',ylabel='Residual ppt');ax.set_ylim(-min(350,max(20,ev.min_depth_ppt.max()*1.1 if len(ev) else 20)),30);fig.tight_layout();fig.savefig(o/f'{int(r.tic)}-events.png',dpi=100);plt.close(fig)
for group in range(1,5):
 ids=list(batch[batch.group==group].tic)
 for part in range((len(ids)+4)//5):
  ims=[Image.open(o/f'{tic}-events.png').convert('RGB') for tic in ids[5*part:5*part+5]];c=Image.new('RGB',(900,300*len(ims)),'white')
  for j,im in enumerate(ims):c.paste(im,(0,300*j))
  c.save(o/f'events-group{group}-{part+1}.jpg',quality=90)
