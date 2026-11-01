import csv,json,pathlib
from astropy.io import fits
b=pathlib.Path(r'[local path omitted]')
for row in csv.DictReader((b/'RESULTS.csv').open(encoding='utf-8-sig')):
 t=row['tic']; m=json.loads((b/t/'measurements.json').read_text()); bad=[]
 for s in m['sources']:
  with fits.open(s['path']) as h:
   p=h[0].header
   print(t,s['sector'],'TICID',p.get('TICID'),'SECTOR',p.get('SECTOR'))
