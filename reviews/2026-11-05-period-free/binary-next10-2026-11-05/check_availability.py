from pathlib import Path
import csv,json,urllib.request,concurrent.futures,datetime
W=Path(__file__).resolve().parent
def check(r):
 url=f"https://mast.stsci.edu/tesscut/api/v0.1/sector?ra={r['ra_deg']}&dec={r['dec_deg']}&radius=0&units=deg"
 packet=json.loads((W/'source-packets'/r['tic']/'sources.json').read_text(encoding='utf8'))
 cached=sorted(int(x['sector']) for x in packet['verified_files'])
 out={'sample_id':r['sample_id'],'tic':r['tic'],'url':url,'queried_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cached_sectors':cached}
 try:
  with urllib.request.urlopen(url,timeout=40) as response:
   out.update(status=response.status,response=json.load(response))
  available=sorted({int(x['sector']) for x in out['response']['results']})
  out.update(available_sectors=available,uncached_sectors=sorted(set(available)-set(cached)))
 except Exception as e:out.update(error=str(e),interpretation='Availability unknown; not an empty sector list.')
 return out
rows=list(csv.DictReader((W/'queue.csv').open(encoding='utf8')))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(check,rows))
(W/'root-availability.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf8')
for x in results:print(x['sample_id'],x.get('uncached_sectors',x.get('error')))
