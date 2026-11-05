"""Root adjudication after all ten reports and deciding image checks."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parent
v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),'batch09'],text=True))
rows=list(csv.DictReader((W/'batch09/RESULTS.csv').open(encoding='utf8')))
a={'accepted':True,'batch':'batch09','queue_sha256':v['queue_sha256'],'results_sha256':v['results_sha256'],'manifest_sha256':v['manifest_sha256'],'manifest_files_verified':v['manifest_files'],'rows':10,
'decisions':{r['sample_id']:{'tic':r['tic'],'physical_verdict':r['physical_verdict'],'completion':r['full_review_completion'],'novelty_status':r['novelty_status']} for r in rows},
'root_review':'Read all ten reports, both audits and final pixel-updated reports. The helper correctly challenged brevity/background correlation as sufficient artifact evidence. Root requested subsequent TESSCut checks of H084/H086/H087 after helper finished, inspected all three difference images and measurement script, and requested correction of fractional-coordinate masks mislabeled 3x3/5x5. Final nearest-integer masks give actual nine/twenty-five pixel apertures. H086 excess is predominantly off-target with near-zero target net change and background/centroid disturbance: refutes selected target brightening. H087 has a targetlike positive image and flarelike time profile: non-eclipse variability, subtype/subpixel source not proved. H084 dipole leaves origin unresolved. H088 gap/background only remains UNRESOLVED. H081/H083/H085 describe non-eclipse aperture modulation, not confirmed target attribution or binary clocks.',
'limits':'New pixel checks were lead/root followup after helper completion. Same photons, unregistered differences and descriptive positive image moments are not fitted PSF localization or independent recurrence. Five unresolved outcomes remain in the selected denominator, not negatives. No measured binary period, eclipse epoch or depth assigned.',
'accounting':'All novelty UNKNOWN. Physical sample adjudication only; no new-system claim or prior-ledger change.'}
(W/'batch09/ROOT-ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n',encoding='utf8')
print(v)
