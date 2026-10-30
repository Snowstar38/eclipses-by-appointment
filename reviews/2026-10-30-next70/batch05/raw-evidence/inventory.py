import json,pathlib,urllib.request,urllib.parse,concurrent.futures
R=pathlib.Path(__file__).parent;ids=list(json.load(open(R/'raw-events.json')))
def task(tic):
 req={'service':'Mast.Caom.Filtered','format':'json','params':{'columns':'obsid,target_name,sequence_number,dataURL,provenance_name,obs_collection','filters':[{'paramName':'target_name','values':[tic]}]},'pagesize':5000,'page':1};data=urllib.parse.urlencode({'request':json.dumps(req)}).encode()
 try:
  with urllib.request.urlopen('https://mast.stsci.edu/api/v0/invoke',data,timeout=40) as h:out=h.read().decode()
  (R/tic/'mast-products.json').write_text(out);d=json.loads(out); pro=[(x.get('provenance_name'),x.get('sequence_number')) for x in d.get('data',[]) if x.get('provenance_name') in ['SPOC','TESS-SPOC','TARS'] and str(x.get('dataURL','')).endswith('_lc.fits')];return tic,pro
 except Exception as e:return tic,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:res=list(ex.map(task,ids))
print(res)
