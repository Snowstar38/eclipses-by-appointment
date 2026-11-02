from pathlib import Path
import json,csv,hashlib,numpy as np
from astropy.io import fits
b=Path(__file__).parent.resolve();out={}
for r in csv.DictReader(open(b/'queue.csv')):
 tic=r['tic'];m=json.load(open(b/tic/'measurements.json'));P=m['period_days'];ep=m['primary_epoch_btjd'];dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')]);wins=[]
 for s in m['sources']:
  with fits.open(s['path']) as h:d=h[1].data;t=np.array(d['TIME']);f=np.array(d['SAP_FLUX']);q=np.array(d['QUALITY'])
  good=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[good];q=q[good]
  for n in range(int(np.floor((t.min()-ep)/P)),int(np.ceil((t.max()-ep)/P))+1):
   c=ep+n*P;core=abs(t-c)<dur*.25;pre=(t<c-.75*dur)&(t>c-1.75*dur)&(q==0);post=(t>c+.75*dur)&(t<c+1.75*dur)&(q==0)
   if c<t.min()-dur or c>t.max()+dur:continue
   wins.append(dict(sector=s['sector'],cycle=n,predicted_btjd=c,core_finite=int(sum(core)),core_quality_zero=int(sum(core&(q==0))),core_flagged=int(sum(core&(q!=0))),bilateral_oot_q0=[int(sum(pre)),int(sum(post))],note='Predicted coverage only, never measured timing or clean null.'))
 out[tic]=wins
json.dump(out,open(b/'primary-coverage.json','w'),indent=2)
p=b.parent/'source-snapshots/search-original-46fe1791.jsonl';json.dump(dict(path=str(p.resolve()),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),note='Immutable root search snapshot used in place of growing historical search input; photometric seed identities checked.'),open(b/'search-snapshot-check.json','w'),indent=2)

