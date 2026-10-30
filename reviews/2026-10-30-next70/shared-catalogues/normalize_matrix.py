"""Normalize the original query assembly without adding catalogue admission gates."""
import csv, json
from pathlib import Path
P = Path(__file__).parent/'coverage-matrix.csv'
rows = list(csv.DictReader(P.open(encoding='utf-8-sig')))
assert len(rows) == 70
for r in rows:
    raw = r.get('historical_battery_raw', r.get('prsa2022_cache', ''))
    assert raw == 'none of the vetted/unvetted EB tables' or raw.startswith('table2 '), (r['tic'], raw)
    r['historical_battery_raw'] = raw
    for key in ['prsa2022_cache', 'ijspeert2024_cache', 'kostov2025_vetted_cache']:
        r.pop(key, None)
    for key in ['prsa2022_status', 'ijspeert2024_status', 'kostov2025_vetted_status']:
        r[key] = 'checked: no rows in original five-arcsecond cone'
    near = json.loads(r['vsx_neighbours_or_unresolved'])
    close = json.loads(r.get('vsx_close_identity_review', '[]'))
    for item in near[:]:
        if float(item['_r']) < 2:
            near.remove(item)
            if item not in close: close.append(item)
    r['vsx_neighbours_or_unresolved'] = json.dumps(near)
    r['vsx_close_identity_review'] = json.dumps(close)
    # In this queue every ambiguous sub-two-arcsecond VSX entry is VAR.
    # Even an exact match to VAR is not a prior eclipsing classification.
    assert all(x['Type'] == 'VAR' for x in close)
    established = [x for x in json.loads(r['asassn_exact']) if x.get('Type') in ('EA', 'EB', 'EW', 'E')]
    assert r['simbad_primary_otype'] == 'SB*' and r['gaia_dr3_eb'] == 'no exact match'
    assert not json.loads(r['prsa_local_exact_tic'])
    assert all(x.get('Type') not in ('EA', 'EB', 'EW', 'E') for x in json.loads(r['vsx_exact_gaia']))
    r['known_prior_eb_identification'] = json.dumps(established)
    r['coverage_complete'] = 'yes'
    r['scoped_prior_eb_status'] = 'known prior EB' if established else 'no identified prior EB'
    r['close_identity_note'] = 'Close VAR entry may be the target; VAR and the exact ASAS-SN ROT: class are not prior EB classifications.' if close else ''
assert [r['tic'] for r in rows if r['scoped_prior_eb_status']=='known prior EB'] == ['432482170']
with P.open('w', newline='', encoding='utf-8') as f:
    w=csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
print('70 scoped records: 69 without identified prior EB; one known prior EB. VAR identity notes retained.')
