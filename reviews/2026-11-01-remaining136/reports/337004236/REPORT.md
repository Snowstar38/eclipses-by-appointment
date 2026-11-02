# TIC 337004236

Physical verdict: **probable**. Full bounded review: **complete**.

Repeated narrow eclipses and measured timing are secure. The target-centered deficit overlaps capable G14.8/14.4 neighbors17.4/21.9 arcsec away. The bright G11.9 source36.9 arcsec away is more clearly displaced, but the closer capable blends remain unresolved; retain probable attribution.

Measured period 3.51357832657 +/- 2.7427902e-06 d; named selected-eclipse epoch BTJD 1741.54138631; depth 51.09119 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 21; sectors [16, 58, 85]; fitted same-kind cycle span 0 to 539. Reduced chi square: 0.4989790327441848. Actual centers, errors and local windows are in [measurements.json](../../campaign/batch07/337004236/measurements.json) and [raw-windows.csv](../../campaign/batch07/337004236/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[16, 0, 1], [16, 1, 2], [16, 5, 6], [58, 325, 326], [58, 326, 327], [58, 327, 328], [58, 328, 329], [58, 329, 330], [58, 330, 331], [58, 331, 332], [85, 532, 533], [85, 533, 534], [85, 534, 535], [85, 535, 536], [85, 536, 537], [85, 537, 538], [85, 538, 539]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](../../campaign/batch07/alias-audit.json) and [../integer-aliases.json](../../campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](../../campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.5220197879014148}

Attribution and alternative reduction: fresh TESScut S58 stacks 8 well-covered target-period eclipses. Target WCS pixel [7.424558564102117, 7.719348868919365]; deficit centroid [7.364408721432765, 7.756422540784422]. Read [fresh-pixels/diff_fresh.png](../../campaign/batch07/337004236/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 28.4878/15.4091/11.7403 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](../../campaign/batch07/identity-check.json) and [../source-hashes.json](../../campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "2218729046544998656", "sep": 17.441909343551004, "G": 14.846255, "depth_needed": 0.4828035144324318, "possible": true, "px": [7.572117209645885, 6.897320943998505], "frac_loss_at_pixel": 0.022524621117210906}, {"source_id": "2218729050841171712", "sep": 21.897788043603484, "G": 14.425405, "depth_needed": 0.34408230359151015, "possible": true, "px": [8.475361222363201, 7.53594751120278], "frac_loss_at_pixel": 0.03196543216302517}, {"source_id": "2218727504652950528", "sep": 36.85720917726252, "G": 11.880404, "depth_needed": 0.07920075278313367, "possible": true, "px": [5.627776870846239, 7.634430601134522], "frac_loss_at_pixel": 0.0024758493026971282}, {"source_id": "2218728329286660096", "sep": 40.93761754595175, "G": 15.695902, "depth_needed": 0.9952678170424939, "possible": true, "px": [8.356826233601392, 9.459576908644294], "frac_loss_at_pixel": 0.021444686500925278}]

Gaia source 2218729050841173120: source-specific NSS period 3.5138385596 d; eccentricity 0.05002; nearest edge-on conjunction offset -0.02113 d (phase -0.00601), linear full-covariance error 0.19878 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](../../campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 2.763 h, approximate central duration 4.759 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets. Capable close neighbors prevent definitive source attribution.

Next check: Higher-resolution time-series localization or a second field orientation resolving capable close sources.


Stable review key: R609.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch07/337004236/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch07/337004236/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch07/337004236/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch07/337004236/fresh-pixels/run.log)
- [historical/diff_s58.json](../../campaign/batch07/337004236/historical/diff_s58.json)
- [historical/diff_s58.png](../../campaign/batch07/337004236/historical/diff_s58.png)
- [historical/gaia.json](../../campaign/batch07/337004236/historical/gaia.json)
- [measurements.json](../../campaign/batch07/337004236/measurements.json)
- [phase.png](../../campaign/batch07/337004236/phase.png)
- [raw-events.png](../../campaign/batch07/337004236/raw-events.png)
- [raw-windows.csv](../../campaign/batch07/337004236/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch07/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
