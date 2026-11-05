"""Root adjudication after final reports, raw plots and coverage receipts."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parent
v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),'batch10'],text=True))
rows=list(csv.DictReader((W/'batch10/RESULTS.csv').open(encoding='utf8')))
a={'accepted':True,'batch':'batch10','queue_sha256':v['queue_sha256'],'results_sha256':v['results_sha256'],'manifest_sha256':v['manifest_sha256'],'manifest_files_verified':v['manifest_files'],'rows':10,
'decisions':{r['sample_id']:{'tic':r['tic'],'physical_verdict':r['physical_verdict'],'completion':r['full_review_completion'],'novelty_status':r['novelty_status']} for r in rows},
'root_review':'Read all ten reports, lead/helper audits and source receipts. Viewed H100 raw/centroid detail and pixel difference, plus H094 new-sector windows. H094 two shallow insecure occasions do not establish event centers, cycle uniqueness or source. S108 target placement/flux is real but scatter and extraction systematics limit exact-fold challenge; S98 near-zero flux is not a null. H100 retained PLAUSIBLE: synchronized centroid motion and broad background do not alone prove an artifact; the available difference image does not localize a dip. Root requested current S59/S85 checks after helper completion: obtained cutouts have absent/nearly zero target flux and no exact-fold predicted core, hence no additional sensitive null. Other selected folds have trend/level/recovery context; H099 S47 0.4 ppt is not a null for its 0.444 ppt screening amplitude. Its selected-signal rejection rests on S60 relaxation morphology, not a universal shallow-eclipse exclusion.',
'limits':'Root-requested WCS/flux checks and H100 additional cutouts were lead followup after helper completion. Near-zero target cutouts and missing phase coverage remain unknown, not negative. No photometric period or eclipse epoch/depth promoted from screening values. Refutations concern selected signals only.',
'accounting':'All novelty UNKNOWN. Physical sample adjudication only; prior claims and public paper unchanged.'}
(W/'batch10/ROOT-ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n',encoding='utf8')
print(v)
