import json,hashlib,requests
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent
P=json.loads((B.parent.parent/'fresh-band-extra500'/'population.json').read_text())['targets']
out=[]
for tic in ('12319637','55662895','141428309','144157102','149477061','149847663','168983144'):
 t=P[tic];r={'tic':tic,'checked_utc':datetime.now(timezone.utc).isoformat(),'qlp_all_sectors':[x[0] for x in t['qlp_all']]}
 try:
  resp=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/sector',params={'ra':t['ra'],'dec':t['dec']},timeout=35)
  r.update(url=resp.url,status=resp.status_code,response_sha256=hashlib.sha256(resp.content).hexdigest())
  resp.raise_for_status();r['response']=resp.json();r['tesscut_sectors']=[int(x['sector']) for x in r['response']['results']]
 except Exception as e:r['error']=str(e)
 out.append(r);print(tic,r.get('tesscut_sectors'),r.get('error'),flush=True)
(B/'lead-current-sector-inventory.json').write_text(json.dumps(out,indent=2),encoding='utf8')



