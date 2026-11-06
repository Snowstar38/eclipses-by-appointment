import csv, json, statistics
from pathlib import Path

B = Path(__file__).parent
SB = Path('[local path omitted] 5/made/sb1-scale/diffimg')
Q = list(csv.DictReader((B/'queue.csv').open()))
G = json.loads((B/'gaia-geometry.json').read_text())
A = json.loads((B/'alias-audit.json').read_text())

notes = {
 '351610379': ('CONFIRMED', 'S58/86 raw repeats and the S58 deficit favor the target. The nearest capable G15.21 neighbor is 20.3 arcsec away and would require about 42% intrinsic eclipse depth; a brighter capable source at 54.1 arcsec is spatially separate. Pixel localization has no calibrated error.', 'Optional resolved eclipse photometry.'),
 '61462126': ('CONFIRMED', 'S13/67/104 raw eclipses repeat. The S27 alternative extraction recovers two events with a target-centered deficit; no Gaia neighbor within 60 arcsec passes the approximate flux-budget test.', 'Optional precision characterization.'),
 '169318948': ('CONFIRMED', 'S32/98 raw repeated eclipses and the S98 alternative extraction agree. The difference image favors the target and lists no capable Gaia neighbor within 60 arcsec.', 'Optional precision characterization.'),
 '441257677': ('CONFIRMED', 'S13/27/67 raw events recur with no persistent odd/even depth split. The S13 alternative extraction shows four events and a target-centered deficit with no capable Gaia neighbor within 60 arcsec.', 'Optional precision characterization.'),
 '153972241': ('CONFIRMED', 'Deep S14/41/76 raw eclipses repeat; the S75 extraction recovers six events. Its target-centered difference image lists no capable Gaia neighbor within 60 arcsec.', 'Optional precision characterization.'),
 '384744266': ('CONFIRMED', 'S12/39/102 raw repeats agree. The S12 deficit is near the target. Three nominally capable neighbors lie 29–60 arcsec away, each requiring about 78–100% intrinsic loss, and none is favored by the observed deficit.', 'Optional resolved eclipse photometry.'),
 '163946960': ('CONFIRMED', 'S10/99/101 raw repeats and the S10 alternative extraction support the eclipse. The deficit lies about 0.26 pixel from the target, away from two capable Gaia neighbors at 15.8 and 29.7 arcsec; those require about 60% and 44% intrinsic losses. Localization is descriptive, without a calibrated uncertainty.', 'Resolved eclipse photometry would strengthen host attribution.'),
 '191634144': ('CONFIRMED', 'S57/84 raw shallow eclipses recur. Odd/even fitted depths vary at roughly the local noise level without a stable half-period interpretation. The S57 difference image favors the target over capable neighbors at 23.9, 34.4 and 53.6 arcsec.', 'Additional-sector timing and resolved photometry could tighten this shallow case.'),
 '219399648': ('CONFIRMED', 'Alternating S32/98 raw depths show that the 4.66571-day SAP search branch is half the orbital eclipse cycle. Deeper even events give the 9.33142-day same-kind period consistent with Gaia. The S98 difference image favors the target with no capable Gaia neighbor within 60 arcsec.', 'Optional secondary-eclipse characterization.'),
 '311398753': ('PROBABLE', 'S93/103 raw eclipses repeat and the S13 alternative extraction recovers two. A capable G15.36 source lies only 9.65 arcsec from the target and shares the bright pixel; further capable sources lie at 20.8 and 38.2 arcsec. The target-near deficit cannot distinguish the closest host at uncalibrated pixel precision. Gaia conjunction offset is −0.685 d at the observed epoch versus a 0.335 d linear orbital timing scale; a projection near Gaia2016 gives +0.012 d with only a 0.026 d photometric period allowance, so phase agreement remains descriptive.', 'Resolved time-series photometry across an eclipse, plus refined Gaia-orbit comparison.'),
}

out=[]
for r in Q:
 tic=r['tic']; m=json.loads((B/tic/'measurements.json').read_text()); g=G[tic]
 verdict,limitation,next_check=notes[tic]
 dpath=next((SB/tic).glob('diff_s*.json'),None)
 if dpath is None: dpath=B/'helper/diff_s44.json'
 d=json.loads(dpath.read_text())
 cap=[x for x in d['neighbours_60'] if x['possible']]
 pts=[e for e in m['events'] if e.get('timing_usable')]
 if tic=='219399648':pts=[e for e in pts if e['cycle']%2==0]
 sectors=sorted({e['sector'] for e in pts})
 reduction_relation=('The extraction and representative QLP raw measurement share TESS photons in this sector; aperture dilution limits depth comparison.' if d['sector'] in sectors else 'This historical TESScut sector is a separate observing occasion on the same instrument from the representative QLP sectors; extraction and aperture differences limit depth comparison.')
 if tic=='219399648': reduction_relation+=' The historical S98 stack mixes deeper and shallower half-period events, so its depth is not a same-kind depth comparison.'
 target_offset=(sum(x*x for x in d['deficit_minus_target_px'])**.5)*21
 lines=[f'# TIC {tic}: {verdict}', '',
  '**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.', '',
  f'1. **Raw repeated events.** {len(pts)} measured, timing-usable raw QLP SAP_FLUX events in representative sectors {sectors}. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.',
  f'2. **Timing and alias.** Same-kind midpoint fit gives P = {m["period_days"]:.10f} ± {m["period_error_days"]:.10f} d and epoch BTJD {m["primary_epoch_btjd"]:.8f} ({m["epoch_kind"]}). {m.get("timing_selection",A[tic]["same_kind_selection"])} Within-sector recurrences and parity are in `../alias-audit.json`. {m["error_meaning"]} This is a bounded alias check, not an exhaustive period search.',
  f'3. **Pixel attribution.** The alternative cutout sector {d["sector"]} deficit centroid is about {target_offset:.2f} arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. {len(cap)} Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `{dpath}`.',
  f'4. **Alternative reduction.** Separately extracted, target-centered TESScut aperture photometry recovers {d["n_events"]} stacked events at 3x3 depth {d["depth_ap3"]*1000:.2f} ppt, versus median selected raw QLP fit depth {m["depth_ppt"]:.2f} ppt. {reduction_relation}',
  f'5. **Gaia geometry.** DR3 source {g["gaia_source_id"]}: orbital P = {g["period_days"]:.9f} d, e = {g["eccentricity"]:.4f}. Closest edge-on conjunction offset at the measured epoch is {g["closest"]["offset_days"]:+.4f} d ({g["closest"]["offset_phase"]:+.4f} phase); linear full-NSS-covariance timing scale {g["closest"]["gaia_covariance_linear_error_days"]:.4f} d. Approximate central duration {g["central_duration_hours_approx"]:.2f} h versus measured median {g["observed_duration_hours"]:.2f} h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.',
  '',f'**Deciding interpretation and limitation:** {limitation}', '',f'**Next check:** {next_check}', '',
  'Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.', '',
  '| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |',
  '|---:|---:|---:|---:|---:|']
 for e in pts:
  lines.append(f'| {e["sector"]} | {e["cycle"]} | {e["mid_btjd"]:.7f} | {e["timing_error_days"]:.6f} | {e["depth_ppt"]:.2f} |')
 lines += ['',f'Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `{dpath}`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.']
 (B/tic/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 out.append(dict(tic=tic,physical_verdict=verdict,full_review_completion='COMPLETE',period_days=m['period_days'],period_error_days=m['period_error_days'],primary_epoch_btjd=m['primary_epoch_btjd'],depth_ppt=m['depth_ppt'],limitations=limitation,next_check=next_check,source_report=str(dpath.resolve()),report=str((B/tic/'REPORT.md').resolve())))
with (B/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)


