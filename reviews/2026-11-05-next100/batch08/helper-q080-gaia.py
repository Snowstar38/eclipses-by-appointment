import urllib.request,urllib.parse,pathlib,hashlib,json
b=pathlib.Path(__file__).parent;q="SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',107.9357811849,-22.4416859984,0.03)) AND phot_g_mean_mag<18";par=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q});url='https://gea.esac.esa.int/tap-server/tap/sync'
try:
 d=urllib.request.urlopen(url,data=par.encode(),timeout=30).read();(b/'99243741/helper-gaia-neighbors.csv').write_bytes(d);r={'query':q,'url':url,'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)}
except Exception as e:r={'query':q,'url':url,'error':str(e)}
(b/'99243741/helper-gaia-receipt.json').write_text(json.dumps(r,indent=2));print(r)
