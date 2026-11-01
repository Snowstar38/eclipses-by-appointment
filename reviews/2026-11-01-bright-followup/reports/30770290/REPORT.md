# TIC 30770290: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 6 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 12, 39, 66, 104. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 8.3804132410 ± 0.0000094619 d from actual midpoints, epoch BTJD 1645.6504646, cycle 1, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** target favored at TESS resolution. The historical sector-39 TESScut difference centroid is 3.33 arcsec from the target coordinate; peak pixel [8, 8], target pixel [8, 8]. Fractional image-model residual 0.988 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 96.05/80.93/45.08 ppt across 2 stacked events, versus median raw QLP SAP fit depth 82.41 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 5955349082236051072 has orbital P = 8.3812349333 d, e = 0.09409. Closest edge-on conjunction is offset by -0.18507 d (-0.02208 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.15637 d. The rough central eclipse duration is 7.78 h versus observed median 6.07 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Sector-39 and sector-66 measured pairs are separated by two historical cycles, but independent inspection finds a real ~69-ppt usable-core deficit at intervening sector-66 cycle 176. Its partial coverage prevents a reliable midpoint fit; it supports the 8.3804-day recurrence over a simple 16.76-day parity alias. Sector-39 cycle 88 is a gap, not a null. The high image-model residual limits localization precision.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 12 | 1 | 1645.6327354 | 0.021612 | 78.19 | used |
| 39 | 87 | 2366.3654077 | 0.003472 | 78.06 | used |
| 39 | 89 | 2383.1275530 | 0.003472 | 85.67 | used |
| 66 | 175 | 3103.8417724 | 0.001157 | 94.86 | used |
| 66 | 177 | 3120.6038978 | 0.001157 | 93.44 | used |
| 104 | 306 | 4201.6764331 | 0.001157 | 79.15 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| 5955349494552910848 | 48.59 | 12.925 | 0.251 | 48.3 |
| 5955349872514790784 | 54.94 | 14.307 | 0.678 | 52.7 |
| 5955349872510033024 | 59.62 | 13.836 | 0.469 | 57.4 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s39.json`, `historical/diff_s39.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R483. Public evidence files: [diff_s39.json](../../evidence/30770290/historical/diff_s39.json), [diff_s39.png](../../evidence/30770290/historical/diff_s39.png), [gaia.json](../../evidence/30770290/historical/gaia.json), [measurements.json](../../evidence/30770290/measurements.json), [raw-events.png](../../evidence/30770290/raw-events.png), [raw-windows.csv](../../evidence/30770290/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
