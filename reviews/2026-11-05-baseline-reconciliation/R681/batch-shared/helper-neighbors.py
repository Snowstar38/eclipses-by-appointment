import csv,json,math
from pathlib import Path
p=Path(__file__).parent; out={}
for r in csv.DictReader((p/'queue.csv').open()):
 path=p/r['tic']/'pixels/gaia-stars.json'
 if not path.exists(): continue
 stars=json.loads(path.read_text()); target=next(s for s in stars if str(s['source_id'])==r['gaia_dr3_source_id']); sector={'24668377':98,'150465032':61,'331650047':79,'384744604':101,'109560492':88}[r['tic']]; depth=max(e['depth_ppt'] for e in json.loads((p/r['tic']/'measurements.json').read_text())['events'] if e.get('timing_usable') and e['sector']==sector)/1000; lim=-2.5*math.log10(depth/(1-depth)); neighbors=[]
 for s in stars:
  if str(s['source_id'])==r['gaia_dr3_source_id'] or s['phot_g_mean_mag'] is None:continue
  dg=s['phot_g_mean_mag']-target['phot_g_mean_mag']; sep=math.hypot((s['ra']-target['ra'])*math.cos(math.radians(target['dec'])),s['dec']-target['dec'])*3600
  if dg<=lim:neighbors.append({'source_id':str(s['source_id']),'separation_arcsec':sep,'delta_g':dg,'conservative_required_intrinsic_fraction':depth*(1+10**(-.4*dg))/10**(-.4*dg)})
 out[r['tic']]={'depth':depth,'max_delta_g':lim,'capable_neighbors':neighbors,'caveat':'full-flux Gaia G approximation, ignores response/aperture, other blends and passband differences; capability is only screening'}
(p/'helper-neighbors.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

