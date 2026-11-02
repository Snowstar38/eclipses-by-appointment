# TIC 17033860: CONFIRMED

Full bounded physical review: COMPLETE. Catalogue novelty is separate from this verdict.

Raw QLP SAP_FLUX contains 5 complete free-center fitted eclipses in representative sectors[14, 41, 75]. Predicted historical centers guided extraction, not timing points. Fits use local linear baselines and trapezoid shapes; quality-zero cadences only. Flagged, partial and uncovered windows are not clean nulls. [raw-events.png](../../campaign/batch02/17033860/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/17033860/raw-sector-fold.png) and [raw-windows.csv](../../campaign/batch02/17033860/raw-windows.csv) show the actual observations.

Measured recurrence P=15.3802677227 +/- 0.0000397687d. Named reference epoch BTJD1698.2949564: selected eclipse kind at phase zero, not an assumed deeper primary. The legacy primary_epoch_btjd column carries this epoch. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when positive-degree-of-freedom reduced chi square exceeds one. With only two centers, no reduced chi square or measured residual scatter exists; covariance propagates input timing allowances. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Consecutive same-kind measured pairs: 2. Same-sector parity and actual coverage are in [alias-coverage.json](../../campaign/batch02/17033860/alias-coverage.json). Other-kind free fits: 6 midpoints; measured phase range 0.27346 to 0.27389. See [secondary-timing.json](../../campaign/batch02/17033860/secondary-timing.json). The exact-half-phase baseline estimates are not interpreted as clean depths where they overlap the other eclipse. This is a bounded alias check, not a blind exhaustive search. Two separated sectors are distinct observing occasions on the same instrument.

Fresh raw TESScut pixel identity agrees with Gaia DR3 2067824378464107520 to 0.00000arcsec by saved WCS; all source bytes are hashed. In sector41, 2 separately recomputed event deficits average0.080px from the target. Event-scatter vector is[0.01026359917147296, 0.024579567158189125]; this is descriptive sampling scatter, not calibrated positional confidence or pixel-response systematics. Lead visually inspected the historical full-field and freshly recomputed core images. Every capable neighbor in the saved60arcsec Gaia list: None within60arcsec under approximate G-band flux budget. Intrinsic source loss requirements and diluted fractional pixel losses are different quantities and are never compared as a veto. The G-band flux screen is approximate and does not exclude unknown unresolved companions.

Alternative extraction: background-subtracted raw TESScut1x1/3x3/5x5 median event depths are220.62/214.36/208.21ppt; selected QLP raw median fit depth249.46ppt. Details, windows, individual centroids, count and depths are in [pixel-evidence.json](../../campaign/batch02/17033860/pixel-evidence.json). This separately extracted reduction shares the same TESS photons as QLP and is not an independent instrument or independent observing occasion. Aperture dilution, cadence and event-core averaging explain differing apparent depths; no intrinsic binary depth is inferred.

Gaia orbit and physical plausibility: source-specific NSS P=15.3825766034d, e=0.30673, omega=164.8905deg, periastron BTJD392.67385. Closest edge-on conjunction offset at the measured epoch=-0.04548d (-0.00296phase); descriptive linear full-SB1-covariance timing error=0.26778d. The covariance uses source-specific P/e/omega/Tp correlations, not only diagonal errors. Mass function=0.0419solar; assumed primary mass=0.979solar gives minimum companion mass=0.438solar. Approximate central duration=5.70h versus observed4.13h. TIC radius/main-sequence companion assumptions and edge-on conjunction are approximations, not a fitted stellar model or arbitrary sigma admission rule. Orbit/geometry are consistent at this descriptive precision and do not establish the identity of an unresolved eclipse source.

Deciding interpretation: Deep selected eclipse and a much shallower second kind at phase+0.2737 establish unequal event separation. No capable Gaia neighbor under the depth budget. Eclipse shapes remain sharp and recurring across S14/41/75.

Next check: Optional resolved photometry and precision binary characterization.

Seven scoped catalogue groups were checked centrally for this identity; see [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv) and verification receipts. A nearby catalogue source is not an exact target match, and the scoped result does not assert exhaustive publication priority.

|Sector|Photometric cycle|Measured midpoint BTJD|Input timing allowance d|Fitted depth ppt|
|---|---:|---:|---:|---:|
|14|0|1698.2907217|0.010417|232.59|
|41|47|2421.1679716|0.003472|251.52|
|41|48|2436.5482295|0.003472|250.70|
|75|107|3343.9835028|0.001157|248.40|
|75|108|3359.3639277|0.001157|249.46|

Evidence and provenance: [measurements.json](../../campaign/batch02/17033860/measurements.json), [raw-windows.csv](../../campaign/batch02/17033860/raw-windows.csv), [raw-events.png](../../campaign/batch02/17033860/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/17033860/raw-sector-fold.png), [alias-coverage.json](../../campaign/batch02/17033860/alias-coverage.json), [pixel-evidence.json](../../campaign/batch02/17033860/pixel-evidence.json), [pixel-recomputed.png](../../campaign/batch02/17033860/pixel-recomputed.png), historical/diff_s*.json/png, [historical/gaia.json](../../campaign/batch02/17033860/historical/gaia.json); batch [../gaia-geometry.json](../../campaign/batch02/gaia-geometry.json), [../alias-audit.json](../../campaign/batch02/alias-audit.json), [../secondary-audit.json](../../campaign/batch02/secondary-audit.json), [../measurement-source-receipts.json](../../campaign/batch02/measurement-source-receipts.json), [../download-receipts.json](../../campaign/batch02/download-receipts.json), [../source-hashes.json](../../campaign/batch02/source-hashes.json), [../LEAD-AUDIT.md](../../campaign/batch02/LEAD-AUDIT.md) and [../helper-audit.md](../../campaign/batch02/helper-audit.md). SHA256SUMS.json covers reports, scripts, raw FITS and original cutouts. Current availability receipt for246857844 is in shared-catalogues and copied locally with its hash. No canonical/public files were edited by this batch.


Stable review key: R554.

Deciding evidence and numeric artifacts:
- [alias-coverage.json](../../campaign/batch02/17033860/alias-coverage.json)
- [historical/diff_s41.json](../../campaign/batch02/17033860/historical/diff_s41.json)
- [historical/diff_s41.png](../../campaign/batch02/17033860/historical/diff_s41.png)
- [historical/gaia.json](../../campaign/batch02/17033860/historical/gaia.json)
- [measurements.json](../../campaign/batch02/17033860/measurements.json)
- [pixel-evidence.json](../../campaign/batch02/17033860/pixel-evidence.json)
- [pixel-recomputed.png](../../campaign/batch02/17033860/pixel-recomputed.png)
- [raw-events.png](../../campaign/batch02/17033860/raw-events.png)
- [raw-sector-fold.png](../../campaign/batch02/17033860/raw-sector-fold.png)
- [raw-windows.csv](../../campaign/batch02/17033860/raw-windows.csv)
- [secondary-timing.json](../../campaign/batch02/17033860/secondary-timing.json)

[Batch audits and scripts](../../campaign/batch02/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
