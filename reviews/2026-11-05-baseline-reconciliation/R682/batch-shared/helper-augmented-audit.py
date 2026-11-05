import json,numpy as np
from pathlib import Path
p=Path(__file__).parent; out={}
for tic in ['331650047','384744604','109560492']:
 a=json.loads((p/tic/'measurements.json').read_text())['augmented_same_kind_fit']; ev=a['events']; n=np.array(a['cycles_from_epoch']); t=np.array([x['time'] for x in ev]); w=1/np.array([x['err'] for x in ev])**2; nb=np.average(n,weights=w); tb=np.average(t,weights=w); P=np.sum(w*(n-nb)*(t-tb))/np.sum(w*(n-nb)**2); epoch=tb-P*nb; residual=t-(epoch+P*n); chi=np.sum(w*residual**2); err=(1/np.sum(w*(n-nb)**2))**.5*max(1,chi/(len(n)-2))**.5; out[tic]={'period':P,'error':err,'epoch':epoch,'chi2':chi,'delta_period':P-a['period_days'],'delta_error':err-a['period_formal_error_days'],'cycles':n.tolist()}
(p/'helper-augmented-audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
