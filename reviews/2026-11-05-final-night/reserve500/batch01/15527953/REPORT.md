# RS001 — TIC 15527953

Review complete; physical tier **REFUTED**. GaiaDR3 6125690306996117504; selection period 43.59355876677294d, G=11.848131.

The rapid repeated screening signal is contamination from the known EW system TIC15527954/Gaia6125690306996118016, P0.251326d, about31arcsec away. The S101 deficit centroid is1.33pixels from the target and0.18pixels from that bright neighbor. It is not a new long-period target eclipser. The neighbor recovery is kept distinct from the target novelty.

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
|37|candidate|2318.8826367208544|0.006356350972223305|172.35810496127013|0.07141167085593528|True|
|101|candidate|4119.522004021737|0.007939518498574834|67.9003952500692|0.05179290095498156|False|

Clock: No accepted target clock.

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {"tic": "15527953", "event": {"sector": 101, "center_btjd": 4119.400357097826, "duration_d": 0.06}, "ra": 185.577838482, "dec": -51.2403945172, "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/H2_vlXlj91rPC5-C/astrocut_185.577838482_-51.2403945172_7.0x7.0px.zip", "zip_sha256": "ed756e5a3d936c096ff08622ea96dfb2d2ec16a32d4ffd1820d22f30917ce0e1", "fits_sha256": "fc65435e3f9c131252a1e32f91d3c9e739d91f668d10907b85783a236e82a2ec", "target_xy": [3.2365756968984645, 3.2267783927016485], "core_n": 12, "side_n": 65, "aperture_loss": 0.08112686200223296, "diff_peak_xy": [2, 4], "positive_diff_centroid_xy": [2.023993067342559, 3.7666052483363766], "centroid_offset_pixels": 1.327316717127149, "status": "measured"}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

No target claim; inspect target-specific residuals only if pursuing another signal.

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
