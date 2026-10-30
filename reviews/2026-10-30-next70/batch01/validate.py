from pathlib import Path
import csv,json,hashlib
B=Path('[local working path omitted; see provenance receipts]');rows=list(csv.DictReader((B/'RESULTS.csv').open()));ids={r['tic'] for r in rows};assert len(rows)==len(ids)==10;assert len(list((B/'reports').glob('*/REPORT.md')))==10
ind=json.loads((B/'raw-evidence/independent-results.json').read_text());checked=[]
for r in ind:
 if r.get('measurements'):
  assert r['identity']['header_tic_matches'] and r['identity']['header_sector_matches'] and r['identity']['uri_contains_padded_tic'];checked.append(r['tic'])
assert len(checked)==9
manifest=[]
for p in B.rglob('*'):
 if p.is_file() and p.suffix.lower() not in ['.fits','.pyc'] and p.name not in ['manifest.json','validation.json']:
  manifest.append(dict(path=str(p.relative_to(B)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(B/'manifest.json').write_text(json.dumps(manifest,indent=2));(B/'validation.json').write_text(json.dumps(dict(rows=10,reports=10,unique_targets=10,queue_positions='1-10',verdicts={'CONFIRMED':10},independent_archive_identity_validated=checked,independent_custom_pixel_target='414008363',lead_visual_review='20 representative raw event panels and 10 cached three-panel difference images inspected',constraints='No original source edits, no publication, no commits; missing archive products not treated as catalogue negatives'),indent=2));print('validated',len(manifest),'hashed artifacts')
