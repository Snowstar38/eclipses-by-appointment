from pathlib import Path
import json
B=Path('[local working path omitted; see provenance receipts]')
p=B/'make_reports.py';s=p.read_text().replace("verdict='CONFIRMED' if complete else 'PLAUSIBLE'","verdict='CONFIRMED' if complete and t not in ['101779765','311918550'] else 'PLAUSIBLE'")
s=s.replace("note='Representative measurements; period conditional on search cycle counts; uncertainty and characterization limitations retained.'","note=('Close capable neighbour unresolved' if t=='101779765' else 'Gaia period tension 8.56 quoted sigma' if t=='311918550' else 'Representative measurements; period conditional on search cycle counts; characterization limitations retained.')")
p.write_text(s)
x=json.loads((B/'source-review.json').read_text())
for t,v in x.items():
 if v['psf_fraction_residual']>.5:v['source_assessment']+=' High PSF fractional residual (%.3f) limits the scaled-image model; attribution instead uses localized eclipse deficit and the capable-neighbour comparison.'%v['psf_fraction_residual']
x['122024194']['lead_visual_inspection']=True
x['122024194']['source_assessment']+=' Lead inspected the three-panel image: bright off-target star dominates total light but the eclipse deficit remains at the target, 59.34 arcsec from the only flux-capable catalogued neighbour.'
(B/'source-review.json').write_text(json.dumps(x,indent=2))
