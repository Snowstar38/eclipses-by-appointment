# TIC 206614346: CONFIRMED

Full bounded physical review: COMPLETE. Catalogue novelty is separate from this verdict.

Raw QLP SAP_FLUX contains 6 complete free-center fitted eclipses in representative sectors[2, 68, 96]. Predicted historical centers guided extraction, not timing points. Fits use local linear baselines and trapezoid shapes; quality-zero cadences only. Flagged, partial and uncovered windows are not clean nulls. [raw-events.png](../../campaign/batch02/206614346/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/206614346/raw-sector-fold.png) and [raw-windows.csv](../../campaign/batch02/206614346/raw-windows.csv) show the actual observations.

Measured recurrence P=11.6830723205 +/- 0.0000162395d. Named reference epoch BTJD1359.9469056: selected eclipse kind at phase zero, not an assumed deeper primary. The legacy primary_epoch_btjd column carries this epoch. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when positive-degree-of-freedom reduced chi square exceeds one. With only two centers, no reduced chi square or measured residual scatter exists; covariance propagates input timing allowances. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Consecutive same-kind measured pairs: 3. Same-sector parity and actual coverage are in [alias-coverage.json](../../campaign/batch02/206614346/alias-coverage.json). No persistent deep alternating-depth pattern in the same-sector parity arrays. Covered half-phase windows lack an eclipse comparable to the selected kind. A perfectly identical two-eclipse2P harmonic is not mathematically excluded by single-kind morphology alone; Gaia orbital association and the lack of a second comparable sequence support the reported recurrence. This is a bounded alias check, not a blind exhaustive search. Two separated sectors are distinct observing occasions on the same instrument.

Fresh raw TESScut pixel identity agrees with Gaia DR3 6607402809430700800 to 0.00000arcsec by saved WCS; all source bytes are hashed. In sector2, 2 separately recomputed event deficits average0.108px from the target. Event-scatter vector is[0.014919760833283377, 0.07233357074091407]; this is descriptive sampling scatter, not calibrated positional confidence or pixel-response systematics. Lead visually inspected the historical full-field and freshly recomputed core images. Every capable neighbor in the saved60arcsec Gaia list: None within60arcsec under approximate G-band flux budget. Intrinsic source loss requirements and diluted fractional pixel losses are different quantities and are never compared as a veto. The G-band flux screen is approximate and does not exclude unknown unresolved companions.

Alternative extraction: background-subtracted raw TESScut1x1/3x3/5x5 median event depths are88.53/87.44/84.64ppt; selected QLP raw median fit depth89.04ppt. Details, windows, individual centroids, count and depths are in [pixel-evidence.json](../../campaign/batch02/206614346/pixel-evidence.json). This separately extracted reduction shares the same TESS photons as QLP and is not an independent instrument or independent observing occasion. Aperture dilution, cadence and event-core averaging explain differing apparent depths; no intrinsic binary depth is inferred.

Gaia orbit and physical plausibility: source-specific NSS P=11.6877344473d, e=0.05379, omega=49.7158deg, periastron BTJD388.97347. Closest edge-on conjunction offset at the measured epoch=-0.29090d (-0.02489phase); descriptive linear full-SB1-covariance timing error=0.31142d. The covariance uses source-specific P/e/omega/Tp correlations, not only diagonal errors. Mass function=0.017288solar; assumed primary mass=0.980solar gives minimum companion mass=0.306solar. Approximate central duration=5.91h versus observed5.31h. TIC radius/main-sequence companion assumptions and edge-on conjunction are approximations, not a fitted stellar model or arbitrary sigma admission rule. Orbit/geometry are consistent at this descriptive precision and do not establish the identity of an unresolved eclipse source.

Deciding interpretation: Six complete selected-kind raw eclipses span S2/68/96. Depth varies with aperture and sector. Narrow sharp eclipses are distinct from broad baseline variability; no capable Gaia neighbor in the saved 60-arcsec screen.

Next check: Optional resolved photometry and precision binary characterization.

Seven scoped catalogue groups were checked centrally for this identity; see [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv) and verification receipts. A nearby catalogue source is not an exact target match, and the scoped result does not assert exhaustive publication priority.

|Sector|Photometric cycle|Measured midpoint BTJD|Input timing allowance d|Fitted depth ppt|
|---|---:|---:|---:|---:|
|2|0|1359.9474701|0.010417|89.02|
|2|1|1371.6310539|0.010417|89.06|
|68|154|3159.1403325|0.001157|90.44|
|68|155|3170.8227458|0.001157|90.03|
|96|219|3918.5402168|0.001157|79.32|
|96|220|3930.2224031|0.001157|78.42|

Evidence and provenance: [measurements.json](../../campaign/batch02/206614346/measurements.json), [raw-windows.csv](../../campaign/batch02/206614346/raw-windows.csv), [raw-events.png](../../campaign/batch02/206614346/raw-events.png), [raw-sector-fold.png](../../campaign/batch02/206614346/raw-sector-fold.png), [alias-coverage.json](../../campaign/batch02/206614346/alias-coverage.json), [pixel-evidence.json](../../campaign/batch02/206614346/pixel-evidence.json), [pixel-recomputed.png](../../campaign/batch02/206614346/pixel-recomputed.png), historical/diff_s*.json/png, [historical/gaia.json](../../campaign/batch02/206614346/historical/gaia.json); batch [../gaia-geometry.json](../../campaign/batch02/gaia-geometry.json), [../alias-audit.json](../../campaign/batch02/alias-audit.json), [../secondary-audit.json](../../campaign/batch02/secondary-audit.json), [../measurement-source-receipts.json](../../campaign/batch02/measurement-source-receipts.json), [../download-receipts.json](../../campaign/batch02/download-receipts.json), [../source-hashes.json](../../campaign/batch02/source-hashes.json), [../LEAD-AUDIT.md](../../campaign/batch02/LEAD-AUDIT.md) and [../helper-audit.md](../../campaign/batch02/helper-audit.md). SHA256SUMS.json covers reports, scripts, raw FITS and original cutouts. Current availability receipt for246857844 is in shared-catalogues and copied locally with its hash. No canonical/public files were edited by this batch.


Stable review key: R553.

Deciding evidence and numeric artifacts:
- [alias-coverage.json](../../campaign/batch02/206614346/alias-coverage.json)
- [historical/diff_s02.json](../../campaign/batch02/206614346/historical/diff_s02.json)
- [historical/diff_s02.png](../../campaign/batch02/206614346/historical/diff_s02.png)
- [historical/gaia.json](../../campaign/batch02/206614346/historical/gaia.json)
- [measurements.json](../../campaign/batch02/206614346/measurements.json)
- [pixel-evidence.json](../../campaign/batch02/206614346/pixel-evidence.json)
- [pixel-recomputed.png](../../campaign/batch02/206614346/pixel-recomputed.png)
- [raw-events.png](../../campaign/batch02/206614346/raw-events.png)
- [raw-sector-fold.png](../../campaign/batch02/206614346/raw-sector-fold.png)
- [raw-windows.csv](../../campaign/batch02/206614346/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch02/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
