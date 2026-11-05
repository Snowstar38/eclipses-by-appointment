"""Root adjudication after reading all reports, audits, and deciding plots."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parent
v=json.loads(subprocess.check_output([sys.executable,str(W/'validate_batch.py'),'batch08'],text=True))
rows=list(csv.DictReader((W/'batch08/RESULTS.csv').open(encoding='utf8')))
a={'accepted':True,'batch':'batch08','queue_sha256':v['queue_sha256'],'results_sha256':v['results_sha256'],'manifest_sha256':v['manifest_sha256'],'manifest_files_verified':v['manifest_files'],'rows':10,
'decisions':{r['sample_id']:{'tic':r['tic'],'physical_verdict':r['physical_verdict'],'completion':r['full_review_completion'],'novelty_status':r['novelty_status']} for r in rows},
'root_review':'Read all ten reports and both audits; checked actual fold-selected evidence, H073 full-sector morphology and H080 predicted-window panels, plus H078 WCS/aperture numeric receipt. H072 retained PLAUSIBLE because single incomplete dip and gapped earlier prediction do not establish or refute recurrence. H073 REFUTED narrowly for selected repeated fold signal: repeated post-gap ramps and broad evolving waves; an insecure hidden isolated event is not excluded. H077 later cutouts and cadence counts are exploratory, not sensitivity-calibrated nulls. H078 aperture-dependent ramps plus contrary current-sector prediction support rejecting selected fold signal. H080 s41 covered P core is inconsistent with the claimed 6.57 ppt dip; sparse/gapped other windows are not independent sensitive nulls. No fold or Gaia period promoted to measured photometric period.',
'limits':'Neighbor cone queries failed; no positive source attribution claimed. Refutations address selected signals, not all possible eclipses. Counts do not measure survey completeness.',
'accounting':'All novelty UNKNOWN. Physical sample adjudication only; prior 913 claims and public paper unchanged.'}
(W/'batch08/ROOT-ACCEPTANCE.json').write_text(json.dumps(a,indent=2)+'\n',encoding='utf8')
print(v)
