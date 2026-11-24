"""Finding 1: column checks on the November 23 host table after the second release.

Reads reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv (855 rows) and the
duration re-measurements Earthshine made for eight rows (earthshine-duration-results.csv,
in this folder). Standard library only. Run from the repository root.
"""
import csv, collections, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
H = list(csv.DictReader(open('reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv', newline='')))
LATE = [r for r in H if 1702 <= int(r['review_id'][1:]) <= 1802]   # second release, Nov 23
TWIN = re.compile(r'twin solution 2P=([\d.]+) d is preferred')


def main():
    out = []
    print(f'rows: {len(H)}; second-release rows R1702-R1802: {len(LATE)} '
          f'({sum(r["physical_tier"] == "confirmed" for r in LATE)} confirmed, '
          f'{sum(r["physical_tier"] == "probable" for r in LATE)} probable)')

    # (a) period adopted at 2P because the alternate dips differ, but no secondary recorded
    a = [r for r in H if r['period_resolution'].startswith('2P') and not r['secondary_phase'].strip()]
    print(f'(a) 2P adopted (alternate dips unequal or odd/even timing) with blank secondary columns: {len(a)}')
    for r in a:
        out.append(dict(review_id=r['review_id'], tier=r['physical_tier'], check='2P adopted, secondary columns blank',
                        detail=r['period_resolution'][:90], suggestion='fill secondary_phase and secondary_depth_ppt from the alternate dip'))

    # (b) text prefers the twin period 2P but the table adopts P and lists 2P as the alternative
    t = [r for r in H if TWIN.search(r['period_resolution'])]
    keep = [r for r in t if abs(2 * float(r['adopted_period_days']) - float(TWIN.search(r['period_resolution']).group(1))) < 1e-3]
    print(f'(b) rows whose text says the twin period 2P is preferred: {len(t)}; adopted period is still P: {len(keep)} '
          f'({sum(r["physical_tier"] == "confirmed" for r in keep)} confirmed; {sum(r in LATE for r in keep)} in the second release)')
    for r in keep:
        out.append(dict(review_id=r['review_id'], tier=r['physical_tier'], check='text prefers 2P, table adopts P',
                        detail=f'adopted {r["adopted_period_days"]} d; alternative {r["period_alternative_days"]} d',
                        suggestion='reword (P adopted, 2P if twins) or adopt 2P; check for a secondary first (see R1758)'))

    # (c) durations on a small set of values
    c = collections.Counter(r['duration_h'] for r in H)
    top = c.most_common(17)
    on = {v for v, _ in top}
    gs = [r for r in H if r['search'].startswith('Spectroscopic')]
    print(f'(c) {sum(n for _, n in top)} of {len(H)} duration_h values sit on 17 recurring values '
          f'(most common: {", ".join(f"{v} h x{n}" for v, n in top[:5])}); '
          f'ground-survey rows: {sum(r["duration_h"] in on for r in gs)} of {len(gs)}')

    # (d) Earthshine's re-measurements of eight short-looking eclipses
    e = list(csv.DictReader(open(os.path.join(HERE, 'earthshine-duration-results.csv'), newline='')))
    ratio = sorted(float(r['dur_tab_h']) / float(r['T14_fit_h']) for r in e)
    print(f'(d) duration_h / fitted T14 for {len(e)} rows: {ratio[0]:.2f} to {ratio[-1]:.2f}, median {ratio[len(ratio)//2]:.2f}')
    for r in e:
        print(f'    {r["review_id"]}: table {r["dur_tab_h"]} h, fitted T14 {r["T14_fit_h"]} h, '
              f'shortest circular T14 {r["T14_min_h"]} h, depth table {r["depth_tab_ppt"]} vs fit {r["depth_fit_ppt"]} ppt')

    with open(os.path.join(HERE, 'nov23-column-flags.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)


if __name__ == '__main__':
    main()
