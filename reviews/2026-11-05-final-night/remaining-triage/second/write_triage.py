"""Transcription of visual screening on frozen sheets 043-083."""
import csv
import hashlib
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parents[1]
out = Path(__file__).resolve().parent

# S: step/gap; V: broad variability; N: noise/rapid oscillation;
# A: ambiguous local prospect; R: repeated discrete trough.
# Eight entries per sheet in the frozen queue's plotted row order.
codes = [
    'SSVNSVSS','SASSVSSA','SSSSSSSS','SSSSSSSS','VSSVSSSS',
    'SVSVSSSS','NSSSVSNA','SSSSSSSS','SSSASSVS','SSSSSSSS',
    'SSSSSNNN','SSSSSSSS','SSSASSVV','ASSSSSSS','SSSSSSSS',
    'SSVSSSSS','SSSVSSSS','VSVSVSSS','SSVVVSSS','SSSSSSSA',
    'SSSSSSAS','SASVVVSS','SSSVSAVS','SVVRSAVS','SSSSSVNS',
    'SNSASASV','SSSVVVSS','SSSSSSSV','NSSVSSSS','SSSSASSS',
    'SVSSSSSS','SSNVVSSS','SSSSSNVS','SSVVNVVS','SSVVVSSS',
    'VAVNSSSS','ASVVSASS','VVSSSSSN','NVVSSVAV','SSSASSSS',
    'SSSSSSSS',
]
assert len(codes) == 41 and all(len(x) == 8 for x in codes)

special = {
  390: ('A','One sparse window suggests a short dip; the other displayed segments are noisy or level changing.','low'),
  436: ('A','A narrow selected depression appears among rapid changes and scatter; no clean counterpart is clear.','low'),
  441: ('A','Two shallow centered low regions are visible, with surrounding variability of comparable size.','low'),
  496: ('A','Broad U-like minima recur in three sectors, but long smooth changes make event boundaries unclear.','medium'),
  503: ('A','Three sectors contain centered low points, while rapid irregular variability produces other comparable troughs.','medium'),
  506: ('A','Sector 49 has a narrow feature and sector 22 a shallow depression; the former is sparsely sampled.','medium'),
  510: ('A','Centered minima repeat, but the waveform is smooth and cyclic rather than clearly discrete.','low'),
  518: ('A','Sector 17 shows a centered trough, while the other displayed windows lack a matching clean shape.','low'),
  524: ('R','Sectors 64 and 63 show narrow, isolated centered troughs on nearly level local baselines; sector 11 is sparse.','high'),
  526: ('A','Sectors 39 and 104 show centered short troughs, but sector 103 is dominated by a level reset.','medium'),
  540: ('A','Sectors 54 and 81 show short centered depressions, with other comparably deep fluctuations.','medium'),
  563: ('A','Three sectors show similarly centered smooth troughs, though each spans about a day and merges into variability.','medium'),
  573: ('A','Three sectors contain centered troughs, but adjacent smooth undulations are comparable.','medium'),
  618: ('A','Sector 24 contains a narrow dip; sector 85 looks step or gap limited and sector 18 is sparse.','low'),
  625: ('A','Sector 93 has a short centered dip, while sectors 12 and 103 show broader changing baselines.','low'),
  630: ('A','Sectors 90 and 63 have selected troughs, but the latter is broad and sector 64 is a level reset.','low'),
  647: ('A','Three centered minima appear in sparse sectors 26, 20 and 18, amid large additional fluctuations.','medium'),
  652: ('A','A sparse short dip in sector 5 and a broader trough in sector 98 coexist with smooth variability.','low'),
}
reason = {
 'S':'Selected low flux meets an abrupt level change, gap edge or recovery; reset morphology dominates.',
 'V':'Selected trough joins broad continuous or cyclic variability with other smooth extrema nearby.',
 'N':'Local scatter or rapid oscillations are comparable to the selected depression; isolation is unclear.',
 'A':'A local depression is present, but the displayed windows do not give a clean discrete repeat.',
 'R':'Discrete centered troughs repeat in displayed raw windows; detailed raw event checks are warranted.',
}
category = {'S':'screening_step_or_gap','V':'screening_broad_variability','N':'screening_noise_or_oscillation','A':'ambiguous_prospect','R':'repeated_discrete_trough'}
priority = {'S':'none','V':'none','N':'none','A':'low','R':'high'}
with (base/'queue.csv').open(newline='',encoding='utf-8-sig') as f:
    q = list(csv.DictReader(f))
rows=[]
for row in q:
    if row['arm'] != 'second': continue
    i = int(row['triage_id'][1:])
    assert 337 <= i <= 664
    assert row['sheet'] == f'sheet-{(i-1)//8+1:03d}.png'
    c = codes[(i-337)//8][(i-337)%8]
    why, pri = reason[c], priority[c]
    if i in special:
        c, why, pri = special[i]
    rows.append(dict(tic=row['tic'],triage_id=row['triage_id'],category=category[c],reason=why,sheet=row['sheet'],followup_priority=pri))
assert len(rows)==328 and len({r['tic'] for r in rows})==328
assert [r['triage_id'] for r in rows] == [f'M{i:03d}' for i in range(337,665)]
with (out/'second-visual-triage.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

shortlist = [524,526,503,540,573,563,647,496,506,441,625,618,652,630]
assert len(shortlist)<=20 and len(set(shortlist))==len(shortlist)
with (out/'second-shortlist.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['rank']+list(rows[0])); w.writeheader()
    for rank,i in enumerate(shortlist,1): w.writerow(dict(rank=rank,**rows[i-337]))

for p in [base/'queue.csv',base/'display-receipts.json',out/'second-visual-triage.csv',out/'second-shortlist.csv']:
    print(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
print(Counter(r['category'] for r in rows))
