import urllib.request,urllib.parse,json,pathlib,concurrent.futures
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet'); T=json.loads((D.parent/'targets-selected.json').read_text())
def task(item):
 tic,t=item;ra=t['gaia']['ra'];dec=t['gaia']['dec']
 q=f"SELECT source_id,ra,dec,phot_g_mean_mag,bp_rp,DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',{ra},{dec}))*3600 AS sep FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.016666667)) AND phot_g_mean_mag<15 ORDER BY sep"
 url='https://gaia.ari.uni-heidelberg.de/tap/sync?'+urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q})
 try:
  with urllib.request.urlopen(url,timeout=45) as r:out=r.read().decode()
 except Exception as e:out='ERROR '+repr(e)
 (D/f'{tic}_neighbors_ari.csv').write_text(out)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:list(x.map(task,T.items()))
