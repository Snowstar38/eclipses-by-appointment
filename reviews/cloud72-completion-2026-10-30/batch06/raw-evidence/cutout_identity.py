from pathlib import Path
import json,numpy as np
from astropy.io import fits
from astropy.wcs import WCS
R=Path(__file__).parent;T=json.load(open(R.parent/'targets-selected.json'));out=[]
for d in json.load(open(R/'tesscut-downloads.json')):
 tic=d['tic']
 with fits.open(R/tic/d['members'][0]) as h:
  x,y=WCS(h[2].header).all_world2pix(T[tic]['ra'],T[tic]['dec'],0);out.append({'tic':tic,'sector':d['sector'],'header_sector':h[0].header.get('SECTOR'),'sector_matches':d['sector']==h[0].header.get('SECTOR'),'target_px':[float(x),float(y)],'target_in_central3x3':bool(3.5<x<6.5 and 3.5<y<6.5),'target_offset_from_cutout_center_arcsec':float(np.hypot(x-5,y-5)*21),'note':'Sky-coordinate cutout identity; WCS target lies in extracted central aperture.'})
assert all(x['sector_matches'] and x['target_in_central3x3'] for x in out);json.dump(out,open(R/'cutout-identity.json','w'),indent=2);print(len(out))
