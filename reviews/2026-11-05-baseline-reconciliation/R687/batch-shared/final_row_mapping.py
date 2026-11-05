"""Assert final numeric cells against frozen, named measurement sources."""
import csv,json,math
from pathlib import Path
W=Path(__file__).resolve().parent
rows={r['tic']:r for r in csv.DictReader((W/'RESULTS.csv').open(newline='',encoding='utf-8'))}
ep=json.loads((W/'ephemeris-167197264.json').read_text())
deep=json.loads((W/'helper-morphology-fits.json').read_text())
m=json.loads((W/'measurements-155346713.json').read_text())
q=list(csv.DictReader((W/'queue.csv').open(newline='',encoding='utf-8')))
assert list(rows)==[r['tic'] for r in q]
def close(a,b,tol): assert abs(float(a)-float(b))<=tol,(a,b,tol)
r=rows['167197264'];d=next(v for v in deep if v['tic']==167197264 and v['sector']==76 and v['window_half_days']==2.0)
close(r['period_days'],ep['shared_period_days_descriptive'],5e-10)
close(r['primary_epoch_btjd'],ep['B_reference_btjd'],5e-7)
close(r['depth_ppt'],d['depth']*1000,.005)
close(r['gaia_period_days'],ep['gaia_period_days'],1e-12)
assert r['period_error_days']==''
r2=rows['155346713'];a=next(v for v in m['events'] if v['kind']=='A' and v['sector']==88)
close(r2['primary_epoch_btjd'],a['center_btjd'],5e-7)
close(r2['depth_ppt'],a['depth_ppt'],.005)
close(r2['gaia_period_days'],m['gaia_period_days'],1e-12)
assert r2['period_days']=='' and r2['period_error_days']==''
out={'status':'pass','mapping':{
 '167197264':{'period_days':'ephemeris-167197264.json:shared_period_days_descriptive',
              'primary_epoch_btjd':'ephemeris-167197264.json:B_reference_btjd (fitted B epoch near s76)',
              'depth_ppt':'helper-morphology-fits.json:tic=167197264,sector=76,window_half_days=2.0,depth*1000',
              'gaia_period_days':'ephemeris-167197264.json:gaia_period_days',
              'period_error_days':'blank; no calibrated photometric period error'},
 '155346713':{'primary_epoch_btjd':'measurements-155346713.json:events[kind=A,sector=88].center_btjd',
              'depth_ppt':'measurements-155346713.json:events[kind=A,sector=88].depth_ppt',
              'gaia_period_days':'measurements-155346713.json:gaia_period_days',
              'period_days':'blank; no same-kind photometric period',
              'period_error_days':'blank'}}}
(W/'final-row-mapping.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
