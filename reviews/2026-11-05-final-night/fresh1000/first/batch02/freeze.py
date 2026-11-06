from pathlib import Path
import json,hashlib,csv
b=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
ids=json.loads((b/'identity-audit.json').read_text());src=[]
s=b.parent.parent.parent/'fresh-band-next1000'
for p in [s/'population.json',s/'downloads.json',b/'queue.csv']:
 src.append(dict(path=str(p),sha256=sha(p),kind='frozen selection'))
for t in ids['targets']:
 for f in t['sources']:
  assert sha(f['path'])==f['sha256'];src.append(dict(path=f['path'],sha256=f['sha256'],tic=t['tic'],kind='raw QLP'))
 for sub in ['bulk-results','appointment-results']:
  p=s/sub/(t['tic']+'.json');src.append(dict(path=str(p),sha256=sha(p),tic=t['tic'],kind=sub))
for p in sorted((b.parent/'shared-catalogues').glob('*')):
 if p.is_file() and p.suffix in ['.json','.csv','.tsv']:src.append(dict(path=str(p),sha256=sha(p),kind='root-owned shared catalogue receipt snapshot'))
(b/'SOURCE-MANIFEST.json').write_text(json.dumps(src,indent=2),encoding='utf8')
files={str(p.relative_to(b)).replace('\\','/'):sha(p) for p in sorted(b.rglob('*')) if p.is_file() and p.name not in ['SHA256SUMS.json','ROOT-ACCEPTANCE.json']}
(b/'SHA256SUMS.json').write_text(json.dumps(files,indent=2),encoding='utf8')
assert len(list(csv.DictReader((b/'RESULTS.csv').open())))==7
for name in ['LEAD-AUDIT.md','RESULTS.csv']:
 txt=(b/name).read_text(encoding='utf8');assert '\ufffd' not in txt and '?' not in txt
print('sealed',len(files),'local artifacts',len(src),'source receipts')

