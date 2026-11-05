"""Independent local Gaussian diagnostics on deciding eclipse-like events.

These centers are conditional morphology diagnostics, not formal timing errors.
"""
import hashlib, json
from pathlib import Path

import numpy as np
from astropy.io import fits
from scipy.optimize import least_squares

B = Path(__file__).resolve().parent
EVENTS = {
    '398073873': {18:(1811.2643,.29),25:(1990.6948,.29),58:(2887.8585,.30),78:(3448.5816,.30),79:(3471.0147,.30)},
    '143497778': {7:(1496.847,.65),8:(1520.076,.65),61:(2970.943,.55),62:(2994.339,.55),88:(3696.361,.65),89:(3719.773,.65),
                   89.1:(3743.182,.65)},
}

def model(p, x):
    a, b, d, c, sig = p
    return a+b*x-d*np.exp(-.5*((x-c)/sig)**2)

for tic, events in EVENTS.items():
    d=B/tic
    ctx=json.loads((d/'lead-context.json').read_text())
    out=[]
    for key,(screen,rad) in events.items():
        sector=int(key)
        s=next(z for z in ctx['sectors'] if z['sector']==sector)
        fp=Path(s['source_path'])
        assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data
            t=np.asarray(a['TIME'],float); f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
        t=t[good];f=f[good]
        inwin=np.abs(t-screen)<rad
        x=t[inwin]-screen;y=f[inwin]/np.median(f[inwin]);edge=np.abs(x)>rad*.67
        if edge.sum()<6:continue
        linear=np.polyfit(x[edge],y[edge],1)
        noise=max(1.4826*np.median(np.abs(y[edge]-np.polyval(linear,x[edge]))),1e-5)
        p0=[linear[1],linear[0],max(.001,linear[1]-np.min(y)),0,.05 if tic=='398073873' else .18]
        lo=[.8,-.3,0,-rad*.45,.01];hi=[1.2,.3,.2,rad*.45,rad*.8]
        fit=least_squares(lambda p:(y-model(p,x))/noise,p0,bounds=(lo,hi),max_nfev=5000)
        p=fit.x
        boundary=any(abs(p[i]-lo[i])<1e-4 or abs(p[i]-hi[i])<1e-4 for i in range(5))
        rec=dict(sector=sector,screen_btjd=screen,diagnostic_center_btjd=float(screen+p[3]),depth_ppt=float(p[2]*1000),sigma_days=float(p[4]),sideband_mad_ppt=float(noise*1000),
                 points=int(inwin.sum()),left_sideband=int(np.sum(x<-rad*.67)),right_sideband=int(np.sum(x>rad*.67)),fit_at_boundary=boundary,
                 local_gaps=[[float(t[i]),float(t[i+1])] for i in np.where((np.diff(t)>3*s['cadence_days'])&(t[:-1]>screen-rad)&(t[1:]<screen+rad))[0]],source_sha256=s['source_sha256'])
        out.append(rec)
    (d/'lead-measure.json').write_text(json.dumps(out,indent=2)+'\n')
    print(tic, [(v['sector'],round(v['diagnostic_center_btjd'],5),round(v['depth_ppt'],2),v['fit_at_boundary']) for v in out])
