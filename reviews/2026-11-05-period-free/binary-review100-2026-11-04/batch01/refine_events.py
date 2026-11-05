"""Local bounded trapezoid fits for the two convincing raw eclipse candidates."""
import hashlib
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares

B=Path(__file__).resolve().parent
CASES={
 '352438536':[(27,2040.08,2.6),(101,4105.95,2.7),(103,4166.13,1.8)],
 '322217134':[(70,3231.91,1.7),(92,3814.80,1.5)],
}

def trapezoid(x,p):
    base,slope,depth,center,dur,ingress=p
    a=np.abs(x-center)
    eclipse=np.clip((dur/2-a)/ingress,0,1)
    return base+slope*x-depth*eclipse

for tic,windows in CASES.items():
    data=json.loads((B/tic/'raw-inspection.json').read_text())
    fits_out=[]
    for sector,guess,half in windows:
        receipt=next(s for s in data['sectors'] if s['sector']==sector)
        fp=Path(receipt['path'])
        if hashlib.sha256(fp.read_bytes()).hexdigest()!=receipt['sha256']:
            raise RuntimeError('source hash mismatch')
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-guess)<half)
        t=t[ok];f=f[ok];x=t-guess
        scale=np.median(f);y=f/scale
        if tic=='352438536':
            p0=[1,0,.04,0,2.5,.25]
            lo=[.8,-.05,.001,-.8,1,.03];hi=[1.2,.05,.2,.8,4,.8]
        else:
            p0=[1,0,.08,0,1.4,.25]
            lo=[.8,-.05,.001,-.7,.4,.03];hi=[1.2,.05,.2,.7,3,.8]
        robust=least_squares(lambda p:trapezoid(x,p)-y,p0,bounds=(lo,hi),loss='soft_l1',f_scale=.003,max_nfev=10000)
        p=robust.x
        residual=y-trapezoid(x,p)
        fit={'sector':sector,'window_guess_btjd':guess,'n_quality0':len(x),'first_btjd':float(min(t)),'last_btjd':float(max(t)),
             'fit_baseline':float(p[0]),'fit_slope_per_day':float(p[1]),'fit_depth_ppt':float(1000*p[2]),
             'fit_center_btjd':float(guess+p[3]),'fit_duration_days':float(p[4]),'fit_ingress_days':float(p[5]),
             'residual_mad_ppt':float(1482.6*np.median(abs(residual-np.median(residual)))),
             'fit_cost':float(robust.cost),'fit_success':bool(robust.success),
             'caution':'Center is exploratory; gap-interrupted/partial windows and nonstationary baselines may make fit unreliable.'}
        fit['timing_usable']=not (tic=='352438536' and sector==103) and not (tic=='322217134' and sector==92)
        if not fit['timing_usable']:
            fit['parameter_exclusion_reason']='Ingress/egress gap or quality censoring makes the fitted center, duration and depth model-dependent; use only morphology and bounded contact timing.'
        fits_out.append(fit)
    (B/tic/'local-fits.json').write_text(json.dumps({'tic':tic,'fits':fits_out},indent=2)+'\n')
    print(tic,[(f['sector'],round(f['fit_center_btjd'],4),round(f['fit_depth_ppt'],1),round(f['fit_duration_days'],2)) for f in fits_out])
