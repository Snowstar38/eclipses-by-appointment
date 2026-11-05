import requests,concurrent.futures,pathlib
B=pathlib.Path('batch07')
def run(z):
 tic,ra,dec=z;q=f"SELECT TOP 100 source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.045)) AND phot_g_mean_mag<18 ORDER BY phot_g_mean_mag";u='https://gea.esac.esa.int/tap-server/tap/sync'
 try:
  r=requests.get(u,params={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=35);(B/f'helper-{tic}-gaia.csv').write_text(r.text);return tic,r.status_code,len(r.content),r.text[:200]
 except Exception as e:return tic,str(e)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:print(list(ex.map(run,[('295176393',270.34925752923124,-69.60515069877758),('341419787',120.15339783069679,-54.50900340546292)])))
