"""Retrieve bounded WCS cutouts for source attribution of repeated Q011/Q015 losses."""
import csv, hashlib, json
from pathlib import Path
import requests
B=Path(__file__).resolve().parent
rows={r['sample_id']:r for r in csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline=''))}
for sid,sectors in {'Q011':[29,69],'Q015':[41,55,82]}.items():
    r=rows[sid]; out=B/r['tic']/'cutouts';out.mkdir(exist_ok=True); receipts=[]
    for sec in sectors:
        args=dict(ra=float(r['ra_deg']),dec=float(r['dec_deg']),x=11,y=11,sector=sec)
        reply=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params=args,timeout=120)
        reply.raise_for_status()
        if reply.headers.get('content-type','').split(';')[0]!='application/zip':raise RuntimeError((sec,reply.text[:300]))
        fp=out/f's{sec:03d}.zip';fp.write_bytes(reply.content)
        receipts.append(dict(sector=sec,url=reply.url,path=str(fp),size=len(reply.content),sha256=hashlib.sha256(reply.content).hexdigest()))
        print(sid,sec,len(reply.content),flush=True)
    (out/'receipts.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
