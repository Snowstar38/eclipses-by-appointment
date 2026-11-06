import csv,json,urllib.request,urllib.parse,datetime,hashlib,concurrent.futures,pathlib
w=pathlib.Path(__file__).parent
old=list(csv.DictReader(open('Astra/made/binary-next40-2026-11-05/queue.csv',encoding='utf8')))
coords=lambda i:next(x['ra_deg']+' '+x['dec_deg'] for x in old if x['sample_id']==i)
items={'vsx':('B/vsx/vsx',coords('F008'),60),'asassn':('II/366/catv2021',coords('F006'),60),'kostov3':('J/ApJS/279/50/table3','219.00555469 -27.56944137',5),'kostov4':('J/ApJS/279/50/table4','219.04301800 -24.33205152',5)}
def probe(job):
 host,key=job;table,c,rad=items[key]; url='https://'+host+'/viz-bin/asu-tsv?'+urllib.parse.urlencode({'-source':table,'-c':c,'-c.rs':rad,'-out.max':100,'-out.all':'','-out.add':'_r'});rec={'url':url,'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'timeout_s':12}
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 astronomy-catalogue-audit'}),timeout=12).read(500001);(w/(key+'-'+host+'-post.tsv')).write_bytes(raw);txt=raw.decode('utf-8-sig');lines=[x for x in txt.splitlines() if x and not x.startswith('#')];assert len(raw)<=500000 and table in txt and '#ERROR' not in txt and len(lines)>=4 and '_r' in lines[0];rec.update(status='success',rows=len(lines)-3,sha256=hashlib.sha256(raw).hexdigest())
 except Exception as e:rec.update(status='unknown',error=repr(e))
 return key+'-'+host,rec
jobs=[(h,k) for h in ['vizier.cfa.harvard.edu'] for k in items]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:out=dict(ex.map(probe,jobs))
(w/'vizier-controls-post.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))

