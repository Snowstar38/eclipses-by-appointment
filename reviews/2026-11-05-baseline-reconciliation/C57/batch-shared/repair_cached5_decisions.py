from pathlib import Path
import json
p=Path(__file__).resolve().parent/'accounting/root-decisions.json'
d=json.loads(p.read_text())
for r in d['decisions']:
 if r['review_id'] in ('R711','R712'):
  assert r['physical_tier']=='plausible' and r['novelty']=='no_prior_eb_identified'
  r['novelty']='not_claim_eligible'
p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
