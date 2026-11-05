import csv, json
from pathlib import Path

B = Path(__file__).resolve().parent
bulk = B.parent.parent / 'binary-exploration-2026-11-04' / 'bulk-results'
for row in csv.DictReader((B / 'queue.csv').open(newline='', encoding='utf8')):
    d = json.loads((bulk / f"{row['tic']}.json").read_text())
    print(row['sample_id'], row['tic'])
    for f in d['files']:
        w = [x for x in f['windows'] if x.get('flag')]
        if w:
            print('  S', f['sector'], ' '.join(f"{x['kind'][0]}:{x['time']:.2f}/{1000*x['depth']:.1f}ppt" for x in w))
