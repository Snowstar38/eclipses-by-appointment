"""Contact coverage refinement: long eclipse and third partial eclipse; no predicted point used as timing."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text())
def model(x,b,s,d,c,w,k):return b+s*x-d*np.clip((w/2-abs(x-c))/k,0,1)
tic='449012335';old=json.loads((B/tic/'measurements.json').read_text());(B/tic/'initial-wide-measurements.json').write_text(json.dumps(old,indent=2)+'\n');events=[];panels=[]
P=21.65482456020135;t0=1616.0634939357894
for r in D[tic]['target']['file_receipts']:
 if r['sector'] not in (11,12,65,100,101,102):continue
 with fits.open(r['path']) as h:
  a=h[1].data;t=np.asarray(a['TIME']);f=np.asarray(a['SAP_FLUX']);q=np.asarray(a['QUALITY'])
 valid=np.isfinite(t)&np.isfinite(f)&(q==0)&(f>0);t=t[valid];f=f[valid];cad=np.median(np.diff(t))
 for n in range(int(np.floor((t.min()-t0)/P)),int(np.ceil((t.max()-t0)/P))+1):
  pred=t0+n*P+.6;ix=abs(t-pred)<2.4;x=t[ix]-pred;y=f[ix];oot=abs(x)>1.3
  if len(x)<30 or sum(oot&(x<0))<4 or sum(oot&(x>0))<4:continue
  y=y/np.median(y[oot]);noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-5)
  if sum(abs(x)<.4)<3 or np.median(y[abs(x)<.4])>.99:continue
  try:
   pars,cov=curve_fit(model,x,y,p0=[1,0,.045,0,1.9,.25],bounds=([.9,-.05,.005,-.6,1,.03],[1.1,.05,.15,.6,3,.8]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=20000)
   c=pars[3];w=pars[4];k=pars[5];contacts=[c-w/2+k/2,c+w/2-k/2];counts=[int(sum(abs(x-z)<max(.1,k/2))) for z in contacts];expected=max(.1,k/2)*2/cad;coverage=[n/expected for n in counts]
   formal=float(np.sqrt(max(0,cov[3,3])));usable=bool(min(coverage)>.6 and abs(c)<.55 and 0<formal<.1)
   e=dict(sector=r['sector'],cycle=n,predicted_btjd=pred,mid_btjd=float(pred+c),formal_timing_error_days=formal,timing_error_days=max(formal,.02),timing_usable=usable,depth_ppt=float(pars[2]*1000),duration_days=float(w),ingress_parameter_days=float(k),oot_scatter_ppt=float(noise*1000),n=len(x),cadence_days=float(cad),source_sha256=r['sha256'],contact_coverage_fractions=coverage)
   events.append(e);panels.append((e,x,y,model(x,*pars)))
  except Exception as exc:print(exc)
good=[e for e in events if e['timing_usable']];n=np.array([e['cycle'] for e in good]);tt=np.array([e['mid_btjd'] for e in good]);err=np.array([e['timing_error_days'] for e in good]);X=np.column_stack([np.ones(len(n)),n-n.min()]);A=X/err[:,None];C=np.linalg.inv(A.T@A);beta=C@(A.T@(tt/err));res=tt-X@beta;red=float(sum((res/err)**2)/(len(n)-2)) if len(n)>2 else None;C*=max(red or 1,1)
old.update(events=events,timing_event_count=len(good),period_days=float(beta[1]),period_error_days=float(np.sqrt(C[1,1])),reference_epoch_btjd=float(beta[0]),epoch_error_days=float(np.sqrt(C[0,0])),reference_cycle=int(n.min()),reduced_chi_square=red,timing_residual_days=res.tolist(),depth_ppt=float(np.median([e['depth_ppt'] for e in good])),timing_error_meaning='Representative contact-covered long-eclipse trapezoids; individual max(formal covariance, 0.02 day conservative model allowance), scatter inflated if reduced chi square >1. The 0.02 day allowance is not a calibrated statistical error.',fit_refinement='2.4-day half-window around shifted search seed, OOT beyond 1.3d; retain timings only if >=60% expected cadence coverage at both modeled contacts. Initial clipped and gapped fits retained separately, excluded from adopted ephemeris.')
(B/tic/'measurements.json').write_text(json.dumps(old,indent=2)+'\n');fig,axs=plt.subplots(len(panels),1,figsize=(9,len(panels)*2.3),squeeze=False)
for ax,(e,x,y,z) in zip(axs[:,0],panels):
 ax.plot(x,y,'.',ms=2);ax.plot(x,z,'r-');ax.set_title(f"s{e['sector']} cycle{e['cycle']} measured {e['mid_btjd']:.5f}, usable={e['timing_usable']} contact fractions {np.round(e['contact_coverage_fractions'],2)}",fontsize=9)
fig.tight_layout();fig.savefig(B/tic/'refined-raw-events.png',dpi=120);plt.close(fig)
print(tic,len(good),old['period_days'],[(e['sector'],e['cycle'],e['timing_usable']) for e in events])
# Third occasion: retain raw central deficit sample times, without using a gapped fit as a timing.
tic='436013770';r=next(r for r in D[tic]['target']['file_receipts'] if r['sector']==98)
with fits.open(r['path']) as h:a=h[1].data;t=np.asarray(a['TIME']);f=np.asarray(a['SAP_FLUX']);q=np.asarray(a['QUALITY'])
sel=np.isfinite(t)&np.isfinite(f)&(q==0)&(abs(t-4010.1)<.7);t=t[sel];f=f[sel];base=np.median(f[abs(t-4010.1)>.4]);deep=t[f/base<.975]
(B/tic/'partial-third-event.json').write_text(json.dumps(dict(sector=98,source_sha256=r['sha256'],central_deficit_sample_times_btjd=deep.tolist(),sample_threshold='raw SAP <0.975 of nearby OOT median; actual sample times, not a fitted center',median_deep_time_btjd=float(np.median(deep))),indent=2)+'\n')

