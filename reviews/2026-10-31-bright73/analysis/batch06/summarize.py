import json,csv
from pathlib import Path
B=Path(__file__).parent
P=json.load(open(B/'pixel-audit.json'));G=json.load(open(B/'gaia-geometry.json'))
for r in csv.DictReader(open(B/'queue.csv')):
 t=r['tic'];m=json.load(open(B/t/'measurements.json'));p=P[t];g=G[t]
 print(t,'n',m['timing_event_count'],'P',m['period_days'],'err',m['period_error_days'],'depth',m['depth_ppt'],'px',round(p['target_deficit_distance_px'],3),'neighbors',[(round(x['separation_arcsec'],2),round(x['deficit_distance_px'],3)) for x in p['capable']],'Gaia',g['period_days'],'near',g['near_reference']['offset_days'])
