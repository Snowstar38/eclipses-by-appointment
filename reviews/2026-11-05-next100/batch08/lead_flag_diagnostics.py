"""Actual endpoint/gap diagnostics around every selected dip window."""
import csv,json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
for row in csv.DictReader((B/'queue.csv').open(encoding='utf8',newline='')):
    D=B/row['tic'];ctx=json.loads((D/'lead-context.json').read_text());series=json.loads((D/'lead-local-series.json').read_text());sectors={s['sector']:s for s in ctx['sectors']};out=[]
    for z in series:
        if z['kind']!='dip':continue
        s=sectors[z['sector']];c=z['screen_center_btjd'];w=z['screen_duration_days'];t=np.array(z['raw_time']);f=np.array(z['raw_sap_flux']);
        if len(t)<3:continue
        half=w/2;core=(t>=c-half)&(t<=c+half);left=(t>=c-1.5*w)&(t<c-half);right=(t>c+half)&(t<=c+1.5*w)
        all_gaps=s['gaps_over_3cadences'];near=min(all_gaps,key=lambda g:min(abs(c-g[0]),abs(c-g[1]))) if all_gaps else None
        nearest_distance=min(abs(c-near[0]),abs(c-near[1])) if near else None
        step=None
        if near and nearest_distance<1.5*w:
            before=f[(t>=near[0]-.2)&(t<=near[0])];after=f[(t>=near[1])&(t<=near[1]+.2)]
            if len(before)>=3 and len(after)>=3:step=float((np.median(after)-np.median(before))/s['raw_flux_median']*1000)
        goodcore=t[core];maxgap=float(np.max(np.diff(goodcore))) if len(goodcore)>1 else None
        expected=int(round(w/s['cadence_days']))+1
        out.append(dict(sector=z['sector'],screen_center_btjd=c,screen_duration_days=w,core_start_btjd=c-half,core_end_btjd=c+half,actual_core_first_btjd=float(goodcore.min()) if len(goodcore) else None,actual_core_last_btjd=float(goodcore.max()) if len(goodcore) else None,core_actual=int(core.sum()),core_expected=expected,core_max_internal_gap_days=maxgap,left_actual=int(left.sum()),right_actual=int(right.sum()),nearest_actual_gap=near,nearest_gap_endpoint_distance_days=nearest_distance,median_step_across_nearest_gap_ppt=step,source_sha256=z['source_sha256']))
    (D/'lead-flag-diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
    print(row['sample_id'],[(z['sector'],round(z['screen_center_btjd'],2),round(z['core_actual']/z['core_expected'],2),round(z['nearest_gap_endpoint_distance_days'],2) if z['nearest_gap_endpoint_distance_days'] is not None else None,round(z['median_step_across_nearest_gap_ppt'],2) if z['median_step_across_nearest_gap_ppt'] is not None else None) for z in out])
