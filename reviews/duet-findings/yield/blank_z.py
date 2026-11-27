"""Why the appointment test's z is blank: room for the null outside the predicted windows.

z = (SNR - null median)/MAD needs a null of random windows "outside every predicted window". The fresh-band
(G 11.5-12) appointment-results JSONs save the null summary (n windows placed, median, MAD) and each window's
half-width; the main-search rows (Fable 5.1) give z, and Fable 5.1's window half-widths give each main-search
target's two conjunction windows. The quantity tested is the room left in one orbit, in window widths:
    room = (P - 2 hw_A - 2 hw_B) / (2 mean(hw)).

Run from the repository root: python3 reviews/duet-findings/yield/blank_z.py
Needs numpy and pandas. Writes blank-z-output.txt here.
"""
import glob, json, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = 'reviews/2026-11-26-fable51-main-search-gaia/main-search-gaia-rows.csv'
HW = 'reviews/duet-findings/gaia-errors/fable51-window-halfwidths.csv'
BINS = [-0.01, 0.5, 1, 1.5, 2, 3, 5, 1000]
PAPER_NO_Z = {'A27', 'A37', 'A40', 'A42', 'A51', 'A54', 'A64'}   # Coverage paragraph: never faced the z test

def fresh():
    rows = []
    for g in glob.glob('reviews/2026-11-05-*/fresh-band*/appointment-results/*.json'):
        if 'stage1' in g: continue
        d = json.load(open(g))
        if d.get('control'): continue
        ws = d.get('windows') or []
        if not ws: continue
        nl = d.get('null') or {}
        hk = {}
        for w in ws: hk.setdefault(w.get('kind'), []).append(w['hw'])
        P = d['P_gaia']; tot = sum(2 * np.median(v) for v in hk.values()); hm = np.mean([np.median(v) for v in hk.values()])
        rows.append(dict(null=bool(nl), n=nl.get('n', 0), mad0=nl.get('mad') == 0, z=d.get('z'), room=max(P - tot, 0) / (2 * hm)))
    return pd.DataFrame(rows)

def main():
    out = open(os.path.join(HERE, 'blank-z-output.txt'), 'w')
    P_ = lambda *a: print(*a, file=out)
    f = fresh(); f['rb'] = pd.cut(f.room, BINS)
    P_(f'G 11.5-12 appointment results: {len(f)} science stars with windows; null placed for {f.null.sum()}, '
       f'all 40 null windows for {(f.n == 40).sum()}; z defined for {f.z.notna().sum()}')
    t = f.groupby('rb', observed=True).agg(stars=('null', 'size'), null_placed=('null', 'mean'), all_40=('n', lambda x: (x == 40).mean()),
                                           mad_0=('mad0', 'mean'), z_defined=('z', lambda x: x.notna().mean()))
    P_('\nby room outside the windows (window widths per orbit):'); P_(t.round(2).to_string())
    nn = f[f.null]
    t = nn.groupby(pd.cut(nn.n, [0, 10, 20, 30, 39, 40]), observed=True).mad0.agg(['size', 'mean'])
    P_('\nstars with a null: MAD = 0 by null windows placed'); P_(t.round(2).to_string())
    f40 = nn[nn.n == 40]
    t = f40.groupby(pd.cut(f40.room, [0, 1.5, 2, 3, 5, 1000]), observed=True).mad0.agg(['size', 'mean'])
    P_('\nstars with all 40 null windows: MAD = 0 by room'); P_(t.round(2).to_string())

    h = pd.read_csv(HW)
    g = h.groupby('source_id').agg(P=('P_d', 'first'), hsum=('halfwidth_independent_d', 'sum'), hm=('halfwidth_independent_d', 'mean'))
    m = pd.read_csv(ROWS, dtype={'tic': str})
    m = m[(m.band != 'G11-11.5') & m.veb.isna()].merge(g, left_on='source_id', right_index=True, how='left')
    m['room'] = (m.P - 2 * m.hsum).clip(lower=0) / (2 * m.hm); m['blank'] = m.z.isna()
    P_(f'\nmain search, G < 11 science rows: {len(m)}; z blank for {m.blank.sum()} (the paper counts 165 with no null and 591 with MAD = 0, 756); '
       f'window half-widths for {m.room.notna().sum()}')
    t = m.groupby(pd.cut(m.room, BINS), observed=True).blank.agg(stars='size', z_blank='mean', blank_n='sum')
    P_('\nby room outside the windows:'); P_(t.round(2).to_string())
    P_(f'room under 1.5 window widths: {(m.room <= 1.5).sum()} rows, {m[m.room <= 1.5].blank.sum()} blank '
       f'({m[m.room <= 1.5].blank.sum() / max(m.blank[m.room.notna()].sum(), 1):.0%} of the blank rows with half-widths)')
    # the same stars under 'overlap' placement (the G 11.5-12 search's mode): its z-defined rate by room, applied to the main-search rooms
    fz = f.groupby(pd.cut(f.room, BINS), observed=True).z.apply(lambda x: x.notna().mean())
    mz = m.groupby(pd.cut(m.room, BINS), observed=True).blank.agg(['size', lambda x: 1 - x.mean()])
    mz.columns = ['stars', 'z_defined_centre']; mz['z_defined_overlap'] = fz
    ex = (mz.stars*mz.z_defined_overlap).sum(); n = mz.stars.sum()
    P_('\nz defined by room, main search (centre placement) against the G 11.5-12 rate (overlap placement):'); P_(mz.round(2).to_string())
    P_(f"if the G < 11 rows' nulls were placed as in the G 11.5-12 search: z defined for {ex:.0f} of {n} ({ex/n:.0%}) against "
       f"{int((~m.blank[m.room.notna()]).sum())} ({(~m.blank[m.room.notna()]).mean():.0%}) as run")
    t = m.groupby('nss_solution_type').agg(rows=('blank', 'size'), z_blank=('blank', 'mean'), room_median=('room', 'median'))
    P_('\nby Gaia solution type:'); P_(t.round(2).to_string())
    a = pd.read_csv('accepted-systems.csv', dtype=str)[['review_id', 'tic']]
    s = m.merge(a, on='tic'); A = s[s.review_id.str.match(r'^A\d+$', na=False)]
    nz = set(A[A.blank].review_id)
    P_(f'\nreported A systems among these rows: {len(A)}; z blank for {sorted(nz, key=lambda x: int(x[1:]))}; '
       f'same as the paper\'s seven: {nz == PAPER_NO_Z}')
    P_(f'their room: ' + ', '.join(f'{r.review_id} {r.room:.2f}' for r in A[A.blank].sort_values('room').itertuples()))
    P_(f'reported A systems per 1,000 rows: z blank {1e3 * len(nz) / m.blank.sum():.1f}, z defined {1e3 * (len(A) - len(nz)) / (~m.blank).sum():.1f}')
    out.close()
    fn = os.path.join(HERE, 'blank-z-output.txt')
    txt = '\n'.join(l.rstrip() for l in open(fn).read().split('\n')); open(fn, 'w').write(txt); print(txt)

if __name__ == '__main__':
    main()
