"""Actual raw SAP cadence coverage at T042 integer-cycle aliases."""
import json, math
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
d=json.loads((B/'255912894'/'lead-numeric.json').read_text(encoding='utf-8'))
times=[e['fit_mid_btjd'] for e in d['events']]
start,end=times;span=end-start
files=[]
for s in d['sources']:
    with fits.open(s['path'],memmap=False) as hd:
        a=hd[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    ok=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0)
    files.append((s['sector'],t[ok],f[ok]))
aliases=[]
for ncycle in range(35,70):
    period=span/ncycle;occasions=[]
    for k in range(1,ncycle):
        pred=start+k*period
        for sector,t,f in files:
            if not len(t) or pred<t.min()-.5 or pred>t.max()+.5:continue
            core=np.abs(t-pred)<.08
            side=(np.abs(t-pred)>.2)&(np.abs(t-pred)<.6)
            if not np.any(core) and not np.any(side):continue
            dt=float(np.median(np.diff(t)))
            def coverage(mask,lo,hi):
                tt=np.sort(t[mask]);count=int(len(tt));maxgap=float(max(np.diff(tt))) if count>1 else None
                # interval endpoints and largest gap, rather than row denominator alone
                return dict(count=count,first_btjd=float(tt.min()) if count else None,last_btjd=float(tt.max()) if count else None,max_gap_days=maxgap,expected=math.ceil((hi-lo)/dt))
            c=coverage(core,pred-.08,pred+.08);b=coverage(side,pred-.6,pred+.6)
            depth=None
            if c['count']>=4 and b['count']>=15:
                base=float(np.median(f[side]));depth=float(1000*(1-np.median(f[core])/base))
            occasions.append(dict(cycle=k,sector=sector,pred_btjd=pred,core=c,baseline=b,core_deficit_ppt=depth))
    sensitive=[o for o in occasions if o['core']['count']>=12 and o['baseline']['count']>=40 and o['core']['max_gap_days'] is not None and o['core']['max_gap_days']<.04 and abs(o['core']['first_btjd']-(o['pred_btjd']-.08))<.03 and abs(o['core']['last_btjd']-(o['pred_btjd']+.08))<.03]
    aliases.append(dict(ncycle=ncycle,conditional_period_days=period,occasions=occasions,sensitive_count=len(sensitive),sensitive=sensitive))
(B/'255912894'/'lead-alias.json').write_text(json.dumps(dict(tic='255912894',event_centers_btjd=times,alias_range_cycles=[35,69],core_half_width_days=.08,baseline_inner_days=.2,baseline_outer_days=.6,aliases=aliases),indent=2)+'\n',encoding='utf-8')
for a in aliases:
    if abs(a['conditional_period_days']-d['gaia_period_days'])<4:
        print(a['ncycle'],round(a['conditional_period_days'],5),[(o['sector'],round(o['pred_btjd'],2),o['core']['count'],o['baseline']['count'],round(o['core_deficit_ppt'],1) if o['core_deficit_ppt'] is not None else None) for o in a['sensitive']])
