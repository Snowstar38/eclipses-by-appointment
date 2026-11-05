"""Diagnostic within-sector SAP periodicity; peaks are not binary periods."""
import csv,json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.timeseries import LombScargle
B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open()):
 tic=row['tic'];r=json.loads((B/tic/'raw-inspection.json').read_text());out=[]
 for s in r['sectors']:
  if 'path' not in s:continue
  p=Path(s['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
  with fits.open(p,memmap=False) as h:
   a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
  m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[m];f=f[m]/np.median(f[m])-1
  # Reject isolated extreme cadences; keep coherent variations and daily trends.
  med=np.median(f);sig=1.4826*np.median(abs(f-med));keep=abs(f-med)<max(8*sig,.04)
  t=t[keep];f=f[keep];coef=np.polyfit(t-t.mean(),f,1);y=f-np.polyval(coef,t-t.mean())
  freq=np.linspace(1/15,1/.5,12000);ls=LombScargle(t,y)
  power=ls.power(freq);ix=int(np.argmax(power));per=float(1/freq[ix]);model=ls.model(t,freq[ix]);amp=float((np.percentile(model,95)-np.percentile(model,5))*500)
  out.append({'sector':s['sector'],'n':len(t),'best_period_0p5_15d':per,'power':float(power[ix]),'half_peak_to_peak_ppt':amp,'linear_slope_ppt_per_day':float(coef[0]*1000),'top_periods_days':[float(1/freq[i]) for i in np.argsort(power)[-5:][::-1]]})
 (B/tic/'period-scan.json').write_text(json.dumps({'tic':tic,'method':'Lomb-Scargle 0.5-15d after per-sector linear detrend, quality0 SAP; diagnostic only','sectors':out},indent=2)+'\n')
 print(row['sample_id'],tic,' '.join(f"s{x['sector']}:{x['best_period_0p5_15d']:.3f}d/{x['half_peak_to_peak_ppt']:.1f}ppt" for x in out))
