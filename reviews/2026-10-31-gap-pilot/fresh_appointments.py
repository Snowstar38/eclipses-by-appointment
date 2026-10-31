"""New conjunction-first G11.5-12 pilot; no preselection using TESS outcomes."""
import csv,json,pathlib,sys,urllib.request,urllib.parse,concurrent.futures,hashlib,math
import numpy as np
O=pathlib.Path(__file__).parent;D=O/'fresh-data';D.mkdir(exist_ok=True)
sys.path.insert(0,'[local path omitted] 5.1/made/appointments');import appoint
def request(url,data=None,timeout=50):return urllib.request.urlopen(url,data,timeout=timeout).read()
def invoke(req):return json.loads(request('http[local path omitted]',urllib.parse.urlencode({'request':json.dumps(req)}).encode()))
def select(n):
 old=json.load(open('[local path omitted]'));have={v['gaia']['source_id'] for v in old.values()}
 rs=list(csv.DictReader(open('[local path omitted]')))
 eligible=sorted([r for r in rs if r['source_id'] not in have and 11.5<=float(r['phot_g_mean_mag'])<12],key=lambda r:(float(r['phot_g_mean_mag']),r['source_id']))
 selected=[r for r in eligible if not r['veb']][:n]+[r for r in eligible if r['veb']][:2]
 (O/f'fresh-preregister-{n}.json').write_text(json.dumps({'rule':f'first{n}noncontrol+first2 GaiaEBcontrols by G; Gaia20-60d, G11.5-12, absent historical targets; maximum3latestQLPsectors per target; no TESS outcomes inspected before selection','eligible':len(eligible),'selected':selected},indent=1))
 ids=','.join(r['source_id'] for r in selected)
 q='SELECT TIC,GAIA,Tmag,RAJ2000,DEJ2000 FROM "IV/39/tic82" WHERE GAIA IN ('+ids+')'
 url='http[local path omitted]'+urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q})
 # CDS TAP unavailable in prior attempt; bounded IDIA position cones with exact Gaia-ID verification.
 def match(g):
  u='http[local path omitted]'+urllib.parse.urlencode({'-source':'IV/39/tic82','-c':g['ra']+' '+g['dec'],'-c.rs':5,'-out':'TIC,GAIA,Tmag,RAJ2000,DEJ2000','-out.max':30})
  try:
   raw=request(u,timeout=20);(O/('fresh-tic-'+g['source_id']+'.tsv')).write_bytes(raw)
   lines=[l for l in raw.decode('latin1').splitlines() if l and not l.startswith('#')];head=[x.strip() for x in lines[0].split('\t')]
   rows=[dict(zip(head,[x.strip() for x in l.split('\t')])) for l in lines[3:]]
   return [r for r in rows if r.get('GAIA')==g['source_id']]
  except Exception as e:return [{'error':repr(e),'source_id':g['source_id']}]
 with concurrent.futures.ThreadPoolExecutor(6) as ex:matched=list(ex.map(match,selected))
 (O/f'fresh-match-receipts-{n}.json').write_text(json.dumps(matched,indent=1));matches={r['GAIA']:r for rows in matched for r in rows if 'GAIA' in r}
 out={}
 for g in selected:
  if g['source_id'] in matches:
   r=matches[g['source_id']];k=r['TIC'];out[k]={'ID':int(k),'gaia':g,'ra':float(r['RAJ2000']),'dec':float(r['DEJ2000']),'control':bool(g['veb']),'qlp':[]}
 req={'service':'Mast.Caom.Filtered','format':'json','pagesize':50000,'page':1,'params':{'columns':'target_name,sequence_number,dataURL,provenance_name','filters':[{'paramName':'provenance_name','values':['QLP']},{'paramName':'target_name','values':list(out)}]}}
 caom=invoke(req);(O/f'fresh-caom-{n}.json').write_text(json.dumps(caom,indent=1))
 for r in caom.get('data',[]):
  k=r['target_name'].lstrip('0')
  if k in out and r.get('dataURL','').endswith('.fits'):out[k]['qlp'].append([int(r['sequence_number']),r['dataURL']])
 for k,v in out.items():
  v['qlp_all']=sorted(v['qlp']);v['qlp']=sorted({s:u for s,u in v['qlp']}.items())[-3:]
 (O/f'fresh-targets-{n}.json').write_text(json.dumps(out,indent=1));print('matched',len(out),'QLP',sum(bool(v['qlp']) for v in out.values()),flush=True)
def run(n):
 tg=json.load(open(O/f'fresh-targets-{n}.json'));jobs=[(k,s,u) for k,v in tg.items() for s,u in v['qlp']]
 def get(job):
  k,s,u=job;p=D/f'{k}_s{s:03d}.fits'
  if p.exists():return {'tic':k,'sector':s,'status':'cached'}
  try:p.write_bytes(request('http[local path omitted]'+u,timeout=55));return {'tic':k,'sector':s,'status':'downloaded','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  except Exception as e:return {'tic':k,'sector':s,'status':'unavailable','error':repr(e)}
 with concurrent.futures.ThreadPoolExecutor(6) as ex:downloads=list(ex.map(get,jobs))
 (O/f'fresh-downloads-{n}.json').write_text(json.dumps(downloads,indent=1));appoint.D=str(D);appoint.NULL_MODE='overlap'
 with open(O/f'fresh-results-{n}.jsonl','w') as fo:
  for k,v in tg.items():
   try:r=appoint.star(k,v,nnull=20)
   except Exception as e:r={'tic':k,'err':repr(e)}
   fo.write(json.dumps(r)+'\n');fo.flush();print(k,r.get('best'),r.get('z'),r.get('err'),flush=True)
if __name__=='__main__':
 n=int(sys.argv[2]);select(n) if sys.argv[1]=='select' else run(n)
