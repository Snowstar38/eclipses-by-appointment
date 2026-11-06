import json,numpy as np
from pathlib import Path
b=Path(__file__).resolve().parent
out={}
for tic,trial,cut in [('347159772',25.97803,100),('322438528',47.77994,20),('317322586',34.76826,85)]:
 e=json.loads((b/tic/'lead-timing.json').read_text())
 if tic=='347159772':ev=[x for x in e if x.get('fit_usable') and x['depth_ppt']<cut]
 elif tic=='322438528':ev=[x for x in e if x.get('fit_usable') and x['depth_ppt']>cut]
 else:ev=[x for x in e if x.get('fit_usable') and x['sector'] in [18,79] or x.get('fit_usable') and abs(x['center_btjd']-3639.90073)<.01]
 t=np.array([x['center_btjd'] for x in ev]);n=np.round((t-t[0])/trial).astype(int);X=np.array([np.ones(len(n)),n]).T
 if len(set(n))<2:continue
 v=np.linalg.lstsq(X,t,rcond=None)[0];out[tic]=dict(kind='opposite conjunction, fitted independently; never mixed with main clock',times=t.tolist(),cycles=n.tolist(),epoch_btjd=v[0],period_d=v[1],residuals_d=(t-X@v).tolist(),note='Unweighted representative same-kind timings; precision conditional on morphology and cadence; no covariance precision claim.')
 print(tic,out[tic])
(b/'lead-secondary-clocks.json').write_text(json.dumps(out,indent=2))
