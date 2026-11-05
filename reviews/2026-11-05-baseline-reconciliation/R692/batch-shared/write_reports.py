"""Write exact-nine bounded physical reviews; catalogue novelty is external to these rows."""
import csv,json,math
from pathlib import Path
B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
G=json.loads((B/'gaia-geometry.json').read_text(encoding='utf-8'))
C=json.loads((B/'coverage-alias.json').read_text(encoding='utf-8'))
X={x['tic']:x for x in json.loads((B/'helper-pixels'/'conservative-neighbors.json').read_text(encoding='utf-8'))}
notes={
'159060569':('CONFIRMED','Six raw SAP eclipses are visibly repeated across four sectors, though two gap-shaped fits have unidentifiable center covariance and are excluded from the timing fit. Sector 98 is shallower, consistent with sector-dependent aperture dilution.','Additional clean sectors to monitor the aperture-dependent depth.'),
'387268955':('CONFIRMED','Fourteen usable broad same-kind eclipses across many sectors; sector 60 is shallower at an edge window. Two additional fitted windows are excluded for incomplete/unidentifiable timing.','Optional new clean events to refine ephemeris.'),
'342060048':('PROBABLE','Four narrow deep events repeat, including consecutive sector 40 cycles. The 17.52-arcsec capable Gaia neighbor lies less than one TESS pixel away; target-centered difference imaging favors the target but does not resolve the blend. Gaia period and conjunction are modestly discrepant at formal error scale.','Resolved-source photometry or multi-source PSF localization, and new timing to test Gaia-orbit identity.'),
'184398115':('PROBABLE','Four very deep repeated eclipses include consecutive sector 97 cycles, and the deficit is target-centered with no capable Gaia neighbor in the 60-arcsec cone. The measured eclipse period and phase are materially inconsistent with the formal Gaia SB2 orbit; a distinct eclipsing binary in a multiple system or a problematic Gaia orbit remains possible.','New radial-velocity orbit and clean eclipse timings to establish whether the Gaia and eclipse clocks belong to the same pair.'),
'64701575':('CONFIRMED','Four clean rounded eclipses across sectors 33/34/87/88; sector 7 contains a partial predicted window. The timing and target-centered difference image support the Gaia-orbit eclipse identification.','Optional clean sector 7 counterpart or future timing.'),
'284613090':('PROBABLE','Four deep same-kind eclipses repeat, with two consecutive sector 33 cycles. Deep opposite half-phase events are also measured; unequal depths support the full 23.1095-day photometric branch. The target-centered difference image has no capable Gaia neighbor, but Gaia SB2 period and conjunction differ materially at formal precision.','New radial velocities and eclipse timing to reconcile the Gaia spectroscopic and photometric orbits.'),
'128720791':('PROBABLE','Three clean narrow same-kind dips in sectors 16/56/83; the earlier sector 56 predicted cycle lies at the sector boundary and is not a clean null. Explicit 15–30 d integer-cycle enumeration found a 16.2798 d alias, but three additional clean predicted windows have near-zero loss and refute that equal-depth branch. The Gaia-near 21.7064 d branch has no contradictory clean window. The signal is reproduced by separate TESScut extraction and a target-centered difference image; Gaia phase/period differences remain a limitation.','Additional clean event and independent Gaia-orbit comparison.'),
'95623701':('PLAUSIBLE','The deep sharp sector 12 and 103 events have similar shape at an assumed 112-cycle alias, but sector 39 is much weaker and a fully covered quality-zero sector 65 predicted window is a clean null for that alias. The helper TESScut 3×3 extraction independently finds 93.06, 13.81, 0.124, and 126.81 ppt in sectors 12/39/65/103; aperture size alone does not explain the null. A 16.81-arcsec Gaia neighbor is capable only under a very deep intrinsic eclipse and remains unresolved at the pixel scale. The assumed alias also disagrees strongly with Gaia. The repeated-looking signal has no secure persistent orbital clock or source ownership.','Resolved multi-source photometry and new clean epochs to test recurrence and source ownership.'),
'56912737':('CONFIRMED','Three compact dips in sectors 21 and 47 give two adjacent sector 47 cycles; measuring the individual centers resolves the apparent phase displacement of the earlier sector 47 window. Timing agrees with the Gaia period within stated errors and the deficit is target-centered.','Optional additional clean timing epoch.'),
}
rows=[]
for q in Q:
 t=q['tic'];m=json.loads((B/t/'measurements.json').read_text(encoding='utf-8'));c=C[t];g=G[t];x=X[t];v,assessment,nextcheck=notes[t]
 P=m.get('period_days',m.get('conditional_112_cycle_period_days'));Pe=m.get('period_error_days',m.get('conditional_112_cycle_formal_period_error_days'));ep=m.get('reference_epoch_btjd',m.get('conditional_112_cycle_reference_epoch_btjd'));epe=m.get('epoch_error_days',m.get('conditional_112_cycle_formal_epoch_error_days'));dep=m.get('depth_ppt',m.get('median_selected_event_realized_depth_ppt'));chi=m.get('reduced_chi_square',m.get('conditional_112_cycle_reduced_chi_square'))
 good=[e for e in m['events'] if e.get('timing_usable')];deep=[w for w in c['windows'] if w['kind']=='same' and w['status']=='measured_clean_window'];half=[w for w in c['windows'] if w['kind']=='half' and w['status']=='measured_clean_window']
 event_table='\n'.join(f"| {e['sector']} | {e['cycle']} | {e['mid_btjd']:.8f} | {e['timing_error_days']:.6f} | {e['depth_ppt']:.2f} |" for e in good)
 observed_hours=sorted(e['duration_days']*24 for e in good)[len(good)//2]
 cov_table='\n'.join(f"| {w['sector']} | {w['cycle']} | {w['n_core_quality0']} | {w.get('core_median_deficit_ppt',float('nan')):.2f} | {w.get('oot_scatter_ppt',float('nan')):.2f} |" for w in deep)
 half_table='\n'.join(f"| {w['sector']} | {w['cycle']} | {w['n_core_quality0']} | {w.get('core_median_deficit_ppt',float('nan')):.2f} |" for w in half)
 nb='\n'.join(f"| {n['id']} | {n['sep_arcsec']:.2f} | {n['G']:.3f} | {100*n['required_fraction']:.1f}% |" for n in x['capable_using_min_qlp_or_ap5']) or '| None | | | |'
 near=g['closest'];p=B/t/'REPORT.md'
 ephemeris=f"{len(good)} identifiable same-kind centers give **P = {P:.9f} ± {Pe:.9f} d**, epoch **BTJD {ep:.8f} ± {epe:.8f} d** for the selected repeating eclipse. This is not automatically the deeper primary. Median realized QLP depth is {dep:.2f} ppt. {m['timing_error_meaning']} Reduced chi-square is {chi:.3f}; formal values are conditional on the chosen event family and timing model."
 if t=='95623701':ephemeris=f"The selected events can be fit under an **assumed 112-cycle alias** with P={P:.9f} d and reference BTJD {ep:.8f}; conditional fit errors {Pe:.9f} d and {epe:.8f} d are retained in measurements.json. The clean sector-65 null refutes an uncomplicated constant-depth interpretation, and alternative integer aliases and source ownership remain open. **No secure period or reference epoch is reported.** The selected-event median realized depth is {dep:.2f} ppt; reduced chi-square for the conditional fit is {chi:.3f}."
 diff_label='Conditional assumed-alias minus Gaia period' if t=='95623701' else 'The photometric minus Gaia period'
 epoch_label='the conditional alias-fit reference epoch' if t=='95623701' else 'the measured eclipse epoch'
 coverage_label='the conditional 112-cycle fit' if t=='95623701' else 'the measured ephemeris'
 report=f'''# TIC {t} — {v}

Bounded full physical review: **COMPLETE**. Review ID {q['review_id']}. {assessment}

## Raw SAP and timing

The sealed SOURCE-SNAPSHOT.json identifies the Gaia source, screening branch, and exact QLP FITS receipts. `measure_raw.py` verified every QLP SHA-256 before extracting quality-zero raw SAP_FLUX. Individual event centers were free trapezoid fits, with realized depth `d × min(1,w/(2k))` recorded separately from fitted model amplitude. Representative raw panels are in `raw-events.png`. The screening predictions only located windows; they are not timing points. {ephemeris}

| Sector | Same-kind cycle | Measured midpoint BTJD | Conservative center error d | Realized depth ppt |
|---|---:|---:|---:|---:|
{event_table}

The independent `coverage_alias.py` samples clean main and opposite half-phase windows from {coverage_label}. Main-window median core deficits and local robust scatter (ppt) are below. Missing or flagged windows are retained in `coverage-alias.json` and never treated as clean nulls.

| Sector | Cycle | Clean core samples | Core deficit ppt | OOT scatter ppt |
|---|---:|---:|---:|---:|
{cov_table}

Clean opposite half-phase windows test the half-period alias. A near-zero deficit is evidence against equal-depth P/2 recurrence; the deep half-phase events for TIC 284613090 are an observed second eclipse kind, not same-kind recurrences.

{'The near-Gaia period alias for TIC 128720791 was separately enumerated in `../alias-128720791.json`; the 16.2798 d branch has three clean, near-zero predicted windows.' if t=='128720791' else ''}

| Sector | Cycle | Clean core samples | Core deficit ppt |
|---|---:|---:|---:|
{half_table}

## Pixel source and alternate reduction

The helper's independent background-subtracted TESScut difference extraction uses the **same TESS FFI photons** as QLP sector {x['sector']}; it checks pipeline/aperture robustness, not a second observation. The positive deficit centroid is {x['offset_px']:.3f} pixel from the target in that sector, with 5×5 aperture depth {x['ap5_depth_ppt']:.2f} ppt. This offset is descriptive, not a calibrated localization likelihood; see `../helper-pixels/{t}/difference.png` and the pixel JSON for the full image and apertures. The Gaia DR3 60-arcsec neighbor cone and optimistic G-band/full-throughput capability screen find:

| Capable Gaia source | Separation arcsec | G | Minimum intrinsic eclipse fraction proxy |
|---|---:|---:|---:|
{nb}

Capability uses the smaller QLP/TESScut representative loss as a conservative screen. A neighbor's required **intrinsic** eclipse loss cannot be equated to its **diluted pixel** loss. Color, aperture throughput, unresolved companions, and subpixel crowding limit attribution.

## Gaia orbit and physical interpretation

Gaia DR3 source {g['gaia_source_id']} has a {g['solution_type']} solution with P = {g['gaia_period_days']:.9f} ± {g['gaia_period_error_days']:.9f} d, eccentricity {g['eccentricity']:.5f}, ω = {g['omega_deg']:.3f}°, and mass function {g['mass_function_solar']:.5g} M☉. The closest edge-on conjunction ({near['kind']}) differs from {epoch_label} by {near['offset_days']:+.4f} d ({near['offset_phase']:+.5f} phase); source-specific Gaia full-covariance linear timing uncertainty at that epoch is {near['gaia_linear_covariance_error_days']:.4f} d. {diff_label} is {g['period_difference_days']:+.6f} d. `gaia-geometry.json` retains both conjunctions, the correlation order, and the exact orbital inputs; `helper-geometry.json` is an independent calculation. Linear covariance is descriptive, not a sigma veto; an RV orbit or component assignment may need revisiting where mismatch is large. Median fitted eclipse duration is about {observed_hours:.2f} h, physically plausible for stellar-size eclipses in a 20–23 d orbit, but no fitted stellar radii or masses are claimed.

## Outcome and next observation

Physical outcome is **{v}** after completed bounded review. Catalogue novelty is a separate shared-catalogue decision; a failed query is unknown, not a non-match. Limits: {assessment} Next decisive check: {nextcheck}
'''
 p.write_text(report,encoding='utf-8')
 rows.append(dict(tic=t,physical_verdict=v,full_review_completion='COMPLETE',period_days='' if t=='95623701' else f'{P:.9f}',period_error_days='' if t=='95623701' else f'{Pe:.9f}',primary_epoch_btjd='' if t=='95623701' else f'{ep:.8f}',depth_ppt=f'{dep:.2f}',limitations=assessment,next_check=nextcheck,source_report=str(B/t/'measurements.json'),report=str(p)))
with (B/'RESULTS.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
