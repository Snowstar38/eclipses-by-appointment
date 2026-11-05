"""Independently map frozen RESULTS rows to deciding measurements and reports.

Reads only; writes verify-result-mapping.json. Depth is the median of realized
central event losses, not the median model amplitude. Older events are included.
"""
import csv, hashlib, json, statistics
from pathlib import Path

P = Path(__file__).resolve().parent
rows = list(csv.DictReader((P / 'RESULTS.csv').open(encoding='utf-8-sig', newline='')))
older = json.loads((P / 'older-events.json').read_text(encoding='utf-8-sig'))
checks = []
for row in rows:
    tic = row['tic']; kind = 'B' if tic == '109560492' else 'A'
    mpath = P / tic / 'measurements.json'
    m = json.loads(mpath.read_text(encoding='utf-8-sig'))
    path = 'augmented_same_kind_fit' if 'augmented_same_kind_fit' in m else f'same_kind_fits.{kind}'
    fit = m['augmented_same_kind_fit'] if path == 'augmented_same_kind_fit' else m['same_kind_fits'][kind]
    events = [(f"events[{i}].depth_ppt", e['depth_ppt']) for i, e in enumerate(m['events']) if e.get('timing_usable') and e['kind'] == kind]
    for i, e in enumerate(older):
        if e['tic'] == tic and e['kind'] == kind and 'center_btjd' in e:
            events.append((f'older-events.json[{i}].depth_ppt', e['depth_ppt']))
    depth = statistics.median(v for _, v in events)
    fields = {'period_days': (fit['period_days'], 9, f'{path}.period_days'),
              'period_error_days': (fit['period_formal_error_days'], 9, f'{path}.period_formal_error_days'),
              'primary_epoch_btjd': (fit['epoch_btjd'], 6, f'{path}.epoch_btjd'),
              'depth_ppt': (depth, 2, 'median of ' + ', '.join(k for k,_ in events))}
    mapping = {}
    for field, (value, digits, src) in fields.items():
        expected = f'{value:.{digits}f}'
        mapping[field] = {'result':row[field], 'expected':expected, 'measurement_value':value, 'source':src, 'match':row[field] == expected}
    text = (P / row['report']).read_text(encoding='utf-8-sig')
    report_expected = {'epoch':f"BTJD {fit['epoch_btjd']:.5f}", 'period':f"{fit['period_days']:.7f} d", 'period_error':f"{fit['period_formal_error_days']:.7f} d", 'depth':f"central depth is {depth:.1f} ppt", 'verdict':f"Physical verdict: {row['physical_verdict']}"}
    semantic = {'kind_named_in_row': f'observed {kind} eclipse' in row['epoch_kind'],
      'kind_named_in_report': f'**{kind} eclipse**' in text,
      'primary_uncertain_when_required': tic not in ('331650047','109560492') or ('primary designation uncertain' in row['epoch_kind'] and 'primary designation is uncertain' in text),
      'conditional_error': 'conditional statistical period error' in text and 'model systematics' in text,
      'same_photons': 'same photons' in text and 'not independent observing epochs' in text,
      'realized_depth_and_dilution': 'realized trapezoid loss' in text and 'dilution' in text,
      'catalogue_failures_unknown': 'not a nonmatch' in text or 'not nonmatches' in text or 'unavailable' in text or 'success' in text,
      'crowded_attribution': tic != '109560492' or ('probable' in row['physical_verdict'] and 'not resolved' in text and 'uncalibrated' in text),
      'marginal_gaia': tic != '331650047' or 'marginal' in text,
      'cycle_assumption': 'integer-cycle assignment' in text}
    report_checks = {k:{'expected_fragment':v,'match':v in text} for k,v in report_expected.items()}
    hashfile=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    checks.append({'tic':tic, 'fit_source':path, 'event_kind':kind, 'depth_inputs':events,
                   'mapping':mapping, 'report_checks':report_checks, 'semantic_checks':semantic,
                   'measurements_sha256':hashfile(mpath), 'report_sha256':hashfile(P / row['report'])})
errors=[]
for rec in checks:
    for category in ('mapping','report_checks'):
        for key, val in rec[category].items():
            if not val['match']: errors.append(f"{rec['tic']} {category}.{key}")
    errors += [f"{rec['tic']} semantic_checks.{key}" for key, val in rec['semantic_checks'].items() if not val]
out={'results_sha256':hashlib.sha256((P/'RESULTS.csv').read_bytes()).hexdigest(), 'older_events_sha256':hashlib.sha256((P/'older-events.json').read_bytes()).hexdigest(), 'targets':checks, 'errors':errors, 'status':'pass' if not errors else 'fail'}
(P/'verify-result-mapping.json').write_text(json.dumps(out, indent=2),encoding='utf-8')
print(json.dumps({'status':out['status'], 'errors':errors},indent=2))
raise SystemExit(bool(errors))
