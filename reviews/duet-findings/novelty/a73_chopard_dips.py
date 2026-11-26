"""Finding 3: the dips Chopard-Vilhem's open pipeline flagged on A73 (TYC 4590-364-1,
Gaia DR3 2290881958791909248) phased on this paper's ephemeris and on his Gaia period.
Uses his v1.2.0 edge-on record copy already in this repository. Standard library only.
Run from the repository root.
"""
import csv, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chopard_overlap import gaia_ids  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
D = 'reviews/novelty-reconciliation/chopard-evidence/extracted/gaia-dr3-edge-on-orbits-tess-eclipses-v1.2.0/'
SID = '2290881958791909248'
P, T0 = 17.538, 2940.800       # paper Table A1: A73, T0 = BJD 2459940.800 (BTJD 2940.800)
P_GAIA = 124.72476732764636    # his period_orbit for this star (known_check.csv)


def astrometric_matches():
    """Accepted systems whose Gaia ID is among his 1,726 selected astrometric orbits."""
    sel = {r['source_id'] for r in csv.DictReader(open(D + 'track3_astrometric_orbits_selected.csv'))}
    g = gaia_ids()
    acc = list(csv.DictReader(open('accepted-systems.csv', newline='')))
    hits = [a['review_id'] for a in acc if g.get(a['tic'].strip(), (None,))[0] in sel]
    print(f'accepted systems among his {len(sel)} astrometric orbits: {hits}')


def main():
    astrometric_matches()
    flagged = [r for r in csv.DictReader(open(D + 'pilot_results/flagged.csv')) if r['source_id'] == SID]
    vet = {(r['sector'], r['author']): r for r in csv.DictReader(open(D + 'pilot_results/artefact_vetting.csv'))
           if r['source_id'] == SID}
    known = [r for r in csv.DictReader(open(D + 'pilot_results/known_check.csv')) if r['source_id'] == SID]
    t_first = min(float(r['dip_t']) for r in flagged)
    out = []
    for r in sorted(flagged, key=lambda r: float(r['dip_t'])):
        t = float(r['dip_t'])
        c = (t - T0) / P
        half = round(c * 2) / 2          # nearest primary (integer) or secondary (half-integer)
        kind = 'primary' if half == int(half) else 'secondary'
        oc_h = (t - (T0 + half * P)) * 24
        v = vet.get((r['sector'], r['author']), {})
        out.append(dict(sector=r['sector'], pipeline=r['author'], dip_btjd=round(t, 4),
                        depth_pct=round(100 * float(r['dip_depth']), 2), his_half_window_d=r['half_window'],
                        cycle=half, kind=kind, oc_hours=round(oc_h, 1),
                        phase_on_his_124_7d=round(((t - t_first) / P_GAIA) % 1, 3),
                        his_verdict=v.get('verdict', '')))
    for o in out:
        print(o)
    print('known_check verdict:', [k['verdict'] for k in known], '| windows:', [k['n_windows'] for k in known],
          '| dip flags:', [k['n_dip_flags'] for k in known])
    hw = [float(r['half_window']) for r in flagged]
    print(f'his half-windows on these dips: {min(hw):.1f} to {max(hw):.1f} d; '
          f'primary-plus-secondary spacing on our ephemeris: {P/2:.2f} d')
    with open(os.path.join(HERE, 'a73-chopard-dips.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)


if __name__ == '__main__':
    main()
