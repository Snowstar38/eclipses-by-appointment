"""Same-kind integer-cycle fits; aliases remain subject to visual and Gaia checks."""
import csv,json
from pathlib import Path
import numpy as np

here=Path(__file__).resolve().parent
for row in csv.DictReader((here/'queue.csv').open()):
    tic=row['tic'];p0=float(row['gaia_period_days'])
    path=here/tic/'measurements.json';data=json.loads(path.read_text())
    fits={}
    for kind in ('A','B'):
        events=[e for e in data['events'] if e.get('timing_usable') and e['kind']==kind]
        if len(events)<2:continue
        events=sorted(events,key=lambda e:e['mid_btjd'])
        t=np.array([e['mid_btjd'] for e in events]);n=np.rint((t-t[0])/p0).astype(int)
        assert len(set(n))==len(n)
        err=np.array([e['conservative_timing_error_days'] for e in events]);X=np.column_stack((np.ones(len(n)),n))
        W=1/err**2;cov=np.linalg.inv(X.T@(W[:,None]*X));beta=cov@(X.T@(W*t))
        resid=t-X@beta;chi2=float(np.sum((resid/err)**2));dof=len(t)-2
        inflate=max(1,chi2/dof) if dof>0 else 1
        cov*=inflate
        fits[kind]=dict(cycles=n.tolist(),event_sectors=[e['sector'] for e in events],
            epoch_btjd=float(beta[0]),period_days=float(beta[1]),
            epoch_formal_error_days=float(np.sqrt(cov[0,0])),
            period_formal_error_days=float(np.sqrt(cov[1,1])),
            timing_residual_hours=(resid*24).tolist(),chi2=chi2,dof=dof,
            reduced_chi2=chi2/dof if dof>0 else None,
            covariance_days2=cov.tolist(),
            timing_note='Conditional weighted linear fit to raw QLP trapezoid centers, half-cadence floor; covariance scatter-inflated if dof>0. Does not include common pipeline timing offset, model or integer-cycle alias error.')
    data['same_kind_fits']=fits
    path.write_text(json.dumps(data,indent=2))
    print(tic,[(k,v['cycles'],round(v['period_days'],6),round(v['period_formal_error_days'],6),v['reduced_chi2']) for k,v in fits.items()])
