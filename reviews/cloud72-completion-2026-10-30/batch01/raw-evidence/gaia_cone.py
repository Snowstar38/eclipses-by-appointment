import urllib.request,urllib.parse,json,pathlib,concurrent.futures
r=pathlib.Path(__file__).parent;ts=json.load(open(r.parent/'targets-selected.json'))
def run(item):
 tic,t=item;g=t['gaia'];ra=g['ra'];dec=g['dec'];q=f"SELECT source_id,ra,dec,phot_g_mean_mag,DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',{ra},{dec}))*3600 AS sep FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.016666667)) ORDER BY sep";u='https://gea.esac.esa.int/tap-server/tap/sync?'+urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'json','QUERY':q})
 try:
  with urllib.request.urlopen(u,timeout=60) as h:b=h.read()
  (r/tic/'gaia-cone.json').write_bytes(b);return (tic,len(b))
 except Exception as e:return (tic,repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as x:res=list(x.map(run,ts.items()))
print(res)
