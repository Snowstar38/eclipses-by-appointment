import json,csv
from pathlib import Path
B=Path('[local path omitted]')
for r in csv.DictReader(open(B/'queue.csv')):
 m=json.load(open(B/r['tic']/'measurements.json'));print(r['tic'],[(e['sector'],e['cycle'],round(e['depth_ppt'],1),round(e['fit_shift_days'],4),round(e['duration_days'],3)) for e in m['events'] if 'mid_btjd' in e])
