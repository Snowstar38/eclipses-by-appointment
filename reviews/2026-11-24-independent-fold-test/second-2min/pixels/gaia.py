import requests,pathlib
p=pathlib.Path(__file__).resolve().parent
q="SELECT source_id,ra,dec,phot_g_mean_mag,pmra,pmdec,DISTANCE(POINT('ICRS',ra,dec),POINT('ICRS',72.6639595885975,40.85798381916))*3600 AS sep FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',72.6639595885975,40.85798381916,0.035)) AND phot_g_mean_mag<19"
r=requests.get('https://gea.esac.esa.int/tap-server/tap/sync',params={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=60);r.raise_for_status();(p/'gaia.csv').write_text(r.text);print(r.text[:3000])
