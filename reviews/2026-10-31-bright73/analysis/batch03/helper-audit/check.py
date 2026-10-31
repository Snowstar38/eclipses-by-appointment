import csv, hashlib, json
from pathlib import Path
import numpy as np

b = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf-8-sig')))
out = {}
for row in rows:
    tic = row['tic']; d = json.loads((b/tic/'measurements.json').read_text())
    ev = [e for e in d['events'] if e.get('timing_usable') and (tic != '16809274' or e['cycle'] % 2 == 0)]
    x = np.array([e.get('orbital_cycle', e['cycle']) for e in ev], float)
    y = np.array([e['mid_btjd'] for e in ev]); s = np.array([e['timing_error_days'] for e in ev]); x -= x.min()
    w = 1/s**2; xm = np.average(x, weights=w); ym = np.average(y, weights=w)
    slope = np.sum(w*(x-xm)*(y-ym))/np.sum(w*(x-xm)**2)
    epoch = ym - slope*xm; residual = y - (epoch+slope*x)
    chi2 = np.sum((residual/s)**2)/max(len(x)-2,1)
    err = np.sqrt(max(1,chi2)/np.sum(w*(x-xm)**2))
    assert abs(slope-d['period_days']) < 1e-8 and abs(epoch-d['primary_epoch_btjd']) < 1e-6
    assert abs(err-d['period_error_days']) < 1e-9
    assert all(abs(float(row[k])-d[k]) < 1e-9 for k in ('period_days','period_error_days','primary_epoch_btjd','depth_ppt'))
    windows = list(csv.DictReader((b/tic/'raw-windows.csv').open()))
    for e in ev:
        v = [float(z['btjd']) for z in windows if int(z['sector'])==e['sector'] and int(z['cycle'])==e['cycle']]
        assert v and min(v) < e['mid_btjd'] < max(v)
    for src in d['sources']:
        assert hashlib.sha256(Path(src['path']).read_bytes()).hexdigest() == src['sha256']
    out[tic] = {'n':len(ev),'sectors':sorted(set(e['sector'] for e in ev)), 'period':slope,'epoch':epoch,'error':err,'reduced_chi_square':chi2,'excluded':sum(not e.get('timing_usable',False) for e in d['events'])}
(b/'helper-audit'/'numeric-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out, indent=2))
