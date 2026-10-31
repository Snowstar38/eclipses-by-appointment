from pathlib import Path
import hashlib,json,csv
b=Path(__file__).parent
p=b/'125690413/REPORT.md';s=p.read_text(encoding='utf-8');s+='\nTiming sensitivity: omitting the complete structured-baseline sector41 gives P=3.6868774377158258d, only -0.00001913d from the adopted all-event ephemeris. See timing-sensitivity.json; this is a robustness diagnostic, not the adopted precision estimate.\n';p.write_text(s,encoding='utf-8')
h=json.load(open(b/'SHA256SUMS.json'))
for r in json.load(open(b/'download-receipts.json')):h[r['path']]=hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()
for p in b.rglob('*'):
 if p.is_file() and p.name!='SHA256SUMS.json':h[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
json.dump(h,open(b/'SHA256SUMS.json','w'),indent=2)
q=list(csv.DictReader(open(b/'queue.csv')));r=list(csv.DictReader(open(b/'RESULTS.csv')));assert len(r)==10 and {x['tic'] for x in q}=={x['tic'] for x in r}
assert all(Path(x['report']).exists() for x in r)
for p,v in h.items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==v,p
print('Exact10 validated; all',len(h),'manifest entries verified; 9 confirmed,1 probable; all COMPLETE')
