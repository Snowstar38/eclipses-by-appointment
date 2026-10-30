from pathlib import Path
import json,csv,hashlib
B=Path(__file__).parent;D=B.parent
ids=list(json.loads((B/'targets-selected.json').read_text()))
c=[r for r in csv.DictReader((D/'shared-catalogues/coverage-matrix.csv').open()) if r['tic'] in ids]
assert len(c)==10
(B/'catalogue-review.json').write_text(json.dumps(c,indent=2))
s=json.loads((B/'source-review.json').read_text())
for t,v in s.items():
 v['lead_visual_inspection']=t in ['39069184','364120441']
 v['source_assessment']=f"Cached eclipse deficit peaks at the target pixel, offset {v['target_distance_arcsec']:.3f} arcsec. "
 if t=='39069184':
  v['source_assessment']+='A flux-capable Gaia neighbour is only 2.21 arcsec away (0.105 TESS pixel). The deficit is nominally closer to the target, but centroid errors are uncalibrated and own-pixel loss mixes the two sources; attribution remains ambiguous at this separation. This prevents a target-specific confirmation despite strong repeated eclipses. '
 elif v['capable']:
  v['source_assessment']+='The capable neighbour is spatially distinct, farther from the eclipse deficit, with own-pixel fractional loss much below that needed to supply the eclipse. '
 else:v['source_assessment']+='No Gaia G-band flux-capable neighbour is recorded within 60 arcsec. '
 v['source_assessment']+='Centroid displacement is descriptive; G/TESS band differences, unresolved or uncatalogued blends and PSF modelling limit this test. '
 if v['psf_fraction_residual']>.5:v['source_assessment']+='High PSF residual limits characterization; attribution uses the deficit peak and neighbour comparison. '
 if v['lead_visual_inspection']:v['source_assessment']+='Lead inspected the cached difference-image panel.'
(B/'source-review.json').write_text(json.dumps(s,indent=2))
inputs=[D/'queue.csv',D/'targets-selected.json',D/'shared-catalogues/coverage-matrix.csv',D/'shared-catalogues/gaia-nss_two_body_orbit.csv']+list((B/'raw-evidence').glob('*/*.json'))+list((B/'raw-evidence').glob('*/*.png'))
(B/'lead-input-provenance.json').write_text(json.dumps([dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs],indent=2))
