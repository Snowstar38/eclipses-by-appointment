"""Bounded half-phase coverage for the two measured clocks."""
import hashlib,json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
EPH={'295176393':(2365.97185,27.25454039,.06),'341419787':(1493.43634,21.06901505,.12)}
for tic,(t0,p,w) in EPH.items():
    ctx=json.loads((B/tic/'lead-context.json').read_text());out=[]
    for s in ctx['sectors']:
        fp=Path(s['source_path']);assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        m=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[m];f=f[m]
        for n in range(int(np.floor((t.min()-t0)/p))-1,int(np.ceil((t.max()-t0)/p))+2):
            c=t0+(n+.5)*p
            if not t.min()<c<t.max():continue
            core=np.abs(t-c)<w/2;base=(np.abs(t-c)>w*1.5)&(np.abs(t-c)<w*5)
            expected=int(round(w/s['cadence_days']))+1
            out.append(dict(sector=s['sector'],half_cycle=n+.5,predicted_btjd=float(c),core_count=int(core.sum()),expected=expected,
                baseline_count=int(base.sum()),core_depth_ppt=float(1000*(1-np.median(f[core])/np.median(f[base]))) if core.sum()>expected*.7 and base.sum()>expected else None))
    (B/tic/'lead-halfphase.json').write_text(json.dumps(dict(measured_epoch_btjd=t0,measured_period_days=p,core_width_days=w,halfphase_windows=out),indent=2)+'\n')
    print(tic,[(z['sector'],round(z['predicted_btjd'],3),z['core_count'],z['expected'],round(z['core_depth_ppt'],2) if z['core_depth_ppt'] is not None else None) for z in out])
