import json
from pathlib import Path
b=Path(__file__).resolve().parent
x=json.loads((b/'lead-alias-covered-windows.json').read_text())
for tic in ['98941880','71295367']:
 print(tic,'NULLS',x[tic][0]['nulls'])
for tic in ['1269035','71295367','95324628','98941880']:
 d=json.loads((b/tic/'lead-context.json').read_text());print(tic,[(e['sector'],round(e['screen_btjd'],4),round(e['screen_depth_ppt'],2),e['screen_duration_d']) for e in d['flag_events']])
