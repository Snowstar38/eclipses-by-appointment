import pathlib,json,sys,os
import numpy as np
from scipy.optimize import least_squares
from astropy.io import fits
O=pathlib.Path(__file__).parent
CASES={'167178300':(12.2153503443,1479.0748,.4),'325573958':(13.0818877332,2772.4944,.35),'155303130':(20.525,3238.1921,.6),'382042754':(25.89421,3979.6704,.35),'389128842':(22.6665,4134.5153,.4)}
out={}
for k,(P,t0,span) in CASES.items():
 paths=sorted((O/'fresh-data').glob(k+'_s*.fits')) if k in ['155303130','382042754','389128842'] else sorted((pathlib.Path(os.environ['TEMP'])/'hunt-sb1-scale').glob(k+'_s*.fits'))
 events=[]
 for p in paths:
  with fits.open(p) as ff:
   d=ff[1].data;m=np.isfinite(d['TIME'])&np.isfinite(d['SAP_FLUX'])&(d['QUALITY']==0);t=np.array(d['TIME'][m],float);f=np.array(d['SAP_FLUX'][m],float);f/=np.median(f)
  for n in range(int(np.ceil((t.min()-t0)/P)),int(np.floor((t.max()-t0)/P))+1):
   pred=t0+n*P;m=abs(t-pred)<1.5*span;x=t[m]-pred;y=f[m]
   if sum(m)<20 or sum(x<-.6*span)<4 or sum(x>.6*span)<4:continue
   def model(z):
    b,s,de,c,w,frac=z;shape=np.clip((w/2-abs(x-c))/(w/2*frac),0,1);return b+s*x-de*shape
   z=[float(np.median(y)),0,max(.001,float(np.median(y)-np.min(y))),0,span*.8,.7]
   fit=least_squares(lambda z:model(z)-y,z,bounds=([.1,-1,0,-span*.5,.03,.05],[3,1,.8,span*.5,span*1.5,1]),loss='soft_l1',f_scale=.005)
   b,s,de,c,w,frac=fit.x;noise=1.4826*np.median(abs(y-model(fit.x)-np.median(y-model(fit.x))));events.append({'sector':int(p.stem[-3:]),'cycle':n,'center':pred+c,'depth_ppt':de*1000,'duration_h':w*24,'rms_ppt':float(np.std(y-model(fit.x))*1000),'n':len(y),'center_at_bound':bool(abs(c)>.49*span),'reliable_for_fit':bool(de>max(.01,5*noise) and abs(c)<.49*span)})
 good=[e for e in events if e['reliable_for_fit']];result={'input_P':P,'input_t0':t0,'events':events}
 if len(good)>2:
  xx=np.array([e['cycle'] for e in good]);yy=np.array([e['center'] for e in good]);fit=np.polyfit(xx,yy,1);res=yy-np.polyval(fit,xx);result.update(period_days=float(fit[0]),epoch_btjd=float(fit[1]),timing_rms_minutes=float(np.sqrt(np.mean(res**2))*1440),events_fit=len(good),period_scatter_se_days=float(np.sqrt(sum(res**2)/(len(res)-2))/np.sqrt(sum((xx-np.mean(xx))**2))),error_meaning='OLSscatter standarderror; excludes cadence/template/systematic uncertainties')
 out[k]=result;print(k,{x:v for x,v in result.items() if x!='events'},flush=True)
(O/'timing-results.json').write_text(json.dumps(out,indent=1))
