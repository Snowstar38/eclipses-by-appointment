import csv, json
from pathlib import Path
B=Path(__file__).resolve().parent
for r in csv.DictReader((B/'queue.csv').open()):
    m=json.loads((B/r['tic']/'lead-numeric.json').read_text())
    print('\n',r['sample_id'],r['tic'],'GaiaP',round(float(r['gaia_period_days']),4))
    for e in sorted(m['events'],key=lambda e:e['fit_mid_btjd']):
        print('s%d %.4f raw %.1f fit %.1f dur %.3f err %s gap %.3f'%(e['sector'],e['fit_mid_btjd'],e['raw_core_median_deficit_ppt'],e['fit_depth_ppt'],e['fit_duration_days'],str(e.get('fit_mid_formal_error_days')),e['local_max_gap_days']))
