"""Bounded adaptive follow-up; does not alter frozen latest-three screening."""
import concurrent.futures,hashlib,json,urllib.parse,urllib.request
from pathlib import Path
from astropy.io import fits

here=Path(__file__).resolve().parent
targets=json.loads((here.parent/'search256'/'fresh-targets-256.json').read_text())
jobs=[('331650047',59),('384744604',12),('384744604',13),('109560492',7)]
def fetch(job):
    tic,sector=job
    rows=[uri for s,uri in targets[tic]['qlp_all'] if s==sector]
    if len(rows)!=1:return dict(tic=tic,sector=sector,error='QLP product identity unavailable')
    url='https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':rows[0]})
    result=dict(tic=tic,sector=sector,uri=rows[0],url=url,
                selection_reason='older QLP product may constrain repeat cycle/alias; adaptive follow-up only')
    try:
        with urllib.request.urlopen(url,timeout=120) as response:raw=response.read(15_000_001)
        if len(raw)>15_000_000:raise ValueError('size cap')
        path=here/tic/f'older-qlp-s{sector:03d}.fits';path.write_bytes(raw)
        with fits.open(path) as h:
            hdr=h[0].header
            identity={key:str(hdr.get(key)) for key in ['TICID','TIC_ID','SECTOR','OBJECT','TELESCOP']}
            data=h[1].data
            t=data['TIME'];q=data['QUALITY']
            import numpy as np
            good=np.isfinite(t)&(q==0)
            coverage=[float(np.min(t[good])),float(np.max(t[good]))] if good.sum() else None
        if str(tic) not in (identity['TICID'],identity['TIC_ID'],identity['OBJECT'].removeprefix('TIC ')):
            raise ValueError('TIC mismatch '+str(identity))
        if identity['SECTOR']!='None' and int(identity['SECTOR'])!=sector:raise ValueError('sector mismatch')
        result.update(path=str(path),sha256=hashlib.sha256(raw).hexdigest(),
                      fits_identity=identity,q0_n=int(good.sum()),q0_btjd_span=coverage,status='ok')
    except Exception as e:result.update(status='error',error=repr(e))
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:out=list(pool.map(fetch,jobs))
(here/'older-qlp-downloads.json').write_text(json.dumps(out,indent=2))
for x in out:print(x['tic'],x['sector'],x['status'],x.get('q0_btjd_span'),x.get('error',''),flush=True)
