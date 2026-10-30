import urllib.request,urllib.parse,json,pathlib,concurrent.futures
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet'); T=json.loads((D.parent/'targets-selected.json').read_text())
def task(item):
 tic,t=item
 for k,p in [('nss',{'-source':'I/357/tbosb1','Source':t['gaia']['source_id'],'-out':'**','-out.max':'5'}),('neighbors',{'-source':'I/355/gaiadr3','-c':f"{t['gaia']['ra']} {t['gaia']['dec']}",'-c.rs':'60','Gmag':'<15','-out':'Source,RA_ICRS,DE_ICRS,Gmag,BP-RP','-out.add':'_r','-out.max':'500'})]:
  for host in ['vizier.cds.unistra.fr','vizier.cfa.harvard.edu']:
   try:
    url='https://'+host+'/viz-bin/asu-tsv?'+urllib.parse.urlencode(p)
    with urllib.request.urlopen(url,timeout=20) as r: out=r.read().decode()
    if '#Table' in out or '#RESOURCE' in out:break
   except Exception as e:out='ERROR '+repr(e)
  (D/f'{tic}_{k}_viz.tsv').write_text(out,encoding='utf8')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:list(x.map(task,T.items()))
