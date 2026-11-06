import json,hashlib,requests,io,zipfile
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent
P=json.loads((B.parent/'fresh-band'/'population.json').read_text())['targets']
old=json.loads((B/'lead-extra-sector-receipts.json').read_text()) if (B/'lead-extra-sector-receipts.json').exists() else []
out=[]
for tic,sec in [('343187602',76),('768070',98),('768070',106),('768070',107),('768070',108),('768070',109)]:
 cached=next((x for x in old if x['tic']==tic and x['sector']==sec and 'fits_path' in x),None)
 if cached:
  out.append(cached);print(tic,sec,cached.get('fits_bytes'),'cached',flush=True);continue
 t=P[tic];r={'tic':tic,'sector':sec,'checked_utc':datetime.now(timezone.utc).isoformat()}
 try:
  resp=requests.get('https://mast.stsci.edu/tesscut/api/v0.1/astrocut',params={'ra':t['ra'],'dec':t['dec'],'x':5,'y':5,'units':'px','sector':sec},timeout=100)
  r.update(url=resp.url,status=resp.status_code,zip_sha256=hashlib.sha256(resp.content).hexdigest(),zip_bytes=len(resp.content));resp.raise_for_status()
  z=zipfile.ZipFile(io.BytesIO(resp.content));data=z.read(z.namelist()[0]);fp=B/tic/f'lead-extra-s{sec}.fits';fp.write_bytes(data)
  r.update(fits_path=str(fp),fits_sha256=hashlib.sha256(data).hexdigest(),fits_bytes=len(data))
 except Exception as e:r['error']=str(e)
 out.append(r);print(tic,sec,r.get('fits_bytes'),r.get('error'),flush=True)
(B/'lead-extra-sector-receipts.json').write_text(json.dumps(out,indent=2),encoding='utf8')
