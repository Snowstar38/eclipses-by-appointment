"""Reproduce cohort denominators, repeated controls, and accepted private counts."""
from pathlib import Path
from collections import Counter
import csv,hashlib,json
W=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cohorts=[];science={};controls={};sources={}
for name in ['pilot48','next256','remaining_cached','resolved125','unmatched512']:
    p=W/name
    if not (p/'pilot.json').exists() or not (p/'screening.jsonl').exists():continue
    pilot=json.loads((p/'pilot.json').read_text(encoding='utf-8'))
    rows=[json.loads(l) for l in (p/'screening.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len({r['tic'] for r in rows})==len(rows)
    assert set(r['tic'] for r in rows)<=set(pilot['targets'])
    complete=len(rows)==len(pilot['targets'])
    sci=[];ctrl=[]
    for r in rows:
        t=pilot['targets'][r['tic']]
        if t['control']:
            ctrl.append(r)
            fingerprint={k:r.get(k) for k in ('status','P','P2','null_med','null_mad','flag')}
            if r['tic'] in controls:assert fingerprint==controls[r['tic']]['fingerprint']
            else:controls[r['tic']]={'fingerprint':fingerprint,'first_cohort':name}
        else:
            assert r['tic'] not in science
            science[r['tic']]=name;sci.append(r)
    cohorts.append(dict(cohort=name,complete=complete,selected_science=pilot['science_targets'],selected_controls=pilot['controls'],completed_science=len(sci),science_outcomes=dict(Counter(r['status'] for r in sci)),flagged_science=sum(bool(r.get('flag')) for r in sci),controls_run=len(ctrl),controls_recovered=sum(bool(r.get('flag')) for r in ctrl)))
    sources[name]={f:sha(p/f) for f in ('pilot.json','screening.jsonl')}
ledger=list(csv.DictReader((W/'accounting/accepted-proposal-ledger.csv').open(encoding='utf-8')))
claims=[r for r in ledger if r['claim_member']=='True']
status=dict(cohorts=cohorts,unique_completed_science=len(science),unique_controls=len(controls),unique_recovered_controls=sum(bool(v['fingerprint']['flag']) for v in controls.values()),repeated_control_statistics_identical=True,accepted_claims=len(claims),accepted_claim_tiers=dict(Counter(r['physical_tier'] for r in claims)),physical_systems=sum(r['physical_member']=='True' for r in ledger),source_hashes=sources,ledger_sha256=sha(W/'accounting/accepted-proposal-ledger.csv'),caveat='Adaptive follow-up, distinct cohorts and repeated control runs; not an occurrence-rate sample or calibrated completeness. Flags are not accepted eclipsing binaries. Original public paper remains unchanged.')
(W/'CAMPAIGN-STATUS.json').write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in status.items() if k not in ('source_hashes',)},indent=2))
