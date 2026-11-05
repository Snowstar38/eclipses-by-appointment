"""Hash frozen physical-review evidence; exclude mutable catalogue logs and self."""
import csv,hashlib,json
from pathlib import Path
here=Path(__file__).resolve().parent
ids=[r['tic'] for r in csv.DictReader((here/'queue.csv').open())]
root_files=['queue.csv','queue-seal.json','SOURCE-SNAPSHOT.json','targets-selected.json',
    'alternative-caom-response.json','alternative-comparison.json','alternative-downloads.json',
    'older-events.json','older-qlp-downloads.json','pixel-download-receipts.json','pixel-retries.json',
    'helper-audit.md','helper-augmented-audit.json','helper-gaia-audit.json',
    'helper-gaia-covariance.json','helper-neighbors.json','helper-numeric-audit.json',
    'LEAD-AUDIT.md','RESULTS.csv']
scripts=sorted(here.glob('*.py'))
paths=[here/name for name in root_files]+scripts
for tic in ids:
    d=here/tic
    paths+=list(d.glob('*.json'))+list(d.glob('*.md'))+list(d.glob('*.png'))+list(d.glob('*.fits'))
    paths+=list((d/'pixels').glob('*'))
paths+=list(here.glob('helper-pixel-*.png'))
paths=[p for p in paths if p.is_file() and p.name!='SHA256SUMS.json']
out={str(p.relative_to(here)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(paths))}
assert len(out)==len(set(paths))
(here/'SHA256SUMS.json').write_text(json.dumps(out,indent=2))
print(len(out),'hashes')
