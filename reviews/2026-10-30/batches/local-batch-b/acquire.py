import json,os,urllib.request,urllib.parse,hashlib,csv
root=os.path.dirname(__file__); d=json.load(open(root+'/selected.json')); cap=100_000_000; total=0; rec=[]
ids=sorted(d['targets']); lists={k:d['targets'][k]['qlp'] for k in ids}
# Spread first two visits across the time baseline; then cover remaining sectors.
for k in ids:
 a=lists[k]; lists[k]=[a[0],a[-1]]+a[1:-1] if len(a)>1 else a
for rank in range(max(map(len,lists.values()))):
 for tic in ids:
  if rank>=len(lists[tic]): continue
  sec,uri=lists[tic][rank]; path=f'{root}/data/{tic}_s{sec:03}.fits'; row={'tic':tic,'sector':sec,'uri':uri,'status':'','bytes':0,'sha256':''}
  if total>=cap: row['status']='omitted_cap'; rec.append(row); continue
  url='https://mast.stsci.edu/api/v0.1/Download/file?uri='+urllib.parse.quote(uri,safe='')
  try:
   with urllib.request.urlopen(url,timeout=45) as r,open(path+'.part','wb') as f:
    while True:
     chunk=r.read(65536)
     if not chunk: break
     if total+f.tell()+len(chunk)>cap: raise ValueError('cap exceeded')
     f.write(chunk)
   os.replace(path+'.part',path); n=os.path.getsize(path); total+=n; row.update(status='ok',bytes=n,sha256=hashlib.sha256(open(path,'rb').read()).hexdigest())
  except Exception as e:
   row['status']=f'failed: {type(e).__name__}: {e}'
   if os.path.exists(path+'.part'): os.remove(path+'.part')
  rec.append(row); print(tic,sec,row['status'],row['bytes'],flush=True)
  with open(root+'/acquisition.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=rec[0].keys()); w.writeheader(); w.writerows(rec)
