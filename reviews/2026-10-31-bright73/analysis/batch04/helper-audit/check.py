import csv, json, math
from pathlib import Path
import numpy as np

B = Path(__file__).resolve().parent.parent
out = {}
for row in csv.DictReader(open(B/'queue.csv')):
    tic = row['tic']; m = json.load(open(B/tic/'measurements.json'))
    explicit_cycles = any('orbital_cycle' in e for e in m['events'])
    good = [e for e in m['events'] if e.get('timing_usable') and (not explicit_cycles or 'orbital_cycle' in e)]
    n = np.array([e.get('orbital_cycle', e['cycle']) for e in good], float)
    t = np.array([e['mid_btjd'] for e in good]); s = np.array([e['timing_error_days'] for e in good])
    x = np.column_stack((np.ones(len(n)), n-n.min()))
    beta, _, _, _ = np.linalg.lstsq(x/s[:,None], t/s, rcond=None)
    cov = np.linalg.inv((x/s[:,None]).T @ (x/s[:,None]))
    residual = t-x@beta; chi = sum((residual/s)**2)/max(len(n)-2,1)
    err = np.sqrt(cov[1,1]*max(chi,1))
    out[tic] = dict(n=len(good), measured_midpoints_distinct_from_predicted=sum(abs(e['mid_btjd']-e['predicted_btjd'])>1e-9 for e in good), period=float(beta[1]), stored_period=m['period_days'], period_delta=float(beta[1]-m['period_days']), epoch=float(beta[0]), stored_epoch=m['primary_epoch_btjd'], error=float(err), stored_error=m['period_error_days'], chi=float(chi), sectors=sorted(set(e['sector'] for e in good)))
json.dump(out, open(B/'helper-audit'/'timing-check.json','w'), indent=2)
