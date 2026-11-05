"""Independent exact identifier cross-check, alerts not automatic reclassification."""
from pathlib import Path
import csv,json,hashlib
W=Path(__file__).resolve().parent;O=W/'catalogue-archives'
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
paths=[W/'accounting/accepted-proposal-ledger.csv',O/'ijspeert-identities.csv',O/'mast-prsa.csv']
ledger,ijs,prsa=map(read,paths)
ii={r['TIC']:r for r in ijs};ig={}
for r in ijs:ig.setdefault(r['GaiaDR3'],[]).append(r)
pi={}
for r in prsa:pi.setdefault(r['tess_id'],[]).append(r)
hits=[]
for r in ledger:
 if r['claim_member']!='True':continue
 i=ii.get(r['tic']);p=pi.get(r['tic'],[]);g=ig.get(r['gaia_dr3'],[]) if r['gaia_dr3'] else []
 if i or p or g:hits.append(dict(ledger=r,ijspeert=i,prsa=p,ijspeert_gaia_matches=g,gaia_exact=bool(g)))
out=dict(claims_checked=sum(r['claim_member']=='True' for r in ledger),claims_with_gaia_ids=sum(r['claim_member']=='True' and bool(r['gaia_dr3']) for r in ledger),exact_identifier_alert_count=len(hits),alerts=hits,source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},interpretation='TIC exact match against both tables and available Gaia DR3 exact match against IJspeert; identity alerts require provenance and clock review, no accounting changes. Missing Gaia IDs in older ledger do not disprove identity.')
(O/'accepted-exact-identity-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(claims=out['claims_checked'],alerts=[dict(review_id=r['ledger']['review_id'],tic=r['ledger']['tic'],ijspeert=bool(r['ijspeert']),prsa=bool(r['prsa']),gaia_exact=r['gaia_exact']) for r in hits]),indent=2))
