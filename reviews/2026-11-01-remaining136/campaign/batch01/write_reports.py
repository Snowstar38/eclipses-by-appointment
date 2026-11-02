import csv,json,hashlib,math
from pathlib import Path
import numpy as np
B=Path(__file__).parent;G=json.load(open(B/'gaia-geometry.json'));rows=[]
notes={
'125783923':'Four deep raw eclipses; compact target-centered deficit and no flux-capable Gaia neighbor within 60 arcsec.',
'24928269':'Twelve deep raw eclipses over S3/30/97. Sector-dependent depth is consistent with changing dilution; isolated target-centered deficit.',
'150008480':'Eleven shallow repeated raw eclipses; eleven capable neighbors within 60 arcsec and a noisy deficit leave source attribution unresolved. The Gaia conjunction discrepancy is -0.043 phase, within the descriptive orbit timing uncertainty, and is not evidence of unique target ownership.',
'370553309':'Five long eclipses repeat. A near-equal G=12.65 source at 16.62 arcsec overlaps the deficit core; target ownership is unresolved at this image resolution.',
'78886343':'Eight deep raw eclipses; compact deficit is near the target, distinct from both capable neighbors (approximately 1.7 and 2.4 pixels away). Bright off-target light displaces the out-of-eclipse centroid; it does not move the deficit peak. Target attribution is favored at TESS resolution.',
'1804347444':'Five repeated eclipses; a brighter G=11.54 source only 3.45 arcsec from target is unresolved. Pixel-aperture depth differs from QLP because of strong dilution; this is not a failed eclipse detection.',
'406972595':'Seven repeated raw eclipses with within-sector recurrence in S93; compact target deficit and no capable Gaia neighbor within 60 arcsec.',
'123220066':'Five actual raw midpoints after inspecting all five currently available QLP sectors (8/35/62/89/99). A bounded 0.8-40 day integer-alias test leaves only the 19.389-day recurrence without clean sampled nulls; the half-period predicts four nulls. Two capable sources at 32 and 45 arcsec are separated from the target-centered deficit. One-event image noise and non-calibrated localization remain limitations.',
'371665307':'Repeated 2.49543-day dips are real. Depth parity is not decisive; the quoted 4.99086-day candidate orbital ephemeris uses even half-period parity only and retains a factor-two ambiguity. The shallow crowded deficit has twenty currently flux-capable neighbors and does not uniquely establish target ownership.',
'65709882':'Four deep raw eclipses including consecutive S7 events support recurrence. Fresh deficit lies 0.12 pixel from target while all five capable alternatives are at least about one pixel away. The very bright off-target light dominates the full image but not its compact deficit. Attribution favors target at TESS resolution; nearest capable neighbor limits subpixel claims.'}
prob={'150008480','370553309','1804347444','371665307'}
for q in csv.DictReader(open(B/'queue.csv')):
 tic=q['tic'];D=B/tic;M=json.load(open(D/'measurements.json'));g=G[tic];f=D/'fresh-pixels/diff_fresh.json';d=json.load(open(f));verdict='PROBABLE' if tic in prob else 'CONFIRMED';ev=[e for e in M['events'] if 'mid_btjd' in e];used=[e for e in ev if e.get('timing_usable') and (tic!='371665307' or e['cycle']%2==0)]
 provenance=('The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations.' if d['sector'] in {r['sector'] for r in M['sources']} else 'The retained QLP sectors do not include this cutout sector. This cutout is a distinct observing occasion on the same instrument; it is an alternative extraction of that sector FFI data, without a direct same-sector QLP comparison here.')
 ntext='; '.join(f"Gaia {n['source_id']}: {n['sep']:.2f} arcsec, G={n['G']:.3f}, intrinsic required loss proxy={n['depth_needed']:.3f}" for n in d['neighbours_60'] if n['possible']) or 'None under the approximate G-band brightness screen within 60 arcsec'
 table='\n'.join(f"| {e['sector']} | {e['cycle']} | {e['mid_btjd']:.7f} | {e['formal_timing_error_days']:.6g} | {e['timing_error_days']:.6g} | {e['depth_ppt']:.2f} | {'selected' if e in used else 'excluded center covariance' if not e.get('timing_usable') else 'other parity'} |" for e in ev)
 timing='Candidate orbital timing; factor-two ambiguity retained.' if tic=='371665307' else 'Measured recurring-eclipse timing supported.'
 nextcheck='Resolved eclipse photometry or multi-source PRF localization; distinguish alternating event kinds.' if tic in prob else 'Optional resolved photometry and spectroscopy for precision physical parameters.'
 report=f'''# TIC {tic}: {verdict}

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** {len(ev)} free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors {sorted(set(e['sector'] for e in ev))}; {len(used)} enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** {timing} P={M['period_days']:.10f} +/- {M['period_error_days']:.10f} d; reference BTJD={M['primary_epoch_btjd']:.7f}. Epoch kind: {M['epoch_kind']}. {M['error_meaning']} The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in ../alias-audit.json. Selected eclipse means the measured recurrence, with no assumption that it is the deeper primary. The bounded half/double check does not prove all possible aliases absent. {'For this sparse case, ../sparse-alias-coverage.json and ../terra/123-half-null.png retain additional current-coverage and alias evidence; the null thresholds are heuristic, not confidence limits. Unequal shallower secondary eclipses are not excluded.' if tic=='123220066' else ''}
3. **Attribution.** Fresh difference stack in sector {d['sector']} has {d['n_events']} events; target coordinate {d['target_px']}, deficit {d['deficit_centroid']}; offset {np.hypot(*d['deficit_minus_target_px']):.3f} pixel. The image-model fractional residual {d['psf_fit_frac_resid']:.3f} is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: {ntext}. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. {notes[tic]}
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are {d['depth_ap1']*1000:.2f}/{d['depth_ap3']*1000:.2f}/{d['depth_ap5']*1000:.2f} ppt; selected QLP fitted median {M['depth_ppt']:.2f} ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. {provenance} Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source {g['gaia_source_id']}, orbital P={g['period_days']:.10f} d, e={g['eccentricity']:.5f}. Closest edge-on conjunction offset={g['closest']['offset_days']:.5f} d ({g['closest']['offset_phase']:.5f} phase), full source-specific covariance linear timing allowance={g['closest']['gaia_covariance_linear_error_days']:.5f} d. Full 6x6 orbit correlation matrix is positive definite (helper receipt). Mass function={g['mass_function_solar']:.5g} solar masses; adopted primary mass={g['assumed_m1_solar']:.3g}, minimum secondary mass={g['minimum_m2_solar']:.3g}. Rough central duration={g['central_duration_hours_approx']:.2f} h versus observed median={g['observed_duration_hours']:.2f} h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Deciding limit:** {notes[tic]}

**Next check:** {nextcheck}

Catalogue recovery is recorded centrally in ../../shared-catalogues/coverage-matrix.csv. A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
{table}

Evidence: measurements.json, raw-windows.csv, raw-events.png, fresh-pixels/diff_fresh.json/png, historical original receipts, ../measurement-source-receipts.json, ../identity-check.json, ../alias-audit.json, ../gaia-geometry.json and ../helper-audit.md. Original inputs and fresh outputs are covered by ../SHA256SUMS.json and ../source-hashes.json.
'''
 (D/'REPORT.md').write_text(report,encoding='utf8');rows.append(dict(tic=tic,physical_verdict=verdict,full_review_completion='COMPLETE',period_days=M['period_days'],period_error_days=M['period_error_days'],primary_epoch_btjd=M['primary_epoch_btjd'],depth_ppt=M['depth_ppt'],limitations=notes[tic],next_check=nextcheck,source_report=str(f),report=str(D/'REPORT.md')))
with open(B/'RESULTS.csv','w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('6 CONFIRMED, 4 PROBABLE')
