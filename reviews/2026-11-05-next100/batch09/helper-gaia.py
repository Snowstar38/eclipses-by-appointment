import requests,json,concurrent.futures
cases=[('Q082',213.0506965594,-59.8044561966),('Q083',10.4607302911,42.9937724794),('Q090',288.2374831584,58.1078730882)]
def go(c):
 q=f"SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{c[1]},{c[2]},0.028)) AND phot_g_mean_mag<18"
 try:
  r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=45);open('helper-'+c[0]+'-gaia.csv','w',encoding='utf8').write(r.text);return [c[0],r.status_code,len(r.content),r.text[:150]]
 except Exception as e:return [c[0],repr(e)]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:out=list(ex.map(go,cases))
print(json.dumps(out,indent=2))

