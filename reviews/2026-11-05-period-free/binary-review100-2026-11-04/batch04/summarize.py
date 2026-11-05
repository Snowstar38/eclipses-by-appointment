import csv,json
from pathlib import Path
B=Path(__file__).resolve().parent
for q in csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')):
 o=json.loads((B/q['tic']/'raw-inspection.json').read_text())
 p=json.loads((B/q['tic']/'orbit-context.json').read_text())
 print(q['sample_id'],q['tic'],'flag windows',[(w['sector'],w['kind'],round(w['screen_center_btjd'],2),round(w['core_median_delta_ppt'],1)) for w in o['representative_flagged_windows']])
 print('  Gaia predicted',[(w['sector'],w['kind'],round(w['predicted_btjd'],2),w['n_core_quality0'],round(w.get('core_side_delta_ppt',0),1)) for w in p['gaia_conjunction_predictions']])
