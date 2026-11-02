from pathlib import Path
import json,hashlib,csv, numpy as np
from astropy.io import fits
b=Path('local-source/Astra/made/remaining136-2026-11-01/batch09');tg=json.load(open(b.parent/'targets-selected.json'));out=[];sources={}
for r in csv.DictReader(open(b/'queue.csv')):
 tic=r['tic'];g=json.load(open(b/tic/'fresh-pixels/gaia.json'));target=tg[tic];assert str(g['src'][0]['source_id'])==str(target['gaia']['source_id']);m=json.load(open(b/tic/'measurements.json'));ql=[]
 for s in m['sources']:
  p=Path(s['path']);sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha==s['sha256'];sources[str(p)]=sha
  with fits.open(p) as h:
   hd=h[0].header;assert str(hd['TICID'])==tic and hd['SECTOR']==s['sector'];ql.append(dict(path=str(p),ticid=hd['TICID'],sector=hd['SECTOR'],ra=hd['RA_OBJ'],dec=hd['DEC_OBJ']))
 d=json.load(open(b/tic/'fresh-pixels/diff_fresh.json'));cut=Path('local-source/sky/data/sb1-scale-c3')/('vet'+tic)/('tesscut_s%03d.fits'%d['sector']);sources[str(cut)]=hashlib.sha256(cut.read_bytes()).hexdigest()
 with fits.open(cut) as h:hdr=dict(h[0].header);sector=h[0].header.get('SECTOR',h[1].header.get('SECTOR'));assert sector==d['sector']
 out.append(dict(tic=tic,gaia_source_id=g['src'][0]['source_id'],qlp_identity=ql,cutout_sector=sector,cutout_path=str(cut),cutout_note='No TIC identity in TESScut; target Gaia coordinate projected by cutout WCS, exact source ID checked.'))
 for p in (Path('local-source/Fable 5/made/sb1-scale/diffimg')/tic).glob('*'):sources[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['c7-sapdepth.json','c8-sapdepth.json','search.jsonl']: 
 p=Path('local-source/Fable 5/made/sb1-scale')/name;sources[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
for p in [b.parent/'targets-selected.json',b.parent/'shared-catalogues/gaia-nss-full.csv']:sources[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
json.dump(out,open(b/'identity-check.json','w'),indent=2);json.dump(sources,open(b/'source-hashes.json','w'),indent=2)
