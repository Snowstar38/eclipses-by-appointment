import csv,json,numpy as np
from pathlib import Path
from scipy.optimize import curve_fit
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
B=Path('[local path omitted]');m=json.load(open(B/'measurements.json'));a=np.genfromtxt(B/'raw-windows.csv',delimiter=',',names=True);evs=[];fig,axs=plt.subplots(3,1,figsize=(9,8))
def f(x,b,s,q,d,c,w,k):return b+s*x+q*x*x-d*np.clip((w/2-abs(x-c))/k,0,1)
for ev in m['events']:
 if 'mid_btjd' not in ev:continue
 a1=a[(a['sector']==ev['sector'])&(a['cycle']==ev['cycle'])];x=a1['btjd']-ev['predicted_btjd'];y=a1['normalized_raw_sap'];ok=abs(x)<.23;x=x[ok];y=y[ok];noise=ev['oot_scatter_ppt']/1000
 try:
  p,c=curve_fit(f,x,y,p0=[1,0,0,.012,0,.10,.035],bounds=([.8,-1,-10,0,-.04,.02,.003],[1.2,1,10,.1,.04,.16,.08]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=20000)
  e=dict(ev);e.update(mid_btjd=ev['predicted_btjd']+p[4],depth_ppt=p[3]*1000,duration_days=p[5],formal_timing_error_days=float(c[4,4]**.5),timing_error_days=max(c[4,4]**.5,ev['cadence_days']/2),quadratic_baseline_coefficient=p[2]);evs.append(e)
  if len(evs) in (1,15,29):ax=axs[(1,15,29).index(len(evs))];ax.plot(x,y,'.');ax.plot(x,f(x,*p),'r');ax.set_title(str(ev['cycle'])+' residual core '+str(round(p[3]*1000,2))+'ppt')
 except Exception as exc:print(exc)
fig.tight_layout();fig.savefig(B/'quadratic-core.png');plt.close(fig)
n=np.array([e['cycle'] for e in evs]);t=np.array([e['mid_btjd'] for e in evs]);er=np.array([e['timing_error_days'] for e in evs]);X=np.array([n*0+1,n-n.min()]).T;C=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]));beta=C@((X/er[:,None]).T@(t/er));red=sum(((t-X@beta)/er)**2)/(len(t)-2);C*=max(red,1)
out=dict(events=evs,period_days=beta[1],period_error_days=C[1,1]**.5,epoch_btjd=beta[0],depth_ppt=np.median([e['depth_ppt'] for e in evs]),duration_days=np.median([e['duration_days'] for e in evs]),note='Quadratic local baseline permits broad phase modulation; free narrow trapezoid residual core. Bounded morphology robustness test; not total precision model.')
json.dump(out,open(B/'quadratic-core.json','w'),indent=2);print({k:v for k,v in out.items() if k!='events'})

(B/'broad-linear-model.json').write_text(json.dumps(m,indent=2))
m.update(events=evs,period_days=float(beta[1]),period_error_days=float(C[1,1]**.5),primary_epoch_btjd=float(beta[0]),epoch_cycle=int(n.min()),depth_ppt=float(out['depth_ppt']),timing_residual_days=(t-X@beta).tolist(),reduced_chi_square=float(red),epoch_kind='Narrow eclipse core atop broad phase modulation; physical primary identity unestablished',baseline_model='Quadratic baseline plus free narrow trapezoid; local window +/-0.23d',timing_event_count=len(evs))
(B/'measurements.json').write_text(json.dumps(m,indent=2))
