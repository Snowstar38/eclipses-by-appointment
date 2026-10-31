import csv, json, pathlib, numpy as np

root = pathlib.Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((root/'RESULTS.csv').open(newline='', encoding='utf-8')))
assert len(rows) == len({r['tic'] for r in rows}) == 10
for row in rows:
    tic = row['tic']
    d = json.loads((root/tic/'measurements.json').read_text())
    events = [e for e in d['events'] if e.get('timing_usable') and (tic not in ('382603504','128825695') or e['cycle'] % 2 == 0)]
    n = np.array([e.get('orbital_cycle', e['cycle']) for e in events]); n = n - n.min()
    y = np.array([e['mid_btjd'] for e in events]); s = np.array([e['timing_error_days'] for e in events]); w = 1/s**2
    # Centered weighted regression to avoid constructing the original normal equations.
    xbar = np.average(n, weights=w); ybar = np.average(y, weights=w)
    slope = np.sum(w*(n-xbar)*(y-ybar))/np.sum(w*(n-xbar)**2)
    intercept = ybar - slope*xbar
    chi = np.sum(((y-intercept-slope*n)/s)**2)/(len(n)-2)
    err = (max(1,chi)/np.sum(w*(n-xbar)**2))**.5
    assert len(events) == d['timing_event_count']
    for key, val in [('period_days',slope),('period_error_days',err),('primary_epoch_btjd',intercept),('depth_ppt',np.median([e['depth_ppt'] for e in events]))]:
        assert abs(float(row[key])-val) < max(1e-9,abs(val)*1e-9), (tic,key,row[key],val)
        assert abs(float(d[key])-val) < max(1e-9,abs(val)*1e-9), (tic,key,d[key],val)
    assert row['physical_verdict'] == ('PROBABLE' if tic == '343340931' else 'CONFIRMED') and row['full_review_completion'] == 'COMPLETE'
    report = (root/tic/'REPORT.md').read_text(encoding='utf-8')
    assert f"P={slope:.10f}" in report and f"+/-{err:.10f}d" in report and f"BTJD{intercept:.7f}" in report
    windows = list(csv.DictReader((root/tic/'raw-windows.csv').open(newline='')))
    for e in events:
        sample = [r for r in windows if int(r['sector']) == e['sector'] and int(r['cycle']) == e['cycle']]
        assert len(sample) == e['n']
        assert min(float(r['btjd']) for r in sample) < e['mid_btjd'] < max(float(r['btjd']) for r in sample)
        assert min(float(r['normalized_raw_sap']) for r in sample) < 1
    assert 'same TESS photons' in report and 'not independent observing occasions' in report
    print(tic, len(events), f'P={slope:.10f}', f'err={err:.10g}', f'epoch={intercept:.7f}', f'redchi={chi:.3f}')
