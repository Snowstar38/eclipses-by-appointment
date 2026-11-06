"""Bounded actual-cadence tests of short integer aliases for two candidate confirmations."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent
jobs=[('259614821',38,2339.50918,23.20817461,.25,[('P/2',2339.50918+23.20817461/2)]),('26486304',75,3357.96887,26.07966434,.4,[(f'P/{n}',3357.96887+26.07966434/n) for n in range(3,7)]+[('P/5 previous',3357.96887-26.07966434/5)]),('356801225',80,3480.15022,46.54776942,.28,[(f'P/{n}',3480.15022+46.54776942/n) for n in range(2,7)]+[('P/6 second',3480.15022+2*46.54776942/6)])]
out=[]
for tic,sec,t0,p,dur,tests in jobs:
 c=json.loads((B/tic/'lead-context.json').read_text());src=next(s for s in c['source'] if s['sector']==sec)
 with fits.open(src['path']) as h:
  a=h[1].data;t=np.asarray(a['TIME'],float);y=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
 ok=np.isfinite(t)&np.isfinite(y)&(y>0)&(q==0);t=t[ok];y=y[ok]
 cad=float(np.median(np.diff(t)))
 for label,pred in tests:
  core=np.abs(t-pred)<dur/2;left=(t>pred-dur*1.7)&(t<pred-dur*.7);right=(t>pred+dur*.7)&(t<pred+dur*1.7)
  if core.sum()<3 or left.sum()<3 or right.sum()<3:continue
  tl=np.median(t[left]);tr=np.median(t[right]);fl=np.median(y[left]);fr=np.median(y[right]);baseline=fl+(fr-fl)*(t-tl)/(tr-tl);z=y/baseline
  d=dict(tic=tic,sector=sec,label=label,predicted_btjd=pred,source_sha256=src['sha256'],core_n=int(core.sum()),expected_core_n=int(round(dur/cad)),left_n=int(left.sum()),right_n=int(right.sum()),first_core_btjd=float(t[core].min()),last_core_btjd=float(t[core].max()),max_core_gap_d=float(np.max(np.diff(t[core]))),median_depth_ppt=float((1-np.median(z[core]))*1000),min_depth_ppt=float((1-np.min(z[core]))*1000),baseline_scatter_ppt=float(1.4826*np.median(np.abs(z[left|right]-np.median(z[left|right])))*1000))
  out.append(d);print(tic,label,round(pred,3),d['core_n'],round(d['median_depth_ppt'],2),flush=True)
# P/2 for U005 is not a null: there is the opposite conjunction, but the
# alternating intervals themselves rule out a single 13.04 d same-kind clock.
events=json.loads((B/'26486304'/'lead-timing.json').read_text())
def center(sec,pred):return next(e['center_btjd'] for e in events if e['sector']==sec and abs(e['screen_btjd']-pred)<.002)
intervals=[center(14,1702.052)-center(14,1688.864),center(15,1714.948)-center(14,1702.052),center(76,3371.143)-center(75,3357.988),center(76,3384.025)-center(76,3371.143)]
out.append(dict(tic='26486304',label='P/2 alternating-event test',successive_intervals_d=intervals,consecutive_differences_d=[intervals[0]-intervals[1],intervals[2]-intervals[3]],interpretation='Both eras have alternating about 13.14 and 12.94 d intervals, incompatible with a constant 13.04 d same-kind cycle; two conjunction kinds in a 26.08 d orbit remain possible.'))
print('26486304 alternating',intervals)
(B/'lead-confirmed-aliases.json').write_text(json.dumps(out,indent=2),encoding='utf8')
