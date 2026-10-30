import json,pathlib,urllib.request,concurrent.futures,hashlib,zipfile,io
r=pathlib.Path(__file__).parent; targets=json.load(open(r.parent/'targets-selected.json')); raw=json.load(open(r/'raw-events.json'))
jobs=[]
for tic,x in raw.items():
 secs=[]
 for e in x['events']:
  if 'tc' in e and not e['edge'] and e['depth']>3*e['residual_rms'] and e['sector'] not in secs:secs.append(e['sector'])
 for sec in secs[:2]:jobs.append((tic,sec))
def run(job):
 tic,sec=job;d=targets[tic]; url=f"https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={d['ra']}&dec={d['dec']}&y=11&x=11&units=px&sector={sec}"; p=r/tic/f'tesscut_s{sec:03d}.zip'
 try:
  with urllib.request.urlopen(url,timeout=90) as h:b=h.read(50000001)
  if len(b)>50000000:raise Exception('size cap')
  z=zipfile.ZipFile(io.BytesIO(b));p.write_bytes(b);z.extractall(r/tic);return dict(tic=tic,sector=sec,url=url,sha256=hashlib.sha256(b).hexdigest(),members=z.namelist())
 except Exception as e:return dict(tic=tic,sector=sec,url=url,error=repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: out=list(ex.map(run,jobs))
json.dump(out,open(r/'tesscut-downloads.json','w'),indent=2);print(out,flush=True)
