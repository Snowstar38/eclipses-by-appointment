"""G: Gaia DR3 period errors, SB1 against SB2, on the appointment sample (tier-blind).
Run from the repository root after a_epoch_test.py:
  python3 reviews/duet-findings/gaia-errors/sb1_vs_sb2_periods.py
"""
import sys, math
import numpy as np, pandas as pd

def fisher_greater(a, b, c, d):
    """One-sided Fisher exact p for [[a, b], [c, d]]: chance of a or more in row 1 given the margins."""
    n1, k, N = a + b, a + c, a + b + c + d
    return sum(math.comb(k, x) * math.comb(N - k, n1 - x) for x in range(a, min(k, n1) + 1)) / math.comb(N, n1)
D = 'reviews/duet-findings/'
sys.path.insert(0, D)
import window_covariance as W
a = pd.read_csv(D + 'gaia-errors/a-epoch-test.csv'); a = a[a.note.isna()]
print('period pull z = (P_Gaia - P_eclipse) / sqrt(sigma_Gaia^2 + sigma_eclipse^2), 184 same-period A systems')
out = {}
for s in ('SB1', 'SB2'):
    q = a[a.sol == s]; z = q.z_period
    n3 = int((z.abs() >= 3).sum()); out[s] = (n3, len(q))
    # the error scale that makes the core Gaussian, and the scale needed so that only 0.27% exceed 3 sigma
    print(f'  {s}: n {len(q)}, robust sd {W.robust_sd(z):.2f}, |z|>=2 {int((z.abs()>=2).sum())}, |z|>=3 {n3} ({n3/len(q):.1%}):'
          f' {", ".join(q[z.abs()>=3].sort_values("review_id", key=lambda c: c.str[1:].astype(int)).review_id)}')
(a1, n1), (a2, n2) = out['SB1'], out['SB2']
print(f'  SB2 more often >=3 sigma than SB1: one-sided Fisher p = {fisher_greater(a2, n2-a2, a1, n1-a1):.1e}')
for s in ('SB1', 'SB2'):
    z = a[a.sol == s].z_period.abs().values
    k = next(k for k in np.arange(1, 10, 0.05) if np.mean(z / k >= 3) <= 0.0027 * 3)  # allow 3x the Gaussian rate
    print(f'  {s}: error inflation needed so that no more than 0.8% exceed 3 sigma: x{k:.2f}')

# does Gaia's own goodness_of_fit flag the bad periods?
n = pd.read_csv(D + 'gaia-errors/fable51-nss-appointments.csv')
n = n[n.nss_solution_type.isin(['SB1', 'SB2'])].drop_duplicates('review_id')
m = a.merge(n[['review_id', 'goodness_of_fit']], on='review_id'); m['bad'] = m.z_period.abs() >= 3
print('\nGaia goodness_of_fit (F2) and the period failures:')
for s, cut in (('SB1', 2), ('SB2', 10)):
    q = m[m.sol == s]; hi, lo = q[q.goodness_of_fit > cut], q[q.goodness_of_fit <= cut]
    print(f'  {s}: median F2 {q[~q.bad].goodness_of_fit.median():.2f} (period ok) vs {q[q.bad].goodness_of_fit.median():.2f} (>=3 sigma);'
          f' F2 > {cut}: {int(hi.bad.sum())}/{len(hi)} fail, F2 <= {cut}: {int(lo.bad.sum())}/{len(lo)};'
          f' one-sided Fisher p = {fisher_greater(int(hi.bad.sum()), len(hi)-int(hi.bad.sum()), int(lo.bad.sum()), len(lo)-int(lo.bad.sum())):.3f}')
