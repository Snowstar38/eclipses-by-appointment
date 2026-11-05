"""Conservative T099 clock check with broad baseline gaps separated from core."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;tic='29551987';m=json.loads((B/tic/'lead-numeric.json').read_text());ev=m['events']
def mid(seed):
 e=min(ev,key=lambda x:abs(x['fit_mid_btjd']-seed));assert abs(e['fit_mid_btjd']-seed)<.004;return e['fit_mid_btjd']
a,b,c=map(mid,[1822.7651,2916.8088,3291.0574]);sa,sb=map(mid,[1837.1432,2931.2046]);pd=(b-a)/38;ps=(sb-sa)/38;adopt=(pd+ps)/2;pred=a+51*adopt
src=next(x for x in m['sources'] if x['sector']==73);p=Path(src['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256']
with fits.open(p,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME'],float);q=np.array(d['QUALITY'],int)
sel=(q==0)&np.isfinite(t)&(abs(t-c)<1.5);u=t[sel];z=np.diff(u);i=int(np.argmax(z))
out=dict(tic=tic,deep_pair_period_days=pd,shallow_pair_period_days=ps,adopted_rounded_period_days=round(adopt,3),conservative_period_allowance_days=.001,reference_deep_mid_btjd=round(a,4),third_deep_fit_mid_btjd=c,predicted_third_deep_btjd=pred,third_residual_days=c-pred,third_fit_conservative_center_allowance_days=.05,third_core_interval_btjd=[c-1.1,c+1.1],local_3day_quality0_n=len(u),local_3day_largest_gap_days=float(z[i]),local_3day_largest_gap_bounds_btjd=[float(u[i]),float(u[i+1])],source_sha256=src['sha256'],note='The 0.05-d center allowance exceeds the 0.041-d disagreement of the third deep fit with the first-two-kind clock. Largest local gap is after the egress; broader-baseline gaps and slope still make a milliday formal fit too optimistic. The 0.001-d period allowance is conservative, not a calibrated 1-sigma error.')
(B/'lead-t099-bounds.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
