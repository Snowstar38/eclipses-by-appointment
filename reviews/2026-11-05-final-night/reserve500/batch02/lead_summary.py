import json,csv,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
b=Path(__file__).resolve().parent
out={};audit=[]
g=json.loads((b/'lead-gaia-covariance.json').read_text())
for tic,tests in json.loads((b/'lead-alias-covered-windows.json').read_text()).items():
 out[tic]={'timing_compatible_no_covered_null':[{'label':z['label'],'period_d':z['period_d'],'covered':z['covered'],'n_dips':len(z['dips']),'gaia_period_difference_sigma':(z['period_d']-g[tic]['gaia_period_d'])/g[tic]['gaia_period_error_d']} for z in tests if z['timing_compatible'] and not z['nulls']], 'measured_test':tests[0], 'scope':'Divisors2..6 plus integer cycles for baseline/100 to baseline/5 days. Timing residual tolerance max(.04d,.1duration), >=75%core sampling, sidebands and no large gap. No claim of exhaustive period search or detection probability.'}
for row in csv.DictReader((b/'queue.csv').open()):
 tic=row['tic'];d=json.loads((b/tic/'lead-context.json').read_text())
 for src in d['source']:
  p=Path(src['path']);h=fits.getheader(p);a=fits.getdata(p,1);q=np.asarray(a['QUALITY']);t=np.asarray(a['TIME']);f=np.asarray(a['SAP_FLUX']);finite=np.isfinite(t)&np.isfinite(f)&(f>0)
  assert str(h.get('TICID'))==tic;assert int(h['SECTOR'])==src['sector'];assert hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256']
  audit.append({'tic':tic,'sector':src['sector'],'header_tic':str(h['TICID']),'sha256':src['sha256'],'finite_raw_n':int(finite.sum()),'quality_zero_n':int((finite&(q==0)).sum()),'flagged_finite_n':int((finite&(q!=0)).sum()),'ra':h.get('RA_OBJ'),'dec':h.get('DEC_OBJ')})
(b/'lead-alias-summary.json').write_text(json.dumps(out,indent=2))
(b/'identity-source-audit.json').write_text(json.dumps({'passed':True,'rows':audit},indent=2))
print('identity checked',len(audit),'sources; aliases summarized')
