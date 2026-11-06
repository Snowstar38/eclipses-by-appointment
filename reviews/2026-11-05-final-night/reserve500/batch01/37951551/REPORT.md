# RS002 — TIC 37951551

Review complete; physical tier **PROBABLE**. GaiaDR3 3178691590530845184; selection period 48.366199351193885d, G=11.740679.

Three bounded raw depressions at1462.18966,2187.65746,4025.53824 have recovered shoulders and depths4.1–4.7ppt. Same-kind cycles0/15/53 give48.3651364d, max residual0.00532d. Additional quality-inclusive panels distinguish the S32 eclipse from the earlier gap-start recovery and the S98 eclipse from flagged ramps. Bounded integer/divisor tests retain only this clock family. Gaia period and same conjunction are consistent with source covariance. The prior VSXROT classification is not an EB identification; actual repeated eclipse morphology decides the physical evidence.

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
|5|candidate|1462.1896637919297|0.006877793718162124|4.700329182077771|0.7229948830226706|True|
|32|candidate|2187.6574590288847|0.007590483149526375|4.574621657867059|0.658456592356769|True|
|98|candidate|4025.538239991378|0.009269752623252931|4.076454473010382|0.6329724570959648|True|

Clock: {"period_d": 48.36513640435166, "epoch_btjd": 1462.18434911912, "formal_period_error_d": 0.00024648120302912086, "cycles": [0, 15, 53], "times": [1462.1896637919297, 2187.6574590288847, 4025.538239991378], "residuals": [0.0053146728096180595, -0.003936155510473327, 0.0016614416199445259], "duration_d": 0.658456592356769, "depth_ppt": 4.574621657867059, "max_residual_d": 0.0053146728096180595, "note": "Same-kind morphology. WLS errors are formal with cadence/2 or .003d floor, not calibrated coverage. Integer aliases tested separately; two-event fit alone does not determine unique clock."}

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {"tic": "37951551", "event": {"sector": 32, "center_btjd": 2187.7, "duration_d": 0.48}, "ra": 66.8738428898, "dec": -11.5603712147, "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/huTORKzI5N6d5WWJ/astrocut_66.8738428898_-11.5603712147_7.0x7.0px.zip", "zip_sha256": "b59615b44ff08faa5d9119c16a24aa5f05040873e9d4d510f64fa35524f258d8", "fits_sha256": "a98e2a1727c7ecd95549205afa35f1ee1e37bf940ed158b80908638ed9be1f1a", "target_xy": [3.1028177129730627, 3.418686619247935], "core_n": 34, "side_n": 141, "aperture_loss": 0.0037562429334626612, "diff_peak_xy": [3, 4], "positive_diff_centroid_xy": [2.8448377741571007, 3.806707008572674], "centroid_offset_pixels": 0.4659543661810775, "status": "measured"}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

Retain shallow-event spatial systematics; obtain another orientation or higher-resolution attribution.

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
