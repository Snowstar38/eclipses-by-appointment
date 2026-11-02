import csv,json,hashlib,math
from pathlib import Path
import numpy as np
B=Path(__file__).parent;G=json.load(open(B/'gaia-geometry.json'));rows=[]
notes={
'306936928':'Repeated narrow primary and secondary dips are secure, but five flux-capable Gaia neighbors include a 10.59 arcsec G16.77 source requiring an almost total intrinsic eclipse. The compact blended deficit does not uniquely resolve target ownership; PROBABLE.',
'158072011':'Repeated box eclipses and a secondary near phase 0.397. The deficit favors the target over the capable 36.05 arcsec neighbor; the bright blended out-of-eclipse image displaces the light centroid. Saturation/blend morphology limits precision localization.',
'5903277':'Repeated eclipses with unequal secondary near phase 0.495. Compact target-centered deficit; no flux-capable Gaia neighbor within 60 arcsec under the approximate G-band screen.',
'314713331':'Repeated box eclipses and weak secondary near phase 0.500; target-centered deficit distinct from two capable neighbors 36.57 and 53.57 arcsec away.',
'356241663':'Repeated narrow eclipses plus weak secondary. Target-centered deficit without a capable neighbor within 60 arcsec. Gaia conjunction offset-0.0457 phase is descriptive and lies within the propagated orbit timing allowance; it is not a fixed phase-cut rejection.',
'392794270':'Repeated sharp box eclipses are distinct from strong changing baseline variability. No secure secondary phase is assigned. The target-centered difference image and no capable Gaia neighbor support ownership.',
'18558131':'Repeated deep eclipses and shallower secondary near phase 0.500; compact target deficit. The nearby known EB Gaia 5634548560328478848 at 48.69 arcsec has period 0.64499 d, unlike this 5.33939 d signal, and is too faint under the G-band loss budget. It is a contamination alert, not a target catalogue recovery.',
'314040568':'Persistent unequal alternating 120/190 ppt dips reject the historical half-period as an orbital period. The quoted 9.180514665 d ephemeris uses seven deeper odd-parity measured eclipses; shallow even-parity events form the phase 0.500 secondary. Fresh pixel stack uses only deeper events and favors target over the 57.49 arcsec capable neighbor.',
'154652154':'Four QLP primary centers span multiple sectors, with sector 84 primaries two cycles apart. Additional free-center custom 3 x 3 cutout timings in sector 57 include consecutive same-kind 83 ppt eclipses, confirming the 7.47035 d cycle count; see cutout-s 57-timing.json and image. No null is inferred at uncovered QLP cycle 244. Compact deficit has no capable Gaia neighbor.',
'49621708':'Four deep primary eclipses include consecutive pairs in sectors 70 and 92, plus a much shallower secondary near phase 0.496. Compact target deficit and no capable Gaia neighbor within 60 arcsec.'}
prob={'306936928'}
S=json.load(open(B/'secondary-phases.json'))
for q in csv.DictReader(open(B/'queue.csv')):
 tic=q['tic'];D=B/tic;M=json.load(open(D/'measurements.json'));g=G[tic];f=D/'fresh-pixels/diff_fresh.json';d=json.load(open(f));verdict='PROBABLE' if tic in prob else 'CONFIRMED';ev=[e for e in M['events'] if 'mid_btjd' in e];used=[e for e in ev if e.get('timing_usable') and (tic!='314040568' or e['cycle']%2==1)]
 provenance=('The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations.' if d['sector'] in {r['sector'] for r in M['sources']} else 'The retained QLP sectors do not include this cutout sector. This cutout is a distinct observing occasion on the same instrument; it is an alternative extraction of that sector FFI data, without a direct same-sector QLP comparison here.')
 ntext='; '.join(f"Gaia {n['source_id']}: {n['sep']:.2f} arcsec, G={n['G']:.3f}, intrinsic required loss proxy={n['depth_needed']:.3f}" for n in d['neighbours_60'] if n['possible']) or 'None under the approximate G-band brightness screen within 60 arcsec'
 table='\n'.join(f"| {e['sector']} | {e['cycle']} | {e['mid_btjd']:.7f} | {e['formal_timing_error_days']:.6g} | {e['timing_error_days']:.6g} | {e['depth_ppt']:.2f} | {'selected' if e in used else 'excluded center covariance' if not e.get('timing_usable') else 'other parity'} |" for e in ev)
 timing='Measured recurring-eclipse timing supported. '+M.get('timing_selection','Selected primary and unequal secondary morphology support the quoted orbital period; half/double hypotheses were checked.')
 nextcheck='Resolved eclipse photometry or multi-source PRF localization; distinguish alternating event kinds.' if tic in prob else 'Optional resolved photometry and spectroscopy for precision physical parameters.'
 report=f'''# TIC {tic}: {verdict}

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** {len(ev)} free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors {sorted(set(e['sector'] for e in ev))}; {len(used)} enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** {timing} P={M['period_days']:.10f} +/- {M['period_error_days']:.10f} d; reference BTJD={M['primary_epoch_btjd']:.7f}. Epoch kind: {M['epoch_kind']}. {M['error_meaning']} The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in ../alias-audit.json. The epoch kind above states whether the fitted events are identified as deeper primary or selected eclipse by convention. The bounded half/double check does not prove all possible aliases absent.
3. **Attribution.** Fresh difference stack in sector {d['sector']} has {d['n_events']} events; target coordinate {d['target_px']}, deficit {d['deficit_centroid']}; offset {np.hypot(*d['deficit_minus_target_px']):.3f} pixel. The image-model fractional residual {d['psf_fit_frac_resid']:.3f} is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: {ntext}. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. {notes[tic]}
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are {d['depth_ap1']*1000:.2f}/{d['depth_ap3']*1000:.2f}/{d['depth_ap5']*1000:.2f} ppt; selected QLP fitted median {M['depth_ppt']:.2f} ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. {provenance} Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source {g['gaia_source_id']}, orbital P={g['period_days']:.10f} d, e={g['eccentricity']:.5f}. Closest edge-on conjunction offset={g['closest']['offset_days']:.5f} d ({g['closest']['offset_phase']:.5f} phase), full source-specific covariance linear timing allowance={g['closest']['gaia_covariance_linear_error_days']:.5f} d. Mass function={g['mass_function_solar']:.5g} solar masses; adopted primary mass={g['assumed_m1_solar']:.3g}, minimum secondary mass={g['minimum_m2_solar']:.3g}. Rough central duration={g['central_duration_hours_approx']:.2f} h versus observed median={g['observed_duration_hours']:.2f} h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Secondary phase check:** {('Pooled raw-window free-center phase='+str(S[tic]['phase'])+', depth='+str(S[tic]['depth_ppt'])+'ppt. '+S[tic]['error_meaning']) if 'phase' in S[tic] else S[tic]['status']} Weak secondary fits (especially314713331) describe inspected narrow dips and are not independent primary-eclipse evidence or calibrated detection significances. See ../secondary-phases.json and ../secondary-contact.png.

**Deciding limit:** {notes[tic]}

**Next check:** {nextcheck}

Catalogue recovery is recorded centrally in ../../shared-catalogues/coverage-matrix.csv. A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
{table}

Evidence: measurements.json, raw-windows.csv, raw-events.png, fresh-pixels/diff_fresh.json/png, historical original receipts, ../download-receipts.json, ../identity-check.json, ../alias-audit.json, ../gaia-geometry.json and ../helper-audit.md. Original inputs and fresh outputs are covered by ../SHA256SUMS.json and ../source-hashes.json.
'''
 (D/'REPORT.md').write_text(report,encoding='utf8');rows.append(dict(tic=tic,physical_verdict=verdict,full_review_completion='COMPLETE',period_days=M['period_days'],period_error_days=M['period_error_days'],primary_epoch_btjd=M['primary_epoch_btjd'],depth_ppt=M['depth_ppt'],limitations=notes[tic],next_check=nextcheck,source_report=str(f),report=str(D/'REPORT.md')))
with open(B/'RESULTS.csv','w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('9 CONFIRMED, 1 PROBABLE')
