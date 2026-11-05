"""Check the observed two-event cycle aliases against actual s72 SAP coverage."""
import json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
m=json.loads((B/'87869692'/'lead-numeric.json').read_text())
e=[next(x for x in m['events'] if x['sector']==s and abs(x['fit_mid_btjd']-t)<.003) for s,t in [(44,2521.286),(71,3243.049)]]
src=next(x for x in m['sources'] if x['sector']==72); p=Path(src['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256']
with fits.open(p) as h:
 d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
out=[]
for n in range(20,25):
 P=(e[1]['fit_mid_btjd']-e[0]['fit_mid_btjd'])/n
 pred=e[1]['fit_mid_btjd']+P
 core=np.abs(t-pred)<.18
 left=(t>pred-.9)&(t<pred-.36);right=(t>pred+.36)&(t<pred+.9);base=left|right
 expected=int(round(.36/np.median(np.diff(t))))
 deficit=1000*(1-np.median(f[core])/np.median(f[base])) if core.sum()>2 and base.sum()>5 else None
 rec=dict(cycle_span=n,conditional_period_days=P,s72_pred_btjd=pred,s72_core_n=int(core.sum()),s72_expected_core_n=expected,s72_core_first=float(t[core].min()) if core.any() else None,s72_core_last=float(t[core].max()) if core.any() else None,s72_core_max_gap_days=float(np.diff(t[core]).max()) if core.sum()>1 else None,s72_baseline_n=int(base.sum()),s72_core_deficit_ppt=float(deficit) if deficit is not None else None)
 out.append(rec)
 print(rec)
(B/'lead-alias-t084.json').write_text(json.dumps(out,indent=2)+'\n')
