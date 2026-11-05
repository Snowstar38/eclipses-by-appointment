import json,csv,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;p=B.parent/'shared-catalogues/gaia-neighbors.json';d=json.loads(p.read_text());rows=list(csv.DictReader((B/'queue.csv').open()));sp=json.loads((B/'helper-spatial.json').read_text())+json.loads((B/'helper-spatial-rest.json').read_text());out=[]
for r,x in zip(rows,sp):
 depth=x['qlp_depths_ppt']['SAP_FLUX']/1000;ns=[]
 for n in d['targets'][r['sample_id']]:
  if n['is_queue_gaia_source'] or not n['phot_g_mean_mag']:continue
  ratio=10**(-.4*(float(n['phot_g_mean_mag'])-float(r['gaia_G'])));need=depth*(1+ratio)/ratio
  if need<=1:ns.append({**n,'flux_ratio_G':ratio,'required_fraction_ideal':need})
 out.append({'sample_id':r['sample_id'],'tic':r['tic'],'sap_depth_ppt':1000*depth,'capable':ns,'gaia_neighbors_sha256':hashlib.sha256(p.read_bytes()).hexdigest()});print(r['sample_id'],[(n['source_id'],round(n['separation_arcsec'],2),round(n['required_fraction_ideal'],2)) for n in ns])
(B/'helper-neighbors-all.json').write_text(json.dumps(out,indent=2))
