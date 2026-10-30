import json, pathlib, urllib.request, hashlib, concurrent.futures, datetime
root=pathlib.Path(__file__).parent.parent
t=json.load(open(root/'targets-selected.json'))
def get(item):
 tic,sec,uri=item; url='https://mast.stsci.edu/api/v0.1/Download/file?uri='+uri; path=root/'data'/f'{tic}_s{sec:03d}.fits'
 try:
  if not path.exists():
   with urllib.request.urlopen(url,timeout=90) as r: path.write_bytes(r.read())
  b=path.read_bytes(); return dict(tic=tic,sector=sec,uri=uri,url=url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 except Exception as e:return dict(tic=tic,sector=sec,uri=uri,url=url,error=str(e))
items=[(tic,int(sec),uri) for tic,v in t.items() for sec,uri in v['qlp']]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: out=list(ex.map(get,items))
json.dump(out,open(root/'full-vet'/'qlp-manifest.json','w'),indent=2); print(len(out),sum('error' in x for x in out),flush=True)
