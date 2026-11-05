"""Full static IJspeert identity-table matching with exact and 5-arcsec outcomes."""
from pathlib import Path
import csv,hashlib,json,numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
W=Path(__file__).resolve().parent;O=W/'catalogue-archives';p=O/'ijspeert-identities.csv'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
receipt=json.loads((O/'ijspeert-identity-table.receipt.json').read_text())
assert receipt['status']=='validated_full_identity_table' and sha(p)==receipt['parsed_sha256']
rows=list(csv.DictReader(p.open(encoding='utf-8')));assert len(rows)==69057
coords=SkyCoord(np.array([float(r['RAJ2000']) for r in rows])*u.deg,np.array([float(r['DEJ2000']) for r in rows])*u.deg)
bytic={r['TIC']:r for r in rows}
assert all(tic in bytic for tic in ['80452824','349978696','230130556','174303697','387268955'])
for name in ['unmatched512','remaining_cached','resolved125','next256']:
    qpath=W/name/'shared-catalogues/queue.csv';queue=list(csv.DictReader(qpath.open(encoding='utf-8-sig')));out=[]
    for q in queue:
        sep=SkyCoord(float(q['ra'])*u.deg,float(q['dec'])*u.deg).separation(coords).arcsec
        hits=[dict(row=rows[i],separation_arcsec=float(sep[i]),exact_tic=rows[i]['TIC']==q['tic'],exact_gaia=rows[i]['GaiaDR3']==q['gaia_dr3']) for i in np.flatnonzero((sep<=5)|np.array([r['TIC']==q['tic'] or r['GaiaDR3']==q['gaia_dr3'] for r in rows]))]
        paired=[h for h in hits if h['exact_tic'] and h['exact_gaia']]
        status='exact TIC and Gaia prior EB' if paired else 'identity alert requires association' if hits else 'no match in full IJspeert identity table'
        out.append(dict(tic=q['tic'],gaia_dr3=q['gaia_dr3'],status=status,matches=hits))
    artifact=dict(catalogue='J/A+A/691/A242/obaf-eb1',source_receipt='ijspeert-identity-table.receipt.json',source_sha256=sha(p),records=69057,queue_sha256=sha(qpath),radius_arcsec=5,controls=['80452824','349978696','230130556','174303697','387268955'],caveat='Static published identity table; all other catalogue scopes separate. Coordinate epoch/proper motion retained in original source context. Exact joint TIC/Gaia IDs preferred to position-only associations.',results=out)
    (O/(name+'-ijspeert-matches.json')).write_text(json.dumps(artifact,indent=2)+'\n',encoding='utf-8')
    print(name,[(r['tic'],r['status']) for r in out if r['matches']],flush=True)
