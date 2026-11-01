# TIC 34759144: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 3 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 27, 67, 94. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 19.3399704780 ± 0.0000322940 d from actual midpoints, epoch BTJD 2043.3791201, cycle 0, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json` and the targeted `../34759144-alias-enumeration.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** target favored at TESS resolution. The historical sector-27 TESScut difference centroid is 1.75 arcsec from the target coordinate; peak pixel [8, 7], target pixel [8, 7]. Fractional image-model residual 0.252 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 44.28/43.68/41.44 ppt across 1 stacked events, versus median raw QLP SAP fit depth 43.81 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 6696505582479751296 has orbital P = 19.3348568551 d, e = 0.21375. Closest edge-on conjunction is offset by 0.50738 d (0.02624 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.89805 d. The rough central eclipse duration is 14.22 h versus observed median 10.29 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Three clean raw eclipses occur one per selected sector. Enumerating neighboring integer cycle counts gives 57 then 37 cycles at 19.33997 d; the next-best pairs disagree by at least 0.0248 d between gaps. This tests nearby aliases, while subharmonics remain bounded by observed coverage.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 27 | 0 | 2043.3782485 | 0.003472 | 43.81 | used |
| 67 | 57 | 3145.7576833 | 0.001157 | 45.02 | used |
| 94 | 94 | 3861.3361958 | 0.001157 | 38.60 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| None | — | — | — | — |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s27.json`, `historical/diff_s27.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R481. Public evidence files: [diff_s27.json](../../evidence/34759144/historical/diff_s27.json), [diff_s27.png](../../evidence/34759144/historical/diff_s27.png), [gaia.json](../../evidence/34759144/historical/gaia.json), [measurements.json](../../evidence/34759144/measurements.json), [raw-events.png](../../evidence/34759144/raw-events.png), [raw-windows.csv](../../evidence/34759144/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
