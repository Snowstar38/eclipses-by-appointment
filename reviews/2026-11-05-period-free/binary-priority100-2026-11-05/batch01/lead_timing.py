"""Curated same-kind eclipse clocks; fit only visually credible, finite fits."""
import csv,json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
# 0-based indices in lead-numeric events. Opposite conjunctions have separate labels.
CHOICES={
 'T001':{},
 'T002':{'deep':[0,1]},
 'T003':{'deep':[1,3],'shallow':[0,2]},
 'T004':{'deep':[0,3],'shallow':[1,2]},
 'T005':{'deep':[0,2,5,7],'shallow':[1,3,6,8]},
 'T006':{'deep':[0,1]},
 'T007':{},  # broad-variable baselines and gapped S34 do not support a precision center
 'T008':{},
 'T009':{'kind_a':[0,3,6],'kind_b':[2,4]},
 'T010':{}
}
for row in Q:
    d=json.loads((B/row['tic']/'lead-numeric.json').read_text()); p0=float(row['gaia_period_days']); out={'sample_id':row['sample_id'],'tic':row['tic'],'gaia_period_days':p0,'kinds':{}}
    if row['sample_id']=='T001':
        good=[(i,e) for i,e in enumerate(d['events']) if e.get('fit_mid_formal_error_days') is not None and e['fit_mid_formal_error_days']<.01 and e.get('fit_depth_ppt',0)>20]
        CHOICES['T001']={'deep':[i for i,e in good if e['fit_depth_ppt']>75 and e['sector']!=79],'shallow':[i for i,e in good if e['fit_depth_ppt']<=75]}
    for kind,ids in CHOICES[row['sample_id']].items():
        ev=[d['events'][i] for i in ids]; t=np.array([x['fit_mid_btjd'] for x in ev]); n=np.rint((t-t[0])/p0).astype(int)
        # Equal weighting avoids spurious precision from short-cadence points and uncalibrated sector offsets.
        A=np.column_stack([np.ones(len(n)),n]);par=np.linalg.lstsq(A,t,rcond=None)[0]; resid=t-A@par
        period_error=None
        if len(n)>=3:
            s2=max(float(np.sum(resid**2)/(len(n)-2)),float(np.median([x['cadence_days'] if 'cadence_days' in x else .00694 for x in ev])**2)/12)
            period_error=float(np.sqrt(s2*np.linalg.inv(A.T@A)[1,1]))
        elif len(n)==2:
            # Half-cadence timing floor for two eclipse centers; formal covariance alone is optimistic.
            errs=[]
            for x in ev:
                c=next(z['cadence_days'] for z in d['coverage'] if z['sector']==x['sector']); formal=x.get('fit_mid_formal_error_days') or 0
                errs.append(max(c/2,min(formal,.1)))
            period_error=float(np.hypot(*errs)/abs(n[1]-n[0]))
        out['kinds'][kind]=dict(event_indices=ids,sector=[x['sector'] for x in ev],mid_btjd=t.tolist(),cycle=n.tolist(),period_days=float(par[1]),period_error_days=period_error,epoch_btjd=float(par[0]),residual_days=resid.tolist(),cycle_condition='Integer cycles chosen near Gaia period; uniqueness requires coverage/other-kind checks.',error_meaning='2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration')
    if row['sample_id']=='T002' and (B/row['tic']/'lead-new-timing.json').is_file():
        new=json.loads((B/row['tic']/'lead-new-timing.json').read_text())
        times=np.array([d['events'][0]['fit_mid_btjd'],d['events'][1]['fit_mid_btjd'],new['events'][0]['center_btjd'],new['events'][2]['center_btjd']]);cycles=np.array([0,29,113,117]);A=np.column_stack([np.ones(len(cycles)),cycles]);par=np.linalg.lstsq(A,times,rcond=None)[0];res=times-A@par
        out['kinds']['deep']=dict(event_indices=[0,1],new_sector_event_indices=[0,2],supporting_partial_new_index=1,sector=[4,31,105,108],mid_btjd=times.tolist(),cycle=cycles.tolist(),period_days=float(par[1]),period_error_days=.00005,epoch_btjd=float(par[0]),residual_days=res.tolist(),cycle_condition='Old 28/30-cycle aliases excluded by sensitive new-sector target-aperture predictions; 29 cycles s4-s31, with two full new events and one partial near S108 start. S108 P/2 null also tested.',error_meaning='0.00005 d conservative allowance for QLP versus custom-pixel timing, exceeding formal regression scatter error')
    (B/row['tic']/'lead-timing.json').write_text(json.dumps(out,indent=2)+'\n')
    print(row['sample_id'],[(k,round(v['period_days'],6),round(v['period_error_days'],6) if v['period_error_days'] else None,round(max(abs(x) for x in v['residual_days']),4)) for k,v in out['kinds'].items()])
