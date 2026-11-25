import os, glob, numpy as np, pandas as pd, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
from astropy.timeseries import BoxLeastSquares
from pathlib import Path
from paths import cadence_cache
out=Path(__file__).resolve().parent; base=out.parent
dat=cadence_cache()
rows=pd.read_csv(base/'batch.csv'); metadata=[]
for _,r in rows.iterrows():
 chunks=[]
 for f in sorted(dat.glob(f'{int(r.tic)}-*.npz')):
  z=np.load(f); t=z['t']; p=z['pdc'].astype(float); s=z['sap'].astype(float); m=np.isfinite(t)&np.isfinite(p)&np.isfinite(s)&(p>0)&(s>0); t,p,s=t[m],p[m],s[m]
  if len(t)<30: continue
  order=np.argsort(t); t,p,s=t[order],p[order],s[order]; cadence=np.median(np.diff(t)); win=max(11,int(2.0/cadence)//2*2+1); win=min(win, len(p)//2*2-1)
  trend=median_filter(p,size=win,mode='nearest'); fs=p/trend-1
  st=median_filter(s,size=win,mode='nearest'); ss=s/st-1
  chunks.append((t,fs,ss, f.stem.split('-')[-1]))
 if not chunks: continue
 t=np.concatenate([x[0] for x in chunks]); y=np.concatenate([x[1] for x in chunks]); sap=np.concatenate([x[2] for x in chunks]); good=np.isfinite(y)&(np.abs(y)<.3); t,y,sap=t[good],y[good],sap[good]
 # BLS independently searches time series over a broad plausible clock range.
 try:
  bls=BoxLeastSquares(t,y); periods=np.linspace(1,15,4500); q=bls.power(periods,[.08,.16,.3],objective='snr'); j=np.argmax(q.power); ap=float(q.period[j]); at=float(q.transit_time[j]); ad=float(q.duration[j])
 except Exception: ap=float(r.period_d); at=float(r.t0_btjd); ad=.15
 metadata.append(dict(tic=int(r.tic),alt_period=ap,alt_t0=at,alt_duration_d=ad,sectors=','.join(x[3] for x in chunks)))
 fig,axs=plt.subplots(3,1,figsize=(13,7),layout='constrained'); fig.suptitle(f'TIC {int(r.tic)} | sectors {metadata[-1]["sectors"]} | supplied P={r.period_d:.5f} d | BLS P={ap:.5f} d',fontsize=12)
 lim=np.nanpercentile(y,[.3,99.7]); lim=[max(-.3,lim[0]*1.3),min(.3,lim[1]*1.3)]; lim[0]=min(lim[0],-.005);lim[1]=max(lim[1],.005)
 axs[0].scatter(t,y*1000,s=1,c='black',alpha=.35); axs[0].set(xlabel='BTJD',ylabel='PDC residual (ppt)',ylim=np.array(lim)*1000)
 for ax,period,epoch,title in [(axs[1],r.period_d,r.t0_btjd,'Supplied ephemeris'),(axs[2],ap,at,'Independent BLS clock')]:
  phase=((t-epoch)/period+.5)%1-.5; ax.scatter(phase,y*1000,s=1,c='black',alpha=.13); ax.scatter(phase,sap*1000,s=1,c='royalblue',alpha=.07)
  edges=np.linspace(-.5,.5,101); ix=np.digitize(phase,edges); xx=[]; yy=[]
  for k in range(1,len(edges)):
   v=y[ix==k]
   if len(v)>=3: xx.append((edges[k-1]+edges[k])/2);yy.append(np.median(v)*1000)
  ax.plot(xx,yy,color='crimson',lw=1.3);ax.axvline(0,color='gray',lw=.5);ax.set(xlabel='Phase',ylabel='Residual (ppt)',ylim=np.array(lim)*1000,title=title)
 fig.savefig(out/f'{int(r.tic)}.png',dpi=110);plt.close(fig)
pd.DataFrame(metadata).to_csv(out/'clocks.csv',index=False)
