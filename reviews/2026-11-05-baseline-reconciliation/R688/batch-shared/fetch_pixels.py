import hashlib,json,requests
from pathlib import Path
H=Path(__file__).parent
rows=json.load(open(H/'mast-availability.json'))['response']['data'];out=[]
for sec in (56,84):
    lc=next(x['dataURL'] for x in rows if x['sequence_number']==sec and x['provenance_name']=='TESS-SPOC')
    uri=lc.replace('_lc.fits','_tp.fits');p=H/f'tess-spoc-s{sec:03d}-tp.fits'
    if not p.exists():
        with requests.get('https://mast.stsci.edu/api/v0.1/Download/file',params={'uri':uri},stream=True,timeout=(10,60)) as r:
            r.raise_for_status()
            with p.open('wb') as f:
                for chunk in r.iter_content(1024*1024):f.write(chunk)
    out.append(dict(sector=sec,path=str(p),mast_uri=uri,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(H/'pixel-receipts.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
