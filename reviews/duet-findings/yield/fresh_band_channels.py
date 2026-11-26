"""Which screening channel found the G 11.5-12 eclipsing binaries: the appointment windows or the period-free dip harvest.

Every science target of the five fresh-band cohorts was screened twice: appoint.py searched the windows at Gaia's
predicted conjunctions (appointment-results/, summarised as appointment_shape_pass by triage_fresh*.py), and
bulk_events.py harvested the strongest local dips in each sector with no period (bulk-results/, dip_flag_sectors).
The visual sheets that chose the review leads plot only harvest dip windows (triage_fresh*.py). This script counts the
finds by channel and tests the unreviewed appointment-only passes for dips repeating at a fixed offset from Gaia's
conjunction: two same-kind window best events with SNR >= 10, offsets within 0.25 d, depths within a factor 1.6 and
at least a day apart, scored at zero lag and at control lags of 0.75-5 d.

Run from the repository root after fresh_band_yield.py: python3 reviews/duet-findings/yield/fresh_band_channels.py
Writes fresh-band-channels-output.txt here.
"""
import glob, itertools, json, os
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
LAGS = [0, 0.75, 1.5, 2.25, 3, 4, 5]

def pair_score(j, lag, snrmin=10, dt=0.25, dfac=1.6):
    best = 0
    for kind in 'AB':
        ev = [(w['tc'], w['best']) for w in j.get('windows', []) if w['kind'] == kind and w.get('best') and w['best']['snr'] >= snrmin]
        for (tc1, b1), (tc2, b2) in itertools.combinations(ev, 2):
            o1, o2 = b1['t'] - tc1, b2['t'] - tc2
            if (min(abs(o1 - o2 - lag), abs(o2 - o1 - lag)) < dt and abs(b1['t'] - b2['t']) > 1 and
                    max(b1['depth_ppm'], b2['depth_ppm'])/max(1, min(b1['depth_ppm'], b2['depth_ppm'])) < dfac):
                best = max(best, min(b1['snr'], b2['snr']))
    return best

def main():
    y = pd.read_csv(os.path.join(HERE, 'fresh-band-yield.csv'), dtype={'tic': str})
    y['found'] = (y.accepted.fillna('') != '') & ~y.off_gaia_period.astype(bool)
    fs = [f for f in glob.glob('reviews/2026-11-05-*/fresh-band*/screening-summary.csv') if 'stage1' not in f]
    s = pd.concat([pd.read_csv(f, dtype={'tic': str}) for f in fs]); s = s[s.control == False].drop_duplicates('tic')
    import collections
    res = {}
    for f in glob.glob('reviews/2026-11-05-*/fresh-band*/appointment-results/*.json'):
        if 'stage1' in f: continue
        j = json.load(open(f)); res[str(j['tic'])] = j
    m = y.merge(s[['tic', 'appointment_shape_pass', 'dip_flag_sectors']], on='tic')
    m['app'] = m.appointment_shape_pass.astype(bool); m['dip'] = m.dip_flag_sectors > 0
    for l in LAGS:
        m[f'lag{l}'] = [pair_score(res[t], l) >= 10 if t in res else False for t in m.tic]
    out = open(os.path.join(HERE, 'fresh-band-channels-output.txt'), 'w')
    print(f'{len(m)} science targets; appointment test passed by {m.app.sum()} ({m.app.mean():.0%}), '
          f'period-free dip flag on {m.dip.sum()} ({m.dip.mean():.0%})', file=out)
    print('\nfinds at Gaia\'s period by channel (rows: appointment pass; columns: dip flag):', file=out)
    print(pd.crosstab(m[m.found].app, m[m.found].dip).to_string(), file=out)
    fail = m[m.found & ~m.app].merge(s[['tic', 'appointment_reasons']], on='tic')
    c = collections.Counter(x for r_ in fail.appointment_reasons for x in r_.split(';'))
    print(f'\nfinds failing the appointment test: {len(fail)}; reasons {dict(c)}', file=out)
    print('pass rate by predicted group: ' + ', '.join(f'{g_} {v:.2f}' for g_, v in m[m.found].groupby('group').app.mean().items()), file=out)
    print('\nrepeated same-offset dip pairs (SNR >= 10) at zero lag and at control lags 0.75-5 d:', file=out)
    groups = [('finds', m.found), ('appointment only, not found', m.app & ~m.dip & ~m.found),
              ('dip only, not found', ~m.app & m.dip & ~m.found), ('both, not found', m.app & m.dip & ~m.found),
              ('neither', ~m.app & ~m.dip)]
    for lab, sel in groups:
        c = [int(m[sel][f'lag{l}'].sum()) for l in LAGS]
        print(f'  {lab:28s} {int(sel.sum()):5d} targets: zero lag {c[0]:3d}, control lags {min(c[1:])}-{max(c[1:])} '
              f'(mean {np.mean(c[1:]):.1f})', file=out)
    out.close(); print(open(os.path.join(HERE, 'fresh-band-channels-output.txt')).read())

if __name__ == '__main__':
    main()
