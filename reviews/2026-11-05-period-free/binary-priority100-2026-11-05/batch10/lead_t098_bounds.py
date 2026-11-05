"""Conservative two-kind T098 clock and shorter-harmonic check."""
import json
from pathlib import Path
B=Path(__file__).resolve().parent;m=json.loads((B/'117404582'/'lead-numeric.json').read_text());ev=m['events']
def mid(seed):
 x=min(ev,key=lambda e:abs(e['fit_mid_btjd']-seed));assert abs(x['fit_mid_btjd']-seed)<.004;return x['fit_mid_btjd']
a,b=map(mid,[1795.4125,2908.5573]);c,d=map(mid,[1805.0055,2883.4018]);pd=(b-a)/32;ps=(d-c)/31
out=dict(tic='117404582',deep_pair_period_days=pd,deep_cycles=32,shallow_pair_period_days=ps,shallow_cycles=31,between_kind_period_difference_days=ps-pd,adopted_rounded_period_days=34.786,conservative_period_allowance_days=.002,short_harmonic_days=pd/2,short_harmonic_predicted_deep_btjd=1812.8054,short_harmonic_observed_depth_fraction=.0015,note='A fully covered raw s18 window around the half-period prediction is visually flat at the expected deep-eclipse duration. The 0.002-d period allowance covers the difference between independent two-kind period estimates; it is not a calibrated one-sigma error. See lead-deciding-null-T098.png and lead-alias.json.')
(B/'lead-t098-bounds.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
