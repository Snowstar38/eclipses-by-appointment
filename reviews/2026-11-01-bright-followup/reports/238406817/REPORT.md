# TIC 238406817: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 9 timing-selected measured eclipses in sectors [57, 84]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=4.7752225643 d, fit error=0.0000050930 d, epoch BTJD 2854.4959258 (Deeper repeating eclipse; historical half-period parity 0). There are 5 consecutive within-sector same-kind cycle pairs. The inventory period was 4.77524 d and the historical SAP search branch was 2.3876213686 d. Deeper parity 0 of historical half-period cycles; consecutive same-kind events have orbital-cycle count one. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: favors target at TESS resolution.** Historical S57 TESScut deficit core is 2.54 arcsec from the target coordinate; peak pixel [7, 8] and target pixel [7, 8]. Fractional PSF model residual is 0.089, not a localization uncertainty. Capable Gaia neighbors: none under the approximate G-band flux budget. The full list and flux-budget calculation are in historical/diff_s57.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 193.58/189.24/185.20 ppt from 10 selected windows. Median selected QLP raw fit depth is 274.77 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 2854017381783700352 has P=4.7751949852 d and e=0.01333. Closest edge-on conjunction differs from the measured epoch by 0.00195 in phase (0.00933 d); linear propagation of the source-specific full SB1 covariance gives 0.12817 d as a descriptive timing scale. The rough central-duration estimate is 5.98 h versus trapezoid median 4.87 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Alternating ~275 and ~116 ppt eclipses identify the 4.7752 d orbital period; the historical 2.38762 d SAP branch is the half-period. The deeper parity defines the epoch.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 57 | 0 | 2854.4959299 | 0.001157 | 273.94 | used |
| 57 | 1 | 2856.8836580 | 0.001157 | 114.76 | other eclipse kind |
| 57 | 2 | 2859.2710510 | 0.001157 | 273.97 | used |
| 57 | 3 | 2861.6590785 | 0.001157 | 115.66 | other eclipse kind |
| 57 | 6 | 2868.8215384 | 0.001157 | 273.49 | used |
| 57 | 7 | 2871.2094824 | 0.001157 | 117.85 | other eclipse kind |
| 57 | 8 | 2873.5968356 | 0.001157 | 274.92 | used |
| 57 | 9 | 2875.9843939 | 0.001157 | 118.62 | other eclipse kind |
| 57 | 10 | 2878.3721685 | 0.001157 | 274.42 | used |
| 57 | 11 | 2880.7598585 | 0.001157 | 118.44 | other eclipse kind |
| 84 | 306 | 3585.1049933 | 0.001157 | 275.17 | used |
| 84 | 307 | 3587.4930233 | 0.001157 | 114.11 | other eclipse kind |
| 84 | 308 | 3589.8803134 | 0.001157 | 276.62 | used |
| 84 | 309 | 3592.2681450 | 0.001157 | 116.02 | other eclipse kind |
| 84 | 310 | 3594.6553399 | 0.001157 | 276.30 | used |
| 84 | 313 | 3601.8182245 | 0.001157 | 115.69 | other eclipse kind |
| 84 | 314 | 3604.2136516 | 53785.751904 | 275.92 | excluded: unidentifiable center covariance |
| 84 | 315 | 3606.5929309 | 0.001157 | 114.09 | other eclipse kind |
| 84 | 316 | 3608.9810451 | 0.001157 | 274.77 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s57.json, historical/diff_s57.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R448. Public evidence files: [diff_s57.json](../../evidence/238406817/historical/diff_s57.json), [diff_s57.png](../../evidence/238406817/historical/diff_s57.png), [gaia.json](../../evidence/238406817/historical/gaia.json), [measurements.json](../../evidence/238406817/measurements.json), [raw-events.png](../../evidence/238406817/raw-events.png), [raw-windows.csv](../../evidence/238406817/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
