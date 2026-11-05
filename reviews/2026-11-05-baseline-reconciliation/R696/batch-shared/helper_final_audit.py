import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;S=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf8')));R=list(csv.DictReader((B/'RESULTS.csv').open(encoding='utf8'))); checks={'exact_queue_ids':{x['tic'] for x in R}=={x['tic'] for x in Q} and len(R)==len(Q)==9};rows=[]
for r in R:
 tic=r['tic'];m=json.loads((B/tic/'measurements.json').read_text(encoding='utf8'));t=(B/tic/'REPORT.md').read_text(encoding='utf8');c={'identity':m['tic']==tic and m['gaia_source_id']==S[tic]['target']['gaia']['source_id'] and f'TIC {tic}' in t and m['gaia_source_id'] in t,'verdict_completion':r['physical_verdict'] in t and r['full_review_completion'] in t,'depth':abs(float(r['depth_ppt'])-m.get('depth_ppt',m.get('median_selected_event_realized_depth_ppt')))<=.0051,'source_hashes':all(hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'] for x in m['source_receipts'])}
 if tic=='95623701': c['conditional_ephemeris']=all(not r[x] for x in ['period_days','period_error_days','primary_epoch_btjd']) and all(x not in m for x in ['period_days','period_error_days','reference_epoch_btjd']) and 'conditional_112_cycle_period_days' in m and 'No secure period or reference epoch' in t
 else:c['period_epoch']=abs(float(r['period_days'])-m['period_days'])<5.1e-10 and abs(float(r['period_error_days'])-m['period_error_days'])<5.1e-10 and abs(float(r['primary_epoch_btjd'])-m['reference_epoch_btjd'])<5.1e-9
 rows.append({'tic':tic,'checks':c,'report_sha256':hashlib.sha256((B/tic/'REPORT.md').read_bytes()).hexdigest()})
out={'checks':checks,'rows':rows};print(json.dumps(out,indent=2));(B/'helper-final-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')

