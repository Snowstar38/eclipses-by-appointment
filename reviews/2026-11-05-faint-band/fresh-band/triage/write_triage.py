import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent

# Visual inspection of every panel in sheet-01..13. Text is indexed by TIC,
# not by screening rank. Windows are diagnostic plots, not eclipse fits.
visual = {
768070: ('repeated_discrete', 'S5 deep narrow dip with resolved contacts; S32 shallower centered dip. S98 has much deeper event on local baseline; depth/shape vary, so attribution needs review.'),
9803589: ('artifact_or_gap', 'S29 positive spike, S69 broad rising discontinuity, S70 noise; no repeated negative contacts.'),
17467626: ('broad_variability', 'S78/S24/S51 multi-day smooth undulation with broad trough, no isolated ingress/egress.'),
18640611: ('noise_limited', 'S70/S43/S71 scatter only; selected dip is not resolved.'),
26486304: ('repeated_discrete', 'S15/S1/S83 deep flat-bottomed dips with sharp contacts, similar widths and depth across distant sectors.'),
36459775: ('artifact_or_gap', 'S9 positive excursion; S99/S62 flux steps at interruptions, no closed dip.'),
44738636: ('noise_limited', 'S4/S31/S5 sparse scatter; few low points do not form contacts.'),
45180023: ('artifact_or_gap', 'S9/S90 large asymmetric shifts adjoining gaps; S35 isolated noisy low point.'),
47333117: ('noise_limited', 'S61/S88/S8 only shallow fluctuations and gaps; no coherent dip.'),
50980132: ('artifact_or_gap', 'S55/S54 broad slope plus level change; S81 scatter, no resolved eclipse.'),
53676078: ('weak_broad', 'S17 shallow broad depression; S57/S84 centered points consistent with noise, recurrence unclear.'),
60730095: ('artifact_or_gap', 'S99 step down at window start; S8/S61 noisy shallow selections lack contacts.'),
70660271: ('artifact_or_gap', 'S73 positive trend, S19/S59 long slope and gap; no closed event.'),
79492201: ('artifact_or_gap', 'S95 ingress runs into long gap; S104 flux step at window, S1 low point only. No complete repeat.'),
81929234: ('artifact_or_gap', 'S100/S99 discontinuous level shifts, S101 declining trend, no resolved trough.'),
82596345: ('weak_broad', 'S49/S22 shallow slow baseline change; dip contacts not separated from trend.'),
84232105: ('artifact_or_gap', 'S56 severe rising systematics; S15/S16 sparse weak lows.'),
86182628: ('repeated_discrete', 'S22 and S49 similarly deep narrow dips with full ingress and egress on stable baseline.'),
89112885: ('noise_limited', 'S4/S31 low points among scatter, no convincing shape.'),
103175571: ('artifact_or_gap', 'S86/S59 apparent trough coincides with interrupted light curve and baseline shift; S26 weak.'),
118754404: ('artifact_or_gap', 'S62/S99/S89 long trends and steps; no discrete eclipse contacts.'),
119576020: ('broad_variability', 'S16/S83/S56 strong smooth repeating multi-day wave with broad minima, no isolated contacts.'),
121565281: ('weak_broad', 'S98 broad low trend; S32/S5 lack repeatable resolved event.'),
130590375: ('noise_limited', 'S46/S91 noisy low points without coherent eclipse shape.'),
134835320: ('artifact_or_gap', 'S101 shallow trough adjacent gap; S100 level step; S64 noise.'),
139364226: ('artifact_or_gap', 'S96/S28 discontinuities and trends; S2 weak dip not recurrent.'),
141275438: ('noise_limited', 'S22/S49 scattered low points, no resolved shape.'),
142504628: ('artifact_or_gap', 'S41/S53 changing slopes and gap, S14 too sparse for contacts.'),
146520853: ('broad_variability', 'S5/S98/S32 broad rounded dips ride multi-day slopes; no stable flat baseline or clean contact pair.'),
147275482: ('artifact_or_gap', 'S9 partial drop at gap; S10 monotonic relaxation; S36 weak.'),
147615405: ('artifact_or_gap', 'S63/S90 level steps; S9 long smooth ramp.'),
148340239: ('artifact_or_gap', 'S61/S34/S6 long slopes and gaps, no isolated eclipse.'),
150948873: ('noise_limited', 'S84 positive bump and scattered lows; S57 noise.'),
154489378: ('broad_variability', 'S57/S83/S84 coherent large smooth periodic wave, not discrete eclipses.'),
155712380: ('artifact_or_gap', 'S72 long drift; S44/S45 noisy points without contacts.'),
157587214: ('artifact_or_gap', 'S74/S80 extreme flux collapse near zero and S54 huge excursion imply severe extraction/systematics; no trusted eclipse.'),
159095480: ('broad_variability', 'S20/S60/S47 broad multi-day slopes with baseline changes, no contacts.'),
159299384: ('noise_limited', 'S14/S75/S19 shallow noisy selections without a repeated shape.'),
172117728: ('artifact_or_gap', 'S87 sloped variation, S6/S33 sparse weak low points; no resolved repeat.'),
172745416: ('noise_limited', 'S51 isolated low point without recurrence evidence.'),
174600114: ('noise_limited', 'S7/S8/S35 sparse weak low points; S8 slope, no contacts.'),
181856790: ('weak_broad', 'S63 and S101 broad troughs around interruption; S91 continuous steep slope. Possible variability, eclipse recurrence unproved.'),
191459528: ('noise_limited', 'S17/S84/S57 scatter and shallow broad drift, no event contacts.'),
220379663: ('artifact_or_gap', 'S103/S94/S102 step changes at gaps and ramps, no closed dip.'),
231280024: ('artifact_or_gap', 'S97/S96 flux step at gap; S29 sparse low points only.'),
234813324: ('artifact_or_gap', 'S87/S6 broad drift and interrupted baseline; S33 noise.'),
234997338: ('artifact_or_gap', 'S103 sharp incomplete fall into a gap; S95/S104 asymmetric ramps and step, no clean repeat.'),
235618971: ('weak_broad', 'S80/S53/S26 shallow broad troughs with sector-dependent slopes; contacts unresolved.'),
237404597: ('artifact_or_gap', 'S98 step at gap; S6/S7 sparse shallow points.'),
238256230: ('artifact_or_gap', 'S54/S81 long drift plus gap; S92 noise.'),
243402396: ('weak_broad', 'S14 apparent dip and S55 similar downturn but both broad/asymmetric near gaps; S82 not confirming.'),
248124207: ('artifact_or_gap', 'S81 severe trend and gap; S54 continuous slope.'),
252475067: ('weak_broad', 'S75 shallow broad minimum; S48 long relaxation, S21 sparse lows; no contacts.'),
252735834: ('artifact_or_gap', 'S17/S57 ramps and S16 isolated low point; no repeat.'),
259614821: ('repeated_discrete', 'S100/S102/S101 deep symmetric dips with complete ingress and egress, nearly matching morphology.'),
265438863: ('artifact_or_gap', 'S103 fall to gap; S94 broad noisy trough, S102 step, not a closed recurring eclipse.'),
266442294: ('broad_variability', 'S61 multi-cycle irregular wave; S88 shallow noise, no discrete contact pair.'),
266786763: ('weak_broad', 'S97 shallow partial downturn ending at gap; S30/S3 no convincing repeat.'),
269316819: ('noise_limited', 'S82/S92 scatter only.'),
271540399: ('noise_limited', 'S14/S75/S74 noisy weak selections, no contacts.'),
271865260: ('weak_broad', 'S88/S61/S34 similar shallow troughs around gaps; no ingress/egress wholly observed.'),
276736435: ('broad_variability', 'S13/S100/S39 multi-day broad waves and level shifts, no stable eclipse contacts.'),
279221287: ('noise_limited', 'S4/S31 low points in sparse scatter, no resolved dip.'),
282593845: ('artifact_or_gap', 'S55/S75 flux steps/spike, S14 sparse; no repeat.'),
282678128: ('artifact_or_gap', 'S81 long asymmetric relaxation to gap; S55 isolated shallow low point.'),
296194107: ('artifact_or_gap', 'S63/S90 broad gap-associated trough and level shift; S9 weak.'),
301654619: ('artifact_or_gap', 'S55/S82 broad ramps and gaps, no closed dip.'),
304271827: ('artifact_or_gap', 'S101/S100 strong smooth trends/steps; S93 partial dip at gap.'),
308358719: ('artifact_or_gap', 'S26/S80 gap-associated level changes; S52 sparse low points.'),
314837744: ('noise_limited', 'S55/S82 scattered lows without resolved ingress/egress.'),
317207574: ('broad_variability', 'S101/S100 repeating short-period irregular wave; S102 large level step.'),
325663405: ('artifact_or_gap', 'S17/S76/S16 baseline discontinuities and ramps; no closed event.'),
330708272: ('artifact_or_gap', 'S83/S76 level steps; S56 positive spike, no eclipse.'),
331643517: ('repeated_discrete', 'S83 and S56 deep narrow primary dips and offset secondary-like dip; similar pattern across sectors. S16 sparse.'),
332460840: ('artifact_or_gap', 'S11/S65/S38 long ramps and gap-associated shifts, no contacts.'),
340990377: ('weak_broad', 'S81 shallow broad trough; S82/S55 scattered lows, no clear repeat.'),
343187602: ('single_discrete', 'S24 compact deep dip with rapid recovery; S16 weak and S84 broad variable trough, recurrence/identity not shown.'),
347471408: ('artifact_or_gap', 'S43 positive spike; S42 isolated low point.'),
350167445: ('noise_limited', 'S80/S53/S54 noisy low points, no coherent shape.'),
351908842: ('broad_variability', 'S80/S74 broad slopes and depressions; S14 sparse, contacts absent.'),
352623773: ('artifact_or_gap', 'S55/S82 flux level steps and slow drift, no discrete trough.'),
356801225: ('repeated_discrete', 'S40/S81/S54 very deep symmetric dips with resolved contacts and stable baseline; S81 has nearby gap but both contacts observed.'),
362481234: ('artifact_or_gap', 'S93 weak partial drop at gap; S103/S100 large ramps/steps.'),
364972072: ('artifact_or_gap', 'S81 level step; S16/S83 sparse/noisy selections.'),
371856921: ('single_discrete', 'S23 clear flat-bottomed deep dip with contacts; S50 broad tidal-looking wave only. Repeat not established.'),
374676046: ('artifact_or_gap', 'S9/S64/S90 ramps and level changes, no closed dip.'),
375942406: ('noise_limited', 'S55/S82 isolated low points among scatter.'),
407996580: ('artifact_or_gap', 'S42 terminal upward ramp, no eclipse.'),
412521418: ('repeated_discrete', 'S7/S61/S34 narrow central dip recurring over broad phase wave; at least one window shows sharp contacts, possible eclipse plus variability.'),
421735152: ('noise_limited', 'S50 isolated low point, no repeat evidence.'),
430376242: ('artifact_or_gap', 'S86/S59 long trends and interrupted flux; S73 noisy low points.'),
431440172: ('artifact_or_gap', 'S92/S91 broad downturns at gap or trend, no resolved contacts.'),
437698875: ('noise_limited', 'S42/S92 scattered lows, no closed event.'),
438357248: ('artifact_or_gap', 'S99/S101/S64 level shifts and long drift, no closed eclipse.'),
450779013: ('artifact_or_gap', 'S99 broad gap trough; S100 baseline step, S37 noisy.'),
452442375: ('artifact_or_gap', 'S90/S64 long sloping level changes and gaps, S11 drift; no contacts.'),
452496185: ('artifact_or_gap', 'S65/S90 partial trough at gap and level step; S10 weak.'),
452748723: ('noise_limited', 'S98/S5/S32 scattered weak lows; no resolved repeat.'),
454222754: ('artifact_or_gap', 'S32 positive spike; S98 flux step, S5 sparse.'),
470676004: ('artifact_or_gap', 'S86/S74/S18 broad ramp and gap-associated changes, no stable contact pair.'),
127365016: ('control_recovered', 'Historical EB control: S84/S57/S17 deep resolved repeated dips; both screeners recover it. Not a new science candidate.'),
56130043: ('control_recovered', 'Historical EB control: S32/S98/S5 deep resolved repeated dips. Appointment maximum_box_shape fails, while event flags recover three sectors.'),
}

rows = list(csv.DictReader((ROOT / 'screening-summary.csv').open(newline='')))
assert len(rows) == 102 and set(map(int, (r['tic'] for r in rows))) == set(visual)
selection = json.loads((ROOT / 'selection.json').read_text())
downloads = json.loads((ROOT / 'downloads.json').read_text())
by_tic = {}
for d in downloads:
    by_tic.setdefault(d['tic'], []).append(d)
assert all(d['status'] == 'success' for d in downloads)
assert len(downloads) == 474
for d in downloads:
    assert hashlib.sha256(Path(d['path']).read_bytes()).hexdigest() == d['sha256']

accepted = list(csv.DictReader((ROOT.parent / 'accepted-ledger.csv').open(newline='')))
accepted_tic = {r['tic'] for r in accepted}
queue_ids = [26486304, 86182628, 259614821, 356801225, 331643517, 768070, 412521418, 371856921, 343187602]
assert not (set(map(str, queue_ids)) & accepted_tic)

out = []
for r in rows:
    tic = int(r['tic'])
    category, reason = visual[tic]
    ds = by_tic[r['tic']]
    assert len(ds) == int(r['files'])
    out.append({
        'tic': r['tic'], 'control': r['control'], 'gaia_dr3': r['gaia_dr3'],
        'gaia_period_d': r['gaia_period'], 'gaia_G': r['gaia_G'],
        'category': category, 'visual_reason': reason, 'sheet': r['sheet'],
        'files': r['files'], 'appointment_shape_pass': r['appointment_shape_pass'],
        'appointment_reasons': r['appointment_reasons'], 'appointment_snr': r['appointment_snr'],
        'dip_flag_sectors': r['dip_flag_sectors'], 'best_contrast': r['best_contrast'],
        'download_sectors': ';'.join(str(x['sector']) for x in ds),
        'download_sha256': ';'.join(x['sha256'] for x in ds),
        'full_review_queue': tic in queue_ids,
    })

with (OUT / 'visual-triage.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader(); w.writerows(out)
with (OUT / 'review-queue.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader(); w.writerows(r for r in out if r['full_review_queue'])

counts = Counter(r['category'] for r in out if r['control'] == 'False')
(OUT / 'SUMMARY.md').write_text(
    '# Fresh-band visual morphology triage\n\n'
    'Screening only. Inspected all 100 science targets and both labeled historical controls in the 13 raw-SAP sheets. '
    'The candidate windows are selections, not fitted eclipses; times and Gaia periods are not adopted ephemerides. '
    'Every successful download was checked against its saved SHA-256 receipt (474 files), and file counts matched all 102 summary rows. '
    'The 9-object queue has no TIC in the accepted ledger. A queue entry invites full source attribution, recurrence and timing review; it is not a C/P verdict or novelty claim.\n\n'
    + 'Science categories: ' + ', '.join(f'{k} {v}' for k,v in sorted(counts.items())) + '.\n\n'
    'The strongest repeated-contact examples are TIC 26486304, 86182628, 259614821 and 356801225. '
    'TIC 331643517 has repeated primary and secondary-like dips; TIC 768070 has changing depths; '
    'TIC 412521418 has sharp central dips superposed on a broad wave. '
    'TIC 371856921 and 343187602 each show one persuasive compact event without demonstrated same-kind recurrence. '
    'The latter two are lower priority and must not be treated as periodic detections.\n\n'
    'Broad tidal or other smooth waves, including TIC 154489378, 119576020, 146520853 and 276736435, '
    'were kept distinct from eclipse contacts. Many apparent dips end at cadence gaps or coincide with level steps. '
    'Other weak cases and noise-limited cases remain explicitly in visual-triage.csv for later slag picking. '
    'Control TIC 56130043 illustrates the appointment maximum_box_shape false negative: event flags recover all three sectors. '
    'Control TIC 127365016 is also recovered. These controls validate sensitivity to obvious deep EBs, not completeness for shallow or long-period eclipses.\n',
    encoding='utf-8')
print(len(out), counts, 'queue', queue_ids)
