# RS004 — TIC 97279198

Review complete; physical tier **PLAUSIBLE**. GaiaDR3 5578452851469250944; selection period 34.84126738475976d, G=11.886518.

S6/S7/S33 raw QLP show repeated bounded troughs near4d, distinctly shorter than the34.841d Gaia orbit. The target-centered independent S7 aperture does not reproduce the QLP loss; the difference structure points toward the cutout edge. Severe ramps/reset sectors34/61/88 are not timing measurements. A repeated eclipse-like bycatch exists in the aperture, but target ownership is not established.

## Representative raw measurements

|Sector|kind|midpoint BTJD|formal fit error d|depth ppt|duration d|usable fit|
|---|---|---|---|---|---|---|
|6|candidate|1473.7658848175279|0.0043669261086951095|6.755429283422482|0.617683905437974|True|
|6|candidate|1485.7974613986657|0.005034595117280761|6.832305214957051|0.6503773363340857|True|
|6|candidate|1481.7749906950544|0.004983177927690498|6.517060765206552|0.6288087890089276|True|
|6|candidate|1469.7712838811253|0.006151546988600477|6.343583451073917|0.6286205218953845|True|
|7|candidate|1493.7826146025795|0.006414755500787188|10.955567441818397|0.6646893422380946|True|
|7|candidate|1497.8108098776518|0.00810455118906628|9.572642984963549|0.6771593524067373|True|
|7|candidate|1501.7914519867968|0.007816729437116513|9.539053401647458|0.6382305253490351|True|
|7|candidate|1513.7721515978644|0.007546479423215998|8.875817863595588|0.7586805998998246|True|
|88|candidate||||||

Clock: No accepted target clock.

Times are BTJD. Primary evidence is finite positive raw SAP, quality-zero for fitting, with flagged cadences separately inspected where decisive. Formal trapezoid midpoint errors describe local fits; WLS uses cadence/2 or0.003d floors. Period errors are formal conditional on cycle count, not calibrated coverage. Failed/boundary fits, opposite conjunctions, flagged spikes and ramps are not precision timing evidence. Raw fitted depths are diluted pipeline measurements, not intrinsic stellar loss.

## Reduction, source and orbit

QLP KSPSAP and independently extracted TESScut aperture use the same TESS photons. They test reduction robustness and attribution, not independent observing occasions. Pixel receipt: {"tic": "97279198", "event": {"sector": 7, "center_btjd": 1493.763987900257, "duration_d": 0.48}, "ra": 106.361559939, "dec": -35.8630969356, "request_url": "https://stpubdata.s3.amazonaws.com/tess/public/staged_cutouts/y0fxAsIENVvYan9H/astrocut_106.361559939_-35.8630969356_7.0x7.0px.zip", "zip_sha256": "0fd18439dec10f0843dd9e333dd7321a02b00455f648883dbec92fb941760396", "fits_sha256": "f73c576d7cf13e872d0802136e507f87d3f9d4935e272d625d40a9a7babd673e", "target_xy": [3.553950362879326, 3.9010374005801323], "core_n": 11, "side_n": 58, "aperture_loss": 0.0009403877337709199, "diff_peak_xy": [4, 6], "positive_diff_centroid_xy": [3.9717882245593357, 5.364432970093289], "centroid_offset_pixels": 1.5218787965945446, "status": "measured"}.

The helper inspected actual difference images and Gaia neighbors. Offset alone is not a calibrated confidence interval; GaiaG/TESS band differences and WCS/PRF systematics remain. Every potentially capable resolved neighbor is assessed spatially rather than comparing intrinsic required eclipse with blended loss. Per-target helper neighbor receipts retain all returned sources.

Source-specific full SB1 covariance uses P,gamma,K,e,omega,Tp indices0/3/4/5, including correlations. Nonlinear100000 draws (seed50701) reject unphysical e/P and unwrap conjunction epoch about the nominal before fixed-cycle propagation. See lead-gaia-covariance.json and lead-nonlinear-gaia.json, including each event and both kinds. Edge-on conjunction geometry is an association test, not a measured inclination. Mass functions are retained in the geometry artifact; positive stellar-binary mass functions, eclipse shapes, durations and periods give no contradictory geometry for the accepted cases.

The covered-window alias scan tests integer families over approximately5–100d and period divisors2–6, requiring both sidebands,75% core cadence coverage and no large interior gap. All same-kind timings must agree; RS008 independently requires the second-kind interval. Missing/flagged windows are not clean nulls. This bounded review does not claim exhaustive all-event/all-sector extraction. Current raw availability is retained in lead-context.json; all promoted cases have actual repeated events, rather than a single-event coverage inference.

## Catalogue status

The shared ROOT-CATALOGUE-SEAL.json validates the seven canonical source groups and source-specific receipts, positive controls and bounded literature search. No prior target EB is found for this queue; RS001 has an explicitly distinct nearby known EW. Non-EB classifications RS002ROT and RS007RS/ROT are retained and do not automatically exclude. Literature scope:244 local eprints, exact27TIC/Gaia identities, no hits; this is not exhaustive discovery priority. Catalogue novelty, physical tier, source association and publication eligibility are separate. Per-target lead-central-catalogue-receipts.json retains the target's exact shared rows and seal reference.

## Limitations and next check

Resolve the off-target source with a wider field and a repeat image; do not count it as a new target eclipser.

Scripts, raw/cutout SHA256 receipts, context panels, timing, alias, geometry, helper independent measurements and final audit accompany this report. Exact8 queue, no substitutions. Lead adapted validated fresh500batch03 primitives; helper independently checked pixels, source identities, hashes and final numeric artifacts. No ledger/public files edited.
