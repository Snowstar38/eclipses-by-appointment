from pathlib import Path
import hashlib,json,csv
B=Path(__file__).parent;h={}
for p in B.rglob('*'):
 if p.is_file() and p.name!='SHA256SUMS.json':h[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
for r in json.load(open(B/'download-receipts.json')):
 p=Path(r['path']);h[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
for r in json.load(open(B/'pixel-audit.json')).values():
 p=Path(r['cutout_path']);h[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
S=Path('[local path omitted] 5/made/sb1-scale')
for p in [S/'search.jsonl',S/'c6-sapdepth.json',S/'c7-sapdepth.json',S/'diffimg/diffstack.py',B.parent/'targets-selected.json',B.parent/'shared-catalogues/gaia-nss-full.csv',Path('[local path omitted] 5.1/made/paper/short/sec_methods.html')]:h[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
json.dump(h,open(B/'SHA256SUMS.json','w'),indent=2)
print('hashed',len(h))
