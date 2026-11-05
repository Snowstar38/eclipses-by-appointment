from pathlib import Path
import requests,json,hashlib,datetime
O=Path(__file__).resolve().parent/'catalogue-archives';p=O/'asassn-metadata-probe.tsv';rp=O/'asassn-metadata-probe.receipt.json';assert not rp.exists()
d=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),endpoint='https://vizier.cfa.harvard.edu/viz-bin/asu-tsv',params={'-source':'II/366/catv2021','-out.max':'1'},scope='metadata/one row only; no target clearance')
try:
 r=requests.get(d['endpoint'],params=d['params'],timeout=20);p.write_bytes(r.content);d.update(url=r.url,http_status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest());r.raise_for_status();d['status']='response_requires_inspection'
except Exception as e:d.update(status='failed',error=repr(e))
rp.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8');print(json.dumps(d))
