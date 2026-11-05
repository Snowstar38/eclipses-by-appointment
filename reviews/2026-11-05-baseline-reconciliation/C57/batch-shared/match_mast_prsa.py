"""Exact identity and full-table five-arcsecond matches; other scopes unknown."""
import csv,hashlib,json
from pathlib import Path
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
W=Path(__file__).resolve().parent;O=W/'catalogue-archives'
p=O/'mast-prsa.csv';receipt=json.loads((O/'mast-prsa.csv.receipt.json').read_text())
assert receipt['status']=='success' and hashlib.sha256(p.read_bytes()).hexdigest()==receipt['sha256']
rows=list(csv.DictReader(p.open(encoding='utf-8-sig')));assert len(rows)==4584
coords=SkyCoord(np.array([float(r['ra']) for r in rows])*u.deg,np.array([float(r['dec']) for r in rows])*u.deg)
assert all(any(r['tess_id']==tic for r in rows) for tic in ['185259483','284613090','56912737'])
qpath=W/'remaining_cached/shared-catalogues/queue.csv'
queue=list(csv.DictReader(qpath.open(encoding='utf-8-sig')));matches=[]
for q in queue:
    c=SkyCoord(float(q['ra'])*u.deg,float(q['dec'])*u.deg);sep=c.separation(coords).arcsec
    found=[dict(row=r,separation_arcsec=float(s),exact_tic=r['tess_id']==q['tic']) for r,s in zip(rows,sep) if s<=5 or r['tess_id']==q['tic']]
    matches.append(dict(tic=q['tic'],gaia_dr3=q['gaia_dr3'],matches=found,status='prior EB aperture identity' if any(x['exact_tic'] for x in found) else 'nearby prior EB' if found else 'no match in Prsa2022 full table'))
out=dict(source_url=receipt['url'],source_sha256=receipt['sha256'],records=4584,unique_keys='tess_id,signal_id',queue_sha256=hashlib.sha256(qpath.read_bytes()).hexdigest(),radius_arcsec=5,controls=['185259483','284613090','56912737'],caveat='Published TIC signal identity and J2000 five-arcsecond cone only; signal_id can describe background or multiple clocks. No claims of other-catalogue clearance. Compare periods/source where relevant.',results=matches)
(O/'remaining75-prsa-matches.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for m in matches:
    if m['matches']:print(m['tic'],m['status'],[(x['row']['tess_id'],x['row']['period'],round(x['separation_arcsec'],3)) for x in m['matches']])
