# TIC 144102918: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 13 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 4, 31, 97. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 5.5018791815 ± 0.0000050961 d from actual midpoints, epoch BTJD 1413.8257574, cycle 0, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** target favored at TESS resolution. The historical sector-97 TESScut difference centroid is 0.50 arcsec from the target coordinate; peak pixel [8, 7], target pixel [8, 7]. Fractional image-model residual 0.058 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 57.89/57.27/55.49 ppt across 8 stacked events, versus median raw QLP SAP fit depth 54.66 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 4841921897857941248 has orbital P = 5.5016102193 d, e = 0.07812. Closest edge-on conjunction is offset by 0.05387 d (0.00979 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.10114 d. The rough central eclipse duration is 4.99 h versus observed median 4.77 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Thirteen measured eclipses span sectors 4, 31 and 97, including adjacent cycles. Difference imaging is sharply target-centered with no capable Gaia neighbor in the 60-arcsec screen.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 4 | 0 | 1413.8270960 | 0.010417 | 55.31 | used |
| 4 | 3 | 1430.3331928 | 0.010417 | 54.66 | used |
| 4 | 4 | 1435.8342838 | 0.010417 | 55.72 | used |
| 31 | 133 | 2145.5757425 | 0.003472 | 57.84 | used |
| 31 | 134 | 2151.0776028 | 0.003472 | 57.54 | used |
| 31 | 136 | 2162.0809820 | 0.003472 | 58.09 | used |
| 31 | 137 | 2167.5827793 | 0.003472 | 58.95 | used |
| 97 | 459 | 3939.1883705 | 0.001157 | 50.45 | used |
| 97 | 460 | 3944.6897340 | 0.001157 | 50.13 | used |
| 97 | 462 | 3955.6948555 | 0.001157 | 49.90 | used |
| 97 | 464 | 3966.6976092 | 0.001157 | 49.73 | used |
| 97 | 465 | 3972.1992965 | 0.001157 | 50.07 | used |
| 97 | 467 | 3983.2031899 | 0.001157 | 50.07 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| None | — | — | — | — |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s97.json`, `historical/diff_s97.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R487. Public evidence files: [diff_s97.json](../../evidence/144102918/historical/diff_s97.json), [diff_s97.png](../../evidence/144102918/historical/diff_s97.png), [gaia.json](../../evidence/144102918/historical/gaia.json), [measurements.json](../../evidence/144102918/measurements.json), [raw-events.png](../../evidence/144102918/raw-events.png), [raw-windows.csv](../../evidence/144102918/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
