import json,hashlib,csv,math
from pathlib import Path
from astropy.io import fits
b=Path('Astra/made/remaining136-2026-11-01/batch01');tg=json.load(open(b.parent/'targets-selected.json'));out=[];hashes={}
for r in json.load(open(b/'measurement-source-receipts.json')):
 p=Path(r['path']);h=fits.getheader(p);tic=r['tic'];t=tg[tic];ident={k:h.get(k) for k in ['TICID','TIC_ID','OBJECT','SECTOR','RA_OBJ','DEC_OBJ']};ra=h.get('RA_OBJ');dec=h.get('DEC_OBJ');sep=math.hypot((float(ra)-float(t['ra']))*math.cos(math.radians(float(t['dec']))),float(dec)-float(t['dec']))*3600 if ra is not None else None
 out.append(dict(tic=tic,sector=r['sector'],header=ident,coordinate_separation_arcsec=sep,sha256=r['sha256'],hash_match=hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']));hashes[str(p)]=r['sha256']
for r in json.load(open(b/'terra/pixel-audit.json')):hashes.update(r['files'])
(b/'identity-check.json').write_text(json.dumps(out,indent=2));(b/'source-hashes.json').write_text(json.dumps(hashes,indent=2));print([(r['tic'],r['sector'],r['coordinate_separation_arcsec'],r['header']['TICID'],r['header']['OBJECT']) for r in out])
