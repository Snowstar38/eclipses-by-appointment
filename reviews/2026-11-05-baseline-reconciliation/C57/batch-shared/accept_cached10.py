"""Explicit root acceptance: one new probable and nine known recoveries."""
import csv,hashlib,json
from pathlib import Path
W=Path(__file__).resolve().parent;R=W/'review_cached10';C=W/'remaining_cached/catalogue-recovery-late';A=W/'accounting'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:list(csv.DictReader(p.open(encoding='utf-8-sig')))
q=read(R/'queue.csv');rs=read(R/'RESULTS.csv');expected=['349978696','230130556','174303697','102305337','343452418','207780183','36721228','431996459','121277143','431589019']
assert [r['tic'] for r in q]==[r['tic'] for r in rs]==expected
assert [r['physical_verdict'] for r in rs]==['CONFIRMED','PROBABLE','PROBABLE','CONFIRMED','PROBABLE','PROBABLE','CONFIRMED','PROBABLE','PROBABLE','PROBABLE']
assert all(r['full_review_completion']=='COMPLETE' for r in rs)
seal=json.loads((R/'queue-seal.json').read_text());assert sha(R/'queue.csv')==seal['sha256'] and sha(R/'SOURCE-SNAPSHOT.json')==seal['snapshot_sha256']
for p,digest in seal['source_hashes'].items():assert sha(W/p)==digest,p
verified={};counts={}
for folder in (R,C):
    manifest=json.loads((folder/'SHA256SUMS.json').read_text(encoding='utf-8'))
    if folder==R:manifest=manifest['files']
    for path,digest in manifest.items():
        f=Path(path);f=f if f.is_absolute() else folder/f
        assert sha(f)==digest,str(f);verified[str(f)]=digest
    counts[str(folder.relative_to(W))]=len(manifest)
    verified[str(folder/'SHA256SUMS.json')]=sha(folder/'SHA256SUMS.json')
snapshot=json.loads((R/'SOURCE-SNAPSHOT.json').read_text())
for t in snapshot.values():
    for rec in t['target']['file_receipts']:
        assert sha(Path(rec['path']))==rec['sha256'];verified[rec['path']]=rec['sha256']
h=json.loads((R/'helper-final-audit.json').read_text());assert h['exact_queue'] and h['results_sha256']==sha(R/'RESULTS.csv')
assert [r['tic'] for r in h['rows']]==expected
for r in h['rows']:
    assert all(r['checks'].values()) and sha(R/r['tic']/'REPORT.md')==r['report_sha256']
    assert sha(R/r['tic']/'measurements.json')==r['measurements_sha256']
catalogue={r['tic']:r for r in read(C/'coverage-matrix.csv')}
for tic in expected:
    assert catalogue[tic]['coverage_complete']=='True'
    assert catalogue[tic]['scoped_prior_eb_status']==('no identified prior EB in queried scope' if tic=='121277143' else 'known prior EB in queried scope')
ds=json.loads((A/'root-decisions.json').read_text());assert not {r['tic'] for r in ds['decisions']}&set(expected)
for i,(qr,rr) in enumerate(zip(q,rs)):
    tic=qr['tic'];rid=f'R{698+i}';assert qr['review_id']==rid
    rationale=('Root accepts repeated measured eclipses at probable tier; 34.55-arcsec neighbor remains nominally capable under optimistic Gaia-G flux proxy and is not securely excluded. Exact ASAS-SN ROT: counterpart is not a prior EB classification; completed scoped checks support a new EB claim.' if tic=='121277143' else 'Root accepts completed physical tier with all stated limitations; exact published IJspeert EB identity excludes a new-system claim.')
    evidence=[str(R/x) for x in ('SHA256SUMS.json','helper-audit.md','helper-final-audit.json',f'{tic}/REPORT.md',f'{tic}/measurements.json')]+[str(C/'coverage-matrix.csv'),str(C/'SHA256SUMS.json')]
    ds['decisions'].append(dict(review_id=rid,tic=tic,gaia_dr3=qr['gaia_dr3_source_id'],physical_tier=rr['physical_verdict'].lower(),novelty='new_claim' if tic=='121277143' else 'known_prior_recovery',accepted_by='root explicit decision 2026-11-04',rationale=rationale+' '+rr['limitations'],queue_file=str(R/'queue.csv'),results_file=str(R/'RESULTS.csv'),catalogue_matrix=str(C/'coverage-matrix.csv'),evidence=evidence))
lock=json.loads((A/'input-lock.json').read_text())
for path,digest in lock.items():assert sha(Path(path))==digest,path
for path,digest in verified.items():
    assert path not in lock or lock[path]==digest,path
    lock[path]=digest
(A/'input-lock.json').write_text(json.dumps(lock,indent=2)+'\n',encoding='utf-8')
(A/'root-decisions.json').write_text(json.dumps(ds,indent=2)+'\n',encoding='utf-8')
receipt=dict(review_ids=[f'R{x}' for x in range(698,708)],new_claim_tics=['121277143'],known_recovery_tics=[t for t in expected if t!='121277143'],manifest_files_verified=counts,all_qlp_source_hashes_verified=True,results_sha256=sha(R/'RESULTS.csv'),manifest_sha256=sha(R/'SHA256SUMS.json'),expected_counts=dict(physical=946,claims=913,confirmed_claims=807,probable_claims=106,pending_novelty_physical=0))
(R/'ROOT-ACCEPTANCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt,indent=2))
