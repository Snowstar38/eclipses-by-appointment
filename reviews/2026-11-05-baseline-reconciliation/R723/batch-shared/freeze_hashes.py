import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((B/'helper-final-audit.json').read_text())
assert h(B/'RESULTS.csv')==a['results_sha256']
assert h(B/'gaia-geometry.json')==a['gaia_geometry_sha256']
assert h(B/'helper-pixels/final-neighbors.json')==a['final_neighbors_sha256']
for r in a['rows']:
 assert all(r['checks'].values())
 assert h(B/r['tic']/'REPORT.md')==r['report_sha256']
 assert h(B/r['tic']/'measurements.json')==r['measurement_sha256']
paths=sorted(p for p in B.rglob('*') if p.is_file() and p.name!='SHA256SUMS.json' and '__pycache__' not in p.parts)
m={str(p.relative_to(B)).replace('\\','/'):h(p) for p in paths}
(B/'SHA256SUMS.json').write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
assert all(h(B/p)==v for p,v in m.items())
print(len(m),'files sealed; manifest SHA256',h(B/'SHA256SUMS.json'))
