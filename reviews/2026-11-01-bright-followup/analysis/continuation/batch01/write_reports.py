import csv, json, statistics
from pathlib import Path

B = Path(__file__).parent
SB = Path('[local path omitted] 5/made/sb1-scale/diffimg')
Q = list(csv.DictReader((B/'queue.csv').open()))
G = json.loads((B/'gaia-geometry.json').read_text())
A = json.loads((B/'alias-audit.json').read_text())

notes = {
 '97649150': ('CONFIRMED', 'S7/34/87 raw eclipses agree. The closest capable neighbor is G17.24 at 13.7 arcsec and would need roughly 54% intrinsic loss; deficit is within 0.12 pixel of target. Faint close-source ambiguity remains below calibrated pixel precision.', 'Optional resolved time-series photometry.'),
 '210343372': ('CONFIRMED', 'S41/82 provide consecutive raw repeats. The closest capable G16.03 source lies 17.8 arcsec away and would require about 22% intrinsic loss; deficit is within 0.20 pixel of target. The Gaia phase offset is descriptive and within its large propagated orbital uncertainty.', 'Optional resolved time-series photometry.'),
 '49901727': ('CONFIRMED', 'Four same-sector raw eclipses establish recurrence and a photometric period, but the short single-sector baseline leaves a comparatively broad period error. No capable Gaia neighbor within 60 arcsec; target-centered difference image.', 'Additional-sector timing would refine the period.'),
 '424636246': ('CONFIRMED', 'S14/55/84 raw repeats and target-centered deficit. Capable catalogued neighbors are at least 50.6 arcsec away and need large intrinsic losses; no nearby source is favored by the deficit image.', 'Optional precision characterization.'),
 '285926385': ('CONFIRMED', 'Deep S9/63/90 raw eclipses recur at the measured period. Difference image favors the target and lists no capable Gaia neighbor within 60 arcsec.', 'Optional precision characterization.'),
 '376799355': ('PROBABLE', 'Raw eclipses repeat in S10/63/90 and the alternative 3x3 aperture also shows a deficit, diluted from roughly 88 ppt QLP to 36 ppt. The field is crowded: capable Gaia sources at 17.4 and 32.0 arcsec remain; the deficit centroid is only approximately target-centered and has no calibrated error. Attribution is unresolved.', 'Resolved photometry across an eclipse or an independent high-resolution centroid.'),
 '234413494': ('PROBABLE', 'Raw eclipses repeat in S7/46/72. A separate S44 TESScut extraction recovers four events, but the available cutout is truncated and its peak/residual panel is corrupted. Capable neighbors at 19.3 and 30.4 arcsec remain, so attribution is unresolved.', 'Acquire a complete cutout or resolved eclipse photometry.'),
 '392763429': ('CONFIRMED', 'S13/94/103 raw eclipses follow the same clock. A brief S103 depth doubling affects consecutive cycles, not stable odd/even alternation; its cause is unresolved. S13 difference image is target-centered with no capable Gaia neighbor within 60 arcsec.', 'Investigate the S103 depth discontinuity with aperture diagnostics.'),
 '1978575696': ('CONFIRMED', 'Alternating raw depths identify the historical 3.486-day clock as half the orbital eclipse cycle. Deeper even cycles yield a measured 6.97216-day same-kind period, consistent with Gaia; S41 difference image favors the target. A capable G14.97 source at 23.9 arcsec is not favored by the target-centered deficit.', 'Optional resolved photometry and secondary-eclipse characterization.'),
 '66072136': ('CONFIRMED', 'S16/76/84 raw repeats and the alternative S76 aperture support a real target-centered eclipse. No capable Gaia neighbor within 60 arcsec. Central catalogue reconciliation identifies the close VSX EA V0693 Lac counterpart as the same object, so this is a known eclipsing-binary recovery, not a new-system addition. VSX lists 1.08916 d versus the measured same-kind 4.58920 d; the disagreement does not negate the measured raw eclipses.', 'Resolve the discordant VSX period for catalogue interpretation; no new-system count.'),
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
 if tic=='1978575696':pts=[e for e in pts if e['cycle']%2==0]
 sectors=sorted({e['sector'] for e in pts})
 provenance=(f'TESScut S{d["sector"]} and representative QLP S{d["sector"]} are reductions of the same TESS observations and share photons.'
             if d['sector'] in sectors else
             f'TESScut S{d["sector"]} and representative QLP sectors {sectors} are separate TESS observing occasions on the same instrument; their photons are distinct.')
 target_offset=(sum(x*x for x in d['deficit_minus_target_px'])**.5)*21
 lines=[f'# TIC {tic}: {verdict}', '',
  '**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.', '',
  f'1. **Raw repeated events.** {len(pts)} measured, timing-usable raw QLP SAP_FLUX events in representative sectors {sectors}. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.',
  f'2. **Timing and alias.** Same-kind midpoint fit gives P = {m["period_days"]:.10f} Â± {m["period_error_days"]:.10f} d and epoch BTJD {m["primary_epoch_btjd"]:.8f} ({m["epoch_kind"]}). {m.get("timing_selection",A[tic]["same_kind_selection"])} Within-sector recurrences and parity are in `../alias-audit.json`. {m["error_meaning"]} This is a bounded alias check, not an exhaustive period search.',
  f'3. **Pixel attribution.** The alternative cutout sector {d["sector"]} deficit centroid is about {target_offset:.2f} arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. {len(cap)} Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `{dpath}`.',
  f'4. **Alternative reduction.** Separately extracted, target-centered TESScut S{d["sector"]} aperture photometry recovers {d["n_events"]} stacked events at 3x3 depth {d["depth_ap3"]*1000:.2f} ppt, versus median selected raw QLP fit depth {m["depth_ppt"]:.2f} ppt. {provenance} Aperture dilution limits depth comparison.' if tic!='234413494' else f'4. **Alternative reduction.** Separately extracted S44 TESScut aperture photometry recovers {d["n_events"]} events at nominal 3x3 depth {d["depth_ap3"]*1000:.2f} ppt. The cutout is truncated, so this establishes a repeated signal in another extraction but cannot settle attribution or precise depth. {provenance}',
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


