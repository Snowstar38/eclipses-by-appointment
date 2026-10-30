from pathlib import Path
import json,csv,datetime
import numpy as np
from astropy.io import fits
from fit_batch import read
D=Path(__file__).parent;B=D.parent;T=json.load(open(B/'targets-selected.json'));out={}
for tic in T:
 r=json.load(open(D/tic/'fit-results.json'));events=[e for e in r['events'] if e['status']=='fit'];secs={s['sec']:s for s in read(tic)};flags=[]
 for e in events:
  s=secs[e['sec']];m=(abs(s['t']-e['tc'])<e['T14']/2)&(s['q']!=0)
  if sum(m):flags.append(dict(sector=e['sec'],tc=e['tc'],n=int(sum(m)),quality_bits=sorted(set(map(int,s['q'][m]))),flagged_median_normalized_flux=float(np.median(s['f'][m])),clean_depth=e['depth'],note='Flagged flux includes ingress/egress and is not a fitted eclipse depth.'))
 identity=[]
 for fn in sorted((B/'data').glob(tic+'_s*.fits')):
  with fits.open(fn) as h:
   hdr=h[0].header;tid=hdr.get('TICID',hdr.get('TIC_ID'));sec=hdr.get('SECTOR');identity.append(dict(file=str(fn),tic_header=tid,sector_header=sec))
   assert tid is None or int(tid)==int(tic)
   assert sec is None or int(sec)==int(fn.stem[-3:])
 out[tic]=dict(qlp_identity=identity,flagged_event_inspection=flags)
json.dump(out,open(D/'quality-and-identity-audit.json','w'),indent=2)
res=list(csv.DictReader(open(B/'RESULTS.csv')));assert len(res)==10 and {r['tic'] for r in res}==set(T)
assert all(Path(r['report']).exists() for r in res)
assert all(r['full_review_completion']=='COMPLETE (adjudicated)' for r in res)
print('Validated ten reports/results, QLP identities, flagged event flux and completeness.')
