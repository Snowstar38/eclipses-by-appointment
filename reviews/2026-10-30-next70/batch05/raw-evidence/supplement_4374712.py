import json,urllib.request,urllib.parse,hashlib,datetime,pathlib
from astropy.io import fits
R=pathlib.Path('.'); t=json.load(open('../targets-selected.json')); m=json.load(open('qlp-manifest.json'))
for sec,uri in t['4374712']['qlp']:
 if sec not in (44,45,46,60,71):continue
 p=R/'4374712'/f'qlp_s{sec:03}.fits'
 try:
  p.write_bytes(urllib.request.urlopen('https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':uri}),timeout=30).read())
  with fits.open(p) as h:
   H=h[0].header; ident={k:H.get(k) for k in ('TICID','OBJECT','SECTOR','RA_OBJ','DEC_OBJ')};assert H['TICID']==4374712 and H['SECTOR']==sec
  m.append(dict(tic='4374712',sector=sec,uri=uri,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,identity=ident,retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
 except Exception as e: m.append(dict(tic='4374712',sector=sec,uri=uri,error=repr(e)))
json.dump(m,open('qlp-manifest.json','w'),indent=2)
