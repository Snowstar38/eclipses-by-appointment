"""Verify the complete 97-target full-frame screen and its 25 two-sector checks."""
import csv
import json
import hashlib
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent

def rows(name):
    with (ROOT/name).open(encoding='utf8',newline='') as f:
        return list(csv.DictReader(f))

def evidence(name):
    return json.loads((ROOT/name).read_text(encoding='utf8'))

def verify():
    candidates=rows('measured-ffi-triage.csv')
    stars=rows('pixel-decisions.csv')
    phases=rows('phase-measurements.csv')
    assert len(candidates)==len({r['tic'] for r in candidates})==97
    assert {r['tic'] for r in candidates if r['status']=='priority for pixel checks'}=={s['aperture_tic'] for s in stars}
    assert len(stars)==25 and len(phases)==100
    assert Counter(s['decision'] for s in stars)=={'known eclipse on neighbour':3,'period and phase follow-up':2,'unresolved host':20}
    for s in stars:
        e=evidence(s['evidence'])
        assert e['tic']==s['aperture_tic'] and e['gaia_dr3']==s['aperture_gaia_dr3']
        p=[r for r in phases if r['aperture_tic']==e['tic']]
        assert len(p)==4 and len({(r['sector'],r['phase']) for r in p})==4
        assert all(v['pixels'].startswith('https://archive.stsci.edu/') for v in e['sectors'])
        if s['decision']=='unresolved host':
            assert json.loads(s['unresolved_candidates'])
        if s['neighbour_evidence']:
            alt=evidence(s['neighbour_evidence'])
            assert alt['gaia_dr3']==s['test_position_gaia_dr3'] and alt['aperture_tic']==e['tic']
            fits=[x['fit'] for c in alt['sectors'] for x in c['fits']]
            assert len(fits)==4 and all(f['verdict']=='on_target' and not f['unresolved_capable'] for f in fits)
    c=evidence('catalogue-screen.json')
    assert len(c['receipts'])==11 and all(v['complete'] for v in c['receipts'])
    for rec in c['receipts']:
        assert (ROOT/'catalogue-queries'/rec['file']).exists()
    print('Verified 97 unique targets, 25 source decisions, 100 phase measurements, 12 reassigned-source fits and 11 catalogue controls.')
if __name__=='__main__':
    verify()
