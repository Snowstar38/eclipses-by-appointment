from pathlib import Path
import json
B=Path('[local working path omitted; see provenance receipts]');s=json.loads((B/'source-review.json').read_text())
for t,v in s.items():
 print(t,'peak',v['peak'],'targetpixel',v['target_pixel'],'residual',v['psf_fraction_residual'])
 v['lead_visual_inspection']=t in ['101779765','233269866','287032105']
 v['source_assessment']='Cached eclipse difference image concentrates the lost flux in the target image; target/deficit distance %.3f arcsec. '%v['target_distance_arcsec']
 v['source_assessment']+=('No Gaia G-band flux-capable neighbour within the cached 60 arcsec search. ' if not v['capable'] else 'Flux-capable neighbours are tested by spatial position and mixed own-pixel losses, which alone are not exclusions. ')
 v['source_assessment']+='Centroid displacements are descriptive, without calibrated uncertainty; bandpass differences, uncatalogued blends and PSF modelling limit attribution. '
 v['attribution_status']='target supported by available spatial evidence'
 if v['lead_visual_inspection']:v['source_assessment']+='Lead inspected the cached three-panel image. '
 if t=='101779765':
  v['attribution_status']='unresolved close capable neighbour'
  v['source_assessment']+='The 3.63 arcsec neighbour lies in the same unresolved TESS image and could reproduce the loss with a 66.95% eclipse. Despite the deficit being nearer the target, these cached diagnostics do not securely distinguish the two sources; retain PLAUSIBLE pending finer spatial evidence.'
 if t=='233269866':
  v['repeatability_receipt']='raw-evidence/233269866/source_repeatability.json'
  v['source_assessment']+='Eight-event bounded repeatability test: four-event half-stack deficit distances 3.10/3.14 arcsec from target versus 6.69/7.21 arcsec from the 9.73 arcsec neighbour. All individual deficits remain closer to target. Shifted empirical image residual is 0.145 at target versus 0.401 at neighbour. The blended template is a diagnostic, not a calibrated likelihood; repeated spatial evidence supports target attribution.'
(B/'source-review.json').write_text(json.dumps(s,indent=2))
