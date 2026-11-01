# TIC 308609252: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 4 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 18, 58, 85. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 13.1993185849 ± 0.0000252249 d from actual midpoints, epoch BTJD 1806.9033855, cycle 1, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** target favored at TESS resolution. The historical sector-18 TESScut difference centroid is 5.39 arcsec from the target coordinate; peak pixel [7, 8], target pixel [7, 8]. Fractional image-model residual 0.940 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 111.44/101.21/64.57 ppt across 2 stacked events, versus median raw QLP SAP fit depth 111.83 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 399670247610908160 has orbital P = 13.1964046632 d, e = 0.26890. Closest edge-on conjunction is offset by 0.20557 d (0.01558 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.25980 d. The rough central eclipse duration is 4.27 h versus observed median 3.44 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Four raw events include an adjacent sector-58 pair. The sector-18 difference core is centered near the target, while the only capable catalogued Gaia neighbor is 54.4 arcsec away. The 0.94 image-model residual limits centroid precision.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 18 | 1 | 1806.9021315 | 0.010417 | 103.31 | used |
| 58 | 83 | 2889.2475745 | 0.001157 | 111.85 | used |
| 58 | 84 | 2902.4468010 | 0.001157 | 111.82 | used |
| 85 | 138 | 3615.2100090 | 0.001157 | 112.73 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| 399673168188672256 | 54.37 | 13.801 | 0.590 | 60.5 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s18.json`, `historical/diff_s18.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R480. Public evidence files: [diff_s18.json](../../evidence/308609252/historical/diff_s18.json), [diff_s18.png](../../evidence/308609252/historical/diff_s18.png), [gaia.json](../../evidence/308609252/historical/gaia.json), [measurements.json](../../evidence/308609252/measurements.json), [raw-events.png](../../evidence/308609252/raw-events.png), [raw-windows.csv](../../evidence/308609252/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
