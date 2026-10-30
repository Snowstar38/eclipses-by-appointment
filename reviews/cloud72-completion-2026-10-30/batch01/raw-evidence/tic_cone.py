import json,pathlib,urllib.request,urllib.parse,concurrent.futures
r=pathlib.Path(__file__).parent;ts=json.load(open(r.parent/'targets-selected.json'))
def run(item):
 tic,t=item;req={'service':'Mast.Catalogs.Filtered.Tic.Position','params':{'ra':t['ra'],'dec':t['dec'],'radius':0.0166667,'columns':'ID,ra,dec,Tmag,GAIAmag,GAIA','filters':[]},'format':'json','pagesize':5000,'page':1};p=urllib.parse.urlencode({'request':json.dumps(req)}).encode()
 try:
  with urllib.request.urlopen('https://mast.stsci.edu/api/v0/invoke',p,timeout=50) as h:b=h.read()
  (r/tic/'tic-cone.json').write_bytes(b);return (tic,len(json.loads(b)['data']))
 except Exception as e:return (tic,repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:res=list(x.map(run,ts.items()))
json.dump(res,open(r/'tic-cone-status.json','w'),indent=2);print(res)
