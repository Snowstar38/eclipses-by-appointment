import json,csv,hashlib,math
from pathlib import Path
from astropy.io import fits
b=Path('[workspace]/Astra/made/final-night-2026-11-05/fresh18/batch02');s=b.parent.parent/'fresh-band-next400';pop=json.loads((s/'population.json').read_text());rows=list(csv.DictReader((b/'queue.csv').open()));out=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
for r in rows:
 tic=r['tic'];p=pop['targets'][tic];assert r['gaia_dr3']==p['gaia']['source_id'];assert abs(float(r['gaia_G'])-float(p['gaia']['phot_g_mean_mag']))<1e-6
 sources=[]
 for ff in p['files']:
  if ff.get('status')!='success':continue
  assert sha(ff['path'])==ff['sha256']
  with fits.open(ff['path']) as h:hdr=h[0].header;assert str(hdr['TICID'])==tic;assert hdr['SECTOR']==ff['sector'];sources.append(dict(path=ff['path'],sha256=ff['sha256'],tic_header=hdr['TICID'],sector=hdr['SECTOR'],ra_header=hdr.get('RA_OBJ'),dec_header=hdr.get('DEC_OBJ')))
 out.append(dict(sample_id=r['sample_id'],tic=tic,gaia_dr3=r['gaia_dr3'],gaia_G=float(r['gaia_G']),gaia=p['gaia'],tic_ra=p['ra'],tic_dec=p['dec'],sources=sources,bulk_sha256=sha(s/'bulk-results'/f'{tic}.json'),appointment_sha256=sha(s/'appointment-results'/f'{tic}.json')))
(b/'identity-audit.json').write_text(json.dumps(dict(population_sha256=sha(s/'population.json'),downloads_sha256=sha(s/'downloads.json'),population_recorded_downloads_sha256=pop['downloads_sha256'],targets=out),indent=2));print('verified',len(out))

