import urllib.request,urllib.parse,json,pathlib,concurrent.futures
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet'); T=json.loads((D.parent/'targets-selected.json').read_text())
def task(item):
 tic,t=item
 urls={'exofop':f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}', 'simbad':'https://simbad.cds.unistra.fr/simbad/sim-id?'+urllib.parse.urlencode({'Ident':'Gaia DR3 '+t['gaia']['source_id'],'output.format':'ASCII'})}
 for name,url in urls.items():
  try:
   with urllib.request.urlopen(url,timeout=15) as r:out='HTTP '+str(r.status)+'\n'+r.read(150000).decode(errors='replace')
  except Exception as e:out='ERROR '+repr(e)
  (D/f'{tic}_{name}.txt').write_text(out,encoding='utf8')
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as x:list(x.map(task,T.items()))
