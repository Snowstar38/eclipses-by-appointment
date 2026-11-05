import json
from pathlib import Path
import numpy as np
here=Path(__file__).resolve().parent
older=json.loads((here/'older-events.json').read_text())
for tic,kind in [('331650047','A'),('384744604','A'),('109560492','B')]:
    path=here/tic/'measurements.json';m=json.loads(path.read_text())
    old=[e for e in older if e['tic']==tic and e['kind']==kind and 'center_btjd' in e]
    current=[e for e in m['events'] if e.get('timing_usable') and e['kind']==kind]
    assert len(old)==1 and len(current)>=2
    all_events=[dict(sector=e['sector'],time=e['mid_btjd'],err=e['conservative_timing_error_days'],depth=e['depth_ppt'],source='frozen latest-three') for e in current]
    all_events += [dict(sector=e['sector'],time=e['center_btjd'],err=e['conservative_timing_error_days'],depth=e['depth_ppt'],source='adaptive older QLP') for e in old]
    all_events.sort(key=lambda e:e['time'])
    p0=m['gaia_period_days'];t=np.array([e['time'] for e in all_events]);n=np.rint((t-t[0])/p0).astype(int)
    assert len(set(n))==len(n)
    err=np.array([e['err'] for e in all_events]);X=np.column_stack((np.ones(len(n)),n));W=1/err**2
    cov=np.linalg.inv(X.T@(W[:,None]*X));beta=cov@(X.T@(W*t));res=t-X@beta
    chi=float(np.sum((res/err)**2));dof=len(n)-2;cov*=max(1,chi/dof) if dof>0 else 1
    m['augmented_same_kind_fit']=dict(kind=kind,events=all_events,cycles_from_epoch=n.tolist(),
        epoch_btjd=float(beta[0]),period_days=float(beta[1]),
        epoch_formal_error_days=float(np.sqrt(cov[0,0])),period_formal_error_days=float(np.sqrt(cov[1,1])),
        covariance_days2=cov.tolist(),timing_residual_hours=(res*24).tolist(),chi2=chi,dof=dof,
        reduced_chi2=chi/dof if dof else None,
        error_meaning='Weighted raw QLP trapezoid centers, each floored at half its cadence; covariance inflated by reduced chi square above one. Conditional statistical precision; model/pipeline and alias uncertainty separate.',
        alias_note='Photometric period based on same-kind cycle assignment; multiple noncommensurate spacings reject adjacent integer-cycle aliases.' if tic!='331650047' else 'Even-cycle spacings alone permit half-period alias, but three adequately sampled odd half-cycles are clean nulls (half-alias-windows.json).')
    path.write_text(json.dumps(m,indent=2))
    print(tic,n.tolist(),beta.tolist(),[float(np.sqrt(cov[0,0])),float(np.sqrt(cov[1,1]))],chi/dof)
