"""Freeze bounded batch08 reports and exact RESULTS schema from measured artifacts."""
import csv, hashlib, json
from pathlib import Path
import numpy as np
B=Path(__file__).resolve().parent; ROOT=B.parent
queue=list(csv.DictReader((B/'queue.csv').open(newline='',encoding='utf-8')))
tim={x['sample_id']:x for x in json.loads((B/'lead-timing.json').read_text())}
geo={x['sample_id']:x for x in json.loads((B/'lead-gaia-covariance.json').read_text())}
pix={x['sample_id']:x for x in json.loads((B/'helper-pixel-audit.json').read_text())}
current={x['sample_id']:x for x in json.loads((B/'lead-current-sectors.json').read_text())}
aliases={x['sample_id']:x for x in json.loads((B/'lead-alias-checks.json').read_text())}
alias_examples={
 'T073':[(2,96,3919.38),(3,96,3923.48)],
 'T076':[(2,93,3846.54),(3,93,3850.95)],
 'T078':[(2,47,2581.86),(3,47,2589.35)],
 'T080':[(2,57,2859.59),(2,77,3420.42),(3,17,1773.87)],
}
classif={
 'T071':('PLAUSIBLE','UNKNOWN','One shallow selected feature is embedded beside a much larger brightening; no secure repeat or eclipse midpoint.','Acquire a target-resolved light curve of a future narrow event and establish recurrence.'),
 'T072':('REFUTED','UNKNOWN','The retained sector-84 feature follows a strong background excursion and disappears in the alternative corrected flux; no eclipse clock.','Revisit only if a new raw event independent of the background transient appears.'),
 'T073':('PROBABLE','UNKNOWN','Target-centered repeated eclipses; photometric period and Gaia SB2 orbit disagree beyond their formal errors, leaving orbital association unresolved.','Obtain new eclipse timing and spectroscopy to test the Gaia SB2 association.'),
 'T074':('CONFIRMED','KNOWN','Previously identified as EA/EB in Thiemann et al. 2021 SuperWASP, with erroneous 1.66-day period; this is a period revision, not a new eclipser.','Update the known-system ephemeris with further timing and cite the prior EA/EB identification.'),
 'T075':('CONFIRMED','UNKNOWN','Repeated two-kind eclipses are target-centered, reduction-robust and consistent with the Gaia SB2 orbit; catalogue novelty remains unverified.','Complete the four unavailable VizieR novelty gates before any new-system claim.'),
 'T076':('PROBABLE','UNKNOWN','Deep same-kind eclipses establish a clock, but Gaia SB2 period and conjunction differ beyond formal errors.','Obtain spectroscopy and new minima to determine whether the eclipses share the Gaia SB2 orbit.'),
 'T077':('PROBABLE','UNKNOWN','Deep eclipses repeat at 14.291 d, nearly half Gaia 28.557 d, but twice the measured period and conjunction disagree with the Gaia formal orbit; a harmonic is unproven.','Obtain independent spectroscopy and resolved imaging to identify the eclipsing orbit.'),
 'T078':('PROBABLE','UNKNOWN','Two-kind target-centered eclipses recur, but measured period and Gaia SB2 conjunction disagree beyond formal errors.','Time further eclipses and reconcile the Gaia spectroscopy.'),
 'T079':('PROBABLE','UNKNOWN','Many target-centered eclipses fix the photometric clock; Gaia SB2 period and conjunction are in tension at formal precision.','Obtain independent RVs or updated Gaia orbit, preserving the measured eclipse clock.'),
 'T080':('PROBABLE','UNKNOWN','Repeated target-centered eclipses survive alternate extraction; Gaia SB2 period and conjunction disagree, and early timing is cadence/gap limited.','Time a complete new eclipse with independent spectroscopy to test the orbit link.'),
}
rows=[]
for q in queue:
 sid=q['sample_id'];tic=q['tic'];out=B/tic;out.mkdir(exist_ok=True)
 verdict,nov,lim,nxt=classif[sid]
 packet=ROOT/'source-packets'/tic/'sources.json'; bulk=Path('[local-path-redacted]')/(tic+'.json')
 pk=json.loads(packet.read_text()); m=json.loads((out/'lead-numeric.json').read_text()); t=tim[sid];g=geo[sid];c=current[sid]
 assert pk['queue_row']['sample_id']==sid and str(pk['target']['gaia']['source_id'])==q['gaia_dr3']
 fit=t.get('period_days'); ferr=t.get('conditional_formal_period_error_days'); depth=None
 if fit:
  depth=float(np.median([e['fit_depth_ppt'] for e in t['events']]))
 report=[f'# {sid}: TIC {tic}', '',f'Physical verdict **{verdict}**; bounded review **COMPLETE**. Catalogue novelty **{nov}**. The fixed queue identity is Gaia DR3 {q["gaia_dr3"]} ({q["nss_type"]}).', '',
 '## Raw evidence and timing','',f'{len(m["sources"])} hashed cached QLP FITS files were read as raw SAP_FLUX with actual QUALITY and time. The detector retained {len(m["events"])} dip windows; these are search windows, not measured eclipses. Representative raw plots are `lead-raw-*.png`, numerical event/coverage records are `lead-numeric.json`, and the explicit same-kind selection and fit are in `lead-timing.json` / `lead_timing.py`.', '']
 if fit:
  report += [f'Selected {t["kind"]} minima give P = **{fit:.6f} d**, epoch BTJD **{t["epoch_btjd"]:.6f}**, and median selected raw trapezoid depth **{depth:.1f} ppt**. The tabulated +/-{ferr:.6f} d period error is conditional on the stated same-kind cycles, selected profiles and scatter-inflated half-cadence timing floor; it is not a total calibrated ephemeris error. Eclipse kind is an internal label, not an assertion of which star is eclipsed.','', '| Sector | BTJD midpoint | Cycle | Raw fit depth (ppt) | O-C (d) |','|---:|---:|---:|---:|---:|']
  report += [f'| {e["sector"]} | {e["mid_btjd"]:.6f} | {e["cycle"]} | {e["fit_depth_ppt"]:.1f} | {e["residual_days"]:+.4f} |' for e in t['events']]
 else:
  report += ['No reliable same-kind repeated eclipse times or orbital period follow from the retained feature. `lead-single-context.png` compares the actual Gaia-period windows in SAP, alternative flux and background; `lead-fold-coverage.json` records time-bin coverage rather than row counts.']
 report += ['', '## Gaia orbit and aliases','',f'Gaia NSS reports P = {float(q["gaia_period_days"]):.9f} d. The edge-on conjunction calculation uses the source-specific full covariance in `shared-catalogues/gaia_nss.csv`, including correlations. At the {"measured selected epoch" if fit else "screening time"}, the nearest nominal conjunction is offset {g["closest"]["offset_days"]:+.3f} d with {g["closest"]["linear_sigma_days"]:.3f} d linear formal allowance. Both conjunctions were tested; this is not a geometric model fit.', '']
 if fit:
  comp=(2*fit if sid=='T077' else fit);gaip=float(q['gaia_period_days']);gaie=float(pk['target']['gaia']['period_error']);report += [f'The comparable photometric period ({"2x " if sid=="T077" else ""}selected P) is {comp:.6f} d; difference from Gaia is {(comp-gaip)/gaie:+.1f} Gaia formal period sigmas. The period and conjunction tests are source-specific evidence, not a universal sigma threshold. Formal Gaia errors may omit systematics; the mismatch does not identify its cause.','']
 if sid=='T073':report += ['The s2 deep A and shallow B events are different eclipse kinds. The s96 A is partly lost in a gap; B in s2, s96 and s104 supplies the 104+11-cycle clock. The shallow s96/s104 non-eclipse flags were not used as timing points.','']
 if sid=='T073':report += ['The 104- and 11-cycle B spacings jointly constrain nearby integer counts. Assigning 10 or 12 cycles to the s96-to-s104 interval gives ~27.051 or ~22.543 d, neither of which gives an integer count for the earlier s2-to-s96 B interval.','']
 if sid=='T075':report += ['The opposite-kind sector-32 B eclipse at BTJD 2194.931 (raw trapezoid ~280 ppt) follows A at 2182.435 (~330 ppt); sector-33 B at 2225.023 (~287 ppt) likewise follows A at 2212.527 (~339 ppt). Both A and B independently recur after 30.092 d, while their unequal depth and ~12.496-d separation reject treating opposite conjunctions as two same-kind repetitions.','']
 if sid=='T076':report += ['Adjacent deep A events in sectors 93, 94 and 95 at BTJD 3833.307, 3859.767 and 3886.226 secure the 26.459-d same-kind interval. Shallower B events near BTJD 1328.660, 3127.901 and 3145.362 occupy a different phase; they are not counted as A minima.','']
 if sid=='T078':report += ['A events at 2020.308, 2604.324 and 3323.115 imply 13 and 16 cycles over the two intervals; B events at 2032.716, 2751.508 and 3335.525 recur at a different phase with shallower raw depths (~84-86 ppt versus A ~198-200 ppt in well sampled sectors). The two consecutive integer spacings and opposite-kind pattern constrain nearby aliases.','']
 if sid=='T080':report += ['The sector-16 A-like event near BTJD 1759.446 is truncated by a gap and excluded from the precision fit; it supplies partial recurrence support only. The selected fit uses sectors 24, 57 and 77. The sector-16/24 shallower B-like events near 1745.410 and 1960.973 support an unequal opposite kind, with sector-84 B near 3600.363. Early 30-min cadence and shape differences keep the stated conditional error from being a total prediction uncertainty.','']
 if sid in alias_examples:
  report += ['Bounded shorter-harmonic checks (`lead-alias-checks.json`) test predicted interleaving same-kind events in actual quality-zero windows, with time-bin core coverage and local side baselines. Representative covered windows (coverage fractions are shown explicitly):','', '| Alias | Sector | Predicted BTJD | Core time coverage | Core deficit (ppt) |','|---:|---:|---:|---:|---:|']
  for den,sec,seed in alias_examples[sid]:
   a=min((w for w in aliases[sid]['windows'] if w['alias_denominator']==den and w['sector']==sec),key=lambda w:abs(w['pred_btjd']-seed))
   assert abs(a['pred_btjd']-seed)<.02 and a['core_time_bin_coverage']>.8 and 'core_deficit_ppt' in a
   report += [f'| P/{den} | {sec} | {a["pred_btjd"]:.3f} | {a["core_time_bin_coverage"]:.2f} | {a["core_deficit_ppt"]:+.1f} |']
  report += ['', 'These near-flat windows argue against P/2 and P/3 aliases at the representative sensitivity shown; they are not a calibrated detection probability or an exhaustive integer-alias proof.','']
 if sid=='T074':report += [f'The earlier comprehensive `Fable 5.1/made/appointments/vet15/REPORT.md` (SHA256 {hashlib.sha256(Path("[local-path-redacted] 5.1/made/appointments/vet15/REPORT.md").read_bytes()).hexdigest()}) finds A P = 22.450574 +/- 0.000054 d and B P = 22.450619 d, five clean eclipses, TESS-SPOC and TARS agreement, on-target TPF deficits and a joint SB2 model. The present selected raw fit independently agrees within its limitations. This target was already reported as EA/EB by Thiemann et al. (2021), 1SWASP J004527.74+210427.9, with P = 1.66 d. Failed contemporary catalogue gates cannot erase that positive prior identification.','']
 if sid=='T077':report += ['Two deep sector-57 A minima are only 14.291 d apart; shallower B minima recur with the same separation, ~6.17 d displaced. Thus the Gaia 28.557 d orbit cannot be assigned to the eclipses merely by calling it a harmonic. A second orbit, Gaia solution error or an incorrect alias remains open.','']
 if sid=='T072':report += ['Positive refutation of the selected feature: sector-84 SAP varies smoothly through a several-thousand-count background excursion; the selected dip vanishes in DET_FLUX. Sector-16 raw ramp also accompanies a severe background drift and is flat in DET_FLUX. These are direct signal/background and reduction contradictions, rather than a conclusion based on lack of repeats.','']
 if sid=='T071':report += ['The sector-45 0.4-ppt selected core lies immediately before a ~1% brightening; the sector-71 predicted window falls on a broad SAP/background drift removed by KSPSAP. The sector-20 window has no compelling matching eclipse. No positive instrumental cause has been established for the tiny sector-45 feature, so the physical interpretation remains plausible rather than refuted.','']
 if sid in pix:
  p=pix[sid]
  report += ['## Source and alternative extraction','',f'Independent TESSCut sector {p["sector"]} raw-pixel extraction measured a **{p["independent_aperture_depth_ppt"]:.1f} ppt** target-centered 3x3 aperture loss, with positive target-pixel median {p["target_pixel_median"]:.1f} counts and positive corrected baseline {p["aperture_baseline"]:.1f} counts. The difference peak is {p["peak_to_target_pixels"]:.2f} pixel from the WCS target position; {p["valid_sky_pixels"]} valid positive sky pixels were used and {p["zero_pixels"]} median pixels were zero. `helper-difference.png`, `helper-pixel-audit.json` and the FITS receipt document this check. It is a separate reduction of the same TESS photons, not another observing occasion.','', 'The shared 120-arcsec Gaia-neighbor inventory finds no neighbor with approximate G-band flux relative to target sufficient to account for the observed 3x3 fractional loss. This is a conservative flux-budget screen, not an absolute localization or a direct comparison of intrinsic neighbor eclipse depth with blended pixel depth. Bandpass, aperture throughput and unresolved sources remain limitations.','']
 else:
  report += ['## Source and alternative reduction','', 'The event morphology was assessed against available QLP processed flux, background and other raw-sector windows in `lead-single-context.png`. A decisive eclipse source was not established, so no target-host claim is made.','']
 report += ['## Coverage, status and next check','',f'Current TESSCut footprint returned {len(c.get("response",{}).get("results",[]))} sector entries (`lead-current-sectors.json`); this is availability, not sensitivity. The present bounded review uses cached sectors and actual quality/time coverage, without extrapolating a null across missing cadences.','',f'Limitation: {lim}',f'Next check: {nxt}','', '## Source receipts','',f'- Queue row: `{B/"queue.csv"}`; exact source packet `{packet}`; SHA256 {hashlib.sha256(packet.read_bytes()).hexdigest()}.',f'- Bulk detector result: `{bulk}`; SHA256 {hashlib.sha256(bulk.read_bytes()).hexdigest()}.', '- Every used QLP FITS SHA256 is in `lead-numeric.json`; TESSCut FITS SHA256 and extraction settings are in `helper-pixel-audit.json` and helper receipts where applicable. The batch SHA manifest freezes reports, scripts and local numeric artifacts.','']
 if sid=='T071':
  i=report.index(f'Limitation: {lim}');report.insert(i,'The availability API also returned `tess-s1751-3-2`, an anomalous sector identifier outside the validated TESS sequence; it was not treated as new sensitive coverage.');report.insert(i+1,'')
 (out/'REPORT.md').write_text('\n'.join(report),encoding='utf-8')
 rows.append(dict(sample_id=sid,tic=tic,sample_stratum=q['sample_stratum'],physical_verdict=verdict,full_review_completion='COMPLETE',novelty_status=nov,period_days=f'{fit:.6f}' if fit else '',period_error_days=f'{ferr:.6f}' if ferr else '',primary_epoch_btjd=f'{t["epoch_btjd"]:.6f}' if fit and t['kind']=='A' else '',depth_ppt=f'{depth:.1f}' if depth else '',limitations=lim,next_check=nxt,report=str(out/'REPORT.md')))
with (B/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('Wrote',len(rows),'reports and RESULTS.csv')
