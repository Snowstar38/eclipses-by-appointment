"""Bounded official Gaia DR3 cone and TESScut FFI cutout retrieval for batch02."""
import concurrent.futures, csv, hashlib, io, json, urllib.parse, urllib.request, zipfile
from pathlib import Path

here=Path(__file__).resolve().parent
rows=list(csv.DictReader((here/'queue.csv').open()))
sectors={'24668377':98,'150465032':61,'331650047':79,
         '384744604':101,'109560492':88}

def fetch(row):
    tic=row['tic'];out=here/tic/'pixels';out.mkdir(exist_ok=True)
    ra=float(row['ra_deg']);dec=float(row['dec_deg']);sector=sectors[tic]
    query=("SELECT TOP 300 source_id,ra,dec,phot_g_mean_mag,bp_rp,parallax "
           "FROM gaiadr3.gaia_source WHERE "
           f"CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.016666667))=1")
    params=urllib.parse.urlencode(dict(REQUEST='doQuery',LANG='ADQL',FORMAT='json',QUERY=query))
    gaia_url='https://gea.esac.esa.int/tap-server/tap/sync?'+params
    receipt=dict(tic=tic,sector=sector,gaia_url=gaia_url)
    try:
        with urllib.request.urlopen(gaia_url,timeout=90) as response: data=response.read(5_000_001)
        if len(data)>5_000_000:raise ValueError('Gaia result exceeds cap')
        (out/'gaia-response.json').write_bytes(data)
        body=json.loads(data); names=[v['name'] for v in body['metadata']]
        stars=[dict(zip(names,v)) for v in body['data']]
        target=[v for v in stars if str(v['source_id'])==row['gaia_dr3_source_id']]
        if len(target)!=1:raise ValueError(f'Gaia target identity mismatch: {len(target)}')
        (out/'gaia-stars.json').write_text(json.dumps(stars,indent=2))
        receipt.update(gaia_sha256=hashlib.sha256(data).hexdigest(),n_gaia_60arcsec=len(stars))
        cut_url='https://mast.stsci.edu/tesscut/api/v0.1/astrocut?'+urllib.parse.urlencode(dict(ra=ra,dec=dec,y=15,x=15,units='px',sector=sector))
        receipt['tesscut_url']=cut_url
        with urllib.request.urlopen(cut_url,timeout=120) as response: raw=response.read(100_000_001)
        if len(raw)>100_000_000:raise ValueError('TESSCut exceeds cap')
        z=zipfile.ZipFile(io.BytesIO(raw));names=z.namelist()
        if len(names)!=1 or not names[0].lower().endswith('.fits'):raise ValueError(f'unexpected archive members {names}')
        fits_bytes=z.read(names[0]);path=out/f'tesscut_s{sector:03d}.fits';path.write_bytes(fits_bytes)
        receipt.update(tesscut_zip_sha256=hashlib.sha256(raw).hexdigest(),
                       tesscut_fits_sha256=hashlib.sha256(fits_bytes).hexdigest(),
                       tesscut_fits_path=str(path),archive_member=names[0])
    except Exception as e:receipt['error']=repr(e)
    return receipt

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    receipts=list(pool.map(fetch,rows))
(here/'pixel-download-receipts.json').write_text(json.dumps(receipts,indent=2))
for item in receipts:print(item['tic'],item.get('n_gaia_60arcsec'),item.get('error','OK'),flush=True)
