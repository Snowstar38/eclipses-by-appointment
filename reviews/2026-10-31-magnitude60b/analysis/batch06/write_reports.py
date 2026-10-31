from pathlib import Path
import csv,json,numpy as np
b=Path(__file__).parent;geo=json.load(open(b/'gaia-geometry.json'));pix=json.load(open(b/'pixel-audit.json'));tg=json.load(open(b.parent/'targets-selected.json'));rows=[];aliases={}
notes={'240786248':'Seven measured eclipses include consecutive cross-sector cycles102/103 and170/171 after checking all five available QLP sectors17,57,58,84,85. Even/odd depths are confounded with sectors/apertures; they do not independently exclude an orbital double alias. Repeated morphology, actual spacing and Gaia period support the retained association.', '377129604':'Only two deep S72 events are established. Their depths50.81/60.59ppt differ in QLP and custom aperture. The18.233234d value is a measured event separation, not an established same-kind orbital period;36.466469d double alias and eclipse-kind ambiguity remain. All available QLP sectors45,46,72 were inspected; earlier weak fits excluded, not used as timings. Earlier absence is not asserted as a clean null. Historical18.266535d period is not adopted.', '601646479':'Unequal alternating eclipses establish full3.535848d orbit from13 deeper even historical half-period cycles, orbital_cycle=cycle/2. Attribution remains unresolved against the capable1.89arcsec neighbor; its deficit distance0.137px is slightly smaller than target0.165px. Image cannot resolve these sources.'}
second={'322048799':'.20','162289987':'.53','367461405':'.61','22026010':'.60','365325928':'.52'}
for r in csv.DictReader(open(b/'queue.csv')):
 t=r['tic'];m=json.load(open(b/t/'measurements.json'));g=geo[t];p=pix[t];ev=[e for e in m['events'] if e.get('timing_usable')];dpath=next((b/t/'historical').glob('diff_s*.json'));d=json.load(open(dpath));verdict='PROBABLE' if t=='601646479' else 'PLAUSIBLE' if t=='377129604' else 'CONFIRMED'
 limit=notes.get(t,'Representative same-kind raw eclipses recur within a sector. Photometric period is fitted from measured centers; the historical photometric branch guides extraction. No exhaustive blind alias scan claimed.')
 if t in second:limit+=' A distinct secondary occurs near phase'+second[t]+'; it is not mixed into selected-event timings.'
 limit+=' Depths depend on aperture dilution and local baseline. Pixel centroid uncertainties and timing systematics are not calibrated.'
 nxt='Resolve source with higher-resolution eclipse photometry' if verdict=='PROBABLE' else 'Obtain a third deep eclipse and test same-kind/double aliases' if verdict=='PLAUSIBLE' else 'Optional precision characterization'
 kind='Deeper alternating eclipse' if t=='601646479' else 'First of the two deep S72 events; primary kind unresolved' if t=='377129604' else 'Selected phase-zero eclipse; deepest primary not assumed'
 m['epoch_kind']=kind;json.dump(m,open(b/t/'measurements.json','w'),indent=2)
 pairs=[(a['sector'],a['cycle'],c['cycle']) for a,c in zip(ev,ev[1:]) if c['cycle']-a['cycle']==(2 if t=='601646479' else 1)]
 aliases[t]=dict(actual_cycles=[e['cycle'] for e in ev],consecutive_event_pairs=pairs,epoch_kind=kind,interpretation=limit)
 caps='; '.join(f"Gaia {n['source_id']}: separation {n['separation_arcsec']:.2f}arcsec, deficit distance {n['deficit_distance_px']:.3f}px, required intrinsic fraction {n['intrinsic_fractional_eclipse_required']:.3f}" for n in p['capable']) or 'No capable Gaia neighbor within the historical60arcsec list.'
 text=f'''# TIC {t}

{verdict}; full_review_completion COMPLETE. The bounded five checks are complete; physical uncertainty is retained separately. Gaia DR3 G={tg[t]['gaia']['phot_g_mean_mag']}; inventory G={r['gaia_g']}.

Raw events and timing: {len(ev)} accepted measured centers in sectors {sorted(set(e['sector'] for e in ev))}, cycles {[e['cycle'] for e in ev]}. Selected period/separation {m['period_days']:.12g} +/- {m['period_error_days']:.6g} days; epoch BTJD {m['primary_epoch_btjd']:.10f} ({kind}). Median QLP raw depth {m['depth_ppt']:.4g}ppt. Predicted centers only guide windows; timings are fitted centers. Singular or zero-covariance fits are excluded. {m['error_meaning']}

Attribution: historical sector{d['sector']} difference deficit lies {p['target_deficit_distance_px']:.3f}px from target. WCS target identity agrees with Gaia {p['identity']['gaia_source_id']}; coordinate check {p['identity']['coordinate_error_arcsec']:.3g}arcsec. {caps} Intrinsic neighbor eclipse requirements and blended pixel losses have different dilution and are not compared as a veto. Helper inspected target/neighbor image morphology; unresolved source confusion remains for601646479.

Alternative reduction: historical custom TESScut3x3 event depths {[round(e['depth_ap3']*1000,3) for e in d['events']]}ppt. These repeat the eclipse pattern in a separate extraction of the same TESS photons; they are not independent observing occasions.

Gaia geometry: full NSS correlation vector propagated at observed epoch. Gaia P={g['period_days']:.10g} +/- {g['period_error_days']:.5g}d, eccentricity {g['eccentricity']:.5g}; nearest edge-on conjunction offset {g['closest']['offset_days']:.5g}d ({g['closest']['offset_phase']:.5g}phase), descriptive linear covariance error {g['closest']['gaia_covariance_linear_error_days']:.5g}d. Mass function {g['mass_function_solar']:.5g}solar, approximate central duration {g['central_duration_hours_approx']:.4g}h versus representative measured {g['observed_duration_hours']:.4g}h. Duration uses TIC radius and main-sequence minimum-mass companion and is not a fitted physical solution. This supports plausibility without an arbitrary sigma veto;377129604 association remains uncertain with its unresolved event period.

Limitations: {limit}

Next check: {nxt}.

Evidence: measurements.json, raw-windows.csv, raw-events.png, historical/{dpath.name}; batch alias-audit.json, recurrence-coverage.json, pixel-audit.json, gaia-geometry.json, download-receipts.json and SHA256SUMS.json. Catalogue novelty is supplied separately by shared-catalogues and does not determine this physical verdict. No claim of exhaustive literature priority.
'''
 text=text.replace('Helper inspected target/neighbor image morphology; unresolved source confusion remains for601646479.', ('Helper inspected target/neighbor image morphology.' if t in ['162289987','249834973','367461405','321044210','365325928'] else 'Helper inspected target/neighbor image morphology; the close source remains unresolved.' if t=='601646479' else 'Historical image and capable-neighbor numeric audit support target attribution.'))
 text=text.replace('This supports plausibility without an arbitrary sigma veto;377129604 association remains uncertain with its unresolved event period.', ('Association remains uncertain with the unresolved event period; no arbitrary sigma veto applied.' if t=='377129604' else 'This supports physical plausibility without an arbitrary sigma veto.'))
 (b/t/'REPORT.md').write_text(text)
 rows.append(dict(tic=t,physical_verdict=verdict,full_review_completion='COMPLETE',period_days=m['period_days'],period_error_days=m['period_error_days'],primary_epoch_btjd=m['primary_epoch_btjd'],depth_ppt=m['depth_ppt'],limitations=limit,next_check=nxt,source_report=p['difference_path'],report=str(b/t/'REPORT.md')))
with open(b/'RESULTS.csv','w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
json.dump(aliases,open(b/'alias-audit.json','w'),indent=2)
