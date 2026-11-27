"""Which automated cut of the appointment search rejected each period-free find at Gaia's period.

periodfree-cut-audit.csv (Sol) holds, for the 31 main-search targets whose period-free find has an eclipse period
within 0.5% of Gaia's, the appointment search's own saved values for that star (results.jsonl on the house disk)
and the cuts of the frozen triage rules they fail: SNR < 8 (faint), far ratio outside [0.6, 1.6] (far), any null
window reaching the event (null), z < 8 where a null exists (lowz), and the triage script's 14-h maximum box with
a far ratio more than 0.25 from 1 (maxbox). This script tallies them.

Run from the repository root: python3 reviews/duet-findings/yield/periodfree_cuts.py
Needs pandas. Writes periodfree-cuts-output.txt here.
"""
import os, sys
sys.dont_write_bytecode = True
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    s = pd.read_csv(os.path.join(HERE, 'periodfree-cut-audit.csv'), dtype={'tic': str, 'failed_cuts': str}, keep_default_na=False,
                    na_values={'z': [''], 'null_exceed': [''], 'far': ['']})
    cuts = ['null', 'maxbox', 'far', 'lowz', 'faint']
    for c in cuts: s[c] = s.failed_cuts.str.split(';').apply(lambda x: c in x)
    out = open(os.path.join(HERE, 'periodfree-cuts-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    P_(f'{len(s)} period-free finds at Gaia\'s period on main-search targets; pass every automated cut: '
       f'{", ".join(s.review_id[s.failed_cuts == "PASS"])}')
    P_('failing each cut (a find can fail several): ' + ', '.join(f'{c} {int(s[c].sum())}' for c in cuts))
    P_('failing only one cut: ' + ', '.join(f'{c} {int((s[c] & (s[cuts].sum(axis=1) == 1)).sum())}' for c in cuts))
    paper = s[['null', 'far', 'lowz', 'faint']].any(axis=1)
    P_(f'failing one of the paper\'s own cuts (null window, far ratio, z, SNR): {int(paper.sum())}; only the triage script\'s maximum box: '
       f'{", ".join(s.review_id[~paper & s.maxbox])}')
    nv = s[s.null]
    P_(f'null-window vetoes: {len(nv)}; with z >= 8 {int((nv.z >= 8).sum())}, z < 8 {int((nv.z < 8).sum())}, z blank {int(nv.z.isna().sum())}; '
       f'null windows reaching the event: median {nv.null_exceed.median():.0f} of 40 '
       f'({nv[nv.z >= 8].null_exceed.median():.0f} where z >= 8, {nv[nv.z < 8].null_exceed.median():.0f} where z < 8)')
    P_('null vetoes with z >= 8: ' + ', '.join(f'{r.review_id} (z {r.z:.0f}, {int(r.null_exceed)} of 40)' for r in nv[nv.z >= 8].sort_values('z', ascending=False).itertuples()))
    P_('\nby band:'); P_(s.groupby('band')[cuts].sum().assign(finds=s.groupby('band').size()).to_string())
    out.close()
    fn = os.path.join(HERE, 'periodfree-cuts-output.txt'); print(open(fn).read())


if __name__ == '__main__':
    main()
