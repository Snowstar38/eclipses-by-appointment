import json,pathlib,urllib.request,urllib.parse,concurrent.futures
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet')
def work(p):
 tic=p.stem.split('_')[0]; a=json.loads(p.read_text()); rows=[x for x in a['data'] if x['provenance_name']=='TESS-SPOC']; r=rows[-1] if tic=='270181578' else rows[0]; url='https://mast.stsci.edu/api/v0.1/Download/file?'+urllib.parse.urlencode({'uri':r['dataURL']}); dest=D/(tic+'_indep.fits')
 try:
  with urllib.request.urlopen(url,timeout=60) as f:
   size=f.headers.get('Content-Length'); print(tic,r['sequence_number'],size,flush=True)
   if size and int(size)>20000000: return
   data=f.read(20000001)
   if len(data)<=20000000: dest.write_bytes(data)
 except Exception as e:print(tic,repr(e),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:list(x.map(work,D.glob('*_mast.json')))
