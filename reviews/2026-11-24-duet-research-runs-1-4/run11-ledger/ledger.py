"""Run 11a: one ledger of the host-table changes Duet's runs 1-10 proposed,
checked against the current host table, with cross-run conflicts flagged.
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run11-ledger/ledger.py
"""
import pandas as pd, numpy as np, sys
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
h = pd.read_csv('reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv').set_index('review_id')
acc = set(pd.read_csv('accepted-systems.csv').review_id)
rows = []
def add(rid, src, col, proposed, why):
    cur = h.loc[rid, col] if (rid in h.index and col in h.columns) else np.nan
    rows.append(dict(review_id=rid, source=src, column=col, current=cur,
                     proposed=proposed, reason=why))

# run 1 (Nov 23 audit): column flags
c1 = pd.read_csv(D + 'nov23-column-flags.csv')
for r in c1.itertuples():
    add(r.review_id, 'run1', 'secondary_phase/secondary_depth_ppt' if 'secondary' in r.check else r.check,
        r.suggestion, r.check)

# run 5 + Earthshine parity: firm 2P
for rid in ['R991', 'R1084', 'R1120', 'R1529']:
    P = h.loc[rid, 'adopted_period_days']
    add(rid, 'run5+Earthshine parity', 'adopted_period_days', 'x2 (twin solution, unequal eclipses)',
        f'TCE period is 2P and Earthshine odd/even confirms (adopted {P})')
# R1117 (errata, Fable; run 9d)
add('R1117', 'errata+Fable (run9d)', 'adopted_period_days', 2.636664, 'B shallower in 27 of 27 sectors')
# R1684, R1737
add('R1684', 'run6b', 'adopted_period_days', 'x2', '"shallower secondary visible in the 2P fold"')
add('R1737', 'run10a+Earthshine', 'adopted_period_days', 80.93, 'Earthshine favours 80.93 d; 252-ppt eclipse needs a 96-ppt secondary at 40.46 d')

# run 6a: secondary column flags
f6 = pd.read_csv(D + 'run6-secondary-columns/secondary-column-flags.csv')
for r in f6.itertuples():
    add(r.review_id, 'run6a', 'secondary_phase/secondary_depth_ppt', 'blank or refit', r.flags)
# run 6b: secondary seen, not tabled -> P is the orbit
s6 = pd.read_csv(D + 'run6-secondary-columns/secondary-seen-not-tabled.csv')
six_b = set(s6.review_id)
for r in s6.itertuples():
    add(r.review_id, 'run6b', 'period_resolution', 'P: secondary seen in the visual review; drop 2P alternative',
        f'visual note: {r.visual_note}')

# run 10a: twins
t = pd.read_csv(D + 'run10-twins-and-r1003/equal-dips-2P-test.csv')
for r in t.itertuples():
    if r.P_excluded_strict is True or str(r.P_excluded_strict) == 'True':
        add(r.review_id, 'run10a strict', 'adopted_period_days', round(2 * r.P_d, 7), f'excl_ratio {r.excl_ratio:.1f}')
    elif str(r.P_excluded_default) == 'True':
        add(r.review_id, 'run10a default', 'period_resolution', '2P favoured (run 10a)', f'excl_ratio {r.excl_ratio:.1f}')
    if str(r.sb2_text_prefers_2P) == 'True':
        add(r.review_id, 'run10a SB2 text', 'adopted_period_days', round(2 * r.P_d, 7), 'row text prefers 2P (SB2 twin)')

L = pd.DataFrame(rows)
L['in_accepted'] = L.review_id.isin(acc)
L['in_host_table'] = L.review_id.isin(h.index)

# applied? a 2P proposal counts as applied if the current period is already ~2x the
# period the proposing run saw
def applied(r):
    if r.column == 'adopted_period_days' and r.review_id in h.index:
        cur = float(h.loc[r.review_id, 'adopted_period_days'])
        try: target = float(r.proposed)
        except ValueError: return 'no' if 'x2' in str(r.proposed) else ''
        return 'yes' if abs(cur / target - 1) < 1e-3 else 'no'
    return ''
L['applied'] = L.apply(applied, axis=1)

# conflicts: rows where one run says P is the orbit (secondary seen) and another says 2P
twoP = set(L[(L.column == 'adopted_period_days') & L.proposed.astype(str).str.contains(r'x2|\.')].review_id) \
     | set(L[L.source == 'run10a default'].review_id)
conf = sorted(six_b & twoP, key=lambda s: int(s[1:]))
L['conflict'] = L.review_id.isin(conf)

# run 11a's reading of each conflict (see README): what the evidence in the repo supports now
RES = {
 'R1684': 'P is the orbit: Earthshine finds an eclipse-shaped 1.7 +- 0.1 ppt secondary at phase 0.520 (3.9 h vs 3.6 h primary) and equal alternate primaries (28.5 vs 28.6 ppt); run 6b\'s x2 is withdrawn; fill secondary columns',
 'R1253': '2P stands on parity (Earthshine 37 sigma, odd deeper in 5 of 7 sectors), but alternate eclipses differ by 2.5%: not twins',
 'R1697': '2P stands: Earthshine searched (best 0.7 ppt at phase 0.39 against >= 44 ppt needed at P); the visual "secondary" is the alternate eclipse of the 2P fold (odd/even 99.9 vs 76.0 ppt): not twins',
 'R1405': 'open: phase-0.5 events median 26.6 ppt (20/21 > 3 sigma), stacked 11.5 ppt, against 14.6 ppt needed at P; P cannot be excluded; take off run 10a strict list',
 'R1352': 'open: Earthshine search locked on the primary; reviewer saw a "shallower secondary between primaries"; take off run 10a strict list until the sheet is read',
 'R1042': 'open: reviewer saw a "weaker secondary"; Earthshine best feature 13.4 ppt at phase 0.60 is 78 h wide (not eclipse-shaped); take off run 10a strict list until the sheet is read',
 'R1488': 'leans 2P (odd/even mid-times differ 9.5 min, 49 sigma, but per-sector signs disagree); Earthshine search locked; keep as "2P favoured", not strict',
 'R1040': 'P not excluded by run 10a (ratio 0.19); SB2 text prefers 2P but the reviewer saw a "weaker feature at the secondary phase", which is what the SB2 argument asks for; leave P and fill secondary from a fit',
}
L['run11_reading'] = L.review_id.map(RES).fillna('')
L.sort_values(['review_id', 'source'], key=lambda s: s.map(lambda v: int(v[1:]) if isinstance(v, str) and v[1:].isdigit() else v) if s.name=='review_id' else s).to_csv(sys.argv[1] if len(sys.argv) > 1 else 'ledger.csv', index=False)

print('proposals:', len(L), 'rows touched:', L.review_id.nunique())
print(L.groupby('source').size().to_string())
p = L[L.column == 'adopted_period_days']
print('\nperiod proposals:', len(p), 'distinct rows:', p.review_id.nunique(),
      'applied:', (p.applied == 'yes').sum())
print('rows no longer in accepted-systems:', sorted(set(L[~L.in_accepted].review_id)))
print('\nCONFLICTS (run 6b says a secondary was seen at P; another run says 2P):', conf)
for rid in conf:
    for r in L[L.review_id == rid].itertuples():
        print(' ', rid, r.source, r.column, r.proposed, '|', str(r.reason)[:90])
