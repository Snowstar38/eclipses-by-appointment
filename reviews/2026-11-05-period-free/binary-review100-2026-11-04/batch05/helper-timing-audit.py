import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares
B=Path(__file__).resolve().parent; raw=json.loads((B/'313617927'/'raw-inspection.json').read_text());res=[]
def model(p,t):
 c,w,ing,depth,b,s=p; x=np.abs(t-c); shape=np.clip((w/2+ing-x)/ing,0,1);return b+s*(t-c)-depth*shape
for sector,guess in [(15,1729.9),(17,1768.37)]:
 z=next(z for z in raw['sectors'] if z['sector']==sector);path=Path(z['path']);assert hashlib.sha256(path.read_bytes()).hexdigest()==z['sha256']
 with fits.open(path) as h:t=np.asarray(h[1].data['TIME'],float);f=np.asarray(h[1].data['SAP_FLUX'],float);q=np.asarray(h[1].data['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-guess)<2.0);t=t[ok];f=f[ok];f=f/np.median(f)
 fit=least_squares(lambda p:model(p,t)-f,[guess,.3,.7,.04,1,0],bounds=([guess-1,0.01,.05,0,.7,-.1],[guess+1,2,2,.3,1.3,.1]),loss='soft_l1',f_scale=.002)
 res.append({'sector':sector,'fitted_center_btjd':float(fit.x[0]),'parameters':fit.x.tolist(),'n':len(t),'rms':float(np.std(model(fit.x,t)-f)),'source_sha256':z['sha256']})
a,b=[z['fitted_center_btjd'] for z in res];out={'method':'Exploratory independent trapezoid plus linear baseline fit, local +/-2 d around s15/s17 troughs, raw SAP QUALITY=0; soft L1 residual. Strong changing baselines and imperfect shape dominate errors; no formal center errors assigned.','fits':res,'center_difference_days':b-a,'integer_period_aliases_days':{str(n):float((b-a)/n) for n in range(1,9)},'caution':'These two fitted troughs do not establish unique cycle count; checking other predicted epochs with explicit gap/coverage and morphology is required. Shorter periods would require unobserved additional events. Near 38.43d is consistent with Gaia but Gaia is not a timing alias test.'};(B/'helper-timing-audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
# Additional alias coverage diagnostics in sector 16, between measured same-kind events.
z=next(z for z in raw['sectors'] if z['sector']==16)
with fits.open(z['path']) as h:T=np.asarray(h[1].data['TIME'],float);F=np.asarray(h[1].data['SAP_FLUX'],float);Q=np.asarray(h[1].data['QUALITY'])
good=np.isfinite(T)&np.isfinite(F)&(Q==0);cad=np.median(np.diff(T[good]));tests=[]
for n in range(2,9):
 for k in range(1,n):
  c=a+(b-a)*k/n; core=good&(abs(T-c)<.25);left=good&(T>c-1.5)&(T<c-.8);right=good&(T>c+.8)&(T<c+1.5)
  def stats(mask,lo,hi):
   tt=T[mask];return {'n':int(mask.sum()),'expected':float((hi-lo)/cad),'coverage':float(min(1,mask.sum()*cad/(hi-lo))),'max_gap_days':float(np.max(np.diff(np.r_[lo,tt,hi]))) if len(tt) else float(hi-lo)}
  cs=stats(core,c-.25,c+.25);ls=stats(left,c-1.5,c-.8);rs=stats(right,c+.8,c+1.5)
  d=float(1000*(np.median(F[core])/(.5*(np.median(F[left])+np.median(F[right])))-1)) if min(core.sum(),left.sum(),right.sum())>3 else None
  tests.append({'alias_n':n,'cycle':k,'predicted_btjd':float(c),'core':cs,'left':ls,'right':rs,'delta_ppt':d})
out['sector16_alias_windows']=tests;out['alias_diagnostic_note']='Window coverage includes endpoints and internal gaps. Deltas are diagnostic only: baselines may contain the opposite conjunction or variability and center uncertainties have not been propagated. Not labeled sensitive nulls.';(B/'helper-timing-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print([(t['alias_n'],t['cycle'],round(t['predicted_btjd'],2),round(t['core']['coverage'],2),round(t['core']['max_gap_days'],2),None if t['delta_ppt'] is None else round(t['delta_ppt'],1)) for t in tests if t['core']['coverage']>.8])
