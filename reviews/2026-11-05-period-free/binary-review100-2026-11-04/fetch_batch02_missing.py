from pathlib import Path
import json,requests,hashlib,datetime
from astropy.io import fits
W=Path(__file__).resolve().parent;O=W/'missing-coverage';O.mkdir(exist_ok=True)
jobs={'231694897':[105,103,1],'323818250':[10,65]}
req={'service':'Mast.Caom.Filtered','format':'json','params':{'columns':'target_name,sequence_number,dataURL,provenance_name','filters':[{'paramName':'provenance_name','values':['QLP']},{'paramName':'target_name','values':list(jobs)}]},'pagesize':5000,'page':1}
(O/'qlp-request.json').write_text(json.dumps(req,indent=2)+'\n',encoding='utf8')
r=requests.post('https://mast.stsci.edu/api/v0/invoke',data={'request':json.dumps(req)},timeout=(10,40))
(O/'qlp-response.json').write_bytes(r.content);r.raise_for_status();x=r.json()
assert x['status']=='COMPLETE' and x['paging']['pagesFiltered']<=1
sha=lambda b:hashlib.sha256(b).hexdigest()
receipts=[]
for tic,sectors in jobs.items():
 for sector in sectors:
  rr={'tic':tic,'sector':sector,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  products=[p for p in x['data'] if str(p['target_name']).lstrip('0')==tic and int(p['sequence_number'])==sector and str(p.get('dataURL','')).endswith('.fits')]
  rr['listed_products']=products
  if len(products)!=1:rr['status']='no_unique_listed_qlp'
  else:
   try:
    uri=products[0]['dataURL'];d=requests.get('https://mast.stsci.edu/api/v0.1/Download/file',params={'uri':uri},timeout=(10,40));d.raise_for_status()
    p=W/'batch02'/tic/f'missing-sector-s{sector:03d}.fits';tmp=p.with_suffix('.part');tmp.write_bytes(d.content)
    with fits.open(tmp) as hd:assert int(hd[0].header['TICID'])==int(tic) and int(hd[0].header['SECTOR'])==sector
    tmp.replace(p);rr.update(status='ok',path=str(p),sha256=sha(d.content),bytes=len(d.content),uri=uri)
   except Exception as e:rr.update(status='unavailable',error=repr(e))
  receipts.append(rr);(O/'download-receipts.json').write_text(json.dumps({'request':req,'response_sha256':sha(r.content),'receipts':receipts},indent=2)+'\n',encoding='utf8')
  print(tic,sector,rr['status'],flush=True)
