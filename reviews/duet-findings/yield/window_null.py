"""The appointment test's null against the number of windows.

The test takes the best event over all of a star's conjunction windows and compares it with "the same statistic
in 40 random windows on the same star outside every predicted window" (z = (SNR - null median)/MAD, a candidate
needing no null window to reach it and z >= 8 where a null exists). The fresh-band appointment-results JSONs
save each window's own best event and the null summary, so they show which statistic the null holds; the
main-search rows (Fable 5.1) give z and the window count for the 6,357 G < 11.5 targets.

Run from the repository root: python3 reviews/duet-findings/yield/window_null.py
Needs numpy and pandas. Writes window-null-output.txt here.
"""
import glob, importlib.util, json, os, sys
sys.dont_write_bytecode = True
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BINS = [0, 3, 6, 10, 20, 1000]

def fresh():
    rows = []
    for g in glob.glob('reviews/2026-11-05-*/fresh-band*/appointment-results/*.json'):
        if 'stage1' in g: continue
        d = json.load(open(g)); ws = d.get('windows') or []; nl = d.get('null') or {}
        wb = [w['best']['snr'] for w in ws if (w.get('best') or {}).get('snr') is not None]
        rows.append(dict(tic=str(d['tic']), control=bool(d.get('control')), nwin=len(wb), best=(d.get('best') or {}).get('snr'),
                         wmed=np.median(wb) if wb else np.nan, nmed=nl.get('med'), nmad=nl.get('mad'), nmax=nl.get('max'),
                         nn=nl.get('n'), z=d.get('z')))
    r = pd.DataFrame(rows)
    acc = set(pd.read_csv('accepted-systems.csv', dtype=str).tic)
    r['accepted'] = r.tic.isin(acc)
    return r

def main():
    out = open(os.path.join(HERE, 'window-null-output.txt'), 'w')
    P = lambda *a: print(*a, file=out)
    r = fresh()
    s = r[~r.control & ~r.accepted & r.nmed.notna() & (r.nwin > 0)].copy()
    P(f'G 11.5-12 appointment results: {len(r)} stars ({int(r.control.sum())} controls); {len(s)} science stars without an accepted '
      f'eclipse that have a null ({(s.nn == 40).mean():.0%} with all 40 null windows; MAD = 0 for {(s.nmad == 0).mean():.0%})')
    P(f'median over stars of (median of the per-window best SNRs - null median): {(s.wmed - s.nmed).median():+.2f}; '
      f'of (best over all windows - null median): {(s.best - s.nmed).median():+.2f}')
    P('so the null holds the single-window statistic and the tested event is the best of N windows.')
    s = s[s.nmad > 0].copy()
    s['above_null_max'] = s.best > s.nmax
    s['matched'] = s.nwin/(s.nwin + s.nn)   # chance that the best of N exceeds the best of n_null under one shared distribution
    t = s.groupby(pd.cut(s.nwin, BINS), observed=True).agg(stars=('tic', 'size'), z_median=('z', 'median'),
                                                           z_ge_8=('z', lambda x: (x.dropna() >= 8).mean()),
                                                           best_above_every_null=('above_null_max', 'mean'),
                                                           same_shape_expectation=('matched', 'mean'))
    P(f'\nstars without an accepted eclipse and a null with MAD > 0 ({len(s)}), by windows with an event:'); P(t.round(2).to_string())
    acc = set(pd.read_csv('accepted-systems.csv', dtype=str).tic); wr = []
    for g in glob.glob('reviews/2026-11-05-*/fresh-band*/appointment-results/*.json'):
        if 'stage1' in g: continue
        d_ = json.load(open(g)); nl = d_.get('null') or {}
        if d_.get('control') or str(d_['tic']) in acc or nl.get('med') is None: continue
        for w in d_.get('windows') or []:
            b = w.get('best') or {}
            if b.get('snr') is None: continue
            wr.append(dict(snr=b['snr'], dur=b.get('dur_h'), fc=w['frac_covered'], hw=w['hw'], nmax=nl['max']))
    w = pd.DataFrame(wr); w['beats_every_null'] = w.snr > w.nmax
    P(f'\nsingle windows of those stars ({len(w)}): share whose own best event beats every null window')
    for col, bins in [('hw', [0, 2, 4, 7.01]), ('fc', [0, 0.5, 0.95, 1.01])]:
        t = w.groupby(pd.cut(w[col], bins), observed=True).beats_every_null.agg(['size', 'mean'])
        P(f'  by {"half-width (d)" if col == "hw" else "covered fraction"}: ' + ', '.join(f'{k} {v["mean"]:.2f} ({int(v["size"])})' for k, v in t.iterrows()))
    t = w.groupby('dur').beats_every_null.agg(['size', 'mean'])
    P('  by best box (h): ' + ', '.join(f'{k:g} {v["mean"]:.2f} ({int(v["size"])})' for k, v in t.iterrows()))
    P(f'  the 14-h maximum box is the best event in {(w.dur == 14).mean():.0%} of windows')
    spec = importlib.util.spec_from_file_location('sc', os.path.join(HERE, 'significance_channels.py'))
    sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
    d = sc.frame()
    for lab, sel in [('no known eclipser', ~d.anyecl), ('catalogued', d.catalogued), ('appointment finds', d.found)]:
        x = d[sel & d.z.notna()]
        nw = pd.read_csv(sc.msy.ROWS, dtype={'tic': str}).set_index('tic').n_windows
        x = x.assign(nw=x.tic.map(nw))
        t = x.groupby(pd.cut(x.nw, BINS), observed=True).z.agg(stars='size', z_median='median', z_ge_8=lambda v: (v >= 8).mean())
        P(f'\nmain search, {lab} ({len(x)} with z), by covered windows:'); P(t.round(2).to_string())
    out.close()
    fn = os.path.join(HERE, 'window-null-output.txt')
    txt = '\n'.join(l.rstrip() for l in open(fn).read().split('\n'))
    open(fn, 'w').write(txt); print(txt)

if __name__ == '__main__':
    main()
