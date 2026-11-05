"""Freeze exact local artifacts and immutable external source receipts for review9."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'))
seal=json.loads((B/'queue-seal.json').read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
exclude={'SHA256SUMS.json','root-verification.json','ROOT-GATE-STATUS.txt'}
local={str(p.relative_to(B)).replace('\\','/'):sha(p) for p in sorted(B.rglob('*')) if p.is_file() and p.name not in exclude and not p.name.startswith('root-')}
assert local['queue.csv']==seal['sha256'] and local['SOURCE-SNAPSHOT.json']==seal['snapshot_sha256']
sources={}
for tic,src in D.items():
 for rec in src['target']['file_receipts']:
  p=Path(rec['path']);h=sha(p);assert h==rec['sha256']
  sources[str(p)]=h
root=B.parent
for rel,h in seal['source_hashes'].items():
 p=B/'selection-time-ledger.csv' if rel.startswith('accounting') else root/rel
 assert sha(p)==h
 sources[str(p)]=h
gaia=root/'next256'/'shared-catalogues'/'raw'/'gaia_nss.txt';sources[str(gaia)]=sha(gaia)
method=Path('[local-path-redacted] 5.1/made/paper/short/sec_methods.html');sources[str(method)]=sha(method)
out=dict(queue_seal_sha256=seal['sha256'],snapshot_seal_sha256=seal['snapshot_sha256'],local_files=local,external_sources=sources,notes='Hash exact immutable local artifacts and source bytes. Excludes this self-referential manifest and root verification/gate files. selection-time-ledger.csv is archived in local_files and external_sources with the same historical source hash; current mutable accounting ledger is not used.')
(B/'SHA256SUMS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(len(local),'local',len(sources),'external')
