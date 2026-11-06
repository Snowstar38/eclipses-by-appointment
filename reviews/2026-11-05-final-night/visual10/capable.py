from pathlib import Path
import json,csv,math
B=Path(__file__).resolve().parent;Q=list(csv.DictReader((B/'queue.csv').open()));C=json.loads((B/'lead-clocks.json').read_text());D=json.loads((B/'lead-deciding-checks.json').read_text());M=json.loads((B/'lead-gaia-covariance.json').read_text());N=json.loads((B/'lead-neighbour-receipts.json').read_text());out=[]
for rec in N:
 if rec['tic']!='233405109' or 'rows' not in rec:continue
 r=next(r for r in Q if r['tic']==rec['tic']);nb=[]
 for n in rec['rows']:
  if not n.get('phot_g_mean_mag') or n['source_id']==r['gaia_dr3']:continue
  sep=math.hypot((float(n['ra'])-float(r['ra_deg']))*math.cos(math.radians(float(r['dec_deg']))),float(n['dec'])-float(r['dec_deg']))*3600;ratio=10**(-.4*(float(n['phot_g_mean_mag'])-float(r['gaia_G'])));required=.0026088*(1+ratio)/ratio
  if required<=1:nb.append(dict(source_id=n['source_id'],separation_arcsec=sep,gaia_G=n['phot_g_mean_mag'],required_intrinsic_fraction_conservative=required,note='Assumes full neighbor throughput and G as flux proxy; actual TESS aperture throughput can only reduce its capability. Compare spatial deficit, not required intrinsic fraction to blended pixel fractional loss.'))
 (B/r['tic']/'lead-capable-neighbours.json').write_text(json.dumps(nb,indent=2))
 print(r['tic'],len(nb),min(x['separation_arcsec'] for x in nb))
