# RS008 — TIC 165828134

Review complete; physical tier **CONFIRMED**. GaiaDR3 6164350162317935616; selection period 38.05470932364795d, G=11.935854.

Two deep same-kind events inS37/S102 give38.0585128d across48cycles. Independently, shallow same-kind events inS11/S37 are separated19cycles on that clock (interval residual0.00256d). Joint tests of both kinds remove the long-baseline integer ambiguity; covered nulls reject divisors. Opposite conjunction kinds are kept separate. S64 shallow coverage is truncated and its unusable fit supplies no precision timing. Deep loss is recovered by independent pixels on target, offset about0.074pixel. Both conjunction kinds agree with source Gaia covariance.

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
|11|candidate|1609.0525024072647|0.00034606485179619633|51.14143232467732|0.3096795858414445|True|
|37|candidate|2310.2662366162517|0.00013089144531165282|203.00910647353774|0.43557524572044387|True|
|102|candidate|4137.074849706838|0.00015147610930660676|177.8776347620097|0.43568245749662965|True|
|37|kindB|2332.166808097136|0.00042732053746101246|53.167757043054046|0.31124594363249447|True|
|64|kindB|3055.294619431737|69216.50981588535|52.762451607782644|0.27780456791356933|False|

Clock: {"period_d": 38.058512772720555, "epoch_btjd": 2310.2662366162517, "formal_period_error_d": 9.560009330379387e-05, "cycles": [0, 48], "times": [2310.2662366162517, 4137.074849706838], "residuals": [0.0, 0.0], "duration_d": 0.43562885160853676, "depth_ppt": 190.44337061777372, "max_residual_d": 0.0, "note": "Same-kind morphology. WLS errors are formal with cadence/2 or .003d floor, not calibrated coverage. Integer aliases tested separately; two-event fit alone does not determine unique clock."}

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {"tic": "165828134", "event": {"sector": 102, "center_btjd": 4137.066228373155, "duration_d": 0.48}, "ra": 204.480772478, "dec": -36.3745706098, "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/gvmcaAkUT7hGmYvw/astrocut_204.480772478_-36.3745706098_7.0x7.0px.zip", "zip_sha256": "15b002236d95ffe37115cc818eaff4fe400aa313831ffe6d89a4a0a4b68a314b", "fits_sha256": "442187c50dd369a429e796ba0ecfbbc9a87168dc3bb713ab722f87635cfe8096", "target_xy": [3.0161753666738758, 3.5558293349954697], "core_n": 104, "side_n": 518, "aperture_loss": 0.2087197658559088, "diff_peak_xy": [3, 4], "positive_diff_centroid_xy": [3.068654621904494, 3.607726962778606], "centroid_offset_pixels": 0.07380674765275436, "status": "measured"}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

The quoted period error is formal conditional precision from two deep events; acquire further complete same-kind eclipses for robust timing uncertainty.

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
