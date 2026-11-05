"""Test actual raw cadence coverage at predicted times; predictions are not fitted events."""
import csv, json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits

B=Path(__file__).resolve().parent
EPH={'295176393':(2365.973,27.248596014673733,0.06),'341419787':(1493.429,21.057140031135734,0.12)}
for tic,(t0,p,duration) in EPH.items():
    ctx=json.loads((B/tic/'lead-context.json').read_text()); out=[]
    for s in ctx['sectors']:
        fp=Path(s['source_path']); assert hashlib.sha256(fp.read_bytes()).hexdigest()==s['source_sha256']
        with fits.open(fp,memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        g=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[g];f=f[g]
        for n in range(int(np.floor((t.min()-t0)/p))-1,int(np.ceil((t.max()-t0)/p))+2):
            c=t0+n*p
            if not t.min()-duration<c<t.max()+duration:continue
            core=(np.abs(t-c)<=duration/2);base=(np.abs(t-c)>duration*1.5)&(np.abs(t-c)<=duration*5)
            ct=t[core];bf=f[base];cf=f[core]
            expected=int(round(duration/s['cadence_days']))+1
            out.append(dict(sector=s['sector'],cycle=n,predicted_btjd=c,core_count=int(core.sum()),expected=expected,
                core_first=float(ct.min()) if len(ct) else None,core_last=float(ct.max()) if len(ct) else None,
                baseline_count=int(base.sum()),relative_depth_ppt=float(1000*(1-np.median(cf)/np.median(bf))) if len(cf)>2 and len(bf)>6 else None,
                minimum_depth_ppt=float(1000*(1-np.min(cf)/np.median(bf))) if len(cf)>2 and len(bf)>6 else None))
    (B/tic/'lead-ephemeris-coverage.json').write_text(json.dumps(dict(t0_screen=t0,gaia_period=p,nominal_core_width_days=duration,windows=out),indent=2)+'\n',encoding='utf8')
    print(tic,len(out),'windows')
