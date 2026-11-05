"""Primary Prsa2022 catalogue alternate host linked by MAST's HLSP page."""
import csv,datetime,hashlib,json,requests
from pathlib import Path
W=Path(__file__).resolve().parent;O=W/'catalogue-archives';O.mkdir(exist_ok=True)
base='https://archive.stsci.edu/hlsps/tess-ebs/hlsp_tess-ebs_tess_lcf-ffi_s0001-s0026_tess_v1.0_'
for suffix,name in [('cat.csv','mast-prsa.csv'),('readme.txt','mast-prsa-readme.txt')]:
    p=O/name;receipt=O/(name+'.receipt.json');assert not receipt.exists()
    info=dict(url=base+suffix,discovery_page='https://archive.stsci.edu/hlsp/tess-ebs',utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        r=requests.get(base+suffix,timeout=30);p.write_bytes(r.content)
        info.update(http_status=r.status_code,sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content));r.raise_for_status()
        if suffix=='cat.csv':
            rows=list(csv.DictReader(r.text.splitlines()));assert len(rows)==4584 and all(x['tess_id'].isdigit() for x in rows)
            assert len({(x['tess_id'],x['signal_id']) for x in rows})==len(rows)
            info['validated_rows']=len(rows)
        else:assert 'README file for TESS-EBs' in r.text
        info['status']='success'
    except Exception as e:info.update(status='unavailable_or_unvalidated',error=repr(e))
    receipt.write_text(json.dumps(info,indent=2)+'\n',encoding='utf-8');print(name,info['status'],info.get('bytes'),info.get('error'),flush=True)
