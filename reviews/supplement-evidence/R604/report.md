# TIC 376669046

Physical verdict: **confirmed**. Full bounded review: **complete**.

Four measured eclipses include the adjacent S13 pair separated by 17.5997332 d, plus S93/104. This local recurrence constrains the long-baseline integer count; it is not merely two isolated events assigned Gaia cycles. The capable G15.5 neighbor at 59.1 arcsec is far from the target deficit.

Measured period 17.59878547351 +/- 6.2049779e-05 d; named selected-eclipse epoch BTJD 1661.44388644; depth 28.43011 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 4; sectors [13, 93, 104]; fitted same-kind cycle span 0 to 144. Reduced chi square: 1.8242035023376544. Actual centers, errors and local windows are in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/measurements.json) and [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[13, 0, 1]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/alias-audit.json) and [../integer-aliases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'No secure secondary established by visual review of full raw phase and predicted-conjunction windows. Baseline variability/coverage limit a null claim; guess is Gaia-predicted separation, not a measured secondary phase.', 'guess_phase': 0.5568678434986611}

Attribution and alternative reduction: fresh TESScut S66 stacks 2 well-covered target-period eclipses. Target WCS pixel [7.993955857085137, 7.638269831945527]; deficit centroid [7.776124354757196, 7.73153610703987]. Read [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 28.2667/28.3465/27.5554 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): [{"source_id": "6421765251930266112", "sep": 59.06363332122609, "G": 15.464915, "depth_needed": 0.4549625741216256, "possible": true, "px": [5.5764040239052886, 5.993544469091036], "frac_loss_at_pixel": 0.011782671141376114}]

Gaia source 6421765629887386240: source-specific NSS period 17.5996928618 d; eccentricity 0.23839; nearest edge-on conjunction offset -0.26671 d (phase -0.01515), linear full-covariance error 1.29274 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 4.304 h, approximate central duration 5.240 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets.

Next check: Additional clean eclipse timing and color-aware neighbor/PRF modeling would refine the bounded result.


Stable review key: R604.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/fresh-pixels/run.log)
- [historical/diff_s66.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/historical/diff_s66.json)
- [historical/diff_s66.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/historical/diff_s66.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/measurements.json)
- [phase.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/phase.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/376669046/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
