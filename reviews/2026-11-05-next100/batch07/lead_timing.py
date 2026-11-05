"""Local Gaussian timing summary for discrete raw SAP dips; model is descriptive."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

B=Path(__file__).resolve().parent
EVENTS={'295176393':[(39,2365.973),(66,3101.843),(93,3837.719),(100,4083.012),(101,4110.262),(102,4137.515)],
        '341419787':[(7,1493.429),(7,1514.492)]}
for tic,events in EVENTS.items():
    data=json.loads((B/tic/'lead-local-series.json').read_text());out=[]
    for sec,guess in events:
        z=min((z for z in data if z['sector']==sec and z['kind']=='dip'),key=lambda z:abs(z['screen_center_btjd']-guess))
        t=np.asarray(z['raw_time']);f=np.asarray(z['raw_sap_flux']);m=np.isfinite(t)&np.isfinite(f)&(np.abs(t-guess)<.18)
        x=t[m]-guess;y=f[m]/np.median(f[m]);assert len(x)>=10
        def resid(v):
            base,slope,depth,center,width=v
            return y-(base+slope*x-depth*np.exp(-.5*((x-center)/width)**2))
        lo=np.array([.95,-.05,0,-.09,.006]);hi=np.array([1.05,.05,.03,.09,.09])
        fit=least_squares(resid,[1,0,.005,0,.025],bounds=(lo,hi),loss='soft_l1',f_scale=.001)
        v=fit.x;out.append(dict(sector=sec,screen_btjd=guess,measured_center_btjd=float(guess+v[3]),depth_ppt=float(1000*v[2]/v[0]),sigma_days=float(v[4]),points=len(x),residual_rms_ppt=float(1000*np.std(fit.fun)),fit_at_bound=bool(np.any(np.isclose(v,lo,atol=1e-5)|np.isclose(v,hi,atol=1e-5)))))
    if tic=='295176393':
        n=np.array([0,27,54,63,64,65]);c=np.array([x['measured_center_btjd'] for x in out]);coef=np.polyfit(n,c,1);period=float(coef[0]);t0=float(coef[1]);oc=(c-(t0+period*n)).tolist()
        extra=dict(cycle_indices=n.tolist(),period_days=period,epoch_btjd=t0,oc_days=oc)
    else:extra=dict(event_separation_days=out[1]['measured_center_btjd']-out[0]['measured_center_btjd'])
    (B/tic/'lead-timing.json').write_text(json.dumps(dict(events=out,summary=extra),indent=2)+'\n',encoding='utf8')
    print(tic,extra,out)
