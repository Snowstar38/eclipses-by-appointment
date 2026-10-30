import json,pathlib,collections,urllib.request,urllib.parse,hashlib,datetime,concurrent.futures
from astropy.io import fits
D=pathlib.Path(__file__).parent; base=D.parent; rows=json.load(open(base.parent/'shared-full-review/mast-next60.json'))['data']; jobs=[]
for p in sorted(D.glob('345589621/fit-results.json')):
 tic=p.parent.name;r=json.load(open(p));counts=collections.Counter(x['sec'] for x in r['events'] if x['status']=='fit'); choices=[x for x in rows if x['target_name']==tic and x['provenance_name'] in ('SPOC','TESS-SPOC','TARS') and x['dataURL'].endswith('_lc.fits') and counts[x['sequence_number']]>0]
 choices.sort(key=lambda x:(counts[x['sequence_number']], {'SPOC':3,'TESS-SPOC':2,'TARS':1}[x['provenance_name']]),reverse=True)
 if tic=='345589621': choices=[x for x in choices if x['sequence_number']==24]
 if choices:jobs.append((tic,choices[0]))
def fetch(job):
 tic,row=job; url='https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':row['dataURL']});path=base/'data'/f"{tic}_indep_s{row['sequence_number']:03}.fits";out=dict(row=row,url=url,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),path=str(path))
 try:
  with urllib.request.urlopen(url,timeout=90) as r: data=r.read()
  path.write_bytes(data);out['sha256']=hashlib.sha256(data).hexdigest()
  with fits.open(path) as h:
   out['header']={k:str(h[0].header.get(k)) for k in ('TICID','TIC_ID','SECTOR','OBJECT','TELESCOP')};out['columns']=h[1].columns.names
  out['status']='ok'
 except Exception as e:out['status']='error';out['error']=repr(e)
 return tic,out
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: out=dict(pool.map(fetch,jobs))
json.dump(out,open(D/'independent-alternative-manifest.json','w'),indent=2);print(json.dumps(out,indent=2))
