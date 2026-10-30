import json,math
from pathlib import Path
B=Path('[local working path omitted; see provenance receipts]');out={}
for p in (B/'raw-evidence').glob('*/diff*.json'):
 d=json.loads(p.read_text());tic=d['tic'];tx,ty=d['target_px'];cx,cy=d['deficit_centroid'];cap=[dict(**n,deficit_distance_arcsec=21*math.hypot(n['px'][0]-cx,n['px'][1]-cy),target_distance_arcsec=21*math.hypot(n['px'][0]-tx,n['px'][1]-ty)) for n in d['neighbours_60'] if n['possible']]
 out[tic]=dict(cached_receipt=str(p.relative_to(B)),sector=d['sector'],n_events=d['n_events'],target_distance_arcsec=21*math.hypot(cx-tx,cy-ty),capable=cap,peak=d['peak_deficit_px'],target_pixel=d['target_pixel'],psf_fraction_residual=d['psf_fit_frac_resid'],source_assessment='Target-centered eclipse deficit, peak at target; capable catalogued neighbours are spatially distinct and not the location of the disappearing source. Lead personally inspected all ten cached three-panel images. Centroid displacement is a descriptive diagnostic, not a calibrated uncertainty. G-band flux feasibility and 60arcsec catalogue radius limit the test.')
 print(tic,'target',out[tic]['target_distance_arcsec'],'cap',[(n['sep'],n['depth_needed'],n['frac_loss_at_pixel'],n['deficit_distance_arcsec']) for n in cap])
(B/'source-review.json').write_text(json.dumps(out,indent=2))
