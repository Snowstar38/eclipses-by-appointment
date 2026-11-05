import urllib.request,urllib.parse,pathlib,json
b=pathlib.Path('[local-path-redacted]')
for tic,ra,dec in [('270523058',293.3773175310484,44.01657359497792),('295351347',223.30317599308512,-61.30028070964274),('280051953',45.67036251522263,-73.54919359108234)]:
 q=f"SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.04)) AND phot_g_mean_mag<18"
 params=urllib.parse.urlencode({'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q})
 try:
  dat=urllib.request.urlopen('https://gea.esac.esa.int/tap-server/tap/sync',data=params.encode(),timeout=45).read();(b/tic/'helper-gaia-neighbors.csv').write_bytes(dat);print(tic,len(dat))
 except Exception as e:print(tic,str(e))
