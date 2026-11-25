"""Run 11a(ii): what stands behind "no secondary" in run 10a's excluded rows.
Run from the repository root:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run11-ledger/twins_premise.py > .../twins-premise-output.txt
Writes twins-premise.csv next to this script.
"""
import pandas as pd, numpy as np, os
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
here = os.path.dirname(os.path.abspath(__file__))
t = pd.read_csv(D + 'run10-twins-and-r1003/equal-dips-2P-test.csv').set_index('review_id')
e = pd.read_csv(D + 'run10-twins-and-r1003/earthshine-pop-results-855.csv').set_index('review_id')
v = pd.read_csv(D + 'run10-twins-and-r1003/earthshine-vet-2p-855.csv').set_index('review_id')
h = pd.read_csv('reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv').set_index('review_id')
ex = t[t.P_excluded_default.astype(str) == 'True'].copy()
ex['strict'] = ex.P_excluded_strict.astype(str) == 'True'
for c in ['sec_phase', 'sec_depth_ppt', 'sec_depth_err_ppt', 'sec_T14_h', 'T14_fit_h', 'sec_real']:
    ex[c] = e[c].reindex(ex.index)
ph = ex.sec_phase
# Earthshine's free secondary search "locked" on the primary: best feature at phase ~0, or as deep as the primary
ex['search_locked'] = (np.minimum(ph, 1 - ph) < 0.05) | (ex.sec_depth_ppt > 0.5 * ex.depth_fit_ppt)
# an eclipse-shaped secondary: duration within a factor 2 of the primary's
ex['sec_eclipse_shaped'] = (ex.sec_T14_h / ex.T14_fit_h).between(0.5, 2)
ex['sec_reaches_pred'] = (~ex.search_locked) & ex.sec_eclipse_shaped & (ex.sec_depth_ppt >= 0.5 * ex.sec_pred_ppt) \
                         & (ex.sec_depth_ppt > 3 * ex.sec_depth_err_ppt)
vis = h.visual_reason.reindex(ex.index).fillna('')
neg = vis.str.contains(r'no (?:clear |convincing |corresponding |obvious |visible |distinct )?secondar|flat secondary', case=False)
ex['visual_mentions_secondary'] = vis.str.contains(r'secondar|weaker|shallower|between primar', case=False) & ~neg
ex['visual_reason'] = vis
ex['parity'] = v.verdict.reindex(ex.index)
ex['pdouble_note'] = h.period_resolution.reindex(ex.index).str.extract(r'(pdouble:.*)$')[0]
ex.to_csv(os.path.join(here, 'twins-premise.csv'))
n = len(ex); s = ex.strict
print(f'run 10a rows with P excluded (default): {n}; strict: {s.sum()}')
print(f'Earthshine search locked on the primary: {ex.search_locked.sum()} ({(ex.search_locked & s).sum()} strict)')
print(f'  -> for these "no secondary" rests on the review text alone')
print(f'searched rows with an eclipse-shaped secondary reaching half the minimum prediction: {ex.sec_reaches_pred.sum()}')
print(f'visual note reports a secondary-like feature: {ex.visual_mentions_secondary.sum()} ({(ex.visual_mentions_secondary & s).sum()} strict)')
print()
cols = ['strict', 'excl_ratio', 'sec_pred_ppt', 'search_locked', 'sec_phase', 'sec_depth_ppt', 'parity']
pd.set_option('display.width', 220); pd.set_option('display.max_colwidth', 120)
w = ex[ex.visual_mentions_secondary | ex.sec_reaches_pred]
print(w[cols].round(3).to_string())
print()
for rid, r in w.iterrows():
    print(rid, '|', r.visual_reason, '|', r.pdouble_note if isinstance(r.pdouble_note, str) else '')
