import json,requests
from pathlib import Path
B=Path(__file__).resolve().parent
for name,ra,dec,radius in [('q011',9.002209629788853,-28.267882554400508,.035),('q015',306.565,54.999,.02)]:
 q={'service':'Mast.Catalogs.GaiaDR3.Cone','params':{'ra':ra,'dec':dec,'radius':radius},'format':'json','pagesize':1000,'page':1}
 r=requests.get('https://mast.stsci.edu/api/v0/invoke',params={'request':json.dumps(q)},timeout=30);r.raise_for_status();d=r.json();assert d['status']=='COMPLETE';(B/f'helper-{name}-gaia.json').write_text(r.text,encoding='utf-8')
