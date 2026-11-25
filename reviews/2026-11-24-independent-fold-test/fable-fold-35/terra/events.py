import numpy as np,pandas as pd
from pathlib import Path
from scipy.ndimage import median_filter
from paths import cadence_cache
o=Path(__file__).resolve().parent; b=o.parent; d=cadence_cache(); all=[]
for _,r in pd.read_csv(b/'batch.csv').iterrows():
 for f in d.glob(f'{int(r.tic)}-*.npz'):
  z=np.load(f); t=z['t']; y=z['pdc'].astype(float); m=np.isfinite(t)&np.isfinite(y)&(y>0);t=t[m];y=y[m];ix=np.argsort(t);t=t[ix];y=y[ix]
  if len(t)<30:continue
  cad=np.median(np.diff(t));win=min(max(11,int(2/cad)//2*2+1),len(y)//2*2-1); v=y/median_filter(y,size=win,mode='nearest')-1
  ids=np.flatnonzero(v<-.01); splits=np.split(ids,np.where(np.diff(t[ids])>max(.15,3*cad))[0]+1)
  for a in splits:
   if len(a)<3:continue
   center=t[a[np.argmin(v[a])]]; left=(t>center-1)&(t<t[a[0]]-.05);right=(t>t[a[-1]]+.05)&(t<center+1); scatter=1.4826*np.median(np.abs(v-np.median(v))); depth=-np.min(v[a]);
   if depth<5*scatter or left.sum()<3 or right.sum()<3:continue
   all.append((int(r.tic),f.stem.split('-')[-1],round(center,5),round(depth*1000,1),len(a),round(scatter*1000,2),round(t[a[-1]]-t[a[0]],3)))
pd.DataFrame(all,columns=['tic','sector','center_btjd','min_depth_ppt','cadences_below_10ppt','sector_scatter_ppt','span_d']).to_csv(o/'event_candidates.csv',index=False)
print(pd.DataFrame(all,columns=['tic','sector','center','depth','n','scatter','span']).groupby('tic').size().to_string())
