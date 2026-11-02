# TIC 21411263

Physical verdict: **confirmed**. Full bounded review: **complete**.

Only two clean same-kind S47 events establish local recurrence. The period uncertainty is the quadrature conservative timing allowance for one cycle, not long-baseline precision; reduced chi square is null (zero degrees of freedom). Fresh MAST availability gives S21/47 only. The two S21 selected windows have one and zero usable core samples with flagged samples; these are not clean nulls and provide no measured timing. S21 all-flag raw plot retained. The capable G15.2 neighbor 27 arcsec away is spatially separate from the target deficit.

Measured period 12.71556726973 +/- 0.0049105801 d; named selected-eclipse epoch BTJD 2585.08632455; depth 73.36144 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 2; sectors [47]; fitted same-kind cycle span 56 to 57. Reduced chi square: None. Actual centers, errors and local windows are in [measurements.json](../../campaign/batch07/21411263/measurements.json) and [raw-windows.csv](../../campaign/batch07/21411263/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[47, 56, 57]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](../../campaign/batch07/alias-audit.json) and [../integer-aliases.json](../../campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](../../campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.7105528086497332}

Attribution and alternative reduction: fresh TESScut S47 stacks 2 well-covered target-period eclipses. Target WCS pixel [7.220473663331138, 7.963336197381196]; deficit centroid [7.314118908275556, 7.9494884024351595]. Read [fresh-pixels/diff_fresh.png](../../campaign/batch07/21411263/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 64.4137/60.1907/53.5166 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](../../campaign/batch07/identity-check.json) and [../source-hashes.json](../../campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "719639160769665792", "sep": 26.957612633467544, "G": 15.173637, "depth_needed": 0.914314664798946, "possible": true, "px": [8.596629988460721, 8.047491428095453], "frac_loss_at_pixel": 0.02242648658657973}]

Gaia source 719639160769665408: source-specific NSS period 12.7169625678 d; eccentricity 0.36656; nearest edge-on conjunction offset -0.12376 d (phase -0.00973), linear full-covariance error 0.31315 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](../../campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 2.576 h, approximate central duration 4.555 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets. Only two clean timings; flagged S21 windows; local recurrence precision only.

Next check: Additional clean eclipse timing and color-aware neighbor/PRF modeling would refine the bounded result.


Stable review key: R606.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch07/21411263/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch07/21411263/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch07/21411263/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch07/21411263/fresh-pixels/run.log)
- [historical/diff_s47.json](../../campaign/batch07/21411263/historical/diff_s47.json)
- [historical/diff_s47.png](../../campaign/batch07/21411263/historical/diff_s47.png)
- [historical/gaia.json](../../campaign/batch07/21411263/historical/gaia.json)
- [mast-availability.json](../../campaign/batch07/21411263/mast-availability.json)
- [measurements.json](../../campaign/batch07/21411263/measurements.json)
- [phase.png](../../campaign/batch07/21411263/phase.png)
- [raw-events.png](../../campaign/batch07/21411263/raw-events.png)
- [raw-windows.csv](../../campaign/batch07/21411263/raw-windows.csv)
- [s21-coverage.png](../../campaign/batch07/21411263/s21-coverage.png)

[Batch audits and scripts](../../campaign/batch07/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
