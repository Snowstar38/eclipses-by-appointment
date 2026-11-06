# RS005 — TIC 100826297

Review complete; physical tier **CONFIRMED**. GaiaDR3 6471375113496624640; selection period 43.06698345851486d, G=11.9454365.

Three clear raw eclipses inS27/S67/S94 give43.0522731d at cycles0/25/42, max residual0.00073d. Bounded timing-compatible integer aliases and divisors are rejected by third-event timing or covered nulls. Independent pixel extraction recovers the eclipse with a compact deficit0.177pixel from target. A capable Gaia neighbor at2.62pixels is spatially distinct. Same Gaia conjunction agrees within source-specific nonlinear covariance.

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
|27|candidate|2057.8170798917713|0.0006132943667442135|62.353209414995554|0.40478729036065797|True|
|67|candidate|3134.1227951914598|0.000315424495314508|63.84911267191919|0.4064784908495357|True|
|94|candidate|3866.01258939138|0.0003104045165374761|52.85732859034353|0.40510209613466|True|
|94|candidate|3875.0084377623657|0.02287550744695169|2.1710644476123817|0.8988624537198758|False|

Clock: {"period_d": 43.05227312462021, "epoch_btjd": 2057.8166886493564, "formal_period_error_d": 0.00010921295909330564, "cycles": [0, 25, 42], "times": [2057.8170798917713, 3134.1227951914598, 3866.01258939138], "residuals": [0.0003912424149348226, -0.0007215734017336217, 0.00042950797478624736], "duration_d": 0.40510209613466, "depth_ppt": 62.353209414995554, "max_residual_d": 0.0007215734017336217, "note": "Same-kind morphology. WLS errors are formal with cadence/2 or .003d floor, not calibrated coverage. Integer aliases tested separately; two-event fit alone does not determine unique clock."}

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {"tic": "100826297", "event": {"sector": 67, "center_btjd": 3134.1446289334694, "duration_d": 0.48}, "ra": 312.043708275, "dec": -52.5065218113, "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/ZtvPnU5_wu6KlF96/astrocut_312.043708275_-52.5065218113_7.0x7.0px.zip", "zip_sha256": "e18b36e3da793d4bb82f714c9e6c7cf3e6b9c35d0dcf414182225afa20e0a034", "fits_sha256": "9bfb954f95405f3f67dec16cf3133c1960e49c50d42138a35575def0973e81cc", "target_xy": [3.117432860584552, 3.456868504968564], "core_n": 103, "side_n": 453, "aperture_loss": 0.0645729664115613, "diff_peak_xy": [3, 3], "positive_diff_centroid_xy": [3.293881698892554, 3.4731250843619423], "centroid_offset_pixels": 0.17719613120442726, "status": "measured"}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

Improve the physical characterization with spectroscopy and more complete events; retain uncalibrated WCS/centroid systematics.

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
