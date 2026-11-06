"""Reproducible transcription of visual screening on sheets 001-042."""
import csv
import hashlib
from collections import Counter
from pathlib import Path

base = Path(__file__).resolve().parents[1]
out = Path(__file__).resolve().parent

# S: flux step/reset dominates; V: broad continuous variability; N: noise or
# rapid oscillations; A: localized but ambiguous; R: repeated discrete trough.
# One eight-character string per sheet, in plotted row order.
codes = [
    'SVVNVVSS', 'VVSSVVSS', 'SSNVVSSS', 'VASSASVV',
    'SSSSSSSN', 'SSVSSSSS', 'VVVVVVAS', 'SSVVVVSS',
    'VSVSSVVS', 'SSSSNNVS', 'SSSSNSSS', 'SSSSVSSS',
    'SVVSSNSS', 'SSSSSSSS', 'VVSSS SVS'.replace(' ', ''),
    'VSVSSVSS', 'NSVSSNVV', 'VSSSVSSN', 'VS S NSSSS'.replace(' ', ''),
    'ASSASSSV', 'SVS VSNSS'.replace(' ', ''), 'SSASSVVA',
    'VVSSSSSV', 'SSVSSSNS', 'SSSSSSVV', 'SSNS S NSV'.replace(' ', ''),
    'NSSSSVNS', 'VSSVSSSV', 'VVSSVNSN', 'VVS SSSSS'.replace(' ', ''),
    'SSVNS SSS'.replace(' ', ''), 'SSSSSSSS', 'SSSSSSVS',
    'SSS NNVRS'.replace(' ', ''), 'VSSVVS SS'.replace(' ', ''),
    'SSSSSSSS', 'VN VSSSVS'.replace(' ', ''), 'VVVVSSSS',
    'SSSVVSSN', 'SSSSSSSS', 'SNNSN NSS'.replace(' ', ''),
    'VSSSSSSS',
]
assert len(codes) == 42, len(codes)
assert all(len(x) == 8 for x in codes), [(i+1,len(x)) for i,x in enumerate(codes) if len(x)!=8]

special = {
  5: ('A','Sector 94 has a localized V, but sector 104 is a gap edge and sector 67 a broad trough.', 'low'),
  16: ('A','Two sharp-looking troughs in sectors 100/101 coincide with changes in baseline and reset edges.', 'low'),
  24: ('A','Sector 101 and 63 show local dips but both meet abrupt recoveries; sector 10 is shallow.', 'low'),
  29: ('A','Sector 44 has a flat-bottomed depression, but 45/46 include steps and broad drift.', 'medium'),
  67: ('A','Sectors 7/8 show shallow localized dips amid comparable short-timescale variability.', 'medium'),
  71: ('A','Three narrow depressions near the selected centers, with other fluctuations at similar scale.', 'medium'),
  142: ('A','Sector 85 shows a very narrow dip; other selected windows are broad slopes without a clean counterpart.', 'low'),
  144: ('A','Sectors 19/25 have narrow selected depressions but sparse points and nearby variability.', 'medium'),
  159: ('A','Two sectors show shallow centered troughs; surrounding undulations are comparable.', 'low'),
  166: ('A','Selected sector 86 dip is broad and partly on a rising baseline; sector 19 is sparse.', 'low'),
  168: ('R','Sectors 7, 88 and 61 show centered narrow dips on relatively flat local baselines.', 'high'),
  171: ('A','Three selected shallow dips are localized, but sector 34 also rises immediately afterward.', 'medium'),
  175: ('A','Three selected narrow troughs, clearest in sector 88, sit amid modest extra variability.', 'high'),
  191: ('A','Two sparse windows suggest short dips but individual event sampling is weak.', 'low'),
  203: ('A','Sector 37 has a short dip-like cluster; sectors 99/11 appear dominated by steps or sparse points.', 'low'),
  206: ('A','Repeated sharp troughs appear, but other deep dips recur within each window on a shorter timescale.', 'medium'),
  209: ('A','Deep narrow dips near centers in three sectors, with other large fluctuations and sparse sampling.', 'medium'),
  215: ('R','All three sectors show isolated, narrow, centered troughs against nearly level local baselines.', 'high'),
  219: ('A','Three narrow low clusters near selected times, but each is shallow relative to local scatter.', 'medium'),
  224: ('A','Centered dips repeat in three windows, though broad oscillations have comparable amplitude.', 'medium'),
  275: ('A','Sectors 2 and 1 have centered dips; sector 96 recovery is a sharp reset-like edge.', 'low'),
  271: ('R','Sectors 76, 83 and 55 show similarly shaped, centered U-like depressions.', 'high'),
  298: ('A','Three sectors show selected troughs, but multiple other broad undulations are similarly deep.', 'medium'),
  303: ('A','Two short centered troughs plus a sector 99 level change; event identity is unclear.', 'medium'),
}

reason = {
 'S':'Selected low flux meets an abrupt level change or gap-edge recovery; morphology is dominated by a reset.',
 'V':'Selected trough is part of broad continuous or roughly sinusoidal variability, with other similar minima nearby.',
 'N':'Local scatter or rapid oscillations are comparable to the selected depression; no isolated event stands out.',
 'A':'A localized depression is present, but the three plotted windows do not show a clean repeat.',
 'R':'Centered discrete troughs repeat in the displayed raw windows; raw event checks are warranted.',
}
category = {'S':'screening_step_or_gap','V':'screening_broad_variability','N':'screening_noise_or_oscillation','A':'ambiguous_prospect','R':'repeated_discrete_trough'}
priority = {'S':'none','V':'none','N':'none','A':'low','R':'high'}

with (base/'queue.csv').open(newline='',encoding='utf-8-sig') as f:
    q = list(csv.DictReader(f))
rows=[]
for row in q:
    if row['arm'] != 'first': continue
    i = int(row['triage_id'][1:])
    assert 1 <= i <= 336
    assert row['sheet'] == f'sheet-{(i-1)//8+1:03d}.png'
    c = codes[(i-1)//8][(i-1)%8]
    why, pri = reason[c], priority[c]
    if i in special:
        c, why, pri = special[i]
    rows.append(dict(tic=row['tic'],triage_id=row['triage_id'],category=category[c],reason=why,sheet=row['sheet'],followup_priority=pri))
assert len(rows)==336 and len({r['tic'] for r in rows})==336
assert [r['triage_id'] for r in rows] == [f'M{i:03d}' for i in range(1,337)]
with (out/'first-visual-triage.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

shortlist = [215,168,271,175,171,29,67,71,144,206,209,219,224,298,303,159,24,142,275,191]
assert len(shortlist)==20 and len(set(shortlist))==20
with (out/'first-shortlist.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['rank']+list(rows[0])); w.writeheader()
    for rank,i in enumerate(shortlist,1): w.writerow(dict(rank=rank,**rows[i-1]))

for p in [base/'queue.csv',base/'display-receipts.json',out/'first-visual-triage.csv',out/'first-shortlist.csv']:
    print(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
print(Counter(r['category'] for r in rows))
