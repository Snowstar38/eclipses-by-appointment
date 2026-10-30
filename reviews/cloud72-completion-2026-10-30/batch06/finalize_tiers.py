from pathlib import Path
import json
B=Path(__file__).parent;p=B/'decisions.json';d=json.load(open(p))
for tic in ['275022619','257575960']:
 d[tic]['verdict']='PLAUSIBLE';d[tic]['assessment']+=' Independent Terra audit retains PLAUSIBLE: the available representative data fail to establish recurring eclipses, but sparse/compromised coverage does not tie the original search detection to a specific demonstrated artifact. This is not a secure eclipse identification.';d[tic]['limitations']+=' Repetition and eclipse morphology remain scientifically uncertain; no calibrated sensitivity or propagated ephemeris-error analysis was performed.';d[tic]['next_check']='Obtain a well-covered predicted candidate event in a distinct reduction and establish a second coherent detached eclipse before claiming an eclipse period or host.'
p.write_text(json.dumps(d,indent=2))
p=B/'write_reports.py';s=p.read_text();s=s.replace("Scientific outcome: submitted eclipse interpretation refuted by morphology and failure of independent eclipse recovery.","Scientific outcome: {('submitted eclipse interpretation refuted by a demonstrated smooth/systematic explanation' if a['verdict']=='REFUTED' else 'eclipse morphology and repetition remain unresolved; this is not a secure eclipse identification')}.");p.write_text(s)
