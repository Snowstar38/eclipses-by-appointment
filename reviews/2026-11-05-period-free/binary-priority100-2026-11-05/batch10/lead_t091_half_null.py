"""Bounded raw test of the T091 P/2 deep-eclipse prediction."""
import json,hashlib
from pathlib import Path
import numpy as np
from astropy.io import fits
B=Path(__file__).resolve().parent;m=json.loads((B/'420645189'/'lead-numeric.json').read_text());src=next(x for x in m['sources'] if x['sector']==26);p=Path(src['path']);assert hashlib.sha256(p.read_bytes()).hexdigest()==src['sha256']
with fits.open(p,memmap=False) as h:
 d=h[1].data;t=np.array(d['TIME'],float);f=np.array(d['SAP_FLUX'],float);q=np.array(d['QUALITY'],int)
c=2025.2678;dur=.27;g=(q==0)&np.isfinite(t)&np.isfinite(f)&(f>0);core=g&(abs(t-c)<dur/2);l=g&(t>c-2*dur)&(t<c-dur);r=g&(t>c+dur)&(t<c+2*dur)
cad=float(np.median(np.diff(t[g])));base=(np.median(f[l])+np.median(f[r]))/2;obs=float(1-np.median(f[core])/base)
out=dict(tic='420645189',sector=26,predicted_deep_btjd=c,hypothesis='P/2=24.267 d would put another 54-ppt deep eclipse here',duration_days=dur,core_n=int(core.sum()),core_coverage_fraction=float(min(1,core.sum()*cad/dur)),core_first_btjd=float(t[core].min()),core_last_btjd=float(t[core].max()),core_max_gap_days=float(np.max(np.diff(t[core]))),left_n=int(l.sum()),left_coverage_fraction=float(min(1,l.sum()*cad/dur)),right_n=int(r.sum()),right_coverage_fraction=float(min(1,r.sum()*cad/dur)),observed_raw_deficit_ppt=1000*obs,expected_deep_deficit_ppt=54,source_sha256=src['sha256'],note='Not a strict three-band numeric null because the left band has 62% cadence; the 93%-covered uninterrupted core and complete right band, plotted in lead-deciding-null-T091.png, rule out a 54-ppt event at this prediction. Do not generalize this partial-band criterion to shallow signals.')
(B/'lead-t091-half-null.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
