"""Quantify release-ID differences without extrapolating to other populations."""
from pathlib import Path
import csv,hashlib,json
W=Path(__file__).resolve().parent
out=[]
old=Path('[local-path-redacted]')
oldids={r['source_id'] for r in csv.DictReader(old.open(encoding='utf-8-sig'))}
for rel in ['unmatched128/resolved/identity-outcomes.json','unmatched512/identity-outcomes.json']:
    p=W/rel;rows=json.loads(p.read_text(encoding='utf-8'))
    good=[r for r in rows if r['status']=='unique_identity']
    assert all(len(r['neighborhood'])==1 and len(r['tic_matches'])==1 for r in good)
    out.append(dict(source=rel,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),frozen=len(rows),unique=len(good),different_dr2_dr3_ids=sum(r['gaia_dr3']!=r['neighborhood'][0]['dr2_source_id'] for r in good),unique_present_in_original_nss=sum(r['gaia_dr3'] in oldids for r in good),same_id_present_in_original_nss=sum(r['gaia_dr3']==r['neighborhood'][0]['dr2_source_id'] and r['gaia_dr3'] in oldids for r in good),ambiguous=len(rows)-len(good)))
targets=json.loads((W/'unmatched512/identity-targets.json').read_text(encoding='utf-8'))
equal=[float(t['gaia']['phot_g_mean_mag']) for t in targets.values() if t['gaia']['source_id']==t['neighborhood']['dr2_source_id']]
out[-1]['same_id_g_range']=[min(equal),max(equal)]
(W/'identity-gap-audit.json').write_text(json.dumps({'cohorts':out,'original_nss_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'interpretation':'Exact identifier equality would miss only the different-ID subset:125 first cohort,48 second cohort. The remaining455 second-cohort identities have equal release IDs, so their absence in local mappings has another cause. These are outcome-independent frozen subsets of the locally unmatched 20-24 day parent, not an estimate of all-Gaia incompleteness or new-EB yield. Coordinates, neighborhoods and full TIC responses remain in the identity receipts.'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
