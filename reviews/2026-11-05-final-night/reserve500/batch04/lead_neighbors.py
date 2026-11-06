import csv,json,requests,hashlib,io,math
from pathlib import Path
b=Path(__file__).resolve().parent
pop=json.loads((b.parent.parent/'fresh-band-reserve500/population.json').read_text())['targets']
for row in csv.DictReader((b/'queue.csv').open()):
 tic=row['tic'];ra=pop[tic]['ra'];dec=pop[tic]['dec'];d=b/tic
 query=f"SELECT source_id,ra,dec,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS',ra,dec),CIRCLE('ICRS',{ra},{dec},0.035))"
 try:
  r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':query},timeout=30);r.raise_for_status();(d/'lead-gaia-neighbors.csv').write_bytes(r.content);ns=list(csv.DictReader(io.StringIO(r.text)))
  for n in ns:
   n['separation_arcsec']=math.hypot((float(n['ra'])-ra)*math.cos(math.radians(dec)),float(n['dec'])-dec)*3600
   n['relative_G_flux']=10**(-.4*(float(n['phot_g_mean_mag'])-float(row['gaia_G']))) if n['phot_g_mean_mag'] else None
  (d/'lead-neighbors.json').write_text(json.dumps({'query':query,'endpoint':r.url,'sha256':hashlib.sha256(r.content).hexdigest(),'neighbors':ns,'note':'G-band brightness ratios are contextual, not direct comparisons of intrinsic neighbor depth to diluted pixel loss.'},indent=2));print(tic,len(ns),flush=True)
 except Exception as e:(d/'lead-neighbors.json').write_text(json.dumps({'error':repr(e)}));print(tic,repr(e),flush=True)
