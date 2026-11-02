# TIC 278966364: CONFIRMED

Full bounded physical review: COMPLETE. Catalogue novelty is separate from this verdict.

Raw QLP SAP_FLUX contains 4 complete free-center fitted eclipses in representative sectors[42, 70, 92]. Predicted historical centers guided extraction, not timing points. Fits use local linear baselines and trapezoid shapes; quality-zero cadences only. Flagged, partial and uncovered windows are not clean nulls. [raw-events.png](../../campaign/batch02/278966364/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/278966364/raw-sector-fold.png) and [raw-windows.csv](../../campaign/batch02/278966364/raw-windows.csv) show the actual observations.

Measured recurrence P=12.5151308867 +/- 0.0000268573d. Named reference epoch BTJD2467.4999809: selected eclipse kind at phase zero, not an assumed deeper primary. The legacy primary_epoch_btjd column carries this epoch. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when positive-degree-of-freedom reduced chi square exceeds one. With only two centers, no reduced chi square or measured residual scatter exists; covariance propagates input timing allowances. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Consecutive same-kind measured pairs: 1. Same-sector parity and actual coverage are in [alias-coverage.json](../../campaign/batch02/278966364/alias-coverage.json). No persistent deep alternating-depth pattern in the same-sector parity arrays. Covered half-phase windows lack an eclipse comparable to the selected kind. A perfectly identical two-eclipse2P harmonic is not mathematically excluded by single-kind morphology alone; Gaia orbital association and the lack of a second comparable sequence support the reported recurrence. This is a bounded alias check, not a blind exhaustive search. Two separated sectors are distinct observing occasions on the same instrument.

Fresh raw TESScut pixel identity agrees with Gaia DR3 2638040248315742080 to 0.00000arcsec by saved WCS; all source bytes are hashed. In sector92, 2 separately recomputed event deficits average0.099px from the target. Event-scatter vector is[0.14133162900382695, 0.06136783897343869]; this is descriptive sampling scatter, not calibrated positional confidence or pixel-response systematics. Lead visually inspected the historical full-field and freshly recomputed core images. Every capable neighbor in the saved60arcsec Gaia list: None within60arcsec under approximate G-band flux budget. Intrinsic source loss requirements and diluted fractional pixel losses are different quantities and are never compared as a veto. The G-band flux screen is approximate and does not exclude unknown unresolved companions.

Alternative extraction: background-subtracted raw TESScut1x1/3x3/5x5 median event depths are10.93/11.09/10.45ppt; selected QLP raw median fit depth11.16ppt. Details, windows, individual centroids, count and depths are in [pixel-evidence.json](../../campaign/batch02/278966364/pixel-evidence.json). This separately extracted reduction shares the same TESS photons as QLP and is not an independent instrument or independent observing occasion. Aperture dilution, cadence and event-core averaging explain differing apparent depths; no intrinsic binary depth is inferred.

Gaia orbit and physical plausibility: source-specific NSS P=12.5169206043d, e=0.09850, omega=89.9261deg, periastron BTJD389.89151. Closest edge-on conjunction offset at the measured epoch=-0.20245d (-0.01617phase); descriptive linear full-SB1-covariance timing error=0.80213d. The covariance uses source-specific P/e/omega/Tp correlations, not only diagonal errors. Mass function=0.077427solar; assumed primary mass=1.020solar gives minimum companion mass=0.584solar. Approximate central duration=5.68h versus observed1.61h. TIC radius/main-sequence companion assumptions and edge-on conjunction are approximations, not a fitted stellar model or arbitrary sigma admission rule. Orbit/geometry are consistent at this descriptive precision and do not establish the identity of an unresolved eclipse source.

Deciding interpretation: Small sharp eclipses repeat in S42/70/92, including adjacent S92 events. Large positive spikes and gaps are visible in the raw sectors; the selected eclipse cores are distinct from those artifacts. The weaker sparse S92 event increases model and timing uncertainty; timing covariance is scatter-inflated.

Next check: Optional resolved photometry and precision binary characterization.

Seven scoped catalogue groups were checked centrally for this identity; see [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv) and verification receipts. A nearby catalogue source is not an exact target match, and the scoped result does not assert exhaustive publication priority.

|Sector|Photometric cycle|Measured midpoint BTJD|Input timing allowance d|Fitted depth ppt|
|---|---:|---:|---:|---:|
|42|1|2467.5018153|0.003472|8.69|
|70|62|3230.9224845|0.001157|11.21|
|92|108|3806.6200069|0.001545|11.10|
|92|109|3819.1335000|0.001670|14.13|

Evidence and provenance: [measurements.json](../../campaign/batch02/278966364/measurements.json), [raw-windows.csv](../../campaign/batch02/278966364/raw-windows.csv), [raw-events.png](../../campaign/batch02/278966364/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/278966364/raw-sector-fold.png), [alias-coverage.json](../../campaign/batch02/278966364/alias-coverage.json), [pixel-evidence.json](../../campaign/batch02/278966364/pixel-evidence.json), [pixel-recomputed.png](../../campaign/batch02/278966364/pixel-recomputed.png), historical/diff_s*.json/png, [historical/gaia.json](../../campaign/batch02/278966364/historical/gaia.json); batch [../gaia-geometry.json](../../campaign/batch02/gaia-geometry.json), [../alias-audit.json](../../campaign/batch02/alias-audit.json), [../secondary-audit.json](../../campaign/batch02/secondary-audit.json), [../measurement-source-receipts.json](../../campaign/batch02/measurement-source-receipts.json), [../download-receipts.json](../../campaign/batch02/download-receipts.json), [../source-hashes.json](../../campaign/batch02/source-hashes.json), [../LEAD-AUDIT.md](../../campaign/batch02/LEAD-AUDIT.md) and [../helper-audit.md](../../campaign/batch02/helper-audit.md). SHA256SUMS.json covers reports, scripts, raw FITS and original cutouts. Current availability receipt for246857844 is in shared-catalogues and copied locally with its hash. No canonical/public files were edited by this batch.


Stable review key: R555.

Deciding evidence and numeric artifacts:
- [alias-coverage.json](../../campaign/batch02/278966364/alias-coverage.json)
- [historical/diff_s92.json](../../campaign/batch02/278966364/historical/diff_s92.json)
- [historical/diff_s92.png](../../campaign/batch02/278966364/historical/diff_s92.png)
- [historical/gaia.json](../../campaign/batch02/278966364/historical/gaia.json)
- [measurements.json](../../campaign/batch02/278966364/measurements.json)
- [pixel-evidence.json](../../campaign/batch02/278966364/pixel-evidence.json)
- [pixel-recomputed.png](../../campaign/batch02/278966364/pixel-recomputed.png)
- [raw-events.png](../../campaign/batch02/278966364/raw-events.png)
- [raw-sector-fold.png](../../campaign/batch02/278966364/raw-sector-fold.png)
- [raw-windows.csv](../../campaign/batch02/278966364/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch02/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
