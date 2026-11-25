"""Run 13e: R systems kept at probable for Gaia conjunction tension, against the A sample's own spread.
How many of the paper's A systems (same-period, SB1/SB2 with corr_vec) are at least as far from Gaia's conjunction?
Run from the repository root after a_epoch_test.py and run 12's gaia_epoch_test.py:
  python3 reviews/2026-11-24-duet-research-runs-1-4/run13-a-sample-gaia-epoch/r_tension_vs_a.py
"""
import pandas as pd
D = 'reviews/2026-11-24-duet-research-runs-1-4/'
a = pd.read_csv(D + 'run13-a-sample-gaia-epoch/a-epoch-test.csv'); a = a[a.note.isna()]
tiers = pd.read_csv('accepted-systems.csv', dtype=str).set_index('review_id').tier
a['tier'] = a.review_id.map(tiers)
r = pd.read_csv(D + 'run12-gaia-tiering/gaia-epoch-test.csv')
q = r[r.gaia_tension_named & (r.z_period.abs() < 3)]
print(f'A sample: {len(a)} systems ({(a.tier == "confirmed").sum()} confirmed)')
print('R systems with a named Gaia tension and period within 3 sigma:')
for _, x in q.sort_values('review_id').iterrows():
    fT = (a.z_tess_full.abs() >= abs(x.z_tess)).mean(); fG = (a.z_full.abs() >= abs(x.z_gaia_epoch)).mean()
    cT = ((a.z_tess_full.abs() >= abs(x.z_tess)) & (a.tier == 'confirmed')).sum()
    print(f'  {x.review_id} ({x.tier}): z at TESS {x.z_tess:+.2f}, at Gaia epoch {x.z_gaia_epoch:+.2f} (phase {x.phase_gaia_epoch:+.4f});'
          f' A systems as far or farther: {fT:.0%} at TESS ({cT} of them confirmed), {fG:.0%} at Gaia epoch')
