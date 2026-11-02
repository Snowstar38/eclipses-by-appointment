# TIC 287756198

Physical verdict: **confirmed**. Full bounded review: **complete**.

Five measured raw events across S11/64/102 give local recurrence in two sectors and a long baseline. Sector depth/continuum differences reflect extraction dilution and variability. Three capable sources45.1-58.5 arcsec away are displaced from the compact target deficit. No secure secondary inferred from continuum changes.

Measured period 15.65984307195 +/- 4.521229e-05 d; named selected-eclipse epoch BTJD 1608.08000769; depth 7.65521 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 5; sectors [11, 64, 102]; fitted same-kind cycle span 0 to 162. Reduced chi square: 1.1437703620814224. Actual centers, errors and local windows are in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/measurements.json) and [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[64, 92, 93], [102, 161, 162]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/alias-audit.json) and [../integer-aliases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.4935567357557127}

Attribution and alternative reduction: fresh TESScut S37 stacks 2 well-covered target-period eclipses. Target WCS pixel [7.348427290117524, 7.069412095525774]; deficit centroid [7.510954246146845, 7.131011385411307]. Read [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 8.9417/8.9589/8.7776 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "6086968256243116288", "sep": 45.10332824606211, "G": 17.159227, "depth_needed": 0.5616780342395038, "possible": true, "px": [9.586378118081019, 6.837241536483282], "frac_loss_at_pixel": 0.004954973487623503}, {"source_id": "6086968256243114624", "sep": 48.12232035178331, "G": 17.555882, "depth_needed": 0.8059984604155195, "possible": true, "px": [8.743292166399184, 9.046623195139022], "frac_loss_at_pixel": 0.015762178206169458}, {"source_id": "6086968015724946816", "sep": 58.48282576005001, "G": 16.633436, "depth_needed": 0.34901412912874746, "possible": true, "px": [6.781240761818138, 9.867458243771992], "frac_loss_at_pixel": -0.002232594969092304}]

Gaia source 6086968080141964672: source-specific NSS period 15.6680577389 d; eccentricity 0.08810; nearest edge-on conjunction offset -0.34982 d (phase -0.02233), linear full-covariance error 0.67634 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 4.767 h, approximate central duration 10.947 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets.

Next check: Additional clean eclipse timing and color-aware neighbor/PRF modeling would refine the bounded result.


Stable review key: R600.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/fresh-pixels/run.log)
- [historical/diff_s37.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/historical/diff_s37.json)
- [historical/diff_s37.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/historical/diff_s37.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/measurements.json)
- [phase.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/phase.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/287756198/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
