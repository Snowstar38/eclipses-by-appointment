import json,pathlib,urllib.request,urllib.parse,concurrent.futures,hashlib,datetime
from astropy.io import fits
R=pathlib.Path(__file__).parent; targets=json.load(open(R.parent/'targets-selected.json'))
def one(item):
 tic,(sec,uri)=item; p=R/tic/f'qlp_s{sec:03}.fits'
 try:
  assert str(tic).zfill(16) in uri
  if not p.exists(): p.write_bytes(urllib.request.urlopen('https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':uri}),timeout=90).read())
  with fits.open(p) as h:
   H=h[0].header; ident={k:H.get(k) for k in ('TICID','OBJECT','SECTOR','RA_OBJ','DEC_OBJ')}; assert str(H.get('TICID'))==tic and H.get('SECTOR')==sec,(tic,sec,ident)
  return dict(tic=tic,sector=sec,uri=uri,path=str(p.relative_to(R.parent)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,identity=ident,retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 except Exception as e:return dict(tic=tic,sector=sec,uri=uri,error=repr(e))
tasks=[]
for tic,t in targets.items():
 q=t['qlp']; sel=[q[i] for i in sorted(set([0,len(q)//2,len(q)-1]))] if q else []
 tasks.extend((tic,a) for a in sel)
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex: res=list(ex.map(one,tasks))
json.dump(res,open(R/'qlp-manifest.json','w'),indent=2);print([(x['tic'],x['sector'],x.get('error','OK')) for x in res])
