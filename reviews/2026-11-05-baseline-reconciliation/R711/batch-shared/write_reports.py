import csv,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'))
G=json.loads((B/'gaia-geometry.json').read_text(encoding='utf-8'))
C=json.loads((B/'coverage-alias.json').read_text(encoding='utf-8'))
N={r['tic']:r for r in json.loads((B/'helper-pixels/final-neighbors.json').read_text(encoding='utf-8'))}
A=json.loads((B/'sparse-aliases.json').read_text(encoding='utf-8'))
K={r['tic']:r for r in csv.DictReader((B.parent/'remaining_cached/catalogue-recovery-late/coverage-matrix.csv').open(encoding='utf-8',newline=''))}
V={'257992903':'PROBABLE','70561926':'CONFIRMED','380395732':'PROBABLE','280950412':'PLAUSIBLE','188908998':'PLAUSIBLE'}
L={
'257992903':'Two Gaia neighbors at 47.26 and 54.64 arcsec remain capable under an optimistic G-band/full-capture screen; the target-like pixel deficit does not calibrate source ownership.',
'70561926':'The Gaia period differs from the eclipse fit by 0.04084 d (1.67 Gaia quoted standard errors), and the closest conjunction is 1.39 d away with 1.48 d source-specific linear covariance uncertainty. The exact VSX counterpart is a known EB.',
'380395732':'Two Gaia neighbors at 39.52 and 52.68 arcsec remain capable under an optimistic G-band/full-capture screen. The 5×5 pixel loss is diluted relative to the 1×1; source ownership needs higher spatial resolution.',
'280950412':'The two putative shallow dips are baseline- and aperture-dependent, with no reliable raw-event timing fit. All tested aliases lack sensitivity to a 1.2-ppt repeat; the screen conjunction is not a measured event. Severe crowding prevents source attribution.',
'188908998':'Only two raw same-kind events, 32 putative cycles apart, have usable centers. The neighboring 31-cycle alias has no sensitive intermediate coverage, so the integer period is untested; two capable Gaia neighbors remain.'}
NX={
'257992903':'Higher-resolution photometry during a predicted event to identify the eclipsing Gaia source.',
'70561926':'Compare a new timed eclipse and radial velocities with the Gaia orbit and VSX ephemeris.',
'380395732':'Higher-resolution event photometry of the target and capable neighbors.',
'280950412':'Obtain a clean, sensitive repeat in a new TESS sector or ground-based time series before fitting an eclipse clock.',
'188908998':'Observe a clean predicted eclipse to distinguish the 31- and 32-cycle aliases and localize the source.'}
weak=json.loads((B/'weak-events-280950412.json').read_text())
m280=json.loads((B/'280950412/measurements.json').read_text());m280['weak_event_candidates']=weak;m280['timing_note']='No reliable repeated raw SAP center or period fit; weak fitted minima are diagnostic, not accepted timings.';(B/'280950412/measurements.json').write_text(json.dumps(m280,indent=2,default=float)+'\n',encoding='utf-8')
rows=[]
for r in Q:
 t=r['tic'];m=json.loads((B/t/'measurements.json').read_text());g=G[t];n=N.get(t);cov=C[t]['windows'];k=K[t]; verdict=V[t]
 lines=[f'# TIC {t} — {verdict}', '', f'Bounded physical review **COMPLETE**, ID {r["review_id"]}. The sealed five-target queue position {r["position_in_batch"]} is operational. Gaia DR3 source {r["gaia_dr3"]}. Physical outcome and catalogue novelty are separate.', '', '## Raw flux and cycle evidence','']
 lines.append('The sealed snapshot gives '+str(len(D[t]['target']['file_receipts']))+' QLP FITS receipts. `../measure_raw.py` verified each SHA-256 and fitted representative quality-zero raw SAP windows with free centers. '+('The weak phase panels are in `../weak-phase-280950412.png` and diagnostic fits in `measurements.json`.' if t=='280950412' else 'Raw event panels and all fits are in `raw-events.png` and `measurements.json`.')+' The screen ephemeris located windows; its predictions are not timings.')
 if t=='280950412':
  lines.append('No event passed the standard timing fit. A deliberately lower-threshold diagnostic in `../weak-events-280950412.json` finds putative s11 BTJD 1603.60784 (1.28 ppt, local OOT scatter 0.61 ppt) and s64 BTJD 3061.50609 (1.16 ppt, scatter 2.15 ppt) minima. The s10 predicted window has no convincing deficit (0.23 ppt low-third against 1.85 ppt scatter), while s99 shows a broad baseline ramp. These are not accepted mid-times. The 64-cycle 22.77966-d quotient and screen 22.77774-d period are conditional aliases, not a measured ephemeris.')
 else:
  ev=[e for e in m['events'] if e.get('timing_usable')];adj=any(b['cycle']-a['cycle']==1 for a,b in zip(ev,ev[1:]));lines.append(f'{len(ev)} usable same-kind centers span cycles {ev[0]["cycle"]}–{ev[-1]["cycle"]}; adjacent-cycle anchor: {"yes" if adj else "no"}. Median realized trapezoid depth {m["depth_ppt"]:.2f} ppt. The weighted fit gives P = {m["period_days"]:.9f} ± {m["period_error_days"]:.9f} d and selected-kind reference epoch BTJD {m["reference_epoch_btjd"]:.8f} ± {m["epoch_error_days"]:.8f} d at cycle {m["reference_cycle"]}. Center errors are max(formal covariance, half cadence), with scatter inflation if reduced χ² > 1; no model, pipeline or long-term systematic allowance is included.')
  lines+=['','| Sector | Cycle | Mid BTJD | Center error d | Depth ppt |','|---:|---:|---:|---:|---:|']
  for e in ev:lines.append(f'| {e["sector"]} | {e["cycle"]} | {e["mid_btjd"]:.5f} | {e["timing_error_days"]:.6f} | {e["depth_ppt"]:.2f} |')
  if t=='70561926':lines.append('The irregularly spaced four sectors fix the cycle count despite no adjacent pair: fitting s8→s35 as 35 cycles predicts s62/s89 within 0.0048 d, while 34 or 36 cycles miss s62 by 0.636 or 0.594 d. These are observed event-center residuals, not predicted-window nulls.')
 lines+=['','`../coverage-alias.json` samples actual main and opposite-phase quality-zero windows, requiring central samples and bilateral sidebands. Incomplete or flagged predictions are not clean nulls. Main clean sample: '+', '.join(f's{w["sector"]}/c{w["cycle"]} {w["core_median_deficit_ppt"]:.1f} ppt (scatter {w["oot_scatter_ppt"]:.1f})' for w in cov if w['kind']=='same' and w['status']=='measured_clean_window')+'.']
 if t in A:
  aa=A[t]['candidate_aliases'];lines.append('`../sparse-aliases.json` tests integer-cycle alternatives with actual quality-zero central and bilateral sideband coverage. '+('The 31-cycle (23.4371 d) alternative has no sensitive intermediate window, as does the 32-cycle (22.7047 d) candidate; 33 cycles has one sensitive null. Thus Gaia agreement does not itself measure the cycle count.' if t=='188908998' else 'For the nominal 64-cycle 22.7797-d quotient, four windows are covered but none has local scatter below one-third of the putative 1.2-ppt depth. No tested alias is excluded by a sensitive clean null.'))
 lines+=['','## Source and orbit checks','']
 if n:
  ap=n.get('pixel_apertures_ppt',{});lines.append('A separate background-subtracted TESScut extraction of the same TESS photons gives 1×1/3×3/5×5 aperture losses '+('/'.join(f'{ap[x]:.2f}' for x in ('1x1','3x3','5x5')) if ap else 'unavailable')+' ppt in sector '+str(n['sector'])+f'. The positive difference peak is {n["cutout"]["centroid_offset_pixels"]:.3f} pixel from the target, a descriptive offset rather than a calibrated localization likelihood. QLP alternative apertures are one pipeline and are not independent reduction.')
  capable=n.get('capable_at_minimum_all_apertures',n.get('capable_at_conservative_depth',[]));lines.append(f'The full 60″ Gaia census has {n["gaia_sources_within_60arcsec"]} sources and {len(capable)} capable other source(s) using the minimum measured aperture loss, G-band flux as a TESS proxy and optimistic full throughput. Required fractions are **intrinsic neighbor eclipses**, not blended pixel deficits. '+('; '.join(f'{x["source_id"]} at {x["sep_arcsec"]:.2f}″ requires {x["intrinsic_eclipse_fraction"]:.3f}' for x in capable) if capable else 'No other Gaia source passes this optimistic capability test.')+'.')
 else:lines.append('The s11/s64 custom TESScut reductions show 1×1/3×3/5×5 losses of 3.53/0.87/1.12 and 2.49/0.72/0.47 ppt, respectively. Strong aperture dependence and baseline uncertainty preclude a positive difference-image localization. The 60″ Gaia cone contains 169 sources, 57 of them conditionally capable at assumed 1.2 ppt under the G-band/full-throughput proxy; this is a capability screen, not evidence that all contaminate the aperture.')
 lines.append(f'Gaia SB1 P = {g["gaia_period_days"]:.8f} ± {g["gaia_period_error_days"]:.8f} d, e = {g["eccentricity"]:.4f}, mass function {g["mass_function_solar"]:.4f} solar masses. '+(f'The raw fitted period differs by {g["period_difference_days"]:+.6f} d. ' if g['period_difference_days'] is not None else 'There is no accepted eclipse period to compare. ')+f'The nearest edge-on conjunction to the {"measured" if g["epoch_source"]=="raw_event_fit" else "unverified screen"} epoch is {g["closest"]["offset_days"]:+.3f} d ({g["closest"]["offset_phase"]:+.4f} phase), with source-specific Gaia covariance linear error {g["closest"]["gaia_linear_covariance_error_days"]:.3f} d. This is a descriptive geometry check, not an ownership probability.')
 lines+=['','## Catalogue, outcome and next check','']
 if t in ('257992903','380395732'):cat='Exact prior EB identification in IJspeert et al. (2024): known recovery in the completed seven-group catalogue scope.'
 elif t=='70561926':cat='VSX EA KELT KS22C028401 (OID 2213487), 0.30″ from the selected Gaia source, has P = 21.49257 d. The Gaia cone contains no second source within 2″ and the raw 21.49419-d clock agrees closely: target association is strongly supported and this is a **known recovery**, resolving the matrix identity alert.'
 else:cat='No prior EB was identified in the completed seven-group queried catalogue scope. This is a catalogue statement only; a plausible physical outcome does not support a new-system claim.'
 lines.append(cat+' Catalogue evidence is `../../remaining_cached/catalogue-recovery-late/coverage-matrix.csv` and its source receipts. No exhaustive literature novelty claim is made.')
 lines+=['',f'**Physical outcome: {verdict}.** {L[t]}', '', '**Next check:** '+NX[t], '', 'Alternative TESScut extraction uses the same photons as QLP, not another observing occasion. MAST QLP availability for the two sparse targets is documented in `../helper-pixels/mast-availability.json`; no newer QLP sectors are listed.']
 (B/t/'REPORT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 rows.append(dict(tic=t,physical_verdict=verdict,full_review_completion='COMPLETE',period_days=f'{m["period_days"]:.9f}' if t not in ('280950412','188908998') else '',period_error_days=f'{m["period_error_days"]:.9f}' if t not in ('280950412','188908998') else '',primary_epoch_btjd=f'{m["reference_epoch_btjd"]:.8f}' if t not in ('280950412','188908998') else '',depth_ppt=f'{m["depth_ppt"]:.2f}' if t!='280950412' else '',limitations=L[t],next_check=NX[t],source_report=str(B/t/'measurements.json'),report=str(B/t/'REPORT.md')))
with (B/'RESULTS.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
