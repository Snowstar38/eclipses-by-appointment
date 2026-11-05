import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).parent
D=json.loads((B/'helper-flags.json').read_text()); bulk=Path('[local-path-redacted]'); out={}
for tic,events in D.items():
 src=json.loads((bulk/(tic+'.json')).read_text());out[tic]=[]
 for e in events:
  f=next(z for z in src['files'] if z['sector']==e['sector']);
  with fits.open(f['path']) as h:
   a=h[1].data;t=np.array(a['TIME']);s=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY']);t=t[np.isfinite(t)&np.isfinite(s)&(s>0)&(q==0)];sel=t[(t>e['time']-2)&(t<e['time']+2)];dx=np.diff(sel); med=np.median(dx); ids=np.where(dx>max(.06,5*med))[0]; gaps=[[round(float(sel[i]),5),round(float(sel[i+1]),5)] for i in ids];out[tic].append({'sector':e['sector'],'flag':e['time'],'gaps':gaps})
(B/'helper-gaps.json').write_text(json.dumps(out,indent=2))
