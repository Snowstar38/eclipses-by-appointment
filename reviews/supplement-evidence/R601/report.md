# TIC 301986385

Physical verdict: **confirmed**. Full bounded review: **complete**.

Fifteen measured narrow raw eclipses in S56/83 establish same-kind recurrence. A shallow narrow secondary-like feature is measured near phase0.50004 relative to the selected deeper eclipse; its pooled formal phase error omits red-noise and sector-normalization systematics. The primary and secondary are unequal, rejecting the half-period interpretation. No capable Gaia neighbor within60 arcsec under the G-band flux-budget proxy.

Measured period 3.41614587598 +/- 3.3342836e-06 d; named selected-eclipse epoch BTJD 2826.84537464; depth 18.36787 ppt (diluted raw QLP). Epoch is the selected recurring eclipse, not an assumed deeper primary. BTJD = BJD_TDB -2457000.

Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.

Timing samples: 15; sectors [56, 83]; fitted same-kind cycle span 0 to 221. Reduced chi square: 1.3554658684751226. Actual centers, errors and local windows are in [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/measurements.json) and [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/raw-windows.csv); predicted centers are labeled and never counted as measurements.

Aliases: within-sector adjacent same-kind pairs [[56, 0, 1], [56, 1, 2], [56, 2, 3], [56, 3, 4], [56, 4, 5], [56, 5, 6], [56, 6, 7], [83, 215, 216], [83, 216, 217], [83, 217, 218], [83, 218, 219], [83, 219, 220], [83, 220, 221]]. Sector parity depths and nearby integer counts are in [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/alias-audit.json) and [../integer-aliases.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/integer-aliases.json). Half-period extra windows are in [../coverage-alias-windows.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/coverage-alias-windows.json); flagged/empty windows are not nulls. No persistent unequal alternating primary depths support a doubled period. Gaia period is a consistency test, not a fixed photometric fit.

Secondary assessment: {'status': 'Secondary-like narrow dip visually inspected; model describes selected pooled raw sector windows.', 'phase': 0.5000448522882945, 'formal_phase_error': 0.0005668116369616375, 'depth_ppt': 3.5258108227907066, 'width_days': 0.06674786377133035, 'n_points': 2397, 'sectors': [56, 83], 'error_meaning': 'Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated.'}

Attribution and alternative reduction: fresh TESScut S56 stacks 8 well-covered target-period eclipses. Target WCS pixel [7.562522340497932, 7.307526992584487]; deficit centroid [7.524055121019407, 7.369991467711694]. Read [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/fresh-pixels/diff_fresh.png) against every capable neighbor below. No fixed centroid threshold applied. Target-centered custom background-subtracted1x1/3x3/5x5 extraction depths are 15.5351/14.6017/14.6204 ppt. This is a separate reduction of the same TESS photons, not independent observations; different sectors are different occasions on one instrument. Source FITS identities and SHA256 hashes are in [../identity-check.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/identity-check.json) and [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/source-hashes.json).

All capable neighbors within60 arcsec (G-band flux-ratio proxy; intrinsic required depth is not directly compared to diluted pixel loss): []

Gaia source 2819970969870456832: source-specific NSS period 3.4160079763 d; eccentricity 0.03899; nearest edge-on conjunction offset 0.09743 d (phase 0.02852), linear full-covariance error 0.10945 d. Source-specific covariance, mass function, assumed masses/radii and approximate central duration are in [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/gaia-geometry.json). This is not a hard phase veto or fitted inclination. Observed duration 1.567 h, approximate central duration 3.805 h; grazing geometry/dilution and radius assumptions can shorten the eclipse. No contradiction that invalidates repeated-eclipse interpretation is established.

Catalogue outcome: no identified prior EB; seven-group coverage yes. Shared coverage-matrix and catalogue receipts support scope only, not exhaustive priority. Physical verdict is separate from novelty.

Limitations: Representative sectors and simplified trapezoid/linear timing errors; shared TESS photons; approximate Gaia edge-on geometry and G-band neighbor flux budgets.

Next check: Additional clean eclipse timing and color-aware neighbor/PRF modeling would refine the bounded result.


Stable review key: R601.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/fresh-pixels/run.log)
- [historical/diff_s56.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/historical/diff_s56.json)
- [historical/diff_s56.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/historical/diff_s56.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/measurements.json)
- [phase.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/phase.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/raw-events.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/301986385/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch07/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
