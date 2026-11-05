import csv,hashlib,json,math
from datetime import datetime,timezone
from pathlib import Path
import requests
B=Path(__file__).resolve().parent
rows={r['tic']:r for r in csv.DictReader((B/'queue.csv').open(encoding='utf8'))}
out={}
for tic in ('280051953','295351347','72497715'):
 q=rows[tic];ra=float(q['ra_deg']);dec=float(q['dec_deg']);payload={'service':'Mast.Catalogs.Filtered.Tic.Position','params':{'columns':'*','filters':[],'ra':ra,'dec':dec,'radius':.025},'format':'json','pagesize':1000,'page':1}
 try:
  response=requests.post('https://mast.stsci.edu/api/v0/invoke',data={'request':json.dumps(payload)},timeout=25);response.raise_for_status();body=response.json();assert body['status']=='COMPLETE'
  stars=[]
  for x in body['data']:
   dra=(float(x['ra'])-ra)*math.cos(math.radians(dec));ddec=float(x['dec'])-dec;sep=math.hypot(dra,ddec)*3600
   stars.append(dict(tic=x['ID'],gaia_dr2=x.get('GAIA'),ra_deg=x['ra'],dec_deg=x['dec'],separation_arcsec=sep,tmag=x.get('Tmag'),gaia_mag=x.get('GAIAmag'),contamination=x.get('contratio')))
  stars.sort(key=lambda x:x['separation_arcsec']);target=next((x for x in stars if str(x['tic'])==tic),None)
  for x in stars:
   if target and x['tmag'] is not None and target['tmag'] is not None:x['approx_t_flux_ratio_to_target']=10**(-.4*(float(x['tmag'])-float(target['tmag'])))
  out[tic]=dict(checked_utc=datetime.now(timezone.utc).isoformat(),api='MAST TIC Position',http_status=response.status_code,request=payload,response_sha256=hashlib.sha256(response.content).hexdigest(),target=target,stars=stars)
  print(tic,len(stars),[(z['tic'],round(z['separation_arcsec'],1),z['tmag'],round(z.get('approx_t_flux_ratio_to_target',-1),4)) for z in stars[:12]],flush=True)
 except Exception as e:
  out[tic]=dict(checked_utc=datetime.now(timezone.utc).isoformat(),api='MAST TIC Position',request=payload,error=repr(e));print(tic,'ERROR',repr(e),flush=True)
(B/'lead-neighbors.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
