import json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.ndimage import median_filter
from scipy.signal import find_peaks
B=Path(__file__).resolve().parent
out={}
for tic,secs in [('191416124',[57,84]),('210963066',[11,99,102]),('243276811',[19,41,54])]:
 ctx=json.loads((B/tic/'lead-context.json').read_text()); out[tic]=[]
 for s in ctx['sectors']:
  if s['sector'] not in secs:continue
  p=Path(s['source_path']); digest=hashlib.sha256(p.read_bytes()).hexdigest()
  with fits.open(p) as h:
   d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY']);k=np.array(d['KSPSAP_FLUX'],float) if 'KSPSAP_FLUX' in d.names else np.full(len(t),np.nan)
  good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good];k=k[good]; f=f/np.median(f); kk=k[np.isfinite(k)&(k>0)];
  entry={'sector':s['sector'],'hash':digest,'hash_matches_context':digest==s['source_sha256'],'time_range':[float(t.min()),float(t.max())],'sap_p05_p95_ppt':[float(x) for x in (np.percentile(f,[5,95])-1)*1000], 'kspsap_p05_p95_ppt':[float(x) for x in (np.percentile(kk/np.median(kk),[5,95])-1)*1000] if len(kk)>10 else None}
  if tic=='191416124':
   sel=(t>2869)&(t<2882) if s['sector']==57 else (t>3598)&(t<3610)
   tt=t[sel]; ff=f[sel]; smooth=median_filter(ff,size=45); peaks,_=find_peaks(-smooth,distance=400,prominence=.0006); entry['smoothed_minima_btjd']=[float(tt[x]) for x in peaks]
  out[tic].append(entry)
(B/'helper-numeric.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

