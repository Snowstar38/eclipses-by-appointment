"""Freeze byte hashes of deciding batch and immutable source artifacts."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;R=B.parent
S=Path('[local-path-redacted] 5/made/sb1-scale/diffimg')
files=[]
files += [B/x for x in ('queue.csv','queue-seal.json','fetch_qlp.py','review_measure.py','phase_review.py','geometry.py','neighbor_audit.py','alias_audit.py','make_reports.py','freeze_hashes.py','download-receipts.json','gaia-geometry.json','neighbor-inspection.json','alias-audit.json','RESULTS.csv','LEAD-AUDIT.md','helper-audit.md')]
for tic in ('357019754','187202091','54054420','462088261','402782627'):
    files += [B/tic/x for x in ('REPORT.md','measurements.json','raw-windows.csv','raw-events.png','phase-review.png')]
    files += sorted((S/tic).glob('diff_s*.json'))+sorted((S/tic).glob('diff_s*.png'))
    files += [S/tic/'gaia.json']
files += [R/'targets-selected.json',R/'source-snapshots/search.jsonl',R/'source-snapshots/c10-sapdepth.json']
files += sorted((R/'shared-qlp').glob('*.fits'))
files += [R/'shared-catalogues/AUDIT.md',R/'shared-catalogues/coverage-matrix.csv',R/'shared-catalogues/gaia-nss-full.csv',R/'shared-catalogues/verification.json']
files += sorted((S/'187202091/cut').glob('*.fits'))
manifest={}
for p in files:
    if not p.is_file():raise FileNotFoundError(p)
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    manifest[str(p)]=h.hexdigest()
(B/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2))
print(len(manifest),'files frozen')
