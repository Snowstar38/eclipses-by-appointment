# RS007 — TIC 160166846

Review complete; physical tier **CONFIRMED**. GaiaDR3 1951294356586328064; selection period 34.64387821568555d, G=11.754888.

Four deep flat-bottom bounded raw eclipses give34.6416475d, cycles0/31/32/53, max residual0.00334d. S55/S56 adjacent repeats and covered-null tests reject aliases. The shallow opposite-kind/baseline structures are not pooled as same-kind timing events. Independent pixels reproduce the deep eclipse at the target, deficit offset about0.10pixel. VSXRS and ASASSNROT periods44.69/44.869d describe prior non-EB variability; the abrupt ingress/egress and repeated flat bottoms establish real eclipses on the34.64d clock. Source covariance supports conjunctionB.

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
|15|candidate|1727.6886954260717|0.0018533510986721877|111.62363058491357|0.7452787608441377|True|
|15|candidate|1716.0331580721472|0.015949344040834056|25.194184156882418|0.8999999999999999|False|
|55|candidate|2801.5842152278396|0.0007079898762581606|108.5476122938786|0.7439339207544087|True|
|56|candidate|2836.224572626715|0.00029880777022624623|106.23214076246249|0.74512150340015|True|
|82|candidate|3551.920043464702|0.00820212385077548|22.442483218418975|0.8999999999999999|False|
|83|candidate|3563.698964677449|0.0009426057396170294|107.83763544828975|0.744143468492924|True|

Clock: {"period_d": 34.64164754284373, "epoch_btjd": 1727.6920261931484, "formal_period_error_d": 0.00014687615390113153, "cycles": [0, 31, 32, 53], "times": [1727.6886954260717, 2801.5842152278396, 2836.224572626715, 3563.698964677449], "residuals": [-0.003330767076704433, 0.0011152065358146501, -0.00017493743280283525, -0.00038128641699586296], "duration_d": 0.744632485946537, "depth_ppt": 108.19262387108418, "max_residual_d": 0.003330767076704433, "note": "Same-kind morphology. WLS errors are formal with cadence/2 or .003d floor, not calibrated coverage. Integer aliases tested separately; two-event fit alone does not determine unique clock."}

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {"tic": "160166846", "event": {"sector": 56, "center_btjd": 2836.2225844848194, "duration_d": 0.48}, "ra": 322.123466817, "dec": 35.1937512677, "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/Z3SgP1ggvekdPM8V/astrocut_322.123466817_35.1937512677_7.0x7.0px.zip", "zip_sha256": "044dce15ea37f1d44d11ae1f914657f1617dc8769a7dab1d22cf0d0c49ae3d26", "fits_sha256": "a42c31f87cbdfac6fc843682d0bb01a8bde3758f366685119ef057a15daafb2d", "target_xy": [3.191099447838549, 3.7037475202644297], "core_n": 103, "side_n": 518, "aperture_loss": 0.12615639294552816, "diff_peak_xy": [3, 4], "positive_diff_centroid_xy": [3.092399297683423, 3.7042265809521067], "centroid_offset_pixels": 0.09870131275614744, "status": "measured"}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

Additional higher-resolution photometry and spectroscopy can characterize the rotating eclipsing binary; prior non-EB types are retained explicitly.

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
