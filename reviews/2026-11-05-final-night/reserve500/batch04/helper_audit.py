import json,hashlib,pathlib,csv
from astropy.io import fits
p=pathlib.Path(r'[workspace]/Astra\made\final-night-2026-11-05\reserve500\batch04')
h=lambda f:hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()
s=json.loads((p/'lead-source-hashes.json').read_text()); out={}
for row in csv.DictReader((p/'queue.csv').open()):
 tic=row['tic']; raw=[]
 for v in s[tic]['source']:
  with fits.open(v['path']) as f: head=f[0].header; raw.append(dict(sector=v['sector'],hash_ok=h(v['path'])==v['sha256'],tic_header=str(head.get('TICID',head.get('OBJECT'))),sector_header=head.get('SECTOR')))
 rec=json.loads((p/tic/'lead-central-catalogue-receipts.json').read_text()); cat={name:h(pathlib.Path(rec['central_path'])/name)==digest for name,digest in rec['source_sha256'].items()}; loc=list((p/tic).glob('lead-localization-*.json'))[0]; l=json.loads(loc.read_text()); pix=h(p/tic/('lead-tesscut-'+str(l['event']['sector'])+'.fits'))==l['fits_sha256'];out[tic]=dict(raw=raw,catalogue_hashes=cat,pixel_hash_ok=pix,gaia=row['gaia_dr3'])
(p/'helper-hash-identity-audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
