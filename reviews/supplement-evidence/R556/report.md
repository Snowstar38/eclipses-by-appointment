# TIC 338072783: CONFIRMED

Full bounded physical review: COMPLETE. Catalogue novelty is separate from this verdict.

Raw QLP SAP_FLUX contains 20 complete free-center fitted eclipses in representative sectors[58, 85]. Predicted historical centers guided extraction, not timing points. Fits use local linear baselines and trapezoid shapes; quality-zero cadences only. Flagged, partial and uncovered windows are not clean nulls. [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-events.png), [raw-sector-fold.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-sector-fold.png) and [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-windows.csv) show the actual observations.

Measured recurrence P=2.5117384941 +/- 0.0000017968d. Named reference epoch BTJD2882.5350707: selected eclipse kind at phase zero, not an assumed deeper primary. The legacy primary_epoch_btjd column carries this epoch. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when positive-degree-of-freedom reduced chi square exceeds one. With only two centers, no reduced chi square or measured residual scatter exists; covariance propagates input timing allowances. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Consecutive same-kind measured pairs: 17. Same-sector parity and actual coverage are in [alias-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/alias-coverage.json). No persistent deep alternating-depth pattern in the same-sector parity arrays. Covered half-phase windows lack an eclipse comparable to the selected kind. A perfectly identical two-eclipse2P harmonic is not mathematically excluded by single-kind morphology alone; Gaia orbital association and the lack of a second comparable sequence support the reported recurrence. This is a bounded alias check, not a blind exhaustive search. Two separated sectors are distinct observing occasions on the same instrument.

Fresh raw TESScut pixel identity agrees with Gaia DR3 2205518861011274240 to 0.00000arcsec by saved WCS; all source bytes are hashed. In sector58, 11 separately recomputed event deficits average0.012px from the target. Event-scatter vector is[0.03857414338079675, 0.0435990507643629]; this is descriptive sampling scatter, not calibrated positional confidence or pixel-response systematics. Lead visually inspected the historical full-field and freshly recomputed core images. Every capable neighbor in the saved60arcsec Gaia list: Gaia 2205518796593429248: separation22.99arcsec, G15.654, intrinsic required fraction0.769, deficit distance1.133px; Gaia 2205524946986588288: separation52.70arcsec, G14.917, intrinsic required fraction0.408, deficit distance2.618px Intrinsic source loss requirements and diluted fractional pixel losses are different quantities and are never compared as a veto. The G-band flux screen is approximate and does not exclude unknown unresolved companions.

Alternative extraction: background-subtracted raw TESScut1x1/3x3/5x5 median event depths are34.84/34.89/33.24ppt; selected QLP raw median fit depth36.89ppt. Details, windows, individual centroids, count and depths are in [pixel-evidence.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/pixel-evidence.json). This separately extracted reduction shares the same TESS photons as QLP and is not an independent instrument or independent observing occasion. Aperture dilution, cadence and event-core averaging explain differing apparent depths; no intrinsic binary depth is inferred.

Gaia orbit and physical plausibility: source-specific NSS P=2.5118018526d, e=0.13911, omega=37.9371deg, periastron BTJD388.00992. Closest edge-on conjunction offset at the measured epoch=0.02489d (0.00991phase); descriptive linear full-SB1-covariance timing error=0.16199d. The covariance uses source-specific P/e/omega/Tp correlations, not only diagonal errors. Mass function=0.021811solar; assumed primary mass=1.120solar gives minimum companion mass=0.363solar. Approximate central duration=3.57h versus observed2.08h. TIC radius/main-sequence companion assumptions and edge-on conjunction are approximations, not a fitted stellar model or arbitrary sigma admission rule. Orbit/geometry are consistent at this descriptive precision and do not establish the identity of an unresolved eclipse source.

Deciding interpretation: Twenty complete timing-usable eclipses and17 within-sector consecutive pairs establish recurrence. Two capable neighbors at23.0 and52.7arcsec are separated from the deficit core. Strong out-of-eclipse variability remains visible; local raw eclipse fits do not use detrended QLP flux.

Next check: Optional resolved photometry and precision binary characterization.

Seven scoped catalogue groups were checked centrally for this identity; see [../../shared-catalogues/coverage-matrix.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/shared-catalogues/coverage-matrix.csv) and verification receipts. A nearby catalogue source is not an exact target match, and the scoped result does not assert exhaustive publication priority.

|Sector|Photometric cycle|Measured midpoint BTJD|Input timing allowance d|Fitted depth ppt|
|---|---:|---:|---:|---:|
|58|454|2882.5356893|0.001157|35.72|
|58|455|2885.0471278|0.001157|35.85|
|58|456|2887.5584785|0.001157|38.68|
|58|457|2890.0703938|0.001157|39.03|
|58|458|2892.5816290|0.001157|35.16|
|58|459|2895.0932130|0.001157|36.16|
|58|460|2897.6056992|0.001157|37.99|
|58|461|2900.1177892|0.001157|37.60|
|58|462|2902.6287876|0.001157|36.38|
|58|463|2905.1405869|0.001157|39.31|
|58|464|2907.6519600|0.001157|39.36|
|85|744|3610.9395215|0.001157|34.92|
|85|745|3613.4520127|0.001157|37.47|
|85|746|3615.9624097|0.001157|36.16|
|85|747|3618.4742793|0.001157|37.29|
|85|748|3620.9858691|0.001157|37.49|
|85|750|3626.0102019|0.001157|34.23|
|85|751|3628.5204741|0.001157|36.48|
|85|752|3631.0329991|0.001157|37.44|
|85|753|3633.5449196|0.001157|34.27|

Evidence and provenance: [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/measurements.json), [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-windows.csv), [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-events.png), [raw-sector-fold.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-sector-fold.png), [alias-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/alias-coverage.json), [pixel-evidence.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/pixel-evidence.json), [pixel-recomputed.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/pixel-recomputed.png), historical/diff_s*.json/png, [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/historical/gaia.json); batch [../gaia-geometry.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/gaia-geometry.json), [../alias-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/alias-audit.json), [../secondary-audit.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/secondary-audit.json), [../measurement-source-receipts.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/measurement-source-receipts.json), [../download-receipts.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/download-receipts.json), [../source-hashes.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/source-hashes.json), [../LEAD-AUDIT.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/LEAD-AUDIT.md) and [../helper-audit.md](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/helper-audit.md). SHA256SUMS.json covers reports, scripts, raw FITS and original cutouts. Current availability receipt for246857844 is in shared-catalogues and copied locally with its hash. No canonical/public files were edited by this batch.


Stable review key: R556.

Deciding evidence and numeric artifacts:
- [alias-coverage.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/alias-coverage.json)
- [historical/diff_s58.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/historical/diff_s58.json)
- [historical/diff_s58.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/historical/diff_s58.png)
- [historical/gaia.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/historical/gaia.json)
- [measurements.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/measurements.json)
- [pixel-evidence.json](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/pixel-evidence.json)
- [pixel-recomputed.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/pixel-recomputed.png)
- [raw-events.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-events.png)
- [raw-sector-fold.png](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-sector-fold.png)
- [raw-windows.csv](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/338072783/raw-windows.csv)

[Batch audits and scripts](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/batch02/INDEX.md). [Depth correction provenance](https://github.com/Snowstar38/eclipses-by-appointment/blob/main/reviews/2026-11-01-remaining136/campaign/depth-audit/README.md).
