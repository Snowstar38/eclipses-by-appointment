import requests
q="SELECT TOP 100 source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',70.71657359926411,7.393721176385869,0.045)) AND phot_g_mean_mag<17 ORDER BY phot_g_mean_mag"
u='https://gea.esac.esa.int/tap-server/tap/sync'
r=requests.get(u,params={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=60);print(r.status_code,len(r.content),r.text[:300]);open('helper-gaia.csv','w',encoding='utf8').write(r.text)
