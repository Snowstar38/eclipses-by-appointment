import json,pathlib,hashlib
from astropy.io import fits
R=pathlib.Path('.');p=R/'independent-results.json';d=json.load(open(p));targets=json.load(open('../targets-selected.json'))
for z in d:
 with fits.open(z['source_path']) as h:
  H=h[0].header;z['identity'].update({k:H.get(k) for k in ['OBJECT','TICID','RA_OBJ','DEC_OBJ','TSTART','TSTOP']}); z['identity']['target_gaia_ra_dec']=[targets[z['tic']]['gaia']['ra'],targets[z['tic']]['gaia']['dec']]
  z['identity']['note']='TESScut header does not necessarily contain TIC identifier; identification rests on requested target cache path and Gaia coordinate projected through WCS, with sector checked.'
json.dump(d,open(p,'w'),indent=2)
for f in ['raw-events.json','independent-results.json','raw-event-panels.png','independent-panels.png','measure.py','pixel_independent.py','supplement_4374712.py','qlp-manifest.json','search-receipts.json']:
 print(hashlib.sha256((R/f).read_bytes()).hexdigest(),f)
