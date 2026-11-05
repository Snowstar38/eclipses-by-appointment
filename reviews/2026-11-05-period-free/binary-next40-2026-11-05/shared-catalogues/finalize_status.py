"""Merge bounded VizieR evidence without conflating variability, EB prior art, and local history."""
import csv, json
from pathlib import Path

H=Path(__file__).resolve().parent
e=json.loads((H/'target-evidence.json').read_text(encoding='utf-8'))
v=json.loads((H/'vizier-gate-results.json').read_text(encoding='utf-8'))
assert e['queue_sha256']==v['queue_sha256'] and len(e['targets'])==len(v['targets'])==40
eb_codes=('EA','EB','EW','ESD','EC','ECL','E')
for t in e['targets']:
    gates=v['targets'][t['sample_id']]
    t['vizier_gates']=gates
    t['published_eb_alerts']=[x for x in t['published_eb_alerts'] if not x.startswith(('vsx ','asassn ','kostov3 ','kostov4 '))]
    t['other_published_variability']=[]
    t['published_eb_neighbors']=[]
    for label,gate in gates.items():
        for hit in gate['nearby_rows']:
            kind=(hit.get('Type') or '').upper()
            near=float(hit.get('_r') or 999)
            if kind.startswith(eb_codes) and near<=2:
                t['published_eb_alerts'].append(f'{label} positional EB classification {kind} at {near:.2f} arcsec; confirm source identity')
            elif kind.startswith(eb_codes):
                t['published_eb_neighbors'].append({'catalogue':label,'type':kind,'separation_arcsec':near,'row':hit})
            elif hit in gate['exact_rows']:
                t.setdefault('other_published_variability',[]).append({'catalogue':label,'type':kind,'row':hit})
    t['prior_alerts']=t['published_eb_alerts']+t['local_prior_candidate_alerts']
    complete=all(t['remote'][k]['status']=='success' for k in ('gaia_eb','gaia_summary','gaia_nss','simbad')) and all(g['status']=='success' for g in gates.values())
    t['novelty_status']=('KNOWN_PUBLISHED_EB_ALERT; inspect prior row' if t['published_eb_alerts'] else 'SCOPED_NONMATCH; no target EB identification in checked tables' if complete else 'UNKNOWN; one or more catalogue gates unavailable')
(H/'target-evidence.json').write_text(json.dumps(e,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
with (H/'TARGET-STATUS.csv').open('w',encoding='utf-8',newline='') as f:
    fields=['sample_id','tic','gaia_dr3','novelty_status','published_eb_alerts','local_prior_candidate_alerts','published_eb_neighbors','other_published_variability','prsa_exact','ijspeert_exact','prsa_5arcsec','ijspeert_5arcsec','gaia_eb','gaia_summary','gaia_nss','simbad','vsx','asassn','kostov3','kostov4']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for t in e['targets']:
        w.writerow({'sample_id':t['sample_id'],'tic':t['tic'],'gaia_dr3':t['gaia_dr3'],'novelty_status':t['novelty_status'],'published_eb_alerts':'; '.join(t['published_eb_alerts']),'local_prior_candidate_alerts':'; '.join(t['local_prior_candidate_alerts']),'published_eb_neighbors':'; '.join(f"{x['catalogue']}:{x['type']}@{x['separation_arcsec']:.2f}" for x in t['published_eb_neighbors']),'other_published_variability':'; '.join(f"{x['catalogue']}:{x['type']}" for x in t.get('other_published_variability',[])),'prsa_exact':len(t['primary_prsa_exact']),'ijspeert_exact':len(t['primary_ijspeert_exact']),'prsa_5arcsec':len(t['primary_prsa_5arcsec']),'ijspeert_5arcsec':len(t['primary_ijspeert_5arcsec']),**{k:t['remote'][k]['status'] for k in ('gaia_eb','gaia_summary','gaia_nss','simbad')},**{k:t['vizier_gates'][k]['status'] for k in ('vsx','asassn','kostov3','kostov4')}})
print('known published EB',[(t['sample_id'],t['tic']) for t in e['targets'] if t['published_eb_alerts']])
print('local history',[(t['sample_id'],t['tic']) for t in e['targets'] if t['local_prior_candidate_alerts']])
