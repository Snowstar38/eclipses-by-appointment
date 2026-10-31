import csv, json, hashlib
from pathlib import Path
from collections import Counter
p=Path(__file__).resolve().parent
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
t=json.loads((p/'targets-selected.json').read_text())
q=list(csv.DictReader((p.parent/'queue.csv').open()))
assert list(t)==[r['tic'] for r in q] and len(t)==len(set(t))==73
assert (p/'targets-selected.json').read_bytes()==(p.parent/'targets-selected.json').read_bytes()
assert len({str(x['gaia']['source_id']) for x in t.values()})==73
for receipt,sub in [('vsx70-receipts.json','vsx'),('asassn-receipts.json','asassn'),('eb-battery-receipts.json','eb-battery')]:
 rs=json.loads((p/receipt).read_text());assert all(r['status']=='success' for r in rs)
 assert {r['tic'] for r in rs}==set(t)
 for r in rs:
  f=p/sub/r.get('file',r['tic']+'.tsv');assert sha(f)==r['sha256']
assert len(json.loads((p/'eb-battery-receipts.json').read_text()))==292
for name,file in [('gaia-nss-receipt.json','gaia-nss-full.csv'),('simbad-targets-receipt.json','simbad-targets.csv'),('control-gaia-eb-exact-receipt.json','control-gaia-eb-exact.csv')]:
 r=json.loads((p/name).read_text());assert r['status']=='success' and sha(p/file)==r['sha256']
for name in ['gaia-vari-receipts.json','cone-positive-controls.json']:
 for r in json.loads((p/name).read_text()):assert r['status']=='success' and sha(p/r['file'])==r['sha256']
for r in json.loads((p/'service-controls.json').read_text()):
 assert r['status']=='success'
 if 'file' in r:assert sha(p/r['file'])==r['sha256']
for r in json.loads((p/'chopard-comparison-summary.json').read_text())['sources']:assert sha(Path(r['path']))==r['sha256']
nss=list(csv.DictReader((p/'gaia-nss-full.csv').open()));assert len(nss)==73 and {r['source_id'] for r in nss}=={str(x['gaia']['source_id']) for x in t.values()}
rows=list(csv.DictReader((p/'coverage-matrix.csv').open()));assert len(rows)==73 and all(r['coverage_complete']=='yes' for r in rows)
known=[{'tic':r['tic'],'matches':json.loads(r['known_prior_eb_identification'])} for r in rows if r['known_prior_eb_identification']!='[]']
(p/'match-exceptions.json').write_text(json.dumps(known,indent=2))
variables=[{'tic':r['tic'],'vsx_exact_gaia':json.loads(r['vsx_exact_gaia']),'vsx_close_identity_review':json.loads(r['vsx_close_identity_review']),'asassn_exact':json.loads(r['asassn_exact'])} for r in rows if any(r[k]!='[]' for k in ['vsx_exact_gaia','vsx_close_identity_review','asassn_exact'])]
(p/'variable-match-exceptions.json').write_text(json.dumps(variables,indent=2))
identity={'queue':str(p.parent/'queue.csv'),'queue_sha256':sha(p.parent/'queue.csv'),'targets_sha256':sha(p/'targets-selected.json'),'identity_check':'73 unique TIC and Gaia DR3 IDs; queue ordered identity exact; all queries fresh; receipt-to-raw hashes verified','query_scope':'VSX/ASAS-SN 60 arcsec; three historical EB groups 5 arcsec (Kostov two tables); exact Gaia DR3 EB and SIMBAD identifiers; cached public Chopard v1.2.0 exact-ID comparison, not embargoed identities or later releases','nss_rows':len(nss),'coverage_rows':len(rows),'known_prior_eb':known}
(p/'identity-provenance.json').write_text(json.dumps(identity,indent=2))
fields=['position','tic','gaia_dr3','coverage_complete','scoped_prior_eb_status','known_prior_eb_identification']
with (p/'coverage-compact.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
(p/'AUDIT.md').write_text(f'''# Final73 scoped catalogue audit

All 73 queue identities verified; 73 complete NSS orbit rows and 73/73 seven-group catalogue coverage. All fresh remote queries succeeded. Six cone positive controls and exact Gaia EB positive control succeeded. Raw receipt hashes independently checked by audit.py. No failed query was interpreted as a non-match.

Prior EB exceptions: {json.dumps(known)}.

Scope: VSX, SIMBAD primary type, Gaia DR3 eclipsing binaries, Prsa 2022, IJspeert 2024, Kostov 2025 (two tables), ASAS-SN. Nearby rows retained separately; positional association is explicitly distinguished from exact identity. Public Chopard v1.2.0 exact comparison is separate; later releases and embargoed identities remain unchecked/unknown. Catalogue outcomes do not supply physical verdicts or global novelty claims. No canonical/public edits.
''')
manifest=[{'file':str(f.relative_to(p)),'sha256':sha(f)} for f in sorted(p.rglob('*')) if f.is_file() and f.name!='sha256-manifest.csv']
with (p/'sha256-manifest.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['file','sha256']);w.writeheader();w.writerows(manifest)
print(json.dumps(identity,indent=2))
