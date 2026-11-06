"""Local trapezoid fits to selected same-kind raw SAP events; no Gaia period fixed."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit

B=Path(__file__).resolve().parent
# Selected by visible raw morphology.  Distinct conjunction kinds are separate.
SEL={}
for fp in B.glob('*/lead-context.json'):
 d=json.loads(fp.read_text());SEL[d['tic']]=[(e['sector'],e['screen_btjd'],'candidate') for e in d['flag_events']]
for tic in ('159860053','436205524','277772867'):
 SEL[tic]=[(sec,c,('deep' if (tic=='159860053' and sec==28 and c<2070) or (tic=='436205524' and any(abs(c-v)<.2 for v in [1695.74,2421.21,2444.61,2819.05])) or (tic=='277772867' and abs(c-1344.83)>.2) else 'shallow')) for sec,c,k in SEL[tic]]
SEL['440995465']=[(64,3049.04,'A'),(64,3058.10,'A'),(64,3067.11,'A'),(65,3076.14,'A'),(65,3085.17,'A'),(65,3094.20,'A'),(64,3044.76,'B'),(64,3053.78,'B'),(64,3062.80,'B'),(65,3071.83,'B'),(65,3080.86,'B'),(65,3089.89,'B')]
def trap(x,b,s,d,c,w,ing):
    z=np.abs(x-c);return b+s*x-d*np.clip((w/2-z)/(w*ing),0,1)

for tic,items in SEL.items():
    context=json.loads((B/tic/'lead-context.json').read_text());out=[]
    for sec,pred,kind in items:
        src=next(s for s in context['source'] if s['sector']==sec)
        with fits.open(src['path']) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(np.abs(t-pred)<.9)
        x=t[ok]-pred;y=f[ok]
        if len(x)<16:continue
        base=(np.abs(x)>.5);scale=float(np.median(y[base])) if base.sum()>8 else float(np.median(y));y=y/scale
        noise=max(float(1.4826*np.median(np.abs(y[base]-np.median(y[base])))),.0002) if base.sum()>8 else .002
        try:
            p,cov=curve_fit(trap,x,y,p0=[1,0,max(1-y.min(),.005),0,.35,.3],bounds=([.8,-.2,0,-.13,.05,.05],[1.2,.2,.8,.13,.9,.49]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000)
            err=float(np.sqrt(max(cov[3,3],0)))
            fit=dict(center_btjd=float(pred+p[3]),center_formal_error_d=err,depth_ppt=float(p[2]*1000),duration_d=float(p[4]),ingress_d=float(p[4]*p[5]),baseline_slope_d=float(p[1]),residual_rms_ppt=float(np.std(y-trap(x,*p))*1000),fit_usable=bool(np.isfinite(err) and err>0 and err<.1 and abs(p[3])<.125 and p[2]>.002 and p[4]>.052 and p[4]<.895))
        except Exception as e:fit={'fit_error':str(e)}
        out.append(dict(sector=sec,screen_btjd=pred,kind=kind,n=len(x),cadence_d=float(np.median(np.diff(t[ok]))),first_btjd=float(t[ok].min()),last_btjd=float(t[ok].max()),scale_sap=scale,noise_ppt=noise*1000,source_sha256=src['sha256'],**fit))
    (B/tic/'lead-timing.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    print(tic,[(e['kind'],e['sector'],round(e.get('center_btjd',0),5),round(e.get('depth_ppt',0),1),e.get('fit_usable')) for e in out],flush=True)
