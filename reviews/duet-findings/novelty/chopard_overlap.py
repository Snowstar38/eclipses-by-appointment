"""Finding 2: accepted systems that are already in Chopard-Vilhem's public September list.

His `calibration/calib_vetting.csv` (version 1.2.0 of the edge-on record, a copy is in
reviews/novelty-reconciliation/chopard-evidence/extracted/) holds 92 of the 93 September
systems as Gaia DR3 source_ids. This matches them by Gaia ID against the Gaia IDs this
repository's own files give for accepted-systems.csv. Standard library only.
Run from the repository root.
"""
import csv, glob, json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CH = ('reviews/novelty-reconciliation/chopard-evidence/extracted/'
      'gaia-dr3-edge-on-orbits-tess-eclipses-v1.2.0/calibration/calib_vetting.csv')
SNAPSHOT = '98b90cf'  # his v2.0.0 cross-match snapshot (917 systems in overview/systems.csv)
NAMED_PRECEDENCE = {'109061795', '22388285', '142084127'}  # README: "his identification precedes ours"


def walk_tic_records(x, add):
    """TIC 8.2 records cached in review folders carry the Gaia source id as GAIA."""
    if isinstance(x, dict):
        if 'ID' in x and 'GAIA' in x and x.get('GAIA'):
            add(str(x['ID']), str(x['GAIA']), 'TIC record')
        for v in x.values():
            walk_tic_records(v, add)
    elif isinstance(x, list):
        for v in x:
            walk_tic_records(v, add)


def gaia_ids():
    """TIC -> (Gaia source_id, where it came from) from the repository's own files."""
    m = {}
    def add(tic, g, src='table'):
        tic = (tic or '').strip(); g = (g or '').strip()
        if tic and g.isdigit() and len(g) > 10:
            m.setdefault(tic, (g, src))
    for f in ['accepted-systems.csv', 'claim-adjudication.csv',
              'reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv'] + \
             sorted(glob.glob('reviews/**/accepted-ledger.csv', recursive=True)):
        for r in csv.DictReader(open(f, newline='')):
            add(r.get('tic'), r.get('gaia_dr3'))
    for f in sorted(glob.glob('reviews/**/targets-selected.json', recursive=True)):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if isinstance(d, dict):
            for tic, t in d.items():
                if isinstance(t, dict) and isinstance(t.get('gaia'), dict):
                    add(str(tic), str(t['gaia'].get('source_id', '')))
    for f in sorted(subprocess.run(['grep', '-rl', '--include=*.json', '"GAIA"', 'reviews'],
                                   capture_output=True, text=True).stdout.split()):
        try:
            walk_tic_records(json.load(open(f)), add)
        except Exception:
            pass
    return m


def snapshot_tics():
    try:
        txt = subprocess.run(['git', 'show', f'{SNAPSHOT}:overview/systems.csv'],
                             capture_output=True, text=True, check=True).stdout
    except Exception:
        return None
    return {r['tic'].strip() for r in csv.DictReader(txt.splitlines())}


def main():
    sept = {r['source_id'].strip() for r in csv.DictReader(open(CH, newline=''))}
    acc = list(csv.DictReader(open('accepted-systems.csv', newline='')))
    g = gaia_ids()
    snap = snapshot_tics()
    gid = lambda r: g.get(r['tic'].strip(), (None, None))[0]
    have = [r for r in acc if gid(r)]
    hits = [r for r in acc if gid(r) in sept]
    print(f'September systems with Gaia IDs: {len(sept)}')
    print(f'accepted systems: {len(acc)}; with a Gaia ID in repo files: {len(have)}; without: {len(acc) - len(have)}')
    print(f'matches: {len(hits)} ({sum(r["tier"] == "confirmed" for r in hits)} confirmed, '
          f'{sum(r["tier"] == "probable" for r in hits)} probable)')
    out = []
    for r in hits:
        tic = r['tic'].strip()
        out.append(dict(review_id=r['review_id'], tic=tic, gaia_id=g[tic][0], gaia_id_source=g[tic][1], tier=r['tier'],
                        release_cohort=r['release_cohort'],
                        in_98b90cf_snapshot='' if snap is None else ('yes' if tic in snap else 'no'),
                        precedence_stated_in_README='yes' if tic in NAMED_PRECEDENCE else ''))
    if snap is not None:
        print('in the 98b90cf snapshot:', sum(o['in_98b90cf_snapshot'] == 'yes' for o in out),
              '; not in it:', [o['review_id'] for o in out if o['in_98b90cf_snapshot'] == 'no'])
    with open(os.path.join(HERE, 'chopard-september-overlap.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader(); w.writerows(out)


if __name__ == '__main__':
    main()
