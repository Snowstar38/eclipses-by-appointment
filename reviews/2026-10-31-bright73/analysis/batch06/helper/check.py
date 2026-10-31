import csv,json,pathlib,numpy as np
b=pathlib.Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((b/'RESULTS.csv').open(encoding='utf-8',newline='')))
assert len(rows)==len({r['tic'] for r in rows})==10
for row in rows:
 t=row['tic'];d=json.loads((b/t/'measurements.json').read_text()); ev=[e for e in d['events'] if e.get('timing_usable') and (t not in ('329559935','76020303') or e['cycle']%2==(1 if t=='329559935' else 0))]
 n=np.array([e.get('orbital_cycle',e['cycle']) for e in ev]);n=n-n.min();y=np.array([e['mid_btjd'] for e in ev]);s=np.array([e['timing_error_days'] for e in ev]);w=1/s**2;xb=np.average(n,weights=w);yb=np.average(y,weights=w);slope=np.sum(w*(n-xb)*(y-yb))/np.sum(w*(n-xb)**2);intercept=yb-slope*xb;chi=np.sum(((y-intercept-slope*n)/s)**2)/(len(n)-2);err=(max(1,chi)/np.sum(w*(n-xb)**2))**.5
 assert len(ev)==d['timing_event_count'],t
 for key,v in [('period_days',slope),('period_error_days',err),('primary_epoch_btjd',intercept),('depth_ppt',np.median([e['depth_ppt'] for e in ev]))]:
  assert abs(float(row[key])-v)<max(1e-9,abs(v)*1e-9),(t,key,row[key],v)
  assert abs(float(d[key])-v)<max(1e-9,abs(v)*1e-9),(t,key,d[key],v)
 report=(b/t/'REPORT.md').read_text(encoding='utf-8');assert f'P = {slope:.10f}' in report and f'+/- {err:.10f} d' in report and f'BTJD {intercept:.7f}' in report,(t,'report')
 windows=list(csv.DictReader((b/t/'raw-windows.csv').open(newline='')))
 for e in ev:
  z=[r for r in windows if int(r['sector'])==e['sector'] and int(r['cycle'])==e['cycle']];assert len(z)==e['n'] and min(float(r['btjd']) for r in z)<e['mid_btjd']<max(float(r['btjd']) for r in z) and min(float(r['normalized_raw_sap']) for r in z)<1,(t,e['cycle'])
 print(t,len(ev),f'{slope:.10f}',f'{err:.10g}',f'{intercept:.7f}',f'{chi:.3f}',row['physical_verdict'])

