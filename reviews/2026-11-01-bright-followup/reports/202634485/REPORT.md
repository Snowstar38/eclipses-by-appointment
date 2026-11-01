# TIC 202634485: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 8 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 14, 55, 82. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 7.8189267254 ± 0.0000356216 d from actual midpoints, epoch BTJD 1688.6785071, cycle 0, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** unresolved. The historical sector-82 TESScut difference centroid is 5.99 arcsec from the target coordinate; peak pixel [7, 7], target pixel [7, 7]. Fractional image-model residual 0.968 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 14.95/8.35/3.26 ppt across 4 stacked events, versus median raw QLP SAP fit depth 33.47 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 2055792762025890176 has orbital P = 7.8183725267 d, e = 0.24161. Closest edge-on conjunction is offset by 0.06916 d (0.00885 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.27464 d. The rough central eclipse duration is 6.77 h versus observed median 3.87 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Sector-55 has three consecutive clean raw eclipses. The sector-82 raw baseline is structured; its same-photon custom-aperture signal is much shallower than QLP SAP, with crowding, aperture and baseline sensitivity likely contributing. A Gaia neighbor 10.1 arcsec away could in principle supply the event if nearly fully eclipsed, and the image-model residual is 0.968. Target attribution remains unresolved.

**Next check:** Resolved eclipse photometry or multi-source pixel-response fitting of the 10.1-arcsec pair.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 14 | 0 | 1688.6631740 | 0.033133 | 37.33 | used |
| 55 | 142 | 2798.9652268 | 0.003472 | 28.70 | used |
| 55 | 143 | 2806.7824513 | 0.003472 | 32.82 | used |
| 55 | 144 | 2814.6078397 | 0.003472 | 28.32 | used |
| 82 | 236 | 3533.9496625 | 0.006967 | 38.02 | used |
| 82 | 237 | 3541.7630557 | 0.005726 | 26.57 | used |
| 82 | 238 | 3549.5839019 | 0.003034 | 34.12 | used |
| 82 | 239 | 3557.3761215 | 0.012302 | 49.90 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| 2055792766332050688 | 10.09 | 15.945 | 0.938 | 13.9 |
| 2055792727666151552 | 58.25 | 9.031 | 0.030 | 67.2 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s82.json`, `historical/diff_s82.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R485. Public evidence files: [diff_s82.json](../../evidence/202634485/historical/diff_s82.json), [diff_s82.png](../../evidence/202634485/historical/diff_s82.png), [gaia.json](../../evidence/202634485/historical/gaia.json), [measurements.json](../../evidence/202634485/measurements.json), [raw-events.png](../../evidence/202634485/raw-events.png), [raw-windows.csv](../../evidence/202634485/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
