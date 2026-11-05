import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path
from astropy.io import fits

here = Path(__file__).resolve().parent
tic = '155346713'
rows = json.loads((here / 'alternative-caom-155346713.json').read_text())['data']
out = []
for provenance in ('TESS-SPOC', 'TGLC'):
    matches = [r for r in rows if r['target_name'] == tic and r['provenance_name'] == provenance and
               r['sequence_number'] == 7 and r.get('dataURL', '').endswith('lc.fits')]
    receipt = {'tic': tic, 'sector': 7, 'provenance': provenance, 'caom_rows': matches}
    try:
        if len(matches) != 1:
            raise ValueError('Nonunique CAOM row')
        url = 'https://mast.stsci.edu/api/v0.1/Download/file?' + urllib.parse.urlencode({'uri': matches[0]['dataURL']})
        with urllib.request.urlopen(url, timeout=120) as response:
            raw = response.read(50_000_001)
        if len(raw) > 50_000_000:
            raise ValueError('FITS exceeds size cap')
        path = here / f'{tic}_s007_{provenance}.fits'
        path.write_bytes(raw)
        with fits.open(path) as h:
            hdr = h[0].header
            identity = {k: str(hdr.get(k)) for k in ('TICID', 'TIC_ID', 'SECTOR', 'OBJECT', 'TELESCOP')}
            columns = h[1].columns.names
        if tic not in (identity['TICID'], identity['TIC_ID'], identity['OBJECT'].removeprefix('TIC ')):
            raise ValueError(f'TIC identity mismatch: {identity}')
        if identity['SECTOR'] != 'None' and int(identity['SECTOR']) != 7:
            raise ValueError(f'Sector mismatch: {identity}')
        receipt.update(status='ok', path=str(path), sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw),
                       fits_identity=identity, columns=columns)
    except Exception as exc:
        receipt.update(status='error', error=repr(exc))
    out.append(receipt)
    print(provenance, receipt['status'], receipt.get('error', ''), flush=True)
(here / 'alternative-downloads-155346713.json').write_text(json.dumps(out, indent=2))
