import csv
import json
import math
from pathlib import Path

B = Path(__file__).parent
D = Path('local-source/Fable 5/made/sb1-scale/diffimg')
for row in csv.DictReader(open(B / 'queue.csv')):
    tic = row['tic']
    p = next((D / tic).glob('diff*.json'))
    x = json.load(open(p))
    d = x['deficit_centroid']
    capable = sorted((n for n in x['neighbours_60'] if n['possible']), key=lambda n: n['sep'])
    print(tic, p.name, 'events', x['n_events'], 'target_off_px', round(math.dist(d, x['target_px']), 3),
          'ap1/3/5_ppt', [round(x[f'depth_ap{i}'] * 1000, 1) for i in (1, 3, 5)],
          'capable', [(round(n['sep'], 1), round(n['G'], 2), round(n['depth_needed'], 2),
                       round(math.dist(d, n['px']), 2)) for n in capable])
