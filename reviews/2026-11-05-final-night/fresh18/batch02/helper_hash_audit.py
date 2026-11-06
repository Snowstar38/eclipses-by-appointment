import json,csv,hashlib,pathlib
from astropy.io import fits
p=pathlib.Path(r'[workspace]/Astra/made/final-night-2026-11-05/fresh18/batch02')
queue=list(csv.DictReader((p/'queue.csv').open(encoding='utf-8-sig'))); ident=json.loads((p/'identity-audit.json').read_text(encoding='utf-8-sig')); hashes=json.loads((p/'lead-source-hashes.json').read_text()); results=[]
for row in queue:
 t=next(x for x in ident['targets'] if x['sample_id']==row['sample_id']); checks=[]
 for s in hashes[row['tic']]['source']:
  path=pathlib.Path(s['path']); h=hashlib.sha256(path.read_bytes()).hexdigest()
  with fits.open(path) as f: hdr=f[0].header; tic=str(hdr.get('TICID')); sector=int(hdr.get('SECTOR'))
  checks.append({'sector':sector,'hash_match':h==s['sha256'],'header_match':tic==row['tic'] and sector==s['sector']})
 results.append({'sample_id':row['sample_id'],'tic':row['tic'],'identity_match':t['tic']==row['tic'] and t['gaia_dr3']==row['gaia_dr3'] and t['gaia']['source_id']==row['gaia_dr3'],'sources':checks})
(p/'helper-hash-audit.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8');print(json.dumps(results))
