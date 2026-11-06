import requests,json,hashlib
from pathlib import Path
p=Path(__file__).parent
q={'service':'Mast.Catalogs.Tic.Cone','params':{'ra':269.339603329087,'dec':56.7263391016778,'radius':90/3600},'format':'json','pagesize':5000,'page':1}
r=requests.post('https://mast.stsci.edu/api/v0/invoke',data={'request':json.dumps(q)},timeout=40);r.raise_for_status();(p/'232-tic-cone.json').write_text(r.text,encoding='utf8')
