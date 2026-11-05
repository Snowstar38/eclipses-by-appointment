"""Root scientific decisions for exact R689-R697 after final lead/helper freeze."""
import csv,hashlib,json
from pathlib import Path
W=Path(__file__).resolve().parent;R=W/'review9';A=W/'accounting'
C=W/'next256/catalogue-recovery-20261105T0117'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
expected=['159060569','387268955','342060048','184398115','64701575','284613090','128720791','95623701','56912737']
tiers=['confirmed','confirmed','probable','probable','confirmed','probable','probable','plausible','confirmed']
q=read(R/'queue.csv');rs=read(R/'RESULTS.csv');seal=json.loads((R/'queue-seal.json').read_text())
assert [x['tic'] for x in q]==[x['tic'] for x in rs]==expected
assert sha(R/'queue.csv')==seal['sha256'] and sha(R/'SOURCE-SNAPSHOT.json')==seal['snapshot_sha256']
assert [x['physical_verdict'].lower() for x in rs]==tiers
assert all(x['full_review_completion']=='COMPLETE' for x in rs)
assert all(rs[7][k]=='' for k in ('period_days','period_error_days','primary_epoch_btjd'))
verified={};counts={}
for folder in (R,C):
    manifest=json.loads((folder/'SHA256SUMS.json').read_text(encoding='utf-8'))
    if folder==R:
        assert manifest['queue_seal_sha256']==sha(R/'queue.csv')
        assert manifest['snapshot_seal_sha256']==sha(R/'SOURCE-SNAPSHOT.json')
        manifest={**manifest['local_files'],**manifest['external_sources']}
    for path,digest in manifest.items():
        f=Path(path);f=f if f.is_absolute() else folder/f
        assert sha(f)==digest,str(f)
        verified[str(f)]=digest
    counts[str(folder.relative_to(W))]=len(manifest)
    verified[str(folder/'SHA256SUMS.json')]=sha(folder/'SHA256SUMS.json')
helpers=json.loads((R/'helper-final-audit.json').read_text(encoding='utf-8'))
assert all(helpers['checks'].values())
helpers=helpers['rows']
assert [x['tic'] for x in helpers]==expected and all(all(x['checks'].values()) for x in helpers)
for x in helpers:assert x['report_sha256']==sha(R/x['tic']/'REPORT.md')
catalogue={x['tic']:x for x in read(C/'coverage-matrix.csv')}
assert all(catalogue[t]['coverage_complete']=='True' for t in expected)
novel={'342060048','184398115'};known=set(expected)-novel-{'95623701'}
for tic in expected:
    status='known prior EB in queried scope' if tic in known else 'no identified prior EB in queried scope'
    assert catalogue[tic]['scoped_prior_eb_status']==status
ds=json.loads((A/'root-decisions.json').read_text(encoding='utf-8'))
assert not {d['tic'] for d in ds['decisions']}&set(expected)
for i,(qr,rr,tier) in enumerate(zip(q,rs,tiers)):
    tic=qr['tic'];rid=f'R{689+i}';assert qr['review_id']==rid
    novelty='new_claim' if tic in novel else 'known_prior_recovery' if tic in known else 'not_claim_eligible'
    rationale=('Repeated measured eclipses pass bounded review, with unresolved close-source attribution and Gaia-clock differences; accept probable new claim within completed catalogue scope.' if tic=='342060048' else 'Repeated deep eclipses and target-centered deficit; material disagreement with Gaia orbit remains. Accept probable new claim, not a confirmed association with the spectroscopic pair.' if tic=='184398115' else 'Completed review finds contradictory clean null for assumed cycle alias and unresolved source; accept plausible, excluded.' if tic=='95623701' else 'Accept completed physical review at stated tier; exact published EB identity excludes a new-system claim.')
    evidence=[str(R/x) for x in ('SHA256SUMS.json','helper-audit.md','helper-final-audit.json',f'{tic}/REPORT.md',f'{tic}/measurements.json')]+[str(C/'coverage-matrix.csv'),str(C/'SHA256SUMS.json')]
    ds['decisions'].append(dict(review_id=rid,tic=tic,gaia_dr3=qr['gaia_dr3'],physical_tier=tier,novelty=novelty,accepted_by='root explicit decision 2026-11-04',rationale=rationale+' '+rr['limitations'],queue_file=str(R/'queue.csv'),results_file=str(R/'RESULTS.csv'),catalogue_matrix=str(C/'coverage-matrix.csv'),evidence=evidence))
lock=json.loads((A/'input-lock.json').read_text(encoding='utf-8'))
for path,digest in lock.items():assert sha(Path(path))==digest,path
for path in [R/'queue.csv',R/'RESULTS.csv',R/'helper-final-audit.json',C/'coverage-matrix.csv']:
    verified[str(path)]=sha(path)
for path,digest in verified.items():
    assert path not in lock or lock[path]==digest,path
    lock[path]=digest
(A/'input-lock.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
(A/'root-decisions.json').write_text(json.dumps(ds,indent=2)+'\n',encoding='utf-8')
receipt=dict(accepted_review_ids=[f'R{x}' for x in range(689,698)],new_claim_tics=sorted(novel),known_recovery_tics=sorted(known),excluded_plausible_tics=['95623701'],manifest_files_verified=counts,results_sha256=sha(R/'RESULTS.csv'),manifest_sha256=sha(R/'SHA256SUMS.json'),expected_counts=dict(physical=936,claims=912,confirmed_claims=807,probable_claims=105,pending_novelty_physical=0))
(R/'ROOT-ACCEPTANCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
