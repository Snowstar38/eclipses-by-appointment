import csv, json
from pathlib import Path
import numpy as np

B=Path(__file__).parent
SB=Path('[local path omitted] 5/made/sb1-scale')
for q in csv.DictReader((B/'queue.csv').open()):
    tic=q['tic']; m=json.loads((B/tic/'measurements.json').read_text())
    dpath=next((SB/'diffimg'/tic).glob('diff_s*.json'))
    d=json.loads(dpath.read_text())
    es=[e for e in m['events'] if 'mid_btjd' in e]
    used=[e for e in es if e.get('timing_usable')]
    print('\n',tic,'historical P',q['period_days'],'measured P',m.get('period_days'),'err',m.get('period_error_days'),'epoch',m.get('primary_epoch_btjd'),'used',len(used),'fits',len(es))
    print(' events',[(e['sector'],e['cycle'],round(e['mid_btjd'],4),round(e['depth_ppt'],1),round(e['timing_error_days'],4),e.get('timing_usable')) for e in es])
    print(' diff',dpath.name,'sector',d['sector'],'offset px',d['deficit_minus_target_px'],'resid',d['psf_fit_frac_resid'],'ap ppt',[round(d['depth_ap'+str(i)]*1000,1) for i in [1,3,5]],'n',d['n_events'])
    print(' capable',[(x['source_id'],round(x['sep'],2),round(x['depth_needed'],3)) for x in d['neighbours_60'] if x['possible']])
