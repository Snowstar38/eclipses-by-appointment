"""Retain the exact dedup-time ledger as later root decisions append rows."""
import csv,hashlib,io,json
from pathlib import Path
W=Path(__file__).resolve().parent;O=W/'unmatched512';P=W/'accounting/accepted-proposal-ledger.csv'
locks=json.loads((O/'dedup-hashes.json').read_text(encoding='utf-8'))
expected=locks[str(P)]
with P.open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
rows=[r for r in rows if r['review_id'] not in {f'R{x}' for x in range(689,698)}]
s=io.StringIO(newline='');writer=csv.DictWriter(s,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
b=s.getvalue().encode('utf-8');assert hashlib.sha256(b).hexdigest()==expected
(O/'dedup-time-ledger.csv').write_bytes(b)
(O/'dedup-ledger-provenance.json').write_text(json.dumps({'original_source':str(P),'sha256':expected,'archived_at':'dedup-time-ledger.csv','reason':'Later root acceptance appended R689-R697. Exact earlier bytes reconstructed by removing only these appended rows, matching the existing frozen dedup hash. Original dedup hash file unchanged.','new_ids_overlap_cohort':False},indent=2)+'\n',encoding='utf-8')
cohort=json.loads((O/'identity-targets.json').read_text(encoding='utf-8'))
assert not set(cohort)&{'159060569','387268955','342060048','184398115','64701575','284613090','128720791','95623701','56912737'}
print('exact dedup-time ledger archived and new review IDs disjoint')
