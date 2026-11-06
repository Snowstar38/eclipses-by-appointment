from pathlib import Path
import json,numpy as np
b=Path(__file__).resolve().parent
for tic in ['241100642','272726082','278185284','280692653']:
 d=b/tic;n=json.loads((d/'lead-neighbors.json').read_text());l=json.loads((d/'helper-localization.json').read_text());g=json.loads((d/'lead-diff-gaussian.json').read_text()) if (d/'lead-diff-gaussian.json').exists() else None
 near=n['nearby_flux_sources'];loss=l['aperture_loss'];out=[]
 for s in near:
  if s['relative_G_flux']>.001 and s['separation_pixels']<3:
   f=s['relative_G_flux'];out.append({'source_id':s['source_id'],'G_relative_flux':f,'separation_pixels':s['separation_pixels'],'xy':s['pixel_xy'],'difference_centroid_distance_pixels':s['difference_centroid_distance_pixels'],'gaussian_distance_pixels':float(np.linalg.norm(np.array(s['pixel_xy'])-g['gaussian_xy'])) if g else None,'illustrative_intrinsic_loss_for_target_only_blend':loss*(1+f)/f})
 (d/'lead-capability-audit.json').write_text(json.dumps({'note':'Illustrative G-band relative flux requirement assuming only target+neighbor. Not a TESS bandpass or aperture throughput model; do not compare directly to blended pixel fractional loss. Geometric localization carries the source attribution.','sources':out},indent=2));print(tic,[(x['source_id'],round(x['G_relative_flux'],4),round(x['gaussian_distance_pixels'] or x['difference_centroid_distance_pixels'],2),round(x['illustrative_intrinsic_loss_for_target_only_blend'],2)) for x in out[:7]])
