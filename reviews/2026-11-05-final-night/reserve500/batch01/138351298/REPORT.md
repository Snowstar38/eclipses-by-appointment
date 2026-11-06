# RS006 — TIC 138351298

Review complete; physical tier **CONFIRMED**. GaiaDR3 2048458748892535808; selection period 29.413650970683932d, G=11.569277.

Five narrow bounded raw eclipses inS14/S40/S41/S55/S75 give29.4295814d, cycles0/24/25/37/56, max residual0.00147d. Adjacent-sector same-kind recurrence and covered-null tests reject integer/divisor aliases. Independent pixel extraction recovers the narrow eclipse and a compact deficit0.15pixel from target. Capable neighbors at1.93–2.95pixels are spatially distinct. Source-specific conjunction covariance includes the measured events despite modest nominal offsets.

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
|14|candidate|1709.310671857435|0.007832213934022092|13.18166607762255|0.15610489924484822|True|
|40|candidate|2415.6182967234204|0.0023572241976408765|14.692614512383821|0.1790659868295576|True|
|41|candidate|2445.0496069354635|0.0018243409684624572|14.291147266145428|0.187925155395166|True|
|55|candidate|2798.2032707973653|0.001925927702651252|16.381665047744768|0.1946497757157829|True|
|75|candidate|3357.3659681281256|0.0028610917409778312|14.52817123439098|0.18986064791589502|True|

Clock: {"period_d": 29.42958137698182, "epoch_btjd": 1709.3092050057999, "formal_period_error_d": 0.00011291014061000483, "cycles": [0, 24, 25, 37, 56], "times": [1709.310671857435, 2415.6182967234204, 2445.0496069354635, 2798.2032707973653, 3357.3659681281256], "residuals": [0.0014668516350866412, -0.0008613299432909116, 0.0008675051180944138, -0.0004451567615433305, 0.0002060113438346889], "duration_d": 0.187925155395166, "depth_ppt": 14.52817123439098, "max_residual_d": 0.0014668516350866412, "note": "Same-kind morphology. WLS errors are formal with cadence/2 or .003d floor, not calibrated coverage. Integer aliases tested separately; two-event fit alone does not determine unique clock."}

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {"tic": "138351298", "event": {"sector": 40, "center_btjd": 2415.6178701536082, "duration_d": 0.12}, "ra": 293.724063021, "dec": 36.1153151857, "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/5xmUQYouabGBT8Ry/astrocut_293.724063021_36.1153151857_7.0x7.0px.zip", "zip_sha256": "397ddd9a3fa0013e1708075a6351bc75032035ab02ab7d8c8c488ae39c5823f0", "fits_sha256": "11b1333ba9f0af726e64d3a3cbd100f75cb0f5ca7b762b28f2c68202b0ead0d7", "target_xy": [3.94171575817487, 3.304483517997113], "core_n": 9, "side_n": 44, "aperture_loss": 0.018101569614179303, "diff_peak_xy": [4, 3], "positive_diff_centroid_xy": [4.0494846170283845, 3.394631469497937], "centroid_offset_pixels": 0.14050188645845169, "status": "measured"}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

Refine the ephemeris and physical parameters; spatial centroids remain subject to WCS/PRF systematics.

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
