from pathlib import Path
import json
b=Path(__file__).parent;p=b/'secondary-phases.json';z=json.load(open(p))
for tic,v in z.items():
 v['visual_status']='Measured secondary-like narrow feature; pooled shape and baseline systematics limit precision' if tic not in ['370138999','264485594'] else 'No secure secondary established; numeric fit is a noise/variability description and not a detection or clean null'
 v['secure_secondary']=tic not in ['370138999','264485594']
 v['search_guess_provenance']='Raw full-phase visual estimate' if tic in ['176048490','76177367'] else 'Source-specific Gaia conjunction separation search guide; fitted center is free'
json.dump(z,open(p,'w'),indent=2)
