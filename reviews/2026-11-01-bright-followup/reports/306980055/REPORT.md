# TIC 306980055: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 5 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 12, 39, 93. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 16.6314800623 ± 0.0000277694 d from actual midpoints, epoch BTJD 1637.8317347, cycle 0, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** target favored at TESS resolution. The historical sector-39 TESScut difference centroid is 3.01 arcsec from the target coordinate; peak pixel [7, 8], target pixel [7, 8]. Fractional image-model residual 0.328 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 71.49/69.24/62.01 ppt across 2 stacked events, versus median raw QLP SAP fit depth 72.73 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 5911278044857572480 has orbital P = 16.6305032216 d, e = 0.36931. Closest edge-on conjunction is offset by -0.13935 d (-0.00838 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.29122 d. The rough central eclipse duration is 7.65 h versus observed median 5.32 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Measured sector-39 and sector-93 adjacent pairs span the long baseline. The capable 55.8-arcsec Gaia neighbor is distinct from the target-centered difference core.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 12 | 0 | 1637.8320133 | 0.010417 | 64.93 | used |
| 39 | 44 | 2369.6168339 | 0.003472 | 72.41 | used |
| 39 | 45 | 2386.2483563 | 0.003472 | 72.73 | used |
| 93 | 132 | 3833.1866950 | 0.001157 | 73.65 | used |
| 93 | 133 | 3849.8189880 | 0.001157 | 79.12 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| 5909777043986816768 | 55.81 | 14.437 | 0.578 | 54.0 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s39.json`, `historical/diff_s39.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R484. Public evidence files: [diff_s39.json](../../evidence/306980055/historical/diff_s39.json), [diff_s39.png](../../evidence/306980055/historical/diff_s39.png), [gaia.json](../../evidence/306980055/historical/gaia.json), [measurements.json](../../evidence/306980055/measurements.json), [raw-events.png](../../evidence/306980055/raw-events.png), [raw-windows.csv](../../evidence/306980055/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
