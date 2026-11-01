# TIC 408189324: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 12 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 32, 98. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 4.3936455322 ± 0.0000035849 d from actual midpoints, epoch BTJD 2174.5912708, cycle 167, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** target favored at TESS resolution. The historical sector-32 TESScut difference centroid is 0.48 arcsec from the target coordinate; peak pixel [8, 8], target pixel [8, 8]. Fractional image-model residual 0.077 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 41.21/41.38/40.39 ppt across 6 stacked events, versus median raw QLP SAP fit depth 40.93 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 2969339250844920832 has orbital P = 4.3934150548 d, e = 0.29683. Closest edge-on conjunction is offset by 0.03354 d (0.00763 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.05028 d. The rough central eclipse duration is 3.93 h versus observed median 2.22 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Six consecutive sector-32 events and six sector-98 events support the same 4.39365-day cycle. The deficit is sharply centered on the target and no capable Gaia neighbor is listed within 60 arcsec.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 32 | 167 | 2174.5917124 | 0.003472 | 43.90 | used |
| 32 | 168 | 2178.9850342 | 0.003472 | 43.13 | used |
| 32 | 169 | 2183.3782386 | 0.003472 | 41.89 | used |
| 32 | 170 | 2187.7723515 | 0.003472 | 42.88 | used |
| 32 | 171 | 2192.1657544 | 0.003472 | 41.42 | used |
| 32 | 172 | 2196.5592879 | 0.003472 | 43.67 | used |
| 98 | 582 | 3997.9537519 | 0.001157 | 40.30 | used |
| 98 | 583 | 4002.3475700 | 0.001157 | 39.77 | used |
| 98 | 585 | 4011.1353392 | 0.001157 | 40.42 | used |
| 98 | 586 | 4015.5288585 | 0.001157 | 39.92 | used |
| 98 | 589 | 4028.7098454 | 0.001157 | 40.44 | used |
| 98 | 592 | 4041.8907654 | 0.001157 | 39.47 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| None | — | — | — | — |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s32.json`, `historical/diff_s32.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R482. Public evidence files: [diff_s32.json](../../evidence/408189324/historical/diff_s32.json), [diff_s32.png](../../evidence/408189324/historical/diff_s32.png), [gaia.json](../../evidence/408189324/historical/gaia.json), [measurements.json](../../evidence/408189324/measurements.json), [raw-events.png](../../evidence/408189324/raw-events.png), [raw-windows.csv](../../evidence/408189324/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
