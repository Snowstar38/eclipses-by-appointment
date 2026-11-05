"""Manually curated visually credible same-kind raw eclipse clocks.

Cycle labels are tested against the separate-kind events and the distinct
sector spans; the screening centers never enter these fits.
"""
import csv,json
from pathlib import Path
import numpy as np

B=Path(__file__).resolve().parent
CHOICES={
 'T012':{'deep':([3,7],[0,16]),'shallow':([2,5,9],[0,30,47])},
 'T014':{'one_kind':([0,1,2,3,4],[0,4,18,22,33])},
}
for row in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
    d=json.loads((B/row['tic']/'lead-numeric.json').read_text()); out={'sample_id':row['sample_id'],'tic':row['tic'],'gaia_period_days':float(row['gaia_period_days']),'kinds':{}}
    for kind,(ids,cycles) in CHOICES.get(row['sample_id'],{}).items():
        ev=[d['events'][i] for i in ids]; t=np.array([e['fit_mid_btjd'] for e in ev]); n=np.array(cycles);A=np.column_stack([np.ones(len(n)),n]);par=np.linalg.lstsq(A,t,rcond=None)[0];res=t-A@par
        if len(n)>2:
            floor=np.median([next(c['cadence_days'] for c in d['coverage'] if c['sector']==e['sector']) for e in ev])/np.sqrt(12)
            variance=max(float(np.sum(res**2)/(len(n)-2)),float(floor*floor));err=float(np.sqrt(variance*np.linalg.inv(A.T@A)[1,1]));meaning='fit residual or cadence floor; uncalibrated for sector offsets'
        else:
            ee=[]
            for e in ev:
                cadence=next(c['cadence_days'] for c in d['coverage'] if c['sector']==e['sector']);ee.append(max(cadence/2,e['fit_mid_formal_error_days']))
            err=float(np.hypot(*ee)/abs(n[-1]-n[0]));meaning='quadrature of formal center errors with half-cadence floor; conditional on cycle count'
        out['kinds'][kind]={'event_indices':ids,'sectors':[e['sector'] for e in ev],'mid_btjd':t.tolist(),'cycles':n.tolist(),'period_days':float(par[1]),'period_error_days':err,'epoch_btjd':float(par[0]),'residual_days':res.tolist(),'error_meaning':meaning,'cycle_note':'Cycle labels near Gaia period, cross-checked against other kind and sector coverage; see report.'}
    (B/row['tic']/'lead-timing.json').write_text(json.dumps(out,indent=2)+'\n')
    print(row['sample_id'],[(k,round(v['period_days'],6),round(v['period_error_days'],6)) for k,v in out['kinds'].items()])
