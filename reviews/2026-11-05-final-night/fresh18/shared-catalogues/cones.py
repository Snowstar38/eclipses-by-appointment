import json,csv,pathlib,hashlib,urllib.request,urllib.parse,datetime,concurrent.futures,time
w=pathlib.Path(__file__).parent; parent=w.parent
targets=json.load(open(w/'targets.json')); (w/'cones').mkdir(exist_ok=True)

def get(job):
 key,table,t=job;url='https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':table,'-c':str(t['ra'])+' '+str(t['dec']),'-c.rs':60,'-out.max':500,'-out.all':'','-out.add':'_r'});rec={'tic':t['tic'],'label':t['label'],'scope':t['scope'],'catalogue':key,'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 astronomy-catalogue-audit'}),timeout=18).read(2000001);txt=raw.decode('utf-8-sig'); assert len(raw)<2000000 and 'VizieR Astronomical Server' in txt and '#ERROR' not in txt and '#RESOURCE=' in txt
  lines=[x for x in txt.splitlines() if x and not x.startswith('#')];assert not lines or ('_r' in lines[0] and len(lines)>=3 and len(lines)-3<500)
  path=w/'cones'/f"{key}-{t['tic']}.tsv";path.write_bytes(raw);rec.update(status='success',rows=max(0,len(lines)-3),sha256=hashlib.sha256(raw).hexdigest(),file=str(path))
 except Exception as e:rec.update(status='unknown',error=repr(e))
 return rec
out=[]; failures=0
for start in range(0,len(targets),4):
 jobs=[(k,tb,t) for t in targets[start:start+4] for k,tb in [('vsx','B/vsx/vsx'),('asassn','II/366/catv2021')]]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:batch=list(ex.map(get,jobs))
 out.extend(batch);(w/'cone-receipts.json').write_text(json.dumps(out,indent=2));print(start,len(out),sum(x['status']=='unknown' for x in batch),flush=True)
 failures=failures+1 if all(x['status']=='unknown' for x in batch) else 0
 if failures>=2:break
 time.sleep(.5)
