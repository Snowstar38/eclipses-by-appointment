import urllib.request,urllib.parse,json,pathlib,concurrent.futures
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet'); T=json.loads((D.parent/'targets-selected.json').read_text())
def task(tic):
 req={'service':'Mast.Caom.Filtered','format':'json','params':{'columns':'obsid,target_name,sequence_number,dataURL,provenance_name,obs_collection','filters':[{'paramName':'target_name','values':[tic]}]},'pagesize':5000,'page':1}
 try:
  data=urllib.parse.urlencode({'request':json.dumps(req)}).encode()
  with urllib.request.urlopen('https://mast.stsci.edu/api/v0/invoke',data,timeout=30) as r: out=r.read().decode()
 except Exception as e:out='ERROR '+repr(e)
 (D/f'{tic}_mast.json').write_text(out)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:list(x.map(task,T))
