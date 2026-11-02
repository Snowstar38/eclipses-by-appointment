from pathlib import Path
import json,csv,hashlib,numpy as np
from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.units as u
B=Path(__file__).parent;tg=json.load(open(B.parent/'targets-selected.json'));download=json.load(open(B/'download-receipts.json'));out=[]
for rec in json.load(open(B/'measurement-source-receipts.json')):
 p=Path(rec['path']);tic=rec['tic'];t=tg[tic]
 with fits.open(p) as h:
  a=h[0].header;head={k:a.get(k) for k in ['TICID','OBJECT','SECTOR','RA_OBJ','DEC_OBJ']}
 sep=SkyCoord(head['RA_OBJ']*u.deg,head['DEC_OBJ']*u.deg).separation(SkyCoord(t['ra']*u.deg,t['dec']*u.deg)).arcsec
 sh=hashlib.sha256(p.read_bytes()).hexdigest();prior=next(r for r in download if r['tic']==tic and r['sector']==rec['sector'])
 assert head['TICID']==int(tic) and head['SECTOR']==rec['sector'] and sep<1 and sh==rec['sha256']==prior['sha256']
 out.append(dict(tic=tic,sector=rec['sector'],header=head,coordinate_separation_arcsec=sep,sha256=sh,hash_match=True))
(B/'identity-check.json').write_text(json.dumps(out,indent=2))
srcs=[B.parent/'targets-selected.json',B.parent/'shared-catalogues/gaia-nss-full.csv',Path('local-source/Fable 5/made/sb1-scale/search.jsonl'),Path('local-source/Fable 5/made/sb1-scale/c7-sapdepth.json')]
(B/'source-hashes.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in srcs},indent=2))
