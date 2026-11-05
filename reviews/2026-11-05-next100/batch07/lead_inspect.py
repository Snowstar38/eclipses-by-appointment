import csv, json
from pathlib import Path

b=Path(__file__).resolve().parent
for r in csv.DictReader((b/'queue.csv').open(encoding='utf8')):
    c=json.loads((b/r['tic']/'lead-context.json').read_text())
    print('\n',r['sample_id'],r['tic'],'sectors',','.join(str(x['sector']) for x in c['sectors']))
    for s in c['sectors']:
        flags=s['flags']
        if flags:
            print(' S',s['sector'],'coverage',round(s['time_start_btjd'],1),round(s['time_end_btjd'],1),
                  'flags',', '.join(f"{f['kind'][0]} {f['screen_center_btjd']:.3f} D{f['duration_days']:.2f} d{f['depth_fraction']:.3f}" for f in flags))
