import csv,json,hashlib
from pathlib import Path
b=Path(__file__).resolve().parent;q=list(csv.DictReader((b/'queue.csv').open()));cl=json.loads((b/'lead-clocks.json').read_text());cats={x['tic']:x for x in json.loads((b.parent/'shared-catalogues/target-results.json').read_text())};local={x['tic']:x for x in json.loads((b.parent/'shared-catalogues/local-table-matches-60arcsec.json').read_text())}
dec={
'15527953':['REFUTED','off-target-known-EW','not-associated','The rapid repeated screening signal is contamination from the known EW system TIC15527954/Gaia6125690306996118016, P0.251326d, about31arcsec away. The S101 deficit centroid is1.33pixels from the target and0.18pixels from that bright neighbor. It is not a new long-period target eclipser. The neighbor recovery is kept distinct from the target novelty.','No target claim; inspect target-specific residuals only if pursuing another signal.'],
'37951551':['PROBABLE','target-supported-with-spatial-limit','consistent','Three bounded raw depressions at1462.18966,2187.65746,4025.53824 have recovered shoulders and depths4.1–4.7ppt. Same-kind cycles0/15/53 give48.3651364d, max residual0.00532d. Additional quality-inclusive panels distinguish the S32 eclipse from the earlier gap-start recovery and the S98 eclipse from flagged ramps. Bounded integer/divisor tests retain only this clock family. Gaia period and same conjunction are consistent with source covariance. The prior VSXROT classification is not an EB identification; actual repeated eclipse morphology decides the physical evidence.','Retain shallow-event spatial systematics; obtain another orientation or higher-resolution attribution.'],
'93104494':['REFUTED','no-credible-event','not-established','The apparent discrete troughs are isolated strongly quality-flagged negative cadences and gap/reset structure. Quality-inclusive raw panels show no resolved bounded eclipse around these screening features; quality-zero raw SAP has smooth low-amplitude variability. This refutes the selected eclipse pattern, not every possible eclipse elsewhere.','No claim from these features; obtain a genuinely resolved event before further eclipse characterization.'],
'97279198':['PLAUSIBLE','off-target-or-unresolved','short-clock-not-Gaia','S6/S7/S33 raw QLP show repeated bounded troughs near4d, distinctly shorter than the34.841d Gaia orbit. The target-centered independent S7 aperture does not reproduce the QLP loss; the difference structure points toward the cutout edge. Severe ramps/reset sectors34/61/88 are not timing measurements. A repeated eclipse-like bycatch exists in the aperture, but target ownership is not established.','Resolve the off-target source with a wider field and a repeat image; do not count it as a new target eclipser.'],
'100826297':['CONFIRMED','target-supported','consistent','Three clear raw eclipses inS27/S67/S94 give43.0522731d at cycles0/25/42, max residual0.00073d. Bounded timing-compatible integer aliases and divisors are rejected by third-event timing or covered nulls. Independent pixel extraction recovers the eclipse with a compact deficit0.177pixel from target. A capable Gaia neighbor at2.62pixels is spatially distinct. Same Gaia conjunction agrees within source-specific nonlinear covariance.','Improve the physical characterization with spectroscopy and more complete events; retain uncalibrated WCS/centroid systematics.'],
'138351298':['CONFIRMED','target-supported','consistent','Five narrow bounded raw eclipses inS14/S40/S41/S55/S75 give29.4295814d, cycles0/24/25/37/56, max residual0.00147d. Adjacent-sector same-kind recurrence and covered-null tests reject integer/divisor aliases. Independent pixel extraction recovers the narrow eclipse and a compact deficit0.15pixel from target. Capable neighbors at1.93–2.95pixels are spatially distinct. Source-specific conjunction covariance includes the measured events despite modest nominal offsets.','Refine the ephemeris and physical parameters; spatial centroids remain subject to WCS/PRF systematics.'],
'160166846':['CONFIRMED','target-supported','consistent','Four deep flat-bottom bounded raw eclipses give34.6416475d, cycles0/31/32/53, max residual0.00334d. S55/S56 adjacent repeats and covered-null tests reject aliases. The shallow opposite-kind/baseline structures are not pooled as same-kind timing events. Independent pixels reproduce the deep eclipse at the target, deficit offset about0.10pixel. VSXRS and ASASSNROT periods44.69/44.869d describe prior non-EB variability; the abrupt ingress/egress and repeated flat bottoms establish real eclipses on the34.64d clock. Source covariance supports conjunctionB.','Additional higher-resolution photometry and spectroscopy can characterize the rotating eclipsing binary; prior non-EB types are retained explicitly.'],
'165828134':['CONFIRMED','target-supported','consistent','Two deep same-kind events inS37/S102 give38.0585128d across48cycles. Independently, shallow same-kind events inS11/S37 are separated19cycles on that clock (interval residual0.00256d). Joint tests of both kinds remove the long-baseline integer ambiguity; covered nulls reject divisors. Opposite conjunction kinds are kept separate. S64 shallow coverage is truncated and its unusable fit supplies no precision timing. Deep loss is recovered by independent pixels on target, offset about0.074pixel. Both conjunction kinds agree with source Gaia covariance.','The quoted period error is formal conditional precision from two deep events; acquire further complete same-kind eclipses for robust timing uncertainty.']}
rows=[]
for r in q:
 t=r['tic'];tier,source,gaia,reason,nxt=dec[t];d=b/t;tim=json.loads((d/'lead-timing.json').read_text());pixp=d/'helper-independent-localization.json';pix=json.loads(pixp.read_text()) if pixp.exists() else None;clock=cl.get(t)
 cat={'scope':'Canonical methods2.7 seven source groups; success scoped nonmatches, not exhaustive priority.','central_target':cats[t],'local_tables':local[t],'seal':'../shared-catalogues/ROOT-CATALOGUE-SEAL.json','literature_adjudication':json.loads((b.parent/'shared-catalogues/literature-adjudication.json').read_text())};(d/'lead-central-catalogue-receipts.json').write_text(json.dumps(cat,indent=2))
 ev='\n'.join('|'+ '|'.join(str(e.get(k,'')) for k in ['sector','kind','center_btjd','center_formal_error_d','depth_ppt','duration_d','fit_usable'])+'|' for e in tim)
 report=f'''# {r['sample_id']} — TIC {t}

Review complete; physical tier **{tier}**. GaiaDR3 {r['gaia_dr3']}; selection period {r['gaia_period']}d, G={r['gaia_G']}.

{reason}

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
{ev}

Clock: {json.dumps(clock) if clock else 'No accepted target clock.'}

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {json.dumps(pix) if pix else 'No deciding pixel extraction required for refuted raw artifacts; unavailable spatial evidence is not a nonmatch.'}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

{nxt}

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
'''
 (d/'REPORT.md').write_text(report,encoding='utf8');rows.append(dict(sample_id=r['sample_id'],tic=t,gaia_dr3=r['gaia_dr3'],completion='complete',tier=tier,period_d=clock['period_d'] if clock else '',period_error_d=clock['formal_period_error_d'] if clock else '',source_association=source,gaia_association=gaia,catalogue_status='scoped-no-target-prior-EB',publication_eligible=str(tier in ['CONFIRMED','PROBABLE'] and t!='97279198').lower(),report=f'{t}/REPORT.md',limitation=nxt))
with (b/'RESULTS.csv').open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
