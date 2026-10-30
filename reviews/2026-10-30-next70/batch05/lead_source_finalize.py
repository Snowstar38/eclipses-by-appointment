from pathlib import Path
import json,hashlib,datetime
B=Path(__file__).parent;D=B.parent
r=json.loads((B/'source-review.json').read_text())
for tic,v in r.items():
 v['lead_visual_inspection']=tic in ['140802498','293946483','4374712']
 v['source_assessment']='Cached difference-image deficit peaks at the target pixel; target/deficit distance %.3f arcsec. '%v['target_distance_arcsec']
 if v['capable']:
  v['source_assessment']+='The deficit centre is closer to the target than the flux-capable catalogued neighbours; own-pixel losses include mixed source light and are supporting spatial diagnostics only. '
 else:v['source_assessment']+='No Gaia G-band flux-capable neighbour within the cached 60 arcsec search. '
 v['source_assessment']+='Centroid displacements are descriptive, without calibrated uncertainty; G/TESS band differences, uncatalogued blends and PSF modelling limit the test. '
 if v['psf_fraction_residual']>.5:v['source_assessment']+='High PSF fractional residual is retained as a characterization limitation; attribution rests on the deficit peak and neighbour comparison, not a formal PSF likelihood. '
 if v['lead_visual_inspection']:v['source_assessment']+='Lead inspected the cached three-panel image.'
v=r['140802498']
v['repeatability_receipt']='raw-evidence/140802498/source_repeatability.json'
v['source_assessment']+=' A bounded repeatability test of the cached sector 97 cutout places seven-event half-stack deficits 3.12/0.77 arcsec from the target versus 12.06/11.36 arcsec from the capable neighbour. Individual event deficits stay nearer the target. Shifted empirical out-of-eclipse template fractional residual is 0.159 at the target versus 0.494 at the neighbour; the template is blended and this is a diagnostic, not a formal PRF likelihood. These repeated spatial comparisons identify the target as the source to the available TESS resolution. The shared rounded pixel and mixed own-pixel flux alone were not used as exclusion evidence.'
v['attribution_status']='target supported by repeated spatial comparison'
(B/'source-review.json').write_text(json.dumps(r,indent=2))
inputs=[D/'queue.csv',D/'targets-selected.json',D/'shared-catalogues/coverage-matrix.csv',D/'shared-catalogues/gaia-nss_two_body_orbit.csv']+list((B/'raw-evidence').glob('*/*.json'))+list((B/'raw-evidence').glob('*/*.png'))
(B/'lead-input-provenance.json').write_text(json.dumps([dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs],indent=2))
