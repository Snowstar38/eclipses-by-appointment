"""Inclusive, reversible queues; no physical acceptance or novelty claims."""
from pathlib import Path
from collections import defaultdict,Counter
import argparse,csv,json
from bulk_events import sha
W=Path(__file__).resolve().parent;B=W.parent/'binary-extension-2026-11-04'
ap=argparse.ArgumentParser();ap.add_argument('--partial',action='store_true');a=ap.parse_args()
pop=json.loads((W/'bulk-population.json').read_text());targets=pop['targets']
prsa=list(csv.DictReader((B/'catalogue-archives/mast-prsa.csv').open(encoding='utf-8-sig')))
ijs=list(csv.DictReader((B/'catalogue-archives/ijspeert-identities.csv').open(encoding='utf-8-sig')))
known_tic=set(r['tess_id'] for r in prsa)|set(r['TIC'] for r in ijs)
known_gaia=set(r['GaiaDR3'] for r in ijs)
fold={}
for sub in ['pool1024','pool900']:
 p=W/sub/'screening.jsonl'
 if p.exists():rs=[json.loads(l) for l in p.read_text().splitlines()]
 else:rs=[json.loads(p.read_text()) for p in (W/sub/'per-target').glob('*.json')]
 for r in rs:
  tic=str(r['tic']);assert tic not in fold;fold[tic]=r
old_register={r['tic']:r for r in csv.DictReader((B/'REVISIT-REGISTER.csv').open(encoding='utf8'))}
pool_rank={}
p=W/'pool1024/candidate-backlog.csv'
if p.exists():pool_rank={r['tic']:r for r in csv.DictReader(p.open(encoding='utf8'))}
common={}
p=W/'common-mode/target-features.csv'
if p.exists():common={r['tic']:r for r in csv.DictReader(p.open(encoding='utf8')) if r['population']=='bulk'}
rows=[]
for tic,tg in targets.items():
 p=W/'bulk-results'/(tic+'.json')
 if not p.exists():continue
 r=json.loads(p.read_text());fs=r['files'];w=[dict(x,sector=f.get('sector')) for f in fs for x in f.get('windows',[])]
 dips=[x for x in w if x['kind']=='dip' and x['flag']];brights=[x for x in w if x['kind']=='brightening' and x['flag']]
 ds=set(x['sector'] for x in dips);bs=set(x['sector'] for x in brights)
 best=max(dips or [x for x in w if x['kind']=='dip'],key=lambda x:x['contrast'],default={})
 fr=fold.get(tic,{});ff=bool(fr.get('flag'));old=old_register.get(tic,{})
 fb=max([fr[k] for k in ['P','P2'] if fr.get(k)],key=lambda x:x.get('z') if x.get('z') is not None else -1e99,default={})
 near=pool_rank.get(tic,{}).get('tier')=='near_flag'
 tier='repeat_sector_dip' if len(ds)>=2 else 'single_sector_dip' if dips else 'brightening_lead' if brights else 'period_fold_only' if ff else 'period_fold_near' if near else 'retained_nonflag'
 known=tic in known_tic or str(tg['gaia']['source_id']) in known_gaia
 rows.append({'tic':tic,'gaia_dr3':tg['gaia']['source_id'],'gaia_period_days':tg['gaia']['period'],'gaia_G':tg['gaia'].get('phot_g_mean_mag'),
  'ra_deg':tg['gaia'].get('ra',''),'dec_deg':tg['gaia'].get('dec',''),'nss_type':tg['gaia'].get('nss_solution_type',''),
  'queue_group':tier,'cached_primary_identity_match':known,'dip_flag_sectors':len(ds),'bright_flag_sectors':len(bs),
  'known_prior_exact_note':pool_rank.get(tic,{}).get('known_prior_exact_note','False'),
  'fold_raw_rank_tier':pool_rank.get(tic,{}).get('tier',''),
  'fold_isolated_window_stat_count':pool_rank.get(tic,{}).get('raw_isolated_stat',''),
  'retained_dip_flags':len(dips),'retained_bright_flags':len(brights),'best_dip_contrast':best.get('contrast',0),'best_dip_depth':best.get('depth',0),
  'best_window_btjd':best.get('time',''),'best_window_duration_days':best.get('duration',''),
  'best_window_slope_ratio':abs(best.get('slope_per_day',0))*best.get('duration',0)/max(abs(best.get('depth',0)),1e-12),
  'max_bright_contrast':max([-x['contrast'] for x in brights]+[0]),
  'period_fold_attempted':bool(fr),'period_fold_flag':ff,'old20_24_flag':old.get('screen_flag','not_in_old1674'),
  'fold_best_z':fb.get('z',''),'fold_screening_period_days':fb.get('P',''),'fold_screening_depth_ppm':fb.get('depth',''),
  'files':len(fs),'usable_files':sum(f['status']=='ok' for f in fs),'failed_files':sum(f['status']=='failed' for f in fs),
  'dip_sameccd_max_other_targets':common.get(tic,{}).get('dip_sameccd_max_targets',''),
  'dip_otherccd_max_other_targets':common.get(tic,{}).get('dip_otherccd_max_targets',''),
  'bright_sameccd_max_other_targets':common.get(tic,{}).get('bright_sameccd_max_targets',''),
  'output':str(p.relative_to(W)),'common_mode_features':str(W/'common-mode/target-features.csv') if tic in common else ''})
order={'repeat_sector_dip':0,'single_sector_dip':1,'period_fold_only':2,'brightening_lead':3,'period_fold_near':4,'retained_nonflag':5}
rows.sort(key=lambda r:(r['cached_primary_identity_match'],order[r['queue_group']],-r['dip_flag_sectors'],-r['best_dip_contrast'],int(r['tic'])))
if not a.partial:assert len(rows)==len(targets)==6186
suffix='-progress' if a.partial else ''
def write(name,data):
 with (W/(name+suffix+'.csv')).open('w',encoding='utf8',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(data)
write('all-targets',rows)
candidate=[r for r in rows if r['queue_group']!='retained_nonflag']
write('candidate-backlog',candidate)
write('primary-nonmatch-leads',[r for r in candidate if not r['cached_primary_identity_match']])
write('cross-method-leads',[r for r in candidate if r['period_fold_flag'] and r['dip_flag_sectors']>0])
for group in ['repeat_sector_dip','single_sector_dip','brightening_lead','period_fold_only','period_fold_near']:
 write(group+'-queue',[r for r in candidate if r['queue_group']==group])
control_rows=[]
for p in (W/'controls').glob('*.json'):
 if p.stem=='seal':continue
 r=json.loads(p.read_text());fs=r['files'];ws=[x for f in fs for x in f.get('windows',[])]
 control_rows.append({'tic':r['tic'],'files':len(fs),'failed_files':sum(f['status']=='failed' for f in fs),
 'dip_flag':any(x['flag'] and x['kind']=='dip' for x in ws),'brightening_flag':any(x['flag'] and x['kind']=='brightening' for x in ws)})
with (W/('control-summary'+suffix+'.csv')).open('w',newline='',encoding='utf8') as f:
 wr=csv.DictWriter(f,fieldnames=list(control_rows[0]));wr.writeheader();wr.writerows(control_rows)
summary={'status':'partial' if a.partial else 'complete','targets_completed':len(rows),'targets_frozen':len(targets),
 'candidate_targets':len(candidate),'candidate_primary_nonmatches':sum(not r['cached_primary_identity_match'] for r in candidate),
 'groups':dict(Counter(r['queue_group'] for r in rows)),
 'primary_nonmatch_groups':dict(Counter(r['queue_group'] for r in rows if not r['cached_primary_identity_match'])),
 'period_fold_outputs_available':len(fold),'period_fold_flags_available':sum(bool(r.get('flag')) for r in fold.values()),
 'cross_method_leads':sum(r['period_fold_flag'] and r['dip_flag_sectors']>0 for r in rows),
 'preexisting_controls':len(control_rows),'controls_dip_flag':sum(r['dip_flag'] for r in control_rows),
 'definitions':['repeat_sector_dip means flagged windows in >=2sectors, NOT demonstrated same-kind recurrence','single_sector includes multiple retained windows in one sector; not necessarily one eclipse','primary nonmatch is NOT novelty clearance','all scores, failed sources and nonflags retained; not a calibrated complete survey','ranking prioritizes groups and support, does not reject artifacts or establish physical ownership'],
 'source_hashes':{'population':sha(W/'bulk-population.json'),'method':sha(W/'bulk_events.py'),
 'prsa':sha(B/'catalogue-archives/mast-prsa.csv'),'ijspeert':sha(B/'catalogue-archives/ijspeert-identities.csv')}}
(W/('BACKLOG-SUMMARY'+suffix+'.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
print(json.dumps(summary,indent=2))
