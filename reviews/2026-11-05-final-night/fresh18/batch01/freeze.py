import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
rows=list(csv.DictReader((B/'queue.csv').open()));expected={'Y001':'22559994','Y002':'65684549','Y003':'70554665','Y004':'93330962','Y005':'111230893','Y006':'122766753','Y008':'140777703','Y009':'156747165'}
assert {r['sample_id']:r['tic'] for r in rows}==expected
result=list(csv.DictReader((B/'RESULTS.csv').open(encoding='utf8')));assert {r['sample_id']:r['tic'] for r in result}==expected;assert len(result)==8
assert all(r['full_review_completion']=='COMPLETE' and Path(r['report']).is_file() for r in result)
assert {r['physical_verdict'] for r in result}=={'CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED'}
audit=json.loads((B/'identity-audit.json').read_text());assert len(audit['targets'])==8
for target in audit['targets']:
 for s in target['sources']:assert sha(s['path'])==s['sha256']
for r in json.loads((B/'helper-hashes.json').read_text(encoding='utf-8-sig')):assert sha(r['Path']).lower()==r['Hash'].lower(),r['Path']
for p in B.rglob('*'):
 if p.suffix.lower() in ['.md','.py','.json','.csv']:
  s=p.read_text(encoding='utf-8-sig');assert '\ufffd' not in s,p
  if p.suffix=='.py':compile(s,str(p),'exec')
for r in result:assert '?' not in Path(r['report']).read_text(encoding='utf8')
S=B.parent.parent/'fresh-band-next400';C=B.parent/'shared-catalogues';external=[S/'population.json',S/'downloads.json',Path('[workspace]/Astra/made/candidate-review-delegation.txt'),Path('[workspace]/Fable 5.1/made/paper/short/sec_methods.html')]
for row in rows:
 tic=row['tic'];external += [S/'bulk-results'/f'{tic}.json',S/'appointment-results'/f'{tic}.json']
 for p in (C/'cones').glob(f'*-{tic}.tsv'):external.append(p)
for p in C.iterdir():
 if p.is_file() and p.suffix.lower() in ['.json','.csv','.tsv','.txt']:external.append(p)
manifest=dict(scope='Exact batch01 eight targets; shared catalogue receipts retain their broader central scope, not a physical review of other targets.',files=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(set(external))],raw_qlp_sources=audit['targets'])
(B/'SOURCE-MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
files=[dict(path=str(p.relative_to(B)).replace('\\','/'),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(B.rglob('*')) if p.is_file() and p.name not in ['SHA256SUMS.json','freeze-verification.json'] and '__pycache__' not in p.parts]
(B/'SHA256SUMS.json').write_text(json.dumps(dict(files=files),indent=2),encoding='utf8')
for f in files:assert sha(B/f['path'])==f['sha256']
counts={v:sum(r['physical_verdict']==v for r in result) for v in ['CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED']}
receipt=dict(exact_rows=8,complete=8,physical_counts=counts,manifest_sha256=sha(B/'SHA256SUMS.json'),source_manifest_sha256=sha(B/'SOURCE-MANIFEST.json'),all_hashes_verified=True,utf8_verified=True,report_literal_question_marks=0,script_syntax_verified=True,identity_audit_sha256=sha(B/'identity-audit.json'))
(B/'freeze-verification.json').write_text(json.dumps(receipt,indent=2),encoding='utf8');print(json.dumps(receipt,indent=2))
