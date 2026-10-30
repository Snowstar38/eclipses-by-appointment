import urllib.request,urllib.parse,json,pathlib,concurrent.futures,time
D=pathlib.Path(r'C:\Home\Astra\made\binary-handoff-2026-10-30\local-batch-a\full-vet'); T=json.loads((D.parent/'targets-selected.json').read_text())
def get(url,timeout=35):
 try:
  with urllib.request.urlopen(url,timeout=timeout) as r:return r.read().decode()
 except Exception as e:return 'ERROR '+repr(e)
def tap(q):
 return get('https://gea.esac.esa.int/tap-server/tap/sync?'+urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'json','QUERY':q}))
def task(item):
 tic,t=item; sid=t['gaia']['source_id']; ra=t['gaia']['ra']; dec=t['gaia']['dec']
 qs={'nss':f'SELECT * FROM gaiadr3.nss_two_body_orbit WHERE source_id={sid}', 'neighbors':f"SELECT source_id,ra,dec,phot_g_mean_mag,bp_rp,DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',{ra},{dec}))*3600 AS sep FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.016666667)) AND phot_g_mean_mag<15 ORDER BY sep",'eb':f'SELECT * FROM gaiadr3.vari_eclipsing_binary WHERE source_id={sid}', 'vari':f'SELECT * FROM gaiadr3.vari_summary WHERE source_id={sid}'}
 for k,q in qs.items(): (D/f'{tic}_{k}.json').write_text(tap(q),encoding='utf8')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:list(x.map(task,T.items()))
