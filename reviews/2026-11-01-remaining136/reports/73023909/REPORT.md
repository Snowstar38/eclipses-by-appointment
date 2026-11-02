# TIC 73023909

Physical verdict: **confirmed**. Full bounded review: **complete**.

Four measured eclipses include adjacent same-kind pairs in S19 and S59. Fresh MAST availability gives these two sectors only. Reusing older 30-minute data required a documented sample-count change, not a prediction counted as a timing. The capable G14.0 neighbor at 52.6 arcsec is separate from the target deficit.

Measured period 13.62032014257 +/- 9.2487252e-05 d; named selected-eclipse epoch BTJD 1824.08749418; depth 110.74048 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 4; sectors [19, 59]; fitted same-kind cycle span 0 to 81. Reduced chi square: 0.036983908911665406. Actual centers, errors and local windows are in [measurements.json](../../campaign/batch07/73023909/measurements.json) and [raw-windows.csv](../../campaign/batch07/73023909/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[19, 0, 1], [59, 80, 81]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](../../campaign/batch07/alias-audit.json) and [../integer-aliases.json](../../campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](../../campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.701995453065198}

Attribution and alternative reduction: fresh TESScut S59 stacks 2 well-covered target-period eclipses. Target WCS pixel [7.989658211071454, 7.5841265686758845]; deficit centroid [8.214022458423065, 7.692949424683915]. Read [fresh-pixels/diff_fresh.png](../../campaign/batch07/73023909/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 110.6783/100.0557/79.5734 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](../../campaign/batch07/identity-check.json) and [../source-hashes.json](../../campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "470143067441747072", "sep": 52.618456286386696, "G": 14.048594, "depth_needed": 0.5600090292954125, "possible": true, "px": [5.554710013364397, 6.833631163060054], "frac_loss_at_pixel": 0.004901240588663546}]

Gaia source 470096127737430912: source-specific NSS period 13.6162926380 d; eccentricity 0.41324; nearest edge-on conjunction offset 0.28890 d (phase 0.02122), linear full-covariance error 0.31395 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](../../campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 2.639 h, approximate central duration 5.139 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets.

Next check: Additional clean eclipse timing and color-aware neighbor/PRF modeling would refine the bounded result.


Stable review key: R608.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch07/73023909/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch07/73023909/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch07/73023909/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch07/73023909/fresh-pixels/run.log)
- [historical/diff_s59.json](../../campaign/batch07/73023909/historical/diff_s59.json)
- [historical/diff_s59.png](../../campaign/batch07/73023909/historical/diff_s59.png)
- [historical/gaia.json](../../campaign/batch07/73023909/historical/gaia.json)
- [mast-availability.json](../../campaign/batch07/73023909/mast-availability.json)
- [measurements.json](../../campaign/batch07/73023909/measurements.json)
- [phase.png](../../campaign/batch07/73023909/phase.png)
- [raw-events.png](../../campaign/batch07/73023909/raw-events.png)
- [raw-windows.csv](../../campaign/batch07/73023909/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch07/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
