from pathlib import Path
import json,hashlib,csv
b=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
ids=json.loads((b/'identity-audit.json').read_text());src=[];s=b.parent.parent.parent/'fresh-band-next1000';cat=b.parent/'shared-catalogues'
seal=json.loads((cat/'ROOT-CATALOGUE-SEAL.json').read_text())
for rel,h in seal['files'].items():assert sha(cat/rel)==h,rel
for p in [s/'population.json',s/'downloads.json',b/'queue.csv',Path('[workspace]/Fable 5.1/made/paper/short/sec_methods.html'),Path('[workspace]/Astra/made/candidate-review-delegation.txt')]:src.append(dict(path=str(p),sha256=sha(p),kind='selection or methodological definition snapshot'))
for t in ids['targets']:
 for f in t['sources']:
  assert sha(f['path'])==f['sha256'];src.append(dict(path=f['path'],sha256=f['sha256'],tic=t['tic'],kind='raw QLP'))
 for sub in ['bulk-results','appointment-results']:
  p=s/sub/(t['tic']+'.json');src.append(dict(path=str(p),sha256=sha(p),tic=t['tic'],kind=sub))
for p in sorted(cat.rglob('*')):
 if p.is_file() and p.suffix in ['.json','.csv','.tsv']:src.append(dict(path=str(p),sha256=sha(p),kind='root-owned sealed catalogue receipt snapshot'))
for p in sorted(b.rglob('*')):
 if p.is_file() and p.suffix.lower() in ['.fits','.zip']:src.append(dict(path=str(p),sha256=sha(p),kind='helper custom extraction archive source; same photons'))
(b/'SOURCE-MANIFEST.json').write_text(json.dumps(src,indent=2),encoding='utf8')
q=list(csv.DictReader((b/'queue.csv').open()));r=list(csv.DictReader((b/'RESULTS.csv').open()));assert len(r)==len(q)==8
assert [(x['sample_id'],x['tic']) for x in r]==[(x['sample_id'],x['tic']) for x in q]
assert all(x['full_review_completion']=='COMPLETE_BOUNDED' for x in r)
assert (b/'HELPER-AUDIT.md').exists()
for p in b.rglob('REPORT.md'):
 txt=p.read_text(encoding='utf8');assert '\ufffd' not in txt
files={str(p.relative_to(b)).replace('\\','/'):sha(p) for p in sorted(b.rglob('*')) if p.is_file() and p.name not in ['SHA256SUMS.json','ROOT-ACCEPTANCE.json','HELPER-FINAL-FREEZE.json']}
(b/'SHA256SUMS.json').write_text(json.dumps(files,indent=2),encoding='utf8')
print('sealed',len(files),'local artifacts',len(src),'source receipts; exact8 outcomes',[(x['tic'],x['physical_verdict']) for x in r])
