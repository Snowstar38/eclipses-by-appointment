import json,numpy as np,hashlib
from pathlib import Path
R=Path(__file__).parent; src=R/'ambiguous-folds.json'; data=json.load(open(src)); out={}
for tic,rows in data.items():
 out[tic]=[]
 for row in rows:
  p=np.array(row['phase_bin_centers']);y=np.array(row['median_flux']);good=np.isfinite(y);p=p[good];y=y[good]; X=np.column_stack([np.ones(len(p))]+[f(2*np.pi*k*p) for k in (1,2,3,4) for f in (np.sin,np.cos)]);coef=np.linalg.lstsq(X,y,rcond=None)[0];res=y-X@coef; j=np.argmin(y); i=np.argmin(res); out[tic].append({'sector':row['sector'],'n_bins':len(p),'harmonic_order':4,'flux_min_phase':float(p[j]),'residual_min_phase':float(p[i]),'residual_min':float(res[i]),'residual_rms':float(np.std(res)),'folded_peak_to_peak':float(np.ptp(y)),'note':'Four-harmonic smooth model of 80-bin folded medians; diagnostic residuals are not detection upper limits and correlated systematics are not modeled.'})
json.dump({'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'results':out},open(R/'harmonic-diagnostic.json','w'),indent=2);print(json.dumps(out,indent=2))
