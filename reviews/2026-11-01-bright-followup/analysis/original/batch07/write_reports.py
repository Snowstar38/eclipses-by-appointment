import csv, json, math
from pathlib import Path

B = Path(__file__).parent
G = json.loads((B / 'gaia-geometry.json').read_text())
A = json.loads((B / 'alias-audit.json').read_text())
H = json.loads((B / 'source-hashes.json').read_text())
notes = {
 '24524336': 'S32 cycles 98/100 and S98 cycles 339/341/343/345 have opposite half-period parity. Intervening windows are quality-flagged, not clean nulls. The within-sector 15.099-day spacing together with cross-sector parity excludes a constant doubled period.',
 '141923153': 'Consecutive raw eclipses in S7 and S34 support recurrence; the capable 51.6-arcsec neighbor is separated from the target-centered deficit despite substantial image-model residual.',
 '167656210': 'A 2.9-arcsec capable Gaia neighbor shares the TESS core. The recurring eclipses are real, but these pixels cannot uniquely assign them to the selected Gaia star.',
 '348773879': 'The capable 17.0-arcsec neighbor is about a pixel away; the deficit core falls much closer to the target. Attribution favors the target at TESS resolution, with uncalibrated subpixel precision.',
 '99493790': 'The target-centered deficit and absence of a brightness-capable Gaia neighbor favor attribution; the image-model residual is high.',
 '460866286': 'The field has 24 brightness-capable Gaia neighbors within 60 arcsec, including one at 12.3 arcsec. The deficit core is near the target, but the weak signal and 0.97 image-model residual cannot uniquely resolve nearby alternatives.',
 '33789753': 'Five raw events in S6/S33/S87 agree in timing and shape. No brightness-capable Gaia neighbor appears within 60 arcsec.',
 '330469458': 'Five deep raw events in S16/S83 recur at the measured period. A capable neighbor 46.3 arcsec away is distinct from the target-centered deficit.',
 '238126968': 'Shallow and deep eclipses alternate at the historical 4.94798-day search interval. Five deep even-cycle midpoints give the 9.89595-day orbital period; shallow odd cycles support the alternating pattern.',
 '220410034': 'S98 contains measured eclipses in both parity classes of the historical period, excluding a simple double-period alias. No brightness-capable Gaia neighbor appears within 60 arcsec.'
}
nexts = {'167656210': 'Resolved time-series photometry or multi-source PRF fitting of the 2.9-arcsec pair.',
         '460866286': 'Higher-resolution eclipse photometry or multi-source PRF fitting in this crowded field.'}
rows = []
for q in csv.DictReader((B / 'queue.csv').open()):
 t = q['tic']; m = json.loads((B / t / 'measurements.json').read_text()); g = G[t]; a = A[t]
 src = Path(H[t]['source_json']); d = json.loads(src.read_text()); cap = [n for n in d['neighbours_60'] if n['possible']]
 assert m['timing_event_count'] >= 2
 verdict = 'PROBABLE' if t in nexts else 'CONFIRMED'
 off = math.hypot(*d['deficit_minus_target_px']) * 21
 caps = 'None under the approximate G-band brightness budget.' if not cap else '; '.join(
  f"Gaia {n['source_id']} ({n['sep']:.1f} arcsec, G {n['G']:.3f}, intrinsic loss needed ~{n['depth_needed']:.2f})" for n in cap) + '.'
 ev = sorted([e for e in m['events'] if 'mid_btjd' in e], key=lambda e: e['mid_btjd'])
 table = '\n'.join(f"| {e['sector']} | {e['cycle']} | {e['mid_btjd']:.7f} | {e['timing_error_days']:.6f} | {e['depth_ppt']:.1f} | {'yes' if e.get('timing_usable') and (t != '238126968' or e['cycle'] % 2 == 0) else 'no: other kind or timing failure'} |" for e in ev)
 alias = f"Within-sector same-kind measured cycle pairs: {a['within_sector_same_kind_pairs']}. "
 if t == '238126968': alias += 'Only the deep even historical cycles enter the orbital fit; odd cycles are the shallower kind. '
 if t == '24524336': alias += 'Flagged intervening cycles are not negative detections; cross-sector parity and within-sector spacing discriminate the alias. '
 report = f"""# TIC {t}: {verdict}

Full bounded review: **COMPLETE**. Actual Gaia DR3 G = {float(q['actual_gaia_dr3_g']):.6f}. The screening period and depth are historical selection values. Physical outcome and central catalogue novelty are separate.

1. **Raw repeated morphology.** Quality-zero QLP SAP_FLUX in representative downloaded sectors {sorted(set(e['sector'] for e in ev))} contains {m['timing_event_count']} selected timing events. Local trapezoids fit free midpoint, depth, duration and baseline; historical predictions only select windows. Numeric windows and a raw event plot accompany this report. Flagged intervals are never clean nulls.
2. **Measured timing and aliases.** Same-kind midpoint regression gives P = {m['period_days']:.10f} ± {m['period_error_days']:.10f} d and epoch BTJD {m['primary_epoch_btjd']:.7f}, kind: {m['epoch_kind']}. {alias}{m['error_meaning']} This bounded alias check does not claim an exhaustive all-period search.
3. **Target attribution.** Historical sector {d['sector']} TESScut difference image has deficit peak {d['peak_deficit_px']} and target pixel {d['target_pixel']}; deficit centroid is {off:.2f} arcsec from the target coordinate. Image-model fractional residual {d['psf_fit_frac_resid']:.3f} and centroid offset are descriptive, not calibrated localization uncertainties. Every brightness-capable Gaia neighbor within 60 arcsec under the historical screen: {caps} The intrinsic-loss budget is approximate and cannot be compared directly with blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1×1/3×3/5×5 aperture depths are {1000*d['depth_ap1']:.1f}/{1000*d['depth_ap3']:.1f}/{1000*d['depth_ap5']:.1f} ppt from {d['n_events']} stacked events, versus median selected raw QLP depth {m['depth_ppt']:.1f} ppt. Different extractions use the same TESS photons. Dilution and mixed eclipse kinds can change depths. Original cutout identity and SHA256 are in ../source-hashes.json.
5. **Gaia geometry.** Matched DR3 NSS source {g['gaia_source_id']} has P = {g['period_days']:.10f} d and e = {g['eccentricity']:.5f}; the closer edge-on conjunction differs from the measured epoch by {g['closest']['offset_days']:.5f} d ({g['closest']['offset_phase']:.5f} phase). Its linearly propagated full source-specific NSS-covariance timing error is {g['closest']['gaia_covariance_linear_error_days']:.5f} d, descriptive rather than a veto threshold. An approximate radius/minimum-mass central duration is {g['central_duration_hours_approx']:.2f} h against {g['observed_duration_hours']:.2f} h observed median; it is not a complete binary model.

**Decision and limitation.** {notes[t]} {'Attribution remains unresolved after the completed pixel check.' if verdict == 'PROBABLE' else 'The available checks favor the target, subject to the stated pixel and timing limits.'}

**Next check.** {nexts.get(t, 'Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.')}

Catalogue novelty is determined by the central seven-group and NSS coverage matrix at ../../shared-catalogues/coverage-matrix.csv; this physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Used in period fit |
|---|---:|---:|---:|---:|---|
{table}

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/{src.name}, historical/{src.stem}.png, historical/gaia.json, ../pixel-contact.png, ../source-hashes.json and ../helper-audit.md. Original TESScut FITS: {H[t]['source_cutout']}. File hashes are frozen in ../SHA256SUMS.json.
"""
 (B / t / 'REPORT.md').write_text(report, encoding='utf-8')
 rows.append(dict(tic=t, physical_verdict=verdict, full_review_completion='COMPLETE', period_days=m['period_days'], period_error_days=m['period_error_days'], primary_epoch_btjd=m['primary_epoch_btjd'], depth_ppt=m['depth_ppt'], limitations=notes[t], next_check=nexts.get(t, 'Optional precision characterization'), source_report=str(src), report=str(B / t / 'REPORT.md')))
with (B / 'RESULTS.csv').open('w', newline='', encoding='utf-8') as f:
 w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print({v: sum(r['physical_verdict'] == v for r in rows) for v in ['CONFIRMED', 'PROBABLE']})
