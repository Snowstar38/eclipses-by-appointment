import csv,json,hashlib,shutil
from pathlib import Path
import numpy as np
B=Path(__file__).parent; SB=Path('[local path omitted]');G=json.load(open(B/'gaia-geometry.json'));P=json.load(open(B/'pixel-audit.json'));rows=[]
notes={
'438188407':'Deep repeated flat-bottom eclipses in three widely separated sectors. Capable neighbors are more than 2.24 pixels from the deficit, versus target 0.173 pixel. Gaia period drift is acknowledged through propagated covariance; no arbitrary formal-error veto is used.',
'62337815':'Four isolated flat-bottom eclipses in sectors 76/83 with consecutive cycles in each. The 12.25 arcsec capable neighbor is 0.833 pixel from the deficit versus target 0.249 pixel; full image favors target, with residual subpixel crowding limitation.',
'399285183':'Seven repeated localized shallow eclipses, with clean flat surrounding baseline in sector 81 and consecutive measured cycles. Capable neighbors are at least 1.135 pixels from the deficit versus target 0.142 pixel.',
'399868192':'Repeated flat-bottom eclipses across sectors 5/71/98. Sector 98 cycle 398 lacks ingress and has singular center covariance, so it is excluded from timing. Other consecutive events anchor the recurrence. Capable neighbors are at least 1.86 pixels from deficit versus target 0.057 pixel.',
'457003443':'Repeated isolated flat-bottom shallow eclipses across sectors 43/45/72. Full deficit image favors target at 0.218 pixel; capable neighbors are at least 1.708 pixels away. Aperture dilution and baseline variability limit depth interpretation.',
'76020303':'Near-equal alternating eclipses recur every 1.85264 d. Same-parity even events give the reported orbital period 3.705279 d, consistent with Gaia 3.705347 d. Photometry alone retains the half-period interpretation because parity depths are indistinguishable; Gaia supplies the orbital interpretation, not an unannounced alias replacement. Both conjunctions are plausible for the paired eclipses. The target is 0.057 pixel from deficit versus capable neighbors beyond 2.12 pixels.',
'251798466':'Three complete deep eclipses in sector 81, consecutive cycles 81-83, measure the period. Earlier sector 54 cycle 0 is a visibly partial raw repeat and supports recurrence but contributes no precision timing. Only the short complete-event baseline sets the stated formal error. Target deficit 0.063 pixel versus capable neighbor 2.789 pixels.',
'363264601':'Repeated localized 4-5 ppt depressions have flat surrounding baseline in sectors 100/103 and support genuine eclipses. Attribution remains unresolved after a completed check: a 5.595 arcsec neighbor can supply the signal with 1.85 percent intrinsic loss. Target/neighbor deficit distances 0.093/0.350 pixel favor the target but do not reliably distinguish these close sources without a calibrated localization. This is PROBABLE because the eclipses repeat and attribution is unresolved, not because their morphology is uncertain.',
'399089869':'Deep repeated isolated eclipses across sectors 23/46/91; sector 46 consecutive cycles 70/71 test recurrence. No capable neighbor in the saved 60 arcsec cone. Aperture-dependent dilution limits intrinsic depth.',
'329559935':'Only sector 80 supplied usable selected QLP data. Unequal alternating depths (odd median about 87.97 ppt; even about 41.28 ppt) establish the doubled orbital period, with five measured odd deeper eclipses spanning cycles -1 to 15. Half-period recurrence mixes two unequal eclipse types. Measured 2.603735 d agrees with Gaia 2.603862 d within the descriptive timing uncertainty; queue 2.60568 d is a historical search value, not adopted. Target deficit 0.081 pixel versus capable neighbors beyond 1.362 pixels.'}
for q in csv.DictReader(open(B/'queue.csv')):
 t=q['tic'];D=B/t;M=json.load(open(D/'measurements.json'));g=G[t];p=P[t];src=Path(p['difference_path']);d=json.load(open(src));ev=[e for e in M['events'] if 'mid_btjd' in e];v='PROBABLE' if t=='363264601' else 'CONFIRMED';nextcheck='Resolved eclipse photometry or calibrated multi-source PRF localization' if v=='PROBABLE' else 'Optional resolved photometry or spectroscopy for precision characterization'
 hist=D/'historical';hist.mkdir(exist_ok=True)
 for f in [src,src.with_suffix('.png'),src.parent/'gaia.json']:shutil.copy2(f,hist/f.name)
 nb='; '.join(f"Gaia {n['source_id']}: separation {n['separation_arcsec']:.3f} arcsec, required intrinsic fractional eclipse {n['intrinsic_fractional_eclipse_required']:.4f}, deficit distance {n['deficit_distance_px']:.3f} pixel" for n in p['capable']) or 'No capable listed source within the saved 60 arcsec cone.'
 table=[]
 for e in ev:
  used=e.get('timing_usable',False) and (t not in ('76020303','329559935') or e['cycle']%2==(1 if t=='329559935' else 0))
  status='used' if used else e.get('timing_failure_reason','other eclipse parity; excluded from same-kind ephemeris')
  table.append(f"| {e['sector']} | {e['cycle']} | {e['mid_btjd']:.7f} | {e['timing_error_days']:.7f} | {e['depth_ppt']:.3f} | {status} |")
 report=f'''# TIC {t}: {v}

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. Current section 2.7 five-check standard applied; historical screening is not itself admission evidence.

1. **Raw flux: pass.** {len(ev)} fitted event windows in sectors {sorted(set(e['sector'] for e in ev))} were examined in raw-events.png and numeric raw-windows.csv. Repeated localized ingress/egress depressions and surrounding baseline were visually inspected; trapezoid fits alone are not the eclipse interpretation. QLP raw SAP_FLUX with quality zero is used for these measurements. Coverage requirements are in review_measure.py; uncovered/flagged windows are not clean nulls. At most three spread available sectors were initially selected; no mandatory all-event or all-sector analysis is implied.
2. **Measured timing: pass.** {M['timing_event_count']} same-kind measured centers give P = {M['period_days']:.10f} +/- {M['period_error_days']:.10f} d and reference epoch BTJD {M['primary_epoch_btjd']:.7f}. Epoch kind: {M['epoch_kind']}. Predicted historical centers only seed windows and cycle counts, not measured timings. Within-sector recurrence/parity tests are retained in alias-audit.json; this is not an exhaustive blind alias scan. Error meaning: {M['error_meaning']} Partial/singular fits remain documented and excluded; the epoch may denote a selected repeating eclipse rather than an independently established deeper primary.
3. **Source attribution: {'unresolved after completed check' if v=='PROBABLE' else 'pass at TESS resolution'}.** Original cutout WCS/Gaia identity audited in pixel-audit.json. Saved sector {d['sector']} deficit-target distance {p['target_deficit_distance_px']:.3f} pixel; full deficit image examined against every flux-capable listed source. Capable neighbors: {nb} Required intrinsic fractional eclipse and observed blended pixel fractional loss have different dilution and are not directly compared to exclude neighbors. The approximate G-band budget and saved 60 arcsec cone limit this check.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut 1x1/3x3/5x5 apertures show depths {d['depth_ap1']*1000:.3f}/{d['depth_ap3']*1000:.3f}/{d['depth_ap5']*1000:.3f} ppt from {d['n_events']} stacked events; current selected-kind QLP median {M['depth_ppt']:.3f} ppt. These are reductions of the same TESS photons, not independent observing occasions. Dilution, aperture differences and mixed primary/secondary stacks can change depth; no claim of equal intrinsic depths is made.
5. **Gaia orbital geometry: pass with limitations.** DR3 {g['gaia_source_id']}, P = {g['period_days']:.10f} +/- {g['period_error_days']:.10f} d, e = {g['eccentricity']:.6f}, omega = {g['omega_deg']:.4f} deg. Closest edge-on conjunction is offset {g['closest']['offset_days']:.6f} d ({g['closest']['offset_phase']:.6f} phase), with full SB1 covariance linear propagated uncertainty {g['closest']['gaia_covariance_linear_error_days']:.6f} d at measured epoch. Projection near Gaia reference gives offset {g['near_reference']['offset_days']:.6f} d; photometric period projection allowance {g['near_reference']['period_projection_allowance_days']:.6f} d excludes covariance and model systematics. Approximate central duration {g['central_duration_hours_approx']:.2f} h versus fitted median {g['observed_duration_hours']:.2f} h is an illustration using TIC radius/mass and a minimum-mass main-sequence companion, not a fitted geometry. No arbitrary sigma veto; gaia-geometry.json preserves all assumptions and both conjunctions.

**Deciding interpretation and limitations:** {notes[t]}

**Next check:** {nextcheck}.

Catalogue novelty: see central ../../shared-catalogues/coverage-matrix.csv; this report does not establish exhaustive literature priority. Current observed repeats remove a single-cycle availability question; the short-baseline cases explicitly state their evidence.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing input error d | Depth ppt | Timing status |
|---|---|---|---|---|---|
{chr(10).join(table)}

Evidence: measurements.json, raw-events.png, raw-windows.csv, historical/{src.name}, historical/{src.stem}.png, historical/gaia.json; batch ../pixel-audit.json, ../alias-audit.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Raw cutout: {p['cutout_path']}. Historical extraction definitions: {SB.as_posix()}/diffstack.py and c3_sapdepth.py. Reused source hashes in source-hashes.json; no historical evidence overwritten.
'''
 (D/'REPORT.md').write_text(report,encoding='utf-8')
 rows.append(dict(tic=t,physical_verdict=v,full_review_completion='COMPLETE',period_days=M['period_days'],period_error_days=M['period_error_days'],primary_epoch_btjd=M['primary_epoch_btjd'],depth_ppt=M['depth_ppt'],limitations=notes[t],next_check=nextcheck,source_report=str(src),report=str(D/'REPORT.md')))
with open(B/'RESULTS.csv','w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
