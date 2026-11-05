"""Actual half-phase coverage for T042 same-kind cycle interpretation."""
import json,math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent/'255912894'
d=json.loads((B/'lead-numeric.json').read_text());clk=json.loads((B/'lead-clock.json').read_text());t0=clk['primary_epoch_btjd'];P=clk['period_days']
out=[]
for s in d['sources']:
    with fits.open(s['path'],memmap=False) as hd:
        a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
    if not len(t):continue
    cadence=float(np.median(np.diff(t)))
    for n in range(math.ceil((t.min()-t0)/P-.5),math.floor((t.max()-t0)/P-.5)+1):
        pred=t0+(n+.5)*P;core=abs(t-pred)<.08;side=(abs(t-pred)>.2)&(abs(t-pred)<.6)
        tc=np.sort(t[core]);ts=np.sort(t[side]);nc=len(tc);ns=len(ts)
        if not nc and not ns:continue
        deficit=float(1000*(1-np.median(f[core])/np.median(f[side]))) if nc>=4 and ns>=20 else None
        out.append(dict(sector=s['sector'],half_cycle=n+.5,pred_btjd=pred,core_n=nc,side_n=ns,core_first_btjd=float(tc.min()) if nc else None,core_last_btjd=float(tc.max()) if nc else None,core_max_gap_days=float(max(np.diff(tc))) if nc>1 else None,side_max_gap_days=float(max(np.diff(ts))) if ns>1 else None,cadence_days=cadence,raw_core_deficit_ppt=deficit,source_sha256=s['sha256']))
(B/'lead-halfphase.json').write_text(json.dumps(dict(period_days=P,epoch_btjd=t0,core_half_width_days=.08,baseline_inner_days=.2,baseline_outer_days=.6,windows=out),indent=2)+'\n')
print([(o['sector'],round(o['pred_btjd'],3),o['core_n'],o['side_n'],round(o['raw_core_deficit_ppt'],2) if o['raw_core_deficit_ppt'] is not None else None) for o in out])
