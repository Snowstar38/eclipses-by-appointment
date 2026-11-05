"""Freeze batch07 human-reviewed classifications and source receipts."""
import csv
import hashlib
import json
from pathlib import Path

B = Path(__file__).resolve().parent
P = B.parent
Q = list(csv.DictReader((B / 'queue.csv').open(newline='', encoding='utf-8')))
SRC = P.parent / 'binary-exploration-2026-11-04' / 'bulk-results'

# Each conclusion follows inspection of raw-windows, full-sector orbit-context,
# original source previews, and alternate channel/context panels. These are
# adjudications, not detector-score conversions.
ADJ = {
 'H061': ('REFUTED',
   'The s80 screening dip at BTJD 3492.646 is a broad fall into a flat lower level. Its 15.4 ppt raw core deficit is accompanied by an almost identical excursion in SAP_BKG and by centroid X/Y movement. The contemporaneous flagged brightening is part of the same changing baseline. The step and plateau, rather than a return to the pre-event level, positively contradict an isolated eclipse interpretation of these flags.',
   'The s40 and s53 raw sectors have unrelated low-amplitude trends; no measured same-kind eclipse sequence is established. Gaia has an SB1 orbit at 29.156806 d, which does not turn this detector window into a timed eclipse.',
   'Positive background and centroid co-movement refutes the selected flag, not the existence of a spectroscopic binary.',
   'If a future uninterrupted eclipse-shaped event appears, extract a stable target aperture and time it.'),
 'H062': ('REFUTED',
   'The s104 flag at BTJD 4197.284 is a downward ramp immediately before an observing gap, followed by an upward flux step. The full seven-sector SAP context shows several sector-edge or gap-adjacent ramps of different shapes, including deep s93 boundary drops. The selected local minimum lacks a continuous ingress and egress on a shared baseline.',
   'The s104 SAP_X changes across the same gap while background and SAP_Y drift. Gaia P=24.217964 d is orbital context only; none of these transitions supplies a measured eclipse center.',
   'Gap/step morphology refutes the selected flag; untested low-depth variability elsewhere is outside this flag review.',
   'Require a continuous candidate event with a stable position and local baseline before timing.'),
 'H063': ('REFUTED',
   'The s97 flag at BTJD 3947.551 sits in a roughly six-percent downward step across missing time. The lower level then recovers slowly. SAP_BKG surges by more than 200,000 units and SAP_X/Y move sharply across the same interval. The s3/s30 brightening flags are separate trends and jumps, not eclipse confirmations.',
   'The raw sector and alternate-channel panel directly associate the selected dip with a changing aperture/background state. No eclipse center or depth can be measured from the discontinuity.',
   'The s97 step refutes this selected eclipse flag. The Gaia SB1 orbit at 25.072237 d remains valid independent context.',
   'If revisited, localize a new complete event on calibrated pixels.'),
 'H064': ('REFUTED',
   'The s23 flagged window at BTJD 1943.472 has a positive raw core displacement despite its dip-screen label: the apparent dip is a post-gap relaxation from an elevated flux level. SAP_BKG decays in the same shape and SAP_X/Y shift. KSPSAP does not preserve a coherent eclipse at this time.',
   'Other cached sectors show changing baselines and no measured same-kind repeat. Gaia P=50.942228 d and the fold-screen period are predictions, not measured eclipse timings.',
   'A gap-linked background/position relaxation positively refutes the selected dip interpretation.',
   'Inspect any future isolated dip after verifying target-centred pixel flux.'),
 'H065': ('REFUTED',
   'Both s98 dip flags, including BTJD 3995.541 and 4002.069, fall within a repeating sawtooth pattern of abrupt low-flux resets followed by slow rises. The full s98 SAP record shows several such resets; centroid X/Y and background shift with the large transitions. The flagged windows are slices of this sector pattern, not separately timed eclipses.',
   'The s5/s32 shapes differ, and there is no stable same-kind cadence at Gaia P=23.532532 d. The s98 changes are much larger and less isolated than the nominal shallow screening dips.',
   'Repeated detector/aperture resets refute the selected flags; no binary-wide exclusion is inferred.',
   'Only a stable-aperture event outside the sawtooth pattern would justify renewed eclipse analysis.'),
 'H066': ('PLAUSIBLE',
   'The s19 raw SAP window at BTJD 1820.954 contains a roughly 1.3 ppt, approximately symmetric depression with data on both sides. Its shape could be a shallow eclipse, but other irregular troughs and time-varying pointing are present in the same sector. The signal is suppressed in KSPSAP; the independent audit finds moderate detrended SAP–centroid-X association, which raises an instrumental alternative without proving it.',
   'Only s19 QLP is cached. MAST lists s59; a WCS-centred 3x3 FFI cutout was fetched and has positive target-aperture flux through nearly all quality-zero cadences, but broad systematics make it an insensitive null at 1.3 ppt. Gaia SB2 P=26.946144 d is orbital context, not a measured photometric period. No source-localized repeated event or secure eclipse timing exists.',
   'One insecure shallow event; corrected suppression, pointing association, and weak new-sector coverage cannot decisively attribute or reject it.',
   'Obtain a stable, source-localized repeat and independent aperture reduction before measuring an ephemeris.'),
 'H067': ('PLAUSIBLE',
   'The s94 window near BTJD 3874.942 has a several-ppt trough before a gap, with partial recovery near the gap and a higher post-gap baseline. The s27 sector has a different broad decline ending at a gap; it is not a measured same-kind repeat. Detrended s94 SAP and centroid X have moderate association, so pointing/systematic contamination is credible, but an overlapping real event is not excluded.',
   'The uncached s66 WCS-centred cutout was fetched; its 3x3 flux shows large broad ramps and is not a sensitive shallow-eclipse null. Gaia P=38.540074 d predicts conjunctions, yet no unambiguous event centers establish a cycle count or recurrence. The s94 feature remains an insecure single-event interpretation.',
   'Gap, centroid association, and varying baseline prevent a secure eclipse measurement, but do not positively refute every possible event.',
   'Recover a clean uninterrupted repeat and test its position and alternate aperture against the target WCS.'),
 'H068': ('REFUTED',
   'The s99 flag at BTJD 4053.691 is a drop across a missing-data boundary, followed by a lower near-flat level. SAP_X jumps and SAP_Y changes shape at the same boundary, while the local background evolves. The raw profile lacks a continuous eclipse egress to its original baseline.',
   'Other cached sectors show scattered gap and baseline effects; the fold-screen statistic is not an event timing. Gaia P=42.475920 d does not identify the s99 step as a conjunction.',
   'The observed step and position change positively refute the selected s99 eclipse flag.',
   'Inspect a complete stable-aperture event if new observations warrant it.'),
 'H069': ('REFUTED',
   'The s94 flags near BTJD 3868.496 and 3874.927 are two portions of a changing sector baseline, not two eclipses. The first flux decline accelerates directly into a roughly one-day gap; after the gap the level jumps above the pre-gap baseline. In the same interval SAP_BKG rises explosively and SAP_X/Y shift. The second flag lies on another broad drift. The s101 brightening is a separate ramp.',
   'No complete same-kind event sequence or measured period follows from these windows. Gaia P=45.783773 d is spectroscopic context.',
   'Background/centroid excursion and discontinuous baseline positively refute the selected eclipse flags.',
   'A future continuous dip would require pixel localization and an independent reduction.'),
 'H070': ('REFUTED',
   'The actual selected s59 dip flag is centered at BTJD 2912.311. Direct quality-zero SAP values are about 0.004 near BTJD 2911.827, rise to about 0.56 near the alleged dip center, and continue toward 0.99 by BTJD 2914.142. Thus the flag lies on a monotonic recovery from near-zero extracted target flux, not at a local flux minimum. The two plotted s59 brightening flags are other slices of this recovery pattern.',
   'The automated representative-window script omitted the exact dip panel because its side-sample requirement failed, so the direct FITS sequence and bulk flag receipt are decisive here. The s59 SAP_BKG and centroid positions evolve strongly during recovery. A zero or near-zero cutout/extraction flux cannot be treated as a sensitive eclipse null.',
   'The original s59 dip is positively contradicted by its rising raw flux and unstable extraction.',
   'Reassess only a complete target-centred event with positive stable flux and local baseline.'),
}

rows = []
for q in Q:
    tic, sid = q['tic'], q['sample_id']
    verdict, evidence, context, limitation, next_check = ADJ[sid]
    d = B / tic
    raw = json.loads((d / 'raw-inspection.json').read_text(encoding='utf-8'))
    bulk_path = SRC / f'{tic}.json'
    bulk = json.loads(bulk_path.read_text(encoding='utf-8'))
    packet_path = P / 'source-packets' / tic / 'sources.json'
    packet = json.loads(packet_path.read_text(encoding='utf-8'))
    flags = [{'sector': f['sector'], 'kind': w['kind'], 'screen_center_btjd': w['time'],
              'screen_duration_days': w['duration'], 'screen_contrast': w['contrast']}
             for f in bulk['files'] if f['status'] == 'ok' for w in f['windows'] if w['flag']]
    used = [{'sector': x['sector'], 'path': x['path'], 'sha256': x['sha256']}
            for x in raw['sectors'] if 'path' in x]
    source = {'sample_id': sid, 'tic': tic, 'queue_sha256': hashlib.sha256((B / 'queue.csv').read_bytes()).hexdigest(),
              'bulk_json': str(bulk_path), 'bulk_json_sha256': hashlib.sha256(bulk_path.read_bytes()).hexdigest(),
              'source_packet': str(packet_path), 'source_packet_sha256': hashlib.sha256(packet_path.read_bytes()).hexdigest(),
              'verified_qlp_fits': used, 'selected_screen_flags': flags,
              'gaia_orbit': packet['target']['gaia'],
              'sector_availability': json.loads((B / 'sector-availability.json').read_text())[tic],
              'note': 'QLP FITS hashes reverified by inspect_raw.py. Screening windows are not measured event times.'}
    for p in sorted(d.glob('s*-tesscut-receipt.json')):
        source.setdefault('new_cutout_receipts', []).append(json.loads(p.read_text()))
    (d / 'source-receipt.json').write_text(json.dumps(source, indent=2) + '\n', encoding='utf-8')
    observed = ', '.join(f"s{x['sector']} ({x['time_start']:.1f}–{x['time_end']:.1f})" for x in raw['sectors'] if 'path' in x)
    report = f"""# {sid} — TIC {tic}

**Verdict:** {verdict} · **Review:** COMPLETE · **Catalogue novelty:** UNKNOWN

{evidence}

{context}

**Coverage and limits.** Hash-verified raw QLP SAP_FLUX, QUALITY=0, covers {observed} BTJD. {limitation} The four shared VizieR novelty gates remain unqueried/unknown; a primary-table nonmatch is not novelty clearance.

**Next check.** {next_check}

Evidence: [raw window numbers](raw-inspection.json), [raw panels](raw-windows.png), [full-sector and Gaia-prediction context](orbit-context.png), [alternate channels and pointing/background](qlp-alternate.png), [source hashes and original flags](source-receipt.json). The Gaia spectroscopic period is {float(q['gaia_period_days']):.6f} d, not a photometrically measured period here.
"""
    (d / 'REPORT.md').write_text(report, encoding='utf-8')
    rows.append({'sample_id': sid, 'tic': tic, 'sample_stratum': q['sample_stratum'],
                 'physical_verdict': verdict, 'full_review_completion': 'COMPLETE',
                 'novelty_status': 'UNKNOWN', 'period_days': '', 'period_error_days': '',
                 'primary_epoch_btjd': '', 'depth_ppt': '', 'limitations': limitation,
                 'next_check': next_check, 'report': str(d / 'REPORT.md')})

columns = ['sample_id','tic','sample_stratum','physical_verdict','full_review_completion',
           'novelty_status','period_days','period_error_days','primary_epoch_btjd',
           'depth_ppt','limitations','next_check','report']
with (B / 'RESULTS.csv').open('w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
print('Wrote', len(rows), 'reports and RESULTS.csv')
