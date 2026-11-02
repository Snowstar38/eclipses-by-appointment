from pathlib import Path
import json,csv,numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
b=Path(__file__).parent
out={};fig,axs=plt.subplots(5,2,figsize=(14,16))
def model(x,base,slope,depth,center,width,ing):return base+slope*x-depth*np.clip((width/2-np.abs(x-center))/ing,0,1)
for ax,r in zip(axs.flat,csv.DictReader(open(b/'queue.csv'))):
 tic=r['tic'];m=json.load(open(b/tic/'measurements.json'));P=m['period_days'];ep=m['primary_epoch_btjd'];dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]);g=json.load(open(b/'gaia-geometry.json'))[tic];a=g['conjunction'];guess=((a[g['closest']['kind']]['offset_days']-a[1-g['closest']['kind']]['offset_days'])/g['period_days'])%1;guess={'73248723':.633,'150162108':.5,'274795477':.632,'14163319':.48,'352113274':.5003}.get(tic,guess);xs=[];ys=[];ss=[];cycles=[]
 for source in m['sources']:
  with fits.open(source['path']) as h:
   d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY']);ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[ok];f=f[ok]
  x=((t-ep)/P-guess+.5)%1-.5;x=x*P;sel=np.abs(x)<3*dur;oot=sel&(np.abs(x)>dur)
  if sum(oot)<10:continue
  y=f/np.median(f[oot]);xs.extend(x[sel]);ys.extend(y[sel]);ss.extend([source['sector']]*sum(sel));cycles.extend(np.rint((t[sel]-ep)/P-guess).astype(int))
 x=np.array(xs);y=np.array(ys);oot=np.abs(x)>dur;noise=1.4826*np.median(abs(y[oot]-np.median(y[oot])));ax.plot(x,y,'.',ms=1,alpha=.4)
 try:
  par,cov=curve_fit(model,x,y,p0=[1,0,max(.001,1-np.percentile(y,5)),0,dur,.2*dur],bounds=([.7,-1,0,-dur,.3*dur,.01*dur],[1.3,1,.8,dur,3*dur,dur]),sigma=np.full(len(x),max(noise,1e-5)),absolute_sigma=True,maxfev=20000)
  result=dict(status='Secondary-like narrow dip visually inspected; model describes selected pooled raw sector windows.',phase=(guess+par[3]/P)%1,formal_phase_error=np.sqrt(cov[3,3])/P,depth_ppt=par[2]*min(par[4]/(2*par[5]),1)*1000,extrapolated_amplitude_ppt=par[2]*1000,ingress_parameter_days=par[5],depth_meaning="Realized central model loss d*min(1,w/(2*k)); not extrapolated amplitude.",width_days=par[4],n_points=len(x),sectors=sorted(set(ss)),error_meaning='Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated.');xx=np.linspace(x.min(),x.max(),1000);ax.plot(xx,model(xx,*par),'r-')
 except Exception as e:result=dict(status='Fit failed; secondary unresolved',guess_phase=guess,error=str(e))
 result['observed_window_cycles']=[dict(sector=int(se),cycles=sorted(set(int(c) for se2,c in zip(ss,cycles) if se2==se))) for se in sorted(set(ss))]
 result['secure_secondary']=tic in ('73248723','352113274','265092213','257773097','150162108','274795477','441356022');result['visual_status']='Narrow shallower secondary visible in raw pooled windows' if result['secure_secondary'] else 'No secure secondary; noisy low-amplitude exploratory fit not interpreted as eclipse'
 np.savetxt(b/tic/'secondary-windows.csv',np.column_stack([ss,cycles,x,y]),delimiter=',',header='sector,orbital_cycle,days_from_search_phase,normalized_raw_sap',comments='')
 result['search_guess_provenance']='Gaia conjunction search guide, adjusted from observed raw phase morphology for this batch. Final phase is a free-center fit to observed raw flux.'
 ax.set_title(tic+' '+(str(round(result['phase'],5)) if 'phase'in result else 'unresolved secondary'));out[tic]=result
fig.tight_layout();fig.savefig(b/'secondary-contact.png',dpi=130);json.dump(out,open(b/'secondary-phases.json','w'),indent=2)

