import os,json,csv,hashlib,glob,urllib.request,concurrent.futures
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).parent
SB=Path('[local-path-redacted] 5/made/sb1-scale')
QUEUE=list(csv.DictReader(open(BASE/'queue.csv')))
SEA={r['tic']:r for r in map(json.loads,open(BASE.parent/'source-snapshots/search.jsonl'))}
SAP=json.load(open(BASE.parent/'source-snapshots/c10-sapdepth.json'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipts=json.load(open(BASE/'download-receipts.json'))

def model(t,b,s,d,c,w,k):
 z=np.abs(t-c);shape=np.clip((w/2-z)/max(k,1e-5),0,1)
 return b+s*t-d*shape
for row in QUEUE:
 tic=row['tic'];out=BASE/tic;out.mkdir(exist_ok=True);sea=SEA[tic]
 # Historical SAP chose this photometric search branch; no Gaia period fixed in fitting.
 seed=SAP.get(tic) or sea['P'];p0=seed['P'];t0=seed['t0'];branch=min((sea[k] for k in ('P','P2')),key=lambda r:abs(r['P']-p0));dur=branch['dur']
 original_seed_period=p0
 # No inherited target-specific branch; inspect parity after the first fit.
 events=[];windows=[];sources=[]
 for receipt in [r for r in receipts if r['tic']==tic and r['status']=='ok']:
  fp=receipt['file'];sources.append(dict(receipt,path=fp))
  with fits.open(fp) as h:
   a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
  if len(t)<12:continue
  cad=float(np.median(np.diff(t)))
  for cycle in range(int(np.ceil((t.min()-t0)/p0)),int(np.floor((t.max()-t0)/p0))+1):
   pred=t0+cycle*p0;ix=np.abs(t-pred)<min(3*dur,.35*p0);x=t[ix]-pred;y=f[ix];oot=np.abs(x)>dur
   if len(x)<12 or sum(oot&(x<0))<3 or sum(oot&(x>0))<3 or sum(abs(x)<dur/3)<2:continue
   y=y/np.median(y[oot]);noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-6)
   try:
    pars,cov=curve_fit(model,x,y,p0=[1,0,max(1-np.min(y),.001),0,dur,dur*.2],bounds=([.7,-1,0,-dur,.3*dur,.01*dur],[1.3,1,1,dur,6*dur,2*dur]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=20000)
    err=max(float(np.sqrt(max(cov[3,3],0))),cad/2);res=y-model(x,*pars)
    jac=np.column_stack([(model(x,*(pars+np.eye(6)[j]*max(abs(pars[j])*1e-5,1e-7)))-model(x,*(pars-np.eye(6)[j]*max(abs(pars[j])*1e-5,1e-7))))/(2*max(abs(pars[j])*1e-5,1e-7)) for j in range(6)])
    sing=np.linalg.svd(jac,compute_uv=False);condition=float(sing[0]/sing[-1]) if sing[-1]>0 else float('inf')
    ev=dict(sector=receipt['sector'],cycle=cycle,predicted_btjd=pred,mid_btjd=pred+pars[3],timing_error_days=err,formal_timing_error_days=float(np.sqrt(max(cov[3,3],0))),jacobian_condition=condition,depth_ppt=pars[2]*min(pars[4]/(2*pars[5]),1)*1000,extrapolated_amplitude_ppt=pars[2]*1000,ingress_parameter_days=pars[5],depth_meaning="Realized central trapezoid model loss d*min(1,w/(2*k)); d is extrapolated if k>w/2.",duration_days=pars[4],cadence_days=cad,oot_scatter_ppt=noise*1000,resid_rms_ppt=float(np.std(res))*1000,n=len(x),fit_shift_days=pars[3])
    events.append(ev);windows.append((ev,x,y,model(x,*pars)))
   except Exception as e:events.append(dict(sector=receipt['sector'],cycle=cycle,error=str(e)))
 
 for e in events:
  if 'mid_btjd' in e:
   e['timing_usable']=bool(np.isfinite(e['formal_timing_error_days']) and 0 < e['formal_timing_error_days'] < dur and np.isfinite(e['jacobian_condition']) and e['jacobian_condition']<1e12)
   if not e['timing_usable']:e['timing_failure_reason']='Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris.'
   if tic=='187202091' and e['sector'] in (73,86):
    e['timing_usable']=False;e['timing_failure_reason']='Curved raw baseline draws trapezoid center away from local dip; excluded from raw trapezoid timing fit.'
 good=[e for e in events if e.get('timing_usable',False)]
 summary=dict(tic=tic,historical_period_days=original_seed_period,fitting_period_seed_days=p0,historical_epoch_btjd=t0,search_duration_days=dur,events=events,sources=sources)
 summary['epoch_kind']='Selected repeating eclipse; deeper identity assessed from observed secondary in report'
 summary['timing_event_count']=len(good)
 if len(good)>1:
  n=np.array([e.get('orbital_cycle',e['cycle']) for e in good]);tt=np.array([e['mid_btjd'] for e in good]);er=np.array([e['timing_error_days'] for e in good]);origin=n.min();X=np.array([np.ones(len(n)),n-origin]).T;cov=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=cov@((X/er[:,None]).T@(tt/er));res=tt-X@beta;red=float(sum((res/er)**2)/(len(n)-2)) if len(n)>2 else None;cov*=max(red or 1,1)
  summary.update(epoch_error_days=float(np.sqrt(cov[0,0])),period_days=float(beta[1]),period_error_days=float(np.sqrt(cov[1,1])),ephemeris_covariance_days2=cov.tolist(),primary_epoch_btjd=float(beta[0]),epoch_cycle=int(origin),timing_residual_days=res.tolist(),reduced_chi_square=red,error_meaning='Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.',depth_ppt=float(np.median([e['depth_ppt'] for e in good])))
 if tic=='187202091':
  summary['raw_trapezoid_ephemeris_crosscheck']={k:summary[k] for k in ('primary_epoch_btjd','period_days','period_error_days','ephemeris_covariance_days2','reduced_chi_square')}
  # Reproduce the earlier local-minimum measurement (persec187-out.txt lines 135-141).
  # Its listed uncertainties are heuristic minima-window widths, not calibrated errors.
  nn=np.array([0,108,109,145,180]);tt=np.array([1824.157,2918.102,2928.286,3292.943,3647.350]);er=np.array([2.16,1.20,.90,1.02,1.68])/24
  X=np.column_stack((np.ones(len(nn)),nn));cov=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=cov@((X/er[:,None]).T@(tt/er));red=float(sum(((tt-X@beta)/er)**2)/(len(nn)-2))
  cov*=max(red,1)
  summary.update(primary_epoch_btjd=float(beta[0]),period_days=float(beta[1]),period_error_days=float(np.sqrt(cov[1,1])),epoch_error_days=float(np.sqrt(cov[0,0])),ephemeris_covariance_days2=cov.tolist(),reduced_chi_square=red,epoch_cycle=0,epoch_kind='Selected repeating dip; deeper primary designation unestablished',timing_event_count=5,adopted_timing_source='Fable 5/made/sb1-scale/persec187-out.txt lines 135-141: local minima remeasured from QLP SAP, independently reproduced here from five rounded midpoints',adopted_local_minima=[dict(sector=s,cycle=int(n),mid_btjd=float(t),heuristic_width_hours=float(h)) for s,n,t,h in zip((19,59,59,73,86),nn,tt,er*24)],error_meaning='Weighted linear fit to rounded historical local-minimum times, with listed heuristic minima widths (0.9-2.16 h); formal covariance conditional on these widths, not calibrated coverage. Curved baselines especially s73/s86 and same-photon processing limit precision.',depth_ppt=float(np.median([e['depth_ppt'] for e in good])))
 if tic=='54054420':
  summary['photometric_interval_fit']={k:summary[k] for k in ('primary_epoch_btjd','period_days','period_error_days','ephemeris_covariance_days2')}
  even=[e for e in good if e['cycle']%2==0];nn=np.array([e['cycle']//2 for e in even]);tt=np.array([e['mid_btjd'] for e in even]);er=np.array([e['timing_error_days'] for e in even]);origin=nn.min();X=np.column_stack((np.ones(len(nn)),nn-origin));cov=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=cov@((X/er[:,None]).T@(tt/er));red=float(sum(((tt-X@beta)/er)**2)/(len(nn)-2));cov*=max(red,1)
  summary.update(primary_epoch_btjd=float(beta[0]),period_days=float(beta[1]),period_error_days=float(np.sqrt(cov[1,1])),epoch_error_days=float(np.sqrt(cov[0,0])),ephemeris_covariance_days2=cov.tolist(),epoch_cycle=int(origin),reduced_chi_square=red,timing_event_count=len(even),timing_selection='Even photometric cycles only, giving same-kind recurrence at Gaia-like 4.4445 d; odd cycles have similar depths so photometry alone does not establish their physical identity.',epoch_kind='One of two nearly equal-depth dips; deeper primary designation unestablished',error_meaning='Weighted same-kind even-cycle fit, per-event max(formal center covariance, half cadence), scatter inflated if reduced chi-square >1; conditional statistical covariance, not calibrated total ephemeris uncertainty.')
 if tic=='357019754':summary['epoch_kind']='Deep selected eclipse (primary by depth); shallower secondary visible near half phase'
 if tic=='402782627':summary['epoch_kind']='Selected recurring dip; deeper primary designation unestablished'
 if tic=='462088261':summary['epoch_kind']='Selected recurring dip; eclipse nature unestablished'
 if windows:
  fig,axs=plt.subplots(min(len(windows),6),1,figsize=(9,min(len(windows),6)*2.3),squeeze=False)
  picks=np.linspace(0,len(windows)-1,min(len(windows),6)).astype(int)
  for ax,i in zip(axs[:,0],picks):
   e,x,y,fit=windows[i];ax.plot(x,y,'.',ms=3);ax.plot(x,fit,'r-');ax.set_title(f"TIC {tic} s{e['sector']} cycle {e['cycle']} depth {e['depth_ppt']:.2f} ppt mid {e['mid_btjd']:.5f}");ax.set_xlabel('Days from historical predicted center');ax.set_ylabel('Raw SAP / local baseline')
  fig.tight_layout();fig.savefig(out/'raw-events.png',dpi=130);plt.close(fig)
  with open(out/'raw-windows.csv','w',newline='') as f:
   w=csv.writer(f);w.writerow(['sector','cycle','btjd','normalized_raw_sap','trapezoid_fit'])
   for e,x,y,fit in windows:w.writerows(zip([e['sector']]*len(x),[e['cycle']]*len(x),x+e['predicted_btjd'],y,fit))
 json.dump(summary,open(out/'measurements.json','w'),indent=2)
 print(tic,len(good),summary.get('period_days'),flush=True)

