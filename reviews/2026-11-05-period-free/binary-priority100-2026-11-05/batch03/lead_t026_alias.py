"""Inspect bounded integer-cycle aliases against actual raw-SAP cadence coverage."""
import json, hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent; tic='341688154'
m=json.loads((B/tic/'lead-numeric.json').read_text())
ev=m['events']; t0=ev[0]['fit_mid_btjd']; t1=ev[1]['fit_mid_btjd']; dt=t1-t0
series=[]
for s in m['sources']:
    p=Path(s['path']); assert hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256']
    with fits.open(p,memmap=False) as h:
        d=h[1].data;t=np.asarray(d['TIME'],float);f=np.asarray(d['SAP_FLUX'],float);q=np.asarray(d['QUALITY'],int)
    good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
    series.append((s['sector'],t[good],f[good],s['sha256']))
out=[]
for k in range(1,13):
    p=dt/k
    for n in range(-12,100):
        if n in (0,k):continue
        center=t0+n*p
        for sector,t,f,sha in series:
            if center<t.min()-.5 or center>t.max()+.5:continue
            x=t-center; core=np.abs(x)<.08; left=(-.38<x)&(x<-.18); right=(.18<x)&(x<.38)
            ct=t[core];cad=np.median(np.diff(t))
            full=bool(len(ct)>=.75*(.16/cad) and len(ct)>2 and ct.min()<center-.06 and ct.max()>center+.06 and np.max(np.diff(ct))<2.5*cad and sum(left)>=.7*.2/cad and sum(right)>=.7*.2/cad)
            base=np.median(np.r_[f[left],f[right]]) if sum(left)+sum(right)>2 else np.nan
            deficit=1000*(1-np.median(f[core])/base) if sum(core)>0 and np.isfinite(base) else None
            scatter=1000*1.4826*np.median(np.abs(np.r_[f[left],f[right]]/base-1)) if np.isfinite(base) else None
            out.append(dict(alias_cycles=k,period_days=p,n=n,center_btjd=center,sector=sector,full_sensitive_window=full,core_n=int(sum(core)),left_n=int(sum(left)),right_n=int(sum(right)),first_core_btjd=float(ct.min()) if len(ct) else None,last_core_btjd=float(ct.max()) if len(ct) else None,max_core_gap_days=float(np.max(np.diff(ct))) if len(ct)>1 else None,raw_deficit_ppt=float(deficit) if deficit is not None else None,side_scatter_ppt=float(scatter) if scatter is not None else None,source_sha256=sha))
for k in range(1,13):
    v=[x for x in out if x['alias_cycles']==k and x['full_sensitive_window']]
    print(k,round(dt/k,6),[(x['sector'],x['n'],round(x['center_btjd'],2),round(x['raw_deficit_ppt'],2)) for x in v])
(B/'lead-t026-alias.json').write_text(json.dumps(dict(two_center_separation_days=dt,first_formal_error_days=ev[0]['fit_mid_formal_error_days'],second_formal_error_days=ev[1]['fit_mid_formal_error_days'],windows=out,notes='Candidates are integer cycle counts over two fitted centers. A full window means cadence core and both baseline flanks pass the stated bounds; it does not imply depth detection. Recheck significant residuals visually.'),indent=2)+'\n')

