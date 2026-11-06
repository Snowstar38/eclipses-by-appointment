from pathlib import Path
import json,numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit
b=Path(__file__).resolve().parent;tic='467864145';d=json.loads((b/tic/'lead-context.json').read_text())
def model(x,base,slope,depth,center,width,ingress):return base+slope*x-depth*np.clip((width/2-abs(x-center))/(width*ingress),0,1)
def get(sec,c):
 src=next(s for s in d['source'] if s['sector']==sec)
 with fits.open(src['path']) as h:a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
 ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(abs(t-c)<3);x=t[ok]-c;y=f[ok];y=y/np.median(y[abs(x)>1.2]);return x,y
out=[]
for kind,c0,c1,N in [('A',2941.54737,3306.08,10),('B',2959.77252,3287.85,9)]:
 x,y=get(60,c0);p,cv=curve_fit(model,x,y,p0=[1,0,.02,0,1.8,.1],bounds=([.8,-.1,0,-.2,1,.03],[1.2,.1,.1,.2,2.5,.49]));mid=c0+p[3];x,y=get(73,c1)
 trials=[]
 for factor in [.95,1,1.05]:
  def fixed(x,base,slope,depth,center):return model(x,base,slope,depth,center,p[4]*factor,p[5])
  pp,cc=curve_fit(fixed,x,y,p0=[1,0,p[2],0],bounds=([.8,-.1,0,-.6],[1.2,.1,.1,.6]));trials.append(dict(width_factor=factor,center_btjd=float(c1+pp[3]),formal_error_d=float(np.sqrt(cc[3,3])),depth_ppt=float(pp[2]*1000)))
 out.append(dict(kind=kind,template_center_btjd=mid,template_width_d=float(p[4]),template_ingress_fraction=float(p[5]),cycles=N,partial_event_trials=trials,period_d=(trials[1]['center_btjd']-mid)/N,note='S73 incomplete event; fixed S60 morphology with +/-5% width sensitivity. Formal errors omit correlated variability and missing ingress. Recurrence evidence, not precision independent epoch.'))
(b/'lead-partial-templates.json').write_text(json.dumps(out,indent=2));print(out)
