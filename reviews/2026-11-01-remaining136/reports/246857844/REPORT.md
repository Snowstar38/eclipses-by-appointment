# TIC 246857844: CONFIRMED

Full bounded physical review: COMPLETE. Catalogue novelty is separate from this verdict.

Raw QLP SAP_FLUX contains 2 complete free-center fitted eclipses in representative sectors[2]. Predicted historical centers guided extraction, not timing points. Fits use local linear baselines and trapezoid shapes; quality-zero cadences only. Flagged, partial and uncovered windows are not clean nulls. [raw-events.png](../../campaign/batch02/246857844/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/246857844/raw-sector-fold.png) and [raw-windows.csv](../../campaign/batch02/246857844/raw-windows.csv) show the actual observations.

Measured recurrence P=14.1724200490 +/- 0.0147317170d. Named reference epoch BTJD1365.8328131: selected eclipse kind at phase zero, not an assumed deeper primary. The legacy primary_epoch_btjd column carries this epoch. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when positive-degree-of-freedom reduced chi square exceeds one. With only two centers, no reduced chi square or measured residual scatter exists; covariance propagates input timing allowances. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Consecutive same-kind measured pairs: 1. Same-sector parity and actual coverage are in [alias-coverage.json](../../campaign/batch02/246857844/alias-coverage.json). No persistent deep alternating-depth pattern in the same-sector parity arrays. Covered half-phase windows lack an eclipse comparable to the selected kind. A perfectly identical two-eclipse2P harmonic is not mathematically excluded by single-kind morphology alone; Gaia orbital association and the lack of a second comparable sequence support the reported recurrence. This is a bounded alias check, not a blind exhaustive search. Two separated sectors are distinct observing occasions on the same instrument.

Fresh raw TESScut pixel identity agrees with Gaia DR3 2347638783375829632 to 0.00000arcsec by saved WCS; all source bytes are hashed. In sector2, 2 separately recomputed event deficits average0.126px from the target. Event-scatter vector is[0.016565559748460818, 0.050466038760845267]; this is descriptive sampling scatter, not calibrated positional confidence or pixel-response systematics. Lead visually inspected the historical full-field and freshly recomputed core images. Every capable neighbor in the saved60arcsec Gaia list: None within60arcsec under approximate G-band flux budget. Intrinsic source loss requirements and diluted fractional pixel losses are different quantities and are never compared as a veto. The G-band flux screen is approximate and does not exclude unknown unresolved companions.

Alternative extraction: background-subtracted raw TESScut1x1/3x3/5x5 median event depths are93.40/94.04/93.69ppt; selected QLP raw median fit depth88.11ppt. Details, windows, individual centroids, count and depths are in [pixel-evidence.json](../../campaign/batch02/246857844/pixel-evidence.json). This separately extracted reduction shares the same TESS photons as QLP and is not an independent instrument or independent observing occasion. Aperture dilution, cadence and event-core averaging explain differing apparent depths; no intrinsic binary depth is inferred.

Gaia orbit and physical plausibility: source-specific NSS P=14.1629385943d, e=0.27949, omega=235.6661deg, periastron BTJD393.16694. Closest edge-on conjunction offset at the measured epoch=0.30047d (0.02122phase); descriptive linear full-SB1-covariance timing error=0.85000d. The covariance uses source-specific P/e/omega/Tp correlations, not only diagonal errors. Mass function=0.02807solar; assumed primary mass=1.000solar gives minimum companion mass=0.376solar. Approximate central duration=8.38h versus observed6.30h. TIC radius/main-sequence companion assumptions and edge-on conjunction are approximations, not a fitted stellar model or arbitrary sigma admission rule. Orbit/geometry are consistent at this descriptive precision and do not establish the identity of an unresolved eclipse source.

Deciding interpretation: Only two complete timed eclipses, both in S2 and adjacent with spacing14.17242d, rather than two long-separated events with unresolved integer count. Current MAST query returns QLP sectors2,29,69, all inspected. S29 starts during a partial real eclipse; it is not used as a midpoint. S69 selected-eclipse windows lack clean coverage. Two-center period error propagates timing allowances with zero fit degrees of freedom; it does not measure timing scatter. Half-cycle covered baselines show no comparable eclipse. This short-baseline photometric period remains imprecise; no all-sector long-baseline precision is claimed.

Next check: A complete new eclipse for a longer-baseline ephemeris.

Seven scoped catalogue groups were checked centrally for this identity; see [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv) and verification receipts. A nearby catalogue source is not an exact target match, and the scoped result does not assert exhaustive publication priority.

|Sector|Photometric cycle|Measured midpoint BTJD|Input timing allowance d|Fitted depth ppt|
|---|---:|---:|---:|---:|
|2|0|1365.8328131|0.010417|89.16|
|2|1|1380.0052332|0.010417|87.07|

Evidence and provenance: [measurements.json](../../campaign/batch02/246857844/measurements.json), [raw-windows.csv](../../campaign/batch02/246857844/raw-windows.csv), [raw-events.png](../../campaign/batch02/246857844/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/246857844/raw-sector-fold.png), [alias-coverage.json](../../campaign/batch02/246857844/alias-coverage.json), [pixel-evidence.json](../../campaign/batch02/246857844/pixel-evidence.json), [pixel-recomputed.png](../../campaign/batch02/246857844/pixel-recomputed.png), historical/diff_s*.json/png, [historical/gaia.json](../../campaign/batch02/246857844/historical/gaia.json); batch [../gaia-geometry.json](../../campaign/batch02/gaia-geometry.json), [../alias-audit.json](../../campaign/batch02/alias-audit.json), [../secondary-audit.json](../../campaign/batch02/secondary-audit.json), [../measurement-source-receipts.json](../../campaign/batch02/measurement-source-receipts.json), [../download-receipts.json](../../campaign/batch02/download-receipts.json), [../source-hashes.json](../../campaign/batch02/source-hashes.json), [../LEAD-AUDIT.md](../../campaign/batch02/LEAD-AUDIT.md) and [../helper-audit.md](../../campaign/batch02/helper-audit.md). SHA256SUMS.json covers reports, scripts, raw FITS and original cutouts. Current availability receipt for246857844 is in shared-catalogues and copied locally with its hash. No canonical/public files were edited by this batch.


Stable review key: R552.

Deciding evidence and numeric artifacts:
- [alias-coverage.json](../../campaign/batch02/246857844/alias-coverage.json)
- [current-mast-availability.json](../../campaign/batch02/246857844/current-mast-availability.json)
- [historical/diff_s02.json](../../campaign/batch02/246857844/historical/diff_s02.json)
- [historical/diff_s02.png](../../campaign/batch02/246857844/historical/diff_s02.png)
- [historical/gaia.json](../../campaign/batch02/246857844/historical/gaia.json)
- [measurements.json](../../campaign/batch02/246857844/measurements.json)
- [pixel-evidence.json](../../campaign/batch02/246857844/pixel-evidence.json)
- [pixel-recomputed.png](../../campaign/batch02/246857844/pixel-recomputed.png)
- [raw-events.png](../../campaign/batch02/246857844/raw-events.png)
- [raw-sector-fold.png](../../campaign/batch02/246857844/raw-sector-fold.png)
- [raw-windows.csv](../../campaign/batch02/246857844/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch02/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
