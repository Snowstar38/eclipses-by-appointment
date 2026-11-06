from pathlib import Path
import csv,json,hashlib,sys
W=Path(__file__).resolve().parent;D=W/sys.argv[1];C=Path('[workspace]/Astra/made/binary-extension-2026-11-04/catalogue-archives')
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prsa=C/'mast-prsa.csv';ijs=C/'ijspeert-identities.csv'
assert sha(prsa)=='97e81f6c01716a431379ab6bd37d1182b611a485107110e0eba830f817ba7a8f'
assert sha(ijs)=='8cc6a6b97bc21195d0564659d637f6928aec4364baa7bfa86f82e015742ef75e'
p={r['tess_id']:r for r in rows(prsa)};ir=rows(ijs);it={r['TIC']:r for r in ir};ig={r['GaiaDR3']:r for r in ir};pop=json.loads((D/'targets.json').read_text());out=[]
for t,g in pop.items():
    out.append(dict(tic=t,gaia_dr3=g['gaia']['source_id'],prsa=p.get(t),ijspeert=it.get(t) or ig.get(g['gaia']['source_id'])))
(D/'exact-prior-identities.json').write_text(json.dumps({'scope':'Exact cached primary-table identity precheck only; no physical verdict, neighbor assessment or complete novelty gate. All selected targets remain in screening denominator.','source_hashes':{'Prsa':sha(prsa),'IJspeert':sha(ijs)},'targets':out},indent=2)+'\n')
print('Prechecked',len(out),'primary exact prior hits',sum(bool(r['prsa'] or r['ijspeert']) for r in out))
