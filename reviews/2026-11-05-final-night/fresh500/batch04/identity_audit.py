import csv,json,hashlib
from pathlib import Path
from astropy.io import fits
b=Path(__file__).resolve().parent;out=[]
for r in csv.DictReader((b/'queue.csv').open()):
 d=json.load(open(b/r['tic']/'lead-context.json'));checks=[]
 for s in d['source']:
  p=Path(s['path']);h=fits.getheader(p,0);checks.append(dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),expected_sha256=s['sha256'],sha_match=hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256'],header_tic=str(h['TICID']),tic_match=str(h['TICID'])==r['tic'],sector=h['SECTOR']))
 out.append(dict(sample_id=r['sample_id'],tic=r['tic'],gaia_dr3=r['gaia_dr3'],selection_gaia_G=float(r['gaia_G']),checks=checks))
(b/'identity-audit.json').write_text(json.dumps(out,indent=2));print(sum(len(x['checks']) for x in out),'source files validated',all(c['sha_match'] and c['tic_match'] for x in out for c in x['checks']))
