"""Explicit positive-match updates; never turn service failures into clearance."""
from pathlib import Path
import csv,json,math,hashlib
W=Path(__file__).resolve().parent
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def write(p,r):
    with p.open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(r[0]));w.writeheader();w.writerows(r)
def main():
    records=json.loads((W/'tap-recovery/vsx-results.json').read_text())
    # These are manually reviewed spatial identities, not an automated type classifier.
    chosen={'Q054':'ASAS J073024-2831.8','Q079':'ASAS J030241-7332.9','Q080':'ASAS J071145-2226.6',
      'prior-294257329':'ASAS J102734-1944.2','prior-313617927':'GSC 03961-01881','prior-219739532':'V0481 Dra','prior-102069549':'AI Phe','prior-99725941':'BMAM-V724'}
    updates=[]
    for r in records:
        if r['key'] not in chosen:continue
        o=next(o for o in r['objects'] if o['Name']==chosen[r['key']])
        sep=3600*math.hypot((float(o['RA2000'])-float(r['ra_deg']))*math.cos(math.radians(float(r['dec_deg']))),float(o['Declination2000'])-float(r['dec_deg']))
        assert sep<1 and r['status']=='success'
        f=W/'tap-recovery'/r['file'];assert hashlib.sha256(f.read_bytes()).hexdigest()==r['sha256']
        updates.append(dict(key=r['key'],tic=r['tic'],gaia_dr3=r['gaia_dr3'],previous_novelty='UNKNOWN',novelty_status='KNOWN',name=o['Name'],type=o['VariabilityType'],period_days=o.get('Period',''),separation_arcsec=f'{sep:.3f}',receipt='tap-recovery/'+r['file'],receipt_sha256=r['sha256'],reason='Sub-arcsecond prior eclipsing-type counterpart. Ambiguous published EB types exclude new-claim eligibility without asserting this review confirmed that classification.'))
    assert len(updates)==8
    write(W/'catalogue-updates.csv',updates)
    # Strong positive identities remain valid despite the later outage. Nonmatches cannot clear all seven scopes.
    note={'successful_target_queries':sum(r['status']=='success' and r.get('scope')=='next100' for r in records),'prior_pending_attempted':sum(r.get('scope')=='prior41' for r in records),'positive_control_before':records[0]['status'],'positive_control_after':records[-1]['status'],'stop_reason':'Three consecutive failures; unattempted and failed requests remain UNKNOWN. No further queries or nonmatch-based claims.','known_updates':len(updates),'other_required_scopes_unavailable':['ASAS-SN','Kostov vetted tables 3 and 4'],'scope':'VSX direct API recovery supplements, and does not overwrite, dated physical-review catalogue freezes.'}
    (W/'catalogue-recovery-summary.json').write_text(json.dumps(note,indent=2)+'\n')
    if not (W/'accepted-results.csv').exists():return
    reviewed=rows(W/'reconciled-results.csv');changes={r['tic']:r for r in updates}
    decisions=[]
    for r in reviewed:
        novelty='KNOWN' if r['tic'] in changes else r['novelty_status']
        cp=r['physical_verdict'] in ('CONFIRMED','PROBABLE')
        decision='KNOWN_RECOVERY' if novelty=='KNOWN' and cp else ('PENDING_CATALOGUE' if cp else 'NOT_CLAIM_ELIGIBLE')
        decisions.append(dict(sample_id=r['sample_id'],tic=r['tic'],physical_verdict=r['physical_verdict'],novelty_status=novelty,claim_decision=decision,count_addition='false',basis=('catalogue-updates.csv' if r['tic'] in changes else 'Physical freeze plus shared-catalogues; unavailable mandatory scopes remain unknown.')))
    write(W/'claim-decisions.csv',decisions)
    print(note)
if __name__=='__main__':main()
