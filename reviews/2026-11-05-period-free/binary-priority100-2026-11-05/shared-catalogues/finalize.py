"""Attach successful bulk catalogues and scoped local comparisons to target evidence."""
import csv, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ev=json.loads((H/'target-evidence.json').read_text(encoding='utf-8'))
bulk=json.loads((H/'bulk-remote-receipts.json').read_text(encoding='utf-8'))
data={}
for cat,rec in bulk.items():
    p=Path(rec['raw']);assert rec['status']=='success' and sha(p)==rec['sha256']
    data[cat]=list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
local={}
for cat,name in [('heartbeat','heartbeat-overlaps.json'),('chopard','chopard-overlaps.json'),('tarrants','tarrants-mendes-overlaps.json')]:
    p=H/name;local[cat]=json.loads(p.read_text(encoding='utf-8'))
    ev['sources'][cat]={'path':str(p),'sha256':sha(p)}
ev['sources']['bulk_remote']={'path':str(H/'bulk-remote-receipts.json'),'sha256':sha(H/'bulk-remote-receipts.json')}
ev['sources']['remote_control']={'path':str(H/'remote-control.json'),'sha256':sha(H/'remote-control.json')}
ev['sources']['alternate_remote_control']={'path':str(H/'alternate-remote-control.json'),'sha256':sha(H/'alternate-remote-control.json')}
ev['sources']['gaia_neighbors']={'path':str(H/'gaia-neighbors.json'),'sha256':sha(H/'gaia-neighbors.json')}
neighbors=json.loads((H/'gaia-neighbors.json').read_text(encoding='utf-8'))
for x in ev['targets']:
    tic=x['tic'];g=x['gaia_dr3']
    x['gaia_neighbors_120arcsec']=neighbors['targets'][x['sample_id']]
    x['local_prior']={cat:local[cat]['targets'][tic] for cat in local}
    x['gaia_eb_rows']=[r for r in data['gaia_eb'] if r['source_id']==g]
    x['gaia_summary_rows']=[{'source_id':r['source_id'],'in_vari_eclipsing_binary':r['in_vari_eclipsing_binary'],'in_vari_classification_result':r['in_vari_classification_result']} for r in data['gaia_summary'] if r['source_id']==g]
    x['gaia_nss_rows']=[{'source_id':r['source_id'],'nss_solution_type':r['nss_solution_type'],'period':r['period']} for r in data['gaia_nss'] if r['source_id']==g]
    x['simbad_rows']=[r for r in data['simbad'] if r['id']=='Gaia DR3 '+g]
    x['gate_status']={cat:('verified cached target cone' if cat in x['verified_historical_cone_receipts'] else 'unknown: VizieR positive control timed out; target query unattempted') for cat in ('vsx','asassn','kostov2025_table3','kostov2025_table4')}
    x['gate_status'].update({'prsa2022':'complete primary table exact identity and 5 arcsec cone nonmatch','ijspeert2024':'complete primary identity table exact identity and 5 arcsec cone nonmatch','gaia_eb':'successful bulk exact Gaia nonmatch','gaia_summary':'successful bulk exact Gaia query','gaia_nss':'successful bulk exact Gaia query','simbad':'successful bulk exact Gaia query'})
    known=bool(x['primary_prsa_exact_rows'] or x['primary_ijspeert_exact_rows'] or x['prior_review_or_register'] or x['local_prior']['chopard'] or x['local_prior']['tarrants'] or any(r.get('eclipses_flag')=='True' for r in x['local_prior']['heartbeat']) or x['gaia_eb_rows'] or any(r['otype'] in ('EB*','Al*','bL*','WU*') for r in x['simbad_rows']))
    x['novelty_status']='prior association alert; target/source interpretation and four VizieR gates unresolved' if known else 'novelty unknown: four VizieR gates unqueried after failed positive controls'
(H/'target-evidence.json').write_text(json.dumps(ev,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
rows=[]
for x in ev['targets']:
    rows.append({'sample_id':x['sample_id'],'tic':x['tic'],'gaia_dr3':x['gaia_dr3'],'ra_deg':x['ra_deg'],'dec_deg':x['dec_deg'],'novelty_status':x['novelty_status'],'prsa_exact':len(x['primary_prsa_exact_rows']),'ijspeert_exact':len(x['primary_ijspeert_exact_rows']),'prsa_5arcsec':len(x['primary_prsa_5arcsec_rows']),'ijspeert_5arcsec':len(x['primary_ijspeert_5arcsec_rows']),'historical_exact':len(x['prior_review_or_register']),'chopard':len(x['local_prior']['chopard']),'tarrants':bool(x['local_prior']['tarrants']),'heartbeat':len(x['local_prior']['heartbeat']),'gaia_eb':len(x['gaia_eb_rows']),'simbad_otype':x['simbad_rows'][0]['otype'] if x['simbad_rows'] else '', 'missing_gates':','.join(k for k,v in x['gate_status'].items() if v.startswith('unknown:'))})
with (H/'TARGET-STATUS.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
print(json.dumps({'targets':len(rows),'prior_alert':sum(x['novelty_status'].startswith('prior association') for x in rows),'unknown':sum(x['novelty_status'].startswith('novelty unknown') for x in rows),'missing_gates_each':len(rows[0]['missing_gates'].split(','))}))
