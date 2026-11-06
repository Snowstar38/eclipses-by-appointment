from pathlib import Path
import json,csv,hashlib
import numpy as np
from astropy.io import fits
from scipy.signal import find_peaks,savgol_filter
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;H=B.parent.parent/'binary-exploration-2026-11-04/bulk-results'
assert hashlib.sha256((B/'queue.csv').read_bytes()).hexdigest()==json.loads((B/'selection.json').read_text())['queue_sha256']
Q=list(csv.DictReader((B/'queue.csv').open()));out={};sources=[]
for r in Q:
 tic=r['tic'];bulk=H/f'{tic}.json';bs=json.loads(bulk.read_text());ss={}
 for f in bs['files']:
  p=Path(f['path']);ha=hashlib.sha256(p.read_bytes()).hexdigest();assert ha==f['sha256']
  with fits.open(p) as h:
   assert str(int(h[0].header['TICID']))==tic
   d=h[1].data;t=np.array(d['TIME'],float);y=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'],int)
  z=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);ss[f['sector']]=(t[z],y[z]/np.median(y[z]))
  sources.append(dict(tic=tic,path=str(p),sha256=ha,bulk_path=str(bulk),bulk_sha256=hashlib.sha256(bulk.read_bytes()).hexdigest()))
 if tic not in ['185744410','149316567','378411251','387124290','233405109','27681485']:continue
 if tic in ['185744410','149316567','378411251','387124290']:
  sec,prom,dist={'185744410':(61,.004,1.0),'149316567':(88,.004,1.7),'378411251':(64,.009,2.4),'387124290':(81,.006,.5)}[tic]
  t,y=ss[sec];idx,_=find_peaks(-savgol_filter(y,5,2),prominence=prom,distance=int(dist/np.median(np.diff(t))))
  ts=t[idx];sp=np.diff(ts);trial=np.median(sp[sp<np.median(sp)*1.5]);n=np.round((ts-ts[0])/trial).astype(int);fit=np.polyfit(n,ts,1);res=ts-np.polyval(fit,n)
  out[tic]=dict(sector=sec,event_times_btjd=ts.tolist(),cycles=n.tolist(),period_d=float(fit[0]),epoch_btjd=float(fit[1]),residuals_d=res.tolist(),interpretation='same-shaped sharp dips; alternating depth doubles orbital period if distinct conjunctions; no long-baseline precise ephemeris claimed',prominence=prom,min_distance_d=dist)
 else:
  windows=[]
  for f in bs['files']:
   for w in f['windows']:
    if (tic=='233405109' and f['sector'] in [55,56,76,81,83] and w['flag'] and abs(w['time']-float(r['best_window_btjd']))%1>=0):
     if min(abs(w['time']-x) for x in [2802.4634,2850.9726,3385.5361,3531.2719,3579.8944])<.02:windows.append((f['sector'],w['time'],.7))
  if tic=='27681485':windows=[(44,2505.55,2.2),(45,2542.05,2.2),(46,2560.15,1.8)]
  ev=[]
  for sec,c,dur in windows:
   t,y=ss[sec];sel=abs(t-c)<dur*1.5;x=t[sel]-c;v=y[sel];side=abs(x)>dur*.65;co=np.polyfit(x[side],v[side],1);norm=v/np.polyval(co,x);core=abs(x)<dur*.6;weights=np.maximum(0,1-norm[core]);ct=float(np.sum(t[sel][core]*weights)/sum(weights));ev.append(dict(sector=sec,center_btjd=ct,seed_btjd=c,core_median_depth=float(1-np.median(norm[abs(x)<dur*.3])),duration_guide_d=dur,n_core=int(sum(core))))
  use=ev if tic=='233405109' else ev[:2];ts=np.array([e['center_btjd'] for e in use]);trial=float(r['gaia_period_days']);n=np.round((ts-ts[0])/trial).astype(int);fit=np.polyfit(n,ts,1)
  out[tic]=dict(events=ev,cycles=n.tolist(),period_d=float(fit[0]),epoch_btjd=float(fit[1]),residuals_d=(ts-np.polyval(fit,n)).tolist(),timing_note='deficit-weighted centroid after linear local sideband baseline; descriptive timing, not calibrated fit error')
  if tic=='27681485':out[tic]['caution']='Only two same-kind deep events; need covered aliases/nulls and later availability before claim'
 print(tic,out[tic],flush=True)
(B/'lead-clocks.json').write_text(json.dumps(out,indent=2));(B/'lead-source-receipts.json').write_text(json.dumps(sources,indent=2))
