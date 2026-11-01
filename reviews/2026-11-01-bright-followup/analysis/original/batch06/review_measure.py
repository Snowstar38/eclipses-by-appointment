import os,json,csv,hashlib,glob,urllib.request,concurrent.futures
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).parent
SB=Path('[local path omitted] 5/made/sb1-scale')
QUEUE=list(csv.DictReader(open(BASE/'queue.csv')))
SEA={r['tic']:r for r in map(json.loads,open(SB/'search.jsonl'))}
SAP=json.load(open(SB/'c6-sapdepth.json'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
receipts=[]
for row in QUEUE:
 tic=row['tic']
 for p in sorted((BASE.parent/'shared-qlp').glob(tic+'_s*.fits')):
  receipts.append(dict(tic=tic,sector=int(p.stem.split('_s')[1]),path=str(p),sha256=sha(p),status='ok'))
json.dump(receipts,open(BASE/'download-receipts.json','w'),indent=2)

def model(t,b,s,d,c,w,k):
 z=np.abs(t-c);shape=np.clip((w/2-z)/max(k,1e-5),0,1)
 return b+s*t-d*shape
for row in QUEUE:
 tic=row['tic'];out=BASE/tic;out.mkdir(exist_ok=True);sea=SEA[tic]
 # Historical SAP chose this photometric search branch; no Gaia period fixed in fitting.
 p0=SAP[tic]['P'];t0=SAP[tic]['t0'];branch=min((sea[k] for k in ('P','P2')),key=lambda r:abs(r['P']-p0));dur=branch['dur']
 events=[];windows=[];sources=[]
 for receipt in [r for r in receipts if r['tic']==tic and r['status']=='ok']:
  fp=receipt['path'];sources.append(receipt)
  with fits.open(fp) as h:
   a=h[1].data;t=np.array(a['TIME'],float);f=np.array(a['SAP_FLUX'],float);q=np.array(a['QUALITY'],int)
  ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok];cad=float(np.median(np.diff(t)))
  for cycle in range(int(np.ceil((t.min()-t0)/p0)),int(np.floor((t.max()-t0)/p0))+1):
   pred=t0+cycle*p0;ix=np.abs(t-pred)<min(3*dur,.35*p0);x=t[ix]-pred;y=f[ix];oot=np.abs(x)>dur
   if len(x)<25 or sum(oot&(x<0))<5 or sum(oot&(x>0))<5 or sum(abs(x)<dur/3)<4:continue
   y=y/np.median(y[oot]);noise=max(1.4826*np.median(abs(y[oot]-np.median(y[oot]))),1e-6)
   try:
    pars,cov=curve_fit(model,x,y,p0=[1,0,max(1-np.min(y),.001),0,dur,dur*.2],bounds=([.7,-1,0,-dur,.3*dur,.01*dur],[1.3,1,1,dur,6*dur,2*dur]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=20000)
    err=max(float(np.sqrt(max(cov[3,3],0))),cad/2);res=y-model(x,*pars)
    ev=dict(sector=receipt['sector'],cycle=cycle,predicted_btjd=pred,mid_btjd=pred+pars[3],timing_error_days=err,formal_timing_error_days=float(np.sqrt(max(cov[3,3],0))),depth_ppt=pars[2]*1000,duration_days=pars[4],cadence_days=cad,oot_scatter_ppt=noise*1000,resid_rms_ppt=float(np.std(res))*1000,n=len(x),fit_shift_days=pars[3])
    events.append(ev);windows.append((ev,x,y,model(x,*pars)))
   except Exception as e:events.append(dict(sector=receipt['sector'],cycle=cycle,error=str(e)))
 
 for e in events:
  if 'mid_btjd' in e:
   e['timing_usable']=bool(np.isfinite(e['formal_timing_error_days']) and 0 < e['formal_timing_error_days'] < dur)
   if not e['timing_usable']:e['timing_failure_reason']='Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris.'
 good=[e for e in events if e.get('timing_usable',False)];summary=dict(tic=tic,historical_period_days=p0,historical_epoch_btjd=t0,search_duration_days=dur,events=events,sources=sources)
 if tic=='102052526':
  good=[e for e in good if e['cycle']%2==0]
  summary['timing_selection']='Deeper even cycles only; alternating primary and secondary depths establish the doubled orbital period.'
  for e in good:e['orbital_cycle']=e['cycle']//2
 summary['epoch_kind']='Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established'
 if tic=='102052526':summary['epoch_kind']='Deeper repeating eclipse; even half-period cycles'
 summary['timing_event_count']=len(good)
 if len(good)>1:
  n=np.array([e.get('orbital_cycle',e['cycle']) for e in good]);tt=np.array([e['mid_btjd'] for e in good]);er=np.array([e['timing_error_days'] for e in good]);origin=n.min();X=np.array([np.ones(len(n)),n-origin]).T;cov=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=cov@((X/er[:,None]).T@(tt/er));res=tt-X@beta;red=float(sum((res/er)**2)/max(len(n)-2,1));cov*=max(red,1)
  summary.update(period_days=float(beta[1]),period_error_days=float(np.sqrt(cov[1,1])),primary_epoch_btjd=float(beta[0]),epoch_cycle=int(origin),timing_residual_days=res.tolist(),reduced_chi_square=red,error_meaning='Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.',depth_ppt=float(np.median([e['depth_ppt'] for e in good])))
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

