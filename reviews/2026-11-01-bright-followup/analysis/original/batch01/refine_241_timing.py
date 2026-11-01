"""Fit actual S18 raw eclipse midpoints; never fit predicted centers as observations."""
import json,numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
from pathlib import Path
B=Path(__file__).parent;D=B/'241089793';m=json.loads((D/'measurements.json').read_text());p=m['historical_period_days'];t0=m['historical_epoch_btjd']
with fits.open(B.parent/'shared-qlp'/'241089793_s018.fits') as h:
 a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
def model(x,b,s,d,c,w,k):return b+s*x-d*np.clip((w/2-np.abs(x-c))/max(k,1e-6),0,1)
fits_out=[]
for cyc in (-1,0,2,3):
 pred=t0+cyc*p;good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(np.abs(t-pred)<.35);x=t[good]-pred;y=f[good];base=np.median(y[np.abs(x)>.14]);y=y/base
 try:
  par,cov=curve_fit(model,x,y,p0=[1,0,.018,0,.09,.025],bounds=([.95,-.2,.005,-.06,.035,.005],[1.05,.2,.05,.06,.18,.09]),maxfev=100000)
  err=float(np.sqrt(max(cov[3,3],0)));usable=bool(np.isfinite(err) and 0<err<.04 and min(x)<-.10 and max(x)>.10)
  fits_out.append(dict(sector=18,cycle=cyc,predicted_guide_btjd=pred,measured_mid_btjd=float(pred+par[3]),formal_error_days=err,conservative_error_days=max(err,.01042),depth_ppt=float(par[2]*1000),duration_days=float(par[4]),usable=usable,quality_zero_points=int(good.sum())))
 except Exception as e:fits_out.append(dict(sector=18,cycle=cyc,error=str(e),usable=False))
selected=[e for e in fits_out if e.get('usable')]+[dict(sector=e['sector'],cycle=e['cycle'],measured_mid_btjd=e['mid_btjd'],conservative_error_days=e['timing_error_days']) for e in m['events'] if e.get('timing_usable')]
n=np.array([e['cycle'] for e in selected]);tt=np.array([e['measured_mid_btjd'] for e in selected]);err=np.array([e['conservative_error_days'] for e in selected]);origin=min(n);X=np.array([np.ones(len(n)),n-origin]).T;cov=np.linalg.inv((X/err[:,None]).T@(X/err[:,None]));beta=cov@((X/err[:,None]).T@(tt/err));res=tt-X@beta;red=float(sum((res/err)**2)/max(len(n)-2,1));cov*=max(red,1)
out=dict(s18_fits=fits_out,selected_midpoints=selected,epoch_kind='repeating eclipse; primary by convention',epoch_cycle=int(origin),primary_epoch_btjd=float(beta[0]),period_days=float(beta[1]),period_error_days=float(np.sqrt(cov[1,1])),residual_days=res.tolist(),reduced_chi_square=red,error_meaning='Linear fit to independently measured raw S18 and S85 midpoints, with max(formal center covariance, half cadence) per event and scatter inflation; formal fit error, not total calibrated uncertainty. Historical period/cycle predictions guided extraction only.',alias_note='S18 quality-zero raw eclipses in successive cycles -1 and 0 and cycle 2 reject the 11.26386-day double-period interpretation; S85 intervening cycle 325 is all flagged and never treated as a clean null.')
(B/'241089793-refined-timing.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
m['initial_s85_only_timing']={k:m[k] for k in ['period_days','period_error_days','primary_epoch_btjd','timing_event_count','error_meaning']}
for e in fits_out:
 if 'measured_mid_btjd' in e:
  m['events'].append(dict(sector=18,cycle=e['cycle'],predicted_btjd=e['predicted_guide_btjd'],mid_btjd=e['measured_mid_btjd'],formal_timing_error_days=e['formal_error_days'],timing_error_days=e['conservative_error_days'],depth_ppt=e['depth_ppt'],duration_days=e['duration_days'],timing_usable=e['usable'],timing_failure_reason='' if e['usable'] else 'Partial coverage; excluded from joint timing fit.',n=e['quality_zero_points']))
for k in ['epoch_kind','epoch_cycle','primary_epoch_btjd','period_days','period_error_days','reduced_chi_square','error_meaning']:
 m[k]=out[k]
m['timing_event_count']=len(selected)
m['depth_ppt']=float(np.median([e['depth_ppt'] for e in m['events'] if e.get('timing_usable')]))
m['timing_selection']='Measured S18 successive-cycle raw eclipses plus two S85 midpoints; S18 partial cycle 3 excluded; flagged S85 odd-cycle windows not nulls.'
(D/'measurements.json').write_text(json.dumps(m,indent=2))
