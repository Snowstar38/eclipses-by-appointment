import hashlib, io, json, time, urllib.parse, urllib.request, zipfile
from pathlib import Path

here=Path(__file__).resolve().parent
failed=[r for r in json.loads((here/'pixel-download-receipts.json').read_text()) if r.get('error')]
out=[]
for old in failed:
    tic=old['tic'];sector=old['sector'];result=dict(tic=tic,sector=sector,attempts=[])
    for size in (11,11,15):
        u=old['tesscut_url'].replace('y=15&x=15',f'y={size}&x={size}')
        try:
            with urllib.request.urlopen(u,timeout=120) as h:raw=h.read(100_000_001)
            if len(raw)>100_000_000:raise ValueError('size cap')
            z=zipfile.ZipFile(io.BytesIO(raw));names=z.namelist()
            if len(names)!=1 or not names[0].lower().endswith('.fits'):raise ValueError(str(names))
            data=z.read(names[0]);path=here/tic/'pixels'/f'tesscut_s{sector:03d}.fits';path.write_bytes(data)
            result['attempts'].append(dict(url=u,ok=True,zip_sha256=hashlib.sha256(raw).hexdigest(),
                                           fits_sha256=hashlib.sha256(data).hexdigest(),path=str(path)))
            break
        except Exception as e:
            result['attempts'].append(dict(url=u,error=repr(e)))
            time.sleep(2)
    out.append(result);print(tic,result['attempts'][-1],flush=True)
(here/'pixel-retries.json').write_text(json.dumps(out,indent=2))
