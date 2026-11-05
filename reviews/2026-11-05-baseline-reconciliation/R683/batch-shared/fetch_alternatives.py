import concurrent.futures,csv,hashlib,json,urllib.parse,urllib.request
from pathlib import Path
from astropy.io import fits
here=Path(__file__).resolve().parent
rows={r['tic']:r for r in csv.DictReader((here/'queue.csv').open())}
caom=json.loads((here/'alternative-caom-response.json').read_text())['data']
choice={'24668377':('TESS-SPOC',33),'150465032':('TESS-SPOC',34),
        '331650047':('TESS-SPOC',79),'384744604':('TESS-SPOC',39),
        '109560492':('TARS',88)}
def fetch(tic):
    prov,sector=choice[tic]
    matches=[r for r in caom if r['target_name']==tic and r['provenance_name']==prov and r['sequence_number']==sector and r.get('dataURL','').endswith('lc.fits')]
    if len(matches)!=1:return dict(tic=tic,error=f'{len(matches)} CAOM matches')
    row=matches[0];url='https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':row['dataURL']})
    out=dict(tic=tic,sector=sector,provenance=prov,caom_row=row,url=url)
    try:
        with urllib.request.urlopen(url,timeout=120) as h:raw=h.read(50_000_001)
        if len(raw)>50_000_000:raise ValueError('file size cap')
        path=here/tic/f'alt-{prov}-s{sector:03d}.fits';path.write_bytes(raw)
        with fits.open(path) as h:
            hdr=h[0].header
            identity={key:str(hdr.get(key)) for key in ['TICID','TIC_ID','SECTOR','OBJECT','TELESCOP']}
            columns=h[1].columns.names
        if str(tic) not in (identity['TICID'],identity['TIC_ID'],identity['OBJECT'].removeprefix('TIC ')):
            raise ValueError('FITS TIC identity mismatch '+str(identity))
        if identity['SECTOR']!='None' and int(identity['SECTOR'])!=sector:raise ValueError('sector mismatch '+str(identity))
        out.update(path=str(path),sha256=hashlib.sha256(raw).hexdigest(),fits_identity=identity,columns=columns,status='ok')
    except Exception as e:out.update(status='error',error=repr(e))
    return out
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:result=list(pool.map(fetch,choice))
(here/'alternative-downloads.json').write_text(json.dumps(result,indent=2))
for r in result:print(r['tic'],r['provenance'],r['sector'],r['status'],r.get('error',''),flush=True)
