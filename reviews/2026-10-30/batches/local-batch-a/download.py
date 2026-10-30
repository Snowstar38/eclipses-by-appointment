import json,os,urllib.request,hashlib,time,concurrent.futures
T=json.load(open('targets-selected.json')); jobs=[(k,s,u) for k,v in T.items() for s,u in v['qlp']]; os.makedirs('data',exist_ok=True)
assert len({(k,s) for k,s,u in jobs})==len(jobs), 'duplicate target-sector entries'
assert len(jobs)*3000000<100000000, 'prospective total file budget exceeded'
def get(j):
 k,s,u=j; p=f'data/{k}_s{s:03d}.fits'; url='https://mast.stsci.edu/api/v0.1/Download/file?uri='+u
 for attempt in range(2):
  try:
   if not os.path.exists(p):
    with urllib.request.urlopen(url,timeout=30) as response,open(p+'.part','wb') as f:
     while True:
      b=response.read(262144)
      if not b: break
      f.write(b)
      if f.tell()>3000000: raise ValueError('single-file 3MB cap')
    os.replace(p+'.part',p)
   raw=open(p,'rb').read(); return {'tic':k,'sector':s,'uri':u,'url':url,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
  except Exception as e:
   if os.path.exists(p+'.part'): os.remove(p+'.part')
   error=str(e)
 return {'tic':k,'sector':s,'uri':u,'error':error}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: results=list(ex.map(get,jobs))
json.dump(results,open('downloads.json','w'),indent=2)
print('files',len(results),'bytes',sum(x.get('bytes',0) for x in results),'failures',[x for x in results if 'error' in x])
