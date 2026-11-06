"""Local trapezoid fits to selected same-kind raw SAP events; no Gaia period fixed."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from scipy.optimize import curve_fit

B=Path(__file__).resolve().parent
# Selected by visible raw morphology.  Distinct conjunction kinds are separate.
SEL={
'259614821':[(38,2339.507,'deep'),(39,2362.688,'deep'),(39,2385.945,'deep'),(65,3082.169,'deep'),(100,4080.125,'deep'),(101,4103.331,'deep'),(102,4149.765,'deep'),(65,3090.183,'shallow'),(99,4064.905,'shallow'),(101,4111.324,'shallow'),(102,4134.531,'shallow')],
'371856921':[(23,1951.953,'single')],
'412521418':[(7,1495.661,'clock'),(34,2231.994,'clock'),(61,2970.146,'clock'),(87,3668.848,'clock'),(88,3699.316,'clock')],
'86182628':[(22,1922.891,'deep'),(49,2662.044,'deep'),(22,1909.495,'shallow'),(49,2648.655,'shallow')],
'26486304':[(14,1702.052,'kind_a'),(15,1728.073,'kind_a'),(75,3357.988,'kind_a'),(76,3384.025,'kind_a'),(80,3501.441,'kind_a'),(81,3527.585,'kind_a'),(82,3553.580,'kind_a'),(83,3579.741,'kind_a'),(14,1688.864,'kind_b'),(15,1714.948,'kind_b'),(75,3345.143,'kind_b'),(76,3371.143,'kind_b'),(80,3488.343,'kind_b'),(81,3514.460,'kind_b'),(82,3540.531,'kind_b'),(83,3566.603,'kind_b')],
'356801225':[(40,2409.543,'deep'),(54,2781.939,'deep'),(80,3480.222,'deep'),(81,3526.698,'deep')],
'331643517':[(56,2829.840,'deep'),(76,3378.185,'deep'),(83,3559.848,'deep'),(56,2830.398,'shallow'),(76,3378.743,'shallow'),(83,3560.406,'shallow')],
'343187602':[(24,1970.092,'single')],
'768070':[(5,1446.202,'single')]}

def trap(x,b,s,d,c,w,ing):
    z=np.abs(x-c);return b+s*x-d*np.clip((w/2-z)/ing,0,1)

for tic,items in SEL.items():
    context=json.loads((B/tic/'lead-context.json').read_text());out=[]
    for sec,pred,kind in items:
        src=next(s for s in context['source'] if s['sector']==sec)
        with fits.open(src['path']) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)&(np.abs(t-pred)<.55)
        x=t[ok]-pred;y=f[ok]
        if len(x)<16:continue
        base=(np.abs(x)>.22);scale=float(np.median(y[base])) if base.sum()>8 else float(np.median(y));y=y/scale
        noise=max(float(1.4826*np.median(np.abs(y[base]-np.median(y[base])))),.0002) if base.sum()>8 else .002
        try:
            p,cov=curve_fit(trap,x,y,p0=[1,0,max(1-y.min(),.005),0,.25,.07],bounds=([.8,-.2,0,-.13,.05,.01],[1.2,.2,.8,.13,.6,.25]),sigma=np.full(len(x),noise),absolute_sigma=True,maxfev=30000)
            err=float(np.sqrt(max(cov[3,3],0)))
            fit=dict(center_btjd=float(pred+p[3]),center_formal_error_d=err,depth_ppt=float(p[2]*1000),duration_d=float(p[4]),ingress_d=float(p[5]),baseline_slope_d=float(p[1]),residual_rms_ppt=float(np.std(y-trap(x,*p))*1000),fit_usable=bool(np.isfinite(err) and err>0 and err<.1 and abs(p[3])<.125 and p[2]>.002 and p[4]>.052 and p[4]<.595))
        except Exception as e:fit={'fit_error':str(e)}
        out.append(dict(sector=sec,screen_btjd=pred,kind=kind,n=len(x),cadence_d=float(np.median(np.diff(t[ok]))),first_btjd=float(t[ok].min()),last_btjd=float(t[ok].max()),scale_sap=scale,noise_ppt=noise*1000,source_sha256=src['sha256'],**fit))
    (B/tic/'lead-timing.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    print(tic,[(e['kind'],e['sector'],round(e.get('center_btjd',0),5),round(e.get('depth_ppt',0),1),e.get('fit_usable')) for e in out],flush=True)
