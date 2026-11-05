"""Apply explicit root adversarial adjudication without modifying sealed batch evidence."""
from pathlib import Path
from collections import Counter
import csv,json,hashlib
W=Path(__file__).resolve().parent
def rows(p):return list(csv.DictReader(p.open(encoding='utf8',newline='')))
def write(p,r):
    with p.open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(r[0]));w.writeheader();w.writerows(r)
def main():
    r=rows(W/'accepted-results.csv');assert len(r)==100
    target=next(x for x in r if x['sample_id']=='Q080');assert target['physical_verdict']=='PROBABLE'
    previous=target['report'];current=str(W/'adjudication/Q080.md')
    target.update(physical_verdict='PLAUSIBLE',report=current)
    target['limitations']='Final adversarial adjudication: only two continuously sampled troughs securely support the interpretation, with untested same-kind cycle count; gapped later depressions and prior VSX identity do not resolve it. '+target['limitations']
    write(W/'reconciled-results.csv',r)
    update=dict(sample_id='Q080',tic=target['tic'],physical_at_batch_freeze='PROBABLE',current_physical_verdict='PLAUSIBLE',novelty_status='KNOWN',claim_count_change='0',reason='Two well-resolved events with untested same-kind cycle count; later gapped/wave-contaminated events do not establish a third secure same-kind occurrence.',original_report=previous,current_report=current,original_results_sha256=hashlib.sha256((W/'accepted-results.csv').read_bytes()).hexdigest())
    write(W/'physical-updates.csv',[update])
    (W/'reconciled-summary.json').write_text(json.dumps({'reviewed':100,'verdicts':dict(Counter(x['physical_verdict'] for x in r)),'physical_overrides':1,'sealed_batch_evidence':'unchanged','deciding_report':'adjudication/Q080.md'},indent=2)+'\n')
if __name__=='__main__':main()
