import csv,json,hashlib,math
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest(); Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8-sig',newline='')));R=list(csv.DictReader((B/'RESULTS.csv').open(encoding='utf-8-sig',newline='')));S=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf8'));G=json.loads((B/'gaia-geometry.json').read_text(encoding='utf8'));N={x['tic']:x for x in json.loads((B/'helper-pixels/final-neighbors.json').read_text(encoding='utf8'))};rows=[]
for q,r in zip(Q,R):
 t=q['tic'];m=json.loads((B/t/'measurements.json').read_text(encoding='utf8'));p=B/t/'REPORT.md';report=p.read_text(encoding='utf8');rec=json.loads((B/'helper-pixels'/t/'receipt.json').read_text(encoding='utf8'));raw=B/'helper-pixels'/t/'tesscut.raw';fits=B/'helper-pixels'/t/'tesscut.fits';g=S[t]['target']['gaia'];checks={}
 checks['identity']=q['tic']==r['tic']==m['tic'] and q['gaia_dr3_source_id']==r['gaia_dr3_source_id']==m['gaia_source_id']==str(g['source_id']) and q['review_id']==r['review_id'] and q['gaia_dr3_source_id'] in report and q['review_id'] in report
 checks['verdict']=r['physical_verdict'] in report and r['full_review_completion'] in report
 checks['all_raw_source_sha256']=all(sha(Path(x['path']))==x['sha256'] for x in m['source_receipts']);checks['tesscut_raw_sha256']=sha(raw)==rec['raw_sha256'];checks['tesscut_fits_sha256']=sha(fits)==rec['fits_sha256']
 checks['same_photons']='same TESS photons' in report or 'same photons' in report
 conditional=t in ['25320385','349527829','95836684'];checks['orbital_fields_correct']=all(not r[x] for x in ['period_days','period_error_days','reference_epoch_btjd']) if conditional else (abs(float(r['period_days'])-m['period_days'])<5.1e-10 and abs(float(r['period_error_days'])-m['period_error_days'])<5.1e-10 and abs(float(r['reference_epoch_btjd'])-m['reference_epoch_btjd'])<5.1e-9)
 checks['depth']=abs(float(r['depth_ppt'])-m['depth_ppt'])<.0051
 checks['neighbor_ids']=all(n['source_id'] in report for n in N[t]['capable_at_minimum_all_apertures'])
 P=float(g['period']);e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));tp=389+float(g['t_periastron']);ep=m['reference_epoch_btjd'];delta=[]
 for k,L in enumerate((math.pi/2,3*math.pi/2)):
  nu=L-w; E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2));pred=tp+((E-e*math.sin(E))%(2*math.pi))*P/(2*math.pi);pred+=round((ep-pred)/P)*P;delta.append(pred-G[t]['conjunctions'][k]['gaia_conjunction_btjd'])
 checks['independent_gaia_conjunction']=max(map(abs,delta))<1e-7
 ev=[x for x in m['events'] if x.get('timing_usable')];fitdelta=None
 if len(ev)>=2:
  n=np.array([x['cycle'] for x in ev]);tt=np.array([x['mid_btjd'] for x in ev]);err=np.array([x['timing_error_days'] for x in ev]);A=np.column_stack([np.ones(len(n)),n-m['reference_cycle']])/err[:,None];beta=np.linalg.lstsq(A,tt/err,rcond=None)[0];fitdelta=[float(beta[0]-m['reference_epoch_btjd']),float(beta[1]-m['period_days'])]
 checks['linear_fit']=(fitdelta is not None and abs(fitdelta[0])<1e-7 and abs(fitdelta[1])<1e-8) if t!='349527829' else (len(ev)==1 and abs((m['events'][1]['mid_btjd']-m['events'][0]['mid_btjd'])/(m['events'][1]['cycle']-m['events'][0]['cycle'])-m['period_days'])<1e-8 and not m['events'][1]['timing_usable'])
 checks['report_numeric']=f"{m['depth_ppt']:.2f}" in report and (f"{m['period_days']:.9f}" in report) and (f"{m['period_error_days']:.9f}" in report) and (f"{m['reference_epoch_btjd']:.8f}" in report)
 rows.append({'review_id':q['review_id'],'tic':t,'checks':checks,'linear_fit_differences_epoch_period':fitdelta,'gaia_conjunction_differences_days':delta,'report_sha256':sha(p),'measurements_sha256':sha(B/t/'measurements.json'),'tesscut_raw_sha256':sha(raw),'tesscut_fits_sha256':sha(fits)})
out={'queue_sha256':sha(B/'queue.csv'),'results_sha256':sha(B/'RESULTS.csv'),'gaia_geometry_sha256':sha(B/'gaia-geometry.json'),'gaia_census_raw_sha256':sha(B/'helper-pixels/gaia-all.raw'),'helper_neighbors_sha256':sha(B/'helper-pixels/final-neighbors.json'),'exact_queue':len(Q)==len(R)==10 and [x['tic'] for x in Q]==[x['tic'] for x in R], 'rows':rows};(B/'helper-final-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print('queue',out['exact_queue']);
for r in rows:print(r['tic'],[k for k,v in r['checks'].items() if not v],r['linear_fit_differences_epoch_period'])
