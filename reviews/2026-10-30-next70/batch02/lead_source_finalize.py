from pathlib import Path
import json,hashlib,datetime
B=Path(__file__).parent;D=B.parent
r=json.loads((B/'source-review.json').read_text())
for tic,v in r.items():
 v['lead_visual_inspection']=tic in ['309981203','301961777','333072525']
 v['source_assessment']='Cached difference-image deficit peaks at the target pixel; target/deficit distance %.3f arcsec. '%v['target_distance_arcsec']
 if v['capable']:
  v['source_assessment']+='All flux-capable catalogued neighbours have deficit centres closer to the target and own-pixel losses substantially below the losses required if they supplied the eclipse. '
 else:v['source_assessment']+='No Gaia G-band flux-capable neighbour within the cached 60 arcsec search. '
 v['source_assessment']+='Centroid displacements are descriptive, without calibrated uncertainty; G/TESS band differences, uncatalogued blends and PSF modelling limit the test. '
 if v['psf_fraction_residual']>.5:v['source_assessment']+='High PSF fractional residual is retained as a characterization limitation; attribution rests on the deficit peak and neighbour comparison, not a formal PSF likelihood. '
 if v['lead_visual_inspection']:v['source_assessment']+='Lead inspected the cached three-panel image.'
(B/'source-review.json').write_text(json.dumps(r,indent=2))
inputs=[D/'queue.csv',D/'targets-selected.json',D/'shared-catalogues/coverage-matrix.csv',D/'shared-catalogues/gaia-nss_two_body_orbit.csv']+list((B/'raw-evidence').glob('*/*.json'))+list((B/'raw-evidence').glob('*/*.png'))
(B/'lead-input-provenance.json').write_text(json.dumps([dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs],indent=2))
