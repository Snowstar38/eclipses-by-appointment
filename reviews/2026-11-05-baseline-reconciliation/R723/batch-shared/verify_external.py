import csv,hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;C=B.parent/'unmatched512'/'catalogue-recovery-selected12';S=B.parent/'unmatched512'/'shared-catalogues';D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());checks=[]
def check(p,h):
 a=hashlib.sha256(p.read_bytes()).hexdigest();assert a==h,str(p);checks.append(dict(path=str(p),sha256=a))
manifest=json.loads((C/'SHA256SUMS.json').read_text())
for rel,h in manifest.items():check(C/rel,h)
r=json.loads((S/'receipts/gaia_nss.json').read_text());check(S/r['file'],r['sha256']);check(S/'receipts/gaia_nss.json',hashlib.sha256((S/'receipts/gaia_nss.json').read_bytes()).hexdigest())
nss={r['source_id']:r for r in csv.DictReader((S/'raw/gaia_nss.txt').open(newline='',encoding='utf-8'))};cats=json.loads((C/'catalogue-results.json').read_text());live=json.loads((C/'selected12-live-vsx-results.json').read_text())
vs=live['results'];print(type(vs))
for tic,src in D.items():
 row=nss[src['target']['gaia']['source_id']];(B/tic/'gaia-nss-row.json').write_text(json.dumps(row,indent=2)+'\n')
 c=[v for v in cats if v.get('tic')==tic];v=[x for x in vs if str(x.get('tic'))==tic] if isinstance(vs,list) else vs.get(tic)
 (B/tic/'catalogue-evidence.json').write_text(json.dumps(dict(tic=tic,gaia_source_id=row['source_id'],catalogue_status='UNKNOWN_INCOMPLETE_SCOPED_CHECKS',scoped_results=c,live_vsx=v,note='Full-source Prsa/IJspeert nonmatches and exact Gaia/SIMBAD scoped checks do not clear missing ASAS-SN/Kostov; direct VSX explicit empty is a scoped supplement with completeness uncertified. No new-system claim.'),indent=2)+'\n')
(B/'external-source-verification.json').write_text(json.dumps(dict(passed=True,checks=checks,catalogue_manifest_path=str(C/'SHA256SUMS.json'),catalogue_manifest_sha256=hashlib.sha256((C/'SHA256SUMS.json').read_bytes()).hexdigest(),gaia_source_receipt=r),indent=2)+'\n')
print(len(checks),'external hashes verified')

