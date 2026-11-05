"""Descriptive separate-kind cycle regressions from helper's 2-day raw-SAP fits."""
import json
from pathlib import Path
import numpy as np
W=Path(__file__).resolve().parent
deep=json.loads((W/'helper-morphology-fits.json').read_text())+json.loads((W/'helper-morphology-s56-fits.json').read_text())
shallow=json.loads((W/'helper-167-shallow.json').read_text())
B={r['sector']:r['mid_btjd'] for r in deep if r['window_half_days']==2.0 or (r['sector']==56 and r['window_half_days']==1.5)}
A={r['sector']:r['center_btjd'] for r in shallow if r['window_half_days']==2.0}
rows=[]
for sec,cy in [(56,-13),(76,0),(82,4)]: rows.append(('B',sec,cy,B[sec]))
for sec,cy in [(15,-39),(55,-13),(75,0),(83,5)]:rows.append(('A',sec,cy,A[sec]))
X=np.array([[1 if kind=='A' else 0,1 if kind=='B' else 0,cy] for kind,sec,cy,t in rows],float)
y=np.array([r[3] for r in rows],float)
interA,interB,P=np.linalg.lstsq(X,y,rcond=None)[0]
fitted=X@np.array([interA,interB,P]);res=y-fitted
out={'tic':167197264,'timescale':'BTJD = BJD_TDB - 2457000','source':'QLP QUALITY=0 SAP local 2-day window trapezoids; numbers descriptive, not calibrated total errors',
     'gaia_period_days':41.804020454205606,'gaia_period_error_days':0.0106868865,
     'shared_period_days_descriptive':float(P),'A_reference_btjd':float(interA),'B_reference_btjd':float(interB),
     'A_to_B_offset_days':float(interB-interA),'half_period_days':float(P/2),
     'max_abs_residual_days':float(np.max(abs(res))),
     'event_rows':[{'kind':k,'sector':s,'cycle':c,'center_btjd':t,'fit_residual_days':float(rr)} for (k,s,c,t),rr in zip(rows,res)],
     'cycle_alias_note':'Same-kind sequences include separated 13, 4, 17 (B) and 26, 13, 5 (A) cycle intervals. Shared P near Gaia and consistent half-orbit phase separate the opposite kinds; orbital and shape systematics remain.',
     'uncertainty_note':'At least ~0.02 d event-center allowance from baseline/extraction differences; no formal precision period uncertainty is claimed.'}
(W/'ephemeris-167197264.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
