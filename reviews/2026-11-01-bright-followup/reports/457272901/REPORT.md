# TIC 457272901: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 11 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 65, 99, 102. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 4.6492170041 ± 0.0000077651 d from actual midpoints, epoch BTJD 3071.2640710, cycle 316, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** target favored at TESS resolution. The historical sector-65 TESScut difference centroid is 2.05 arcsec from the target coordinate; peak pixel [7, 7], target pixel [8, 7]. Fractional image-model residual 0.474 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 7.12/6.92/6.01 ppt across 5 stacked events, versus median raw QLP SAP fit depth 8.09 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 5869945139392446336 has orbital P = 4.6494664348 d, e = 0.06671. Closest edge-on conjunction is offset by -0.13084 d (-0.02814 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.36286 d. The rough central eclipse duration is 3.53 h versus observed median 1.47 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** The added sector-65 raw events anchor the 4.649217-day timing baseline; later sector-99/102 troughs repeat. The difference centroid is 2.1 arcsec from the target and the closest capable neighbor is about 17 arcsec from that centroid. Twenty-seven capable Gaia sources lie within 60 arcsec; the crowded image and uncalibrated residual limit precision, but the spatial deficit favors the target.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 65 | 316 | 3071.2627207 | 0.001744 | 9.13 | used |
| 65 | 318 | 3080.5639080 | 0.001896 | 11.27 | used |
| 65 | 319 | 3085.2108687 | 0.001497 | 7.92 | used |
| 65 | 320 | 3089.8630025 | 0.003589 | 6.91 | used |
| 99 | 526 | 4047.5992838 | 0.002607 | 5.54 | used |
| 99 | 527 | 4052.2519805 | 0.001235 | 7.51 | used |
| 99 | 530 | 4066.1981510 | 0.001357 | 11.54 | used |
| 99 | 531 | 4070.8470307 | 0.001829 | 8.09 | used |
| 102 | 544 | 4131.2844012 | 0.001576 | 8.11 | used |
| 102 | 545 | 4135.9353243 | 0.001157 | 7.21 | used |
| 102 | 548 | 4149.8784550 | 0.001157 | 9.20 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| 5869942184454493952 | 15.81 | 16.636 | 0.461 | 18.0 |
| 5869945139392446080 | 18.08 | 13.674 | 0.037 | 17.1 |
| 5869945139392446592 | 25.28 | 16.453 | 0.390 | 27.5 |
| 5869939263875939200 | 30.92 | 15.973 | 0.254 | 29.4 |
| 5869939263875937536 | 31.84 | 13.624 | 0.036 | 30.3 |
| 5869942184454489344 | 33.36 | 17.052 | 0.672 | 35.8 |
| 5869939263875934336 | 35.40 | 16.042 | 0.270 | 34.0 |
| 5869942184454491520 | 38.07 | 17.429 | 0.947 | 40.8 |
| 5869942184454483712 | 40.77 | 16.711 | 0.493 | 43.2 |
| 5869936308938425216 | 41.37 | 17.197 | 0.767 | 40.9 |
| 5869942184389479424 | 41.48 | 17.384 | 0.910 | 42.0 |
| 5869945139392447744 | 42.24 | 16.755 | 0.513 | 43.7 |
| 5869942184454487552 | 44.96 | 15.517 | 0.169 | 47.7 |
| 5869942218814236544 | 45.73 | 15.875 | 0.232 | 48.4 |
| 5869942184454478976 | 47.67 | 15.702 | 0.199 | 49.8 |
| 5869939332595420544 | 48.37 | 17.389 | 0.914 | 47.2 |
| 5869945203761021568 | 49.50 | 17.171 | 0.749 | 48.9 |
| 5869939332595414400 | 52.30 | 15.832 | 0.224 | 51.1 |
| 5869942184468745088 | 52.87 | 17.290 | 0.834 | 53.7 |
| 5869942218814234240 | 53.06 | 16.785 | 0.527 | 56.0 |
| 5869942218814243584 | 53.79 | 16.964 | 0.620 | 56.1 |
| 5869942218814234112 | 54.64 | 15.222 | 0.131 | 57.6 |
| 5869942115735005312 | 56.67 | 17.032 | 0.660 | 59.5 |
| 5869939328228898560 | 56.94 | 16.642 | 0.463 | 56.2 |
| 5869939332595433344 | 57.44 | 16.012 | 0.262 | 56.7 |
| 5869939332595426432 | 57.93 | 15.601 | 0.182 | 57.0 |
| 5869939332595430144 | 58.16 | 13.894 | 0.044 | 57.3 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s65.json`, `historical/diff_s65.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R486. Public evidence files: [diff_s65.json](../../evidence/457272901/historical/diff_s65.json), [diff_s65.png](../../evidence/457272901/historical/diff_s65.png), [gaia.json](../../evidence/457272901/historical/gaia.json), [measurements.json](../../evidence/457272901/measurements.json), [raw-events.png](../../evidence/457272901/raw-events.png), [raw-windows.csv](../../evidence/457272901/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
