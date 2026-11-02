# TIC 338069871

Physical verdict: **confirmed**. Full bounded review: **complete**.

Nearby VSX EW ZTF J223118.37+625844.7 is not a target identity match. Helper coordinate matching identifies Gaia2205143893189353088 (G20.066), not the nearby G16.234 star Gaia2205143897488641664. The EW period0.3798394 d is not a simple half/double alias of3.962546 d; its G-band proxy requires more than total eclipse to explain the target dip. Actual target-period pixel deficit is on the target core; all six capable G-brighter sources are tabulated separately. See helper-ew-identity.json for coordinate/flux details; G-to-TESS colors remain approximate.

Measured period 3.96254638108 +/- 4.3226427e-06 d; named selected-eclipse epoch BTJD 1741.60582969; depth 11.25101 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 18; sectors [16, 58, 85]; fitted same-kind cycle span 0 to 478. Reduced chi square: 0.7116230204122657. Actual centers, errors and local windows are in [measurements.json](../../campaign/batch07/338069871/measurements.json) and [raw-windows.csv](../../campaign/batch07/338069871/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[16, 0, 1], [16, 4, 5], [58, 288, 289], [58, 289, 290], [58, 290, 291], [58, 291, 292], [58, 292, 293], [58, 293, 294], [85, 472, 473], [85, 473, 474], [85, 474, 475], [85, 475, 476], [85, 476, 477], [85, 477, 478]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](../../campaign/batch07/alias-audit.json) and [../integer-aliases.json](../../campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](../../campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.540651351513166}

Attribution and alternative reduction: fresh TESScut S58 stacks 7 well-covered target-period eclipses. Target WCS pixel [7.4025834574938845, 7.389609467582433]; deficit centroid [7.399890389818373, 7.296142161827592]. Read [fresh-pixels/diff_fresh.png](../../campaign/batch07/338069871/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 10.0732/9.7479/9.1477 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](../../campaign/batch07/identity-check.json) and [../source-hashes.json](../../campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "2205144103647068416", "sep": 31.744151016273438, "G": 17.049454, "depth_needed": 0.7372380928625721, "possible": true, "px": [8.613755801806303, 6.4089632108756796], "frac_loss_at_pixel": 0.006262394924843417}, {"source_id": "2205143897488641664", "sep": 45.07735523812263, "G": 16.233866, "depth_needed": 0.35377713128883725, "possible": true, "px": [8.419577068006419, 5.4508963391071035], "frac_loss_at_pixel": 0.004079026599741608}, {"source_id": "2205144069287321344", "sep": 50.59139836390038, "G": 16.862913, "depth_needed": 0.6226327929244058, "possible": true, "px": [8.61393551776237, 9.573178900263184], "frac_loss_at_pixel": 0.07190680289687322}, {"source_id": "2205144000569024000", "sep": 51.19503519528747, "G": 16.588661, "depth_needed": 0.4861614261939211, "possible": true, "px": [5.099306692000399, 8.45162930281466], "frac_loss_at_pixel": 0.0037810706138147895}, {"source_id": "2205143794409428992", "sep": 56.47541442802353, "G": 16.947376, "depth_needed": 0.672093096663929, "possible": true, "px": [4.595234150122819, 6.953839839800815], "frac_loss_at_pixel": 0.005797162709764999}, {"source_id": "2205143794409431296", "sep": 58.17134723671152, "G": 16.609413, "depth_needed": 0.4953258325990786, "possible": true, "px": [4.780869236939971, 6.095863681663631], "frac_loss_at_pixel": 0.005625215061238802}]

Gaia source 2205143996267667968: source-specific NSS period 3.9625723454 d; eccentricity 0.06519; nearest edge-on conjunction offset 0.07817 d (phase 0.01973), linear full-covariance error 0.16767 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](../../campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 1.998 h, approximate central duration 6.501 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets.

Next check: Additional clean eclipse timing and color-aware neighbor/PRF modeling would refine the bounded result.

Depth correction audit (2026-11-02): realized trapezoid decrement replaces its unconstrained amplitude parameter. Original input windows, fitted centers/widths, timing selections and physical verdict are retained; capable-neighbor membership is unchanged. See [../../depth-audit/README.md](../../campaign/depth-audit/README.md).


Stable review key: R605.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch07/338069871/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch07/338069871/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch07/338069871/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch07/338069871/fresh-pixels/run.log)
- [historical/diff_s58.json](../../campaign/batch07/338069871/historical/diff_s58.json)
- [historical/diff_s58.png](../../campaign/batch07/338069871/historical/diff_s58.png)
- [historical/gaia.json](../../campaign/batch07/338069871/historical/gaia.json)
- [measurements.json](../../campaign/batch07/338069871/measurements.json)
- [phase.png](../../campaign/batch07/338069871/phase.png)
- [raw-events.png](../../campaign/batch07/338069871/raw-events.png)
- [raw-windows.csv](../../campaign/batch07/338069871/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch07/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
