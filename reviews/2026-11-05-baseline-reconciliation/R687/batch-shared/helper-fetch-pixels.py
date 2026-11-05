import hashlib
import io
import json
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

from astropy.io import fits

here = Path(__file__).resolve().parent
target = json.loads((here.parent / 'search256' / 'fresh-targets-256.json').read_text())['167197264']['gaia']
ra, dec = float(target['ra']), float(target['dec'])
gid = target['source_id']
receipt = {'tic': '167197264', 'gaia_source_id': gid, 'sector': 76, 'ra': ra, 'dec': dec}
try:
    query = ("SELECT TOP 300 source_id,ra,dec,phot_g_mean_mag,bp_rp,parallax FROM gaiadr3.gaia_source WHERE "
             f"CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.016666667))=1")
    gaia_url = 'https://gea.esac.esa.int/tap-server/tap/sync?' + urllib.parse.urlencode(
        {'REQUEST': 'doQuery', 'LANG': 'ADQL', 'FORMAT': 'json', 'QUERY': query})
    with urllib.request.urlopen(gaia_url, timeout=90) as response:
        raw = response.read(5_000_001)
    if len(raw) > 5_000_000: raise ValueError('Gaia size cap')
    (here / 'helper-gaia-cone-167197264.json').write_bytes(raw)
    body = json.loads(raw)
    names = [v['name'] for v in body['metadata']]
    stars = [dict(zip(names, v)) for v in body['data']]
    if len([v for v in stars if str(v['source_id']) == gid]) != 1: raise ValueError('Gaia target mismatch')
    (here / 'helper-gaia-stars-167197264.json').write_text(json.dumps(stars, indent=2))
    receipt.update(gaia_url=gaia_url, gaia_sha256=hashlib.sha256(raw).hexdigest(), n_gaia_60arcsec=len(stars))
    url = 'https://mast.stsci.edu/tesscut/api/v0.1/astrocut?' + urllib.parse.urlencode(
        {'ra': ra, 'dec': dec, 'y': 9, 'x': 9, 'units': 'px', 'sector': 76})
    with urllib.request.urlopen(url, timeout=120) as response:
        archive = response.read(100_000_001)
    if len(archive) > 100_000_000: raise ValueError('TESScut size cap')
    zipfile_obj = zipfile.ZipFile(io.BytesIO(archive))
    members = zipfile_obj.namelist()
    if len(members) != 1 or not members[0].lower().endswith('.fits'): raise ValueError(f'Unexpected members {members}')
    fits_raw = zipfile_obj.read(members[0])
    path = here / 'helper-167197264_tesscut_s076.fits'
    path.write_bytes(fits_raw)
    with fits.open(path) as h:
        header = h[1].header
        n = len(h[1].data)
    receipt.update(tesscut_url=url, tesscut_zip_sha256=hashlib.sha256(archive).hexdigest(),
                   tesscut_fits_sha256=hashlib.sha256(fits_raw).hexdigest(), fits_path=str(path),
                   archive_member=members[0], n_cadences=n,
                   fits_header_identity={k: str(header.get(k)) for k in ('TICID', 'SECTOR', 'OBJECT')}, status='ok')
except Exception as exc:
    receipt.update(status='error', error=repr(exc))
(here / 'helper-pixel-download-167197264.json').write_text(json.dumps(receipt, indent=2))
print(receipt['status'], receipt.get('n_gaia_60arcsec'), receipt.get('n_cadences'), receipt.get('error', ''))

