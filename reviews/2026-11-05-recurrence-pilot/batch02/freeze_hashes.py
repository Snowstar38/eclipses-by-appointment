"""Freeze exact batch02 outputs and all checked cached inputs."""
from pathlib import Path
import csv,hashlib,json
B=Path(__file__).resolve().parent;W=B.parent;H=W.parent/'binary-exploration-2026-11-04'/'bulk-results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={}
for p in sorted(B.rglob('*')):
    if p.is_file() and p.name not in ('SHA256SUMS.json','ROOT-ACCEPTANCE.json'):
        out[str(p.relative_to(B)).replace('\\','/')]=sha(p)
external=[W/'pilot-seal.json',W/'novelty-audit'/'live'/'target-results.json']
for q in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf8')):
    tic=q['tic'];bp=H/f'{tic}.json';bulk=json.loads(bp.read_text(encoding='utf8'));assert bulk['tic']==tic
    external.append(bp)
    for r in bulk['files']:
        p=Path(r['path']);assert sha(p)==r['sha256'],p;external.append(p)
for p in external:
    assert p.is_file(),p
    out[str(p)]=sha(p)
(B/'SHA256SUMS.json').write_text(json.dumps({'files':out,'scope':'V011-V020 outputs; queue seal; central target-specific catalogue receipt; ten bulk JSON and all cached FITS. ROOT-ACCEPTANCE excluded.'},indent=2)+'\n',encoding='utf8')
print('manifest entries',len(out))
