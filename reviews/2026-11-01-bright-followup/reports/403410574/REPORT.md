# TIC 403410574: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate from the historical screening label.

1. **Raw morphology:** 16 timing-usable measured eclipses in quality-zero QLP SAP_FLUX across sectors 99, 102. Local trapezoids fit free centers, depths, widths and baselines. Predicted centers only selected windows; they were not timing points. The raw window CSV and plot preserve the observations. Flagged or uncovered windows are not clean nulls.
2. **Timing and alias:** P = 2.1148563262 ± 0.0000186810 d from actual midpoints, epoch BTJD 4048.0101157, cycle 796, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Within-sector recurrence and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than an exhaustive all-period search.
3. **Source attribution:** unresolved. The historical sector-39 TESScut difference centroid is 5.38 arcsec from the target coordinate; peak pixel [8, 7], target pixel [7, 7]. Fractional image-model residual 0.896 is not a calibrated localization error. Every capable Gaia neighbor in the 60-arcsec screen is listed below; its required intrinsic eclipse fraction is an approximate flux-budget bound, not a blended pixel fractional loss.
4. **Alternative reduction:** A separately extracted, target-centered, background-subtracted TESScut 1x1/3x3/5x5-pixel aperture gives 6.46/6.39/3.75 ppt across 12 stacked events, versus median raw QLP SAP fit depth 7.55 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Crowding, aperture dilution and different event selections limit depth equality.
5. **Gaia geometry:** DR3 source 5792684548884156800 has orbital P = 2.1148150688 d, e = 0.11270. Closest edge-on conjunction is offset by 0.12513 d (0.05917 phase) at the measured epoch; full SB1 covariance gives descriptive linear timing error 0.15197 d. The rough central eclipse duration is 3.34 h versus observed median 1.20 h. TIC radius and main-sequence minimum-mass companion assumptions make this a plausibility check, not a fitted binary model or a sigma veto. Agreement cannot identify an unresolved eclipsing neighbor.

**Deciding interpretation and limitation:** Sixteen measured shallow but discrete raw eclipses in sectors 99 and 102 establish a repeated 2.11486-day signal. The early sector-39 cadence is too sparse for the local trapezoid timing criterion, although its stacked custom aperture shows the event. A capable Gaia neighbor 12.2 arcsec from the target lies only 10.9 arcsec from the deficit centroid; the residual is 0.896. TESS pixels do not settle attribution.

**Next check:** Resolved eclipse photometry or multi-source pixel-response fitting of the 12.2-arcsec pair.

**Catalogue novelty:** The central seven-group result is in `../../shared-catalogues/coverage-matrix.csv`: complete scoped checks and no identified prior eclipsing-binary match for this TIC. This does not establish exhaustive literature priority or resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 99 | 796 | 4048.0105152 | 0.001157 | 8.23 | used |
| 99 | 797 | 4050.1226481 | 0.001157 | 9.29 | used |
| 99 | 798 | 4052.2403352 | 0.001157 | 9.02 | used |
| 99 | 799 | 4054.3551161 | 0.001157 | 7.41 | used |
| 99 | 804 | 4064.9275859 | 0.001224 | 7.78 | used |
| 99 | 805 | 4067.0446358 | 0.001614 | 7.45 | used |
| 99 | 806 | 4069.1605614 | 0.001162 | 8.17 | used |
| 102 | 834 | 4128.3760132 | 0.001412 | 6.84 | used |
| 102 | 835 | 4130.4900083 | 0.001157 | 7.18 | used |
| 102 | 836 | 4132.6052166 | 0.001538 | 6.87 | used |
| 102 | 837 | 4134.7170281 | 0.001157 | 7.54 | used |
| 102 | 838 | 4136.8335795 | 0.002748 | 6.88 | used |
| 102 | 840 | 4141.0646915 | 0.001157 | 8.53 | used |
| 102 | 841 | 4143.1801215 | 0.001203 | 7.13 | used |
| 102 | 843 | 4147.4086149 | 0.001170 | 7.82 | used |
| 102 | 844 | 4149.5210460 | 0.001157 | 7.56 | used |

Capable Gaia neighbors in the historical difference-image 60-arcsec screen:

| Gaia DR3 source | Target separation arcsec | G | Approximate required intrinsic eclipse fraction | Deficit-centroid separation arcsec |
|---|---:|---:|---:|---:|
| 5792684347027309312 | 12.23 | 15.744 | 0.202 | 10.9 |
| 5792684518826000768 | 18.96 | 17.228 | 0.771 | 25.2 |
| 5792684347027309184 | 21.08 | 16.978 | 0.614 | 21.3 |
| 5792684347027308416 | 27.46 | 16.298 | 0.332 | 30.4 |
| 5792684347027308032 | 29.35 | 15.674 | 0.190 | 35.4 |
| 5792684312667569408 | 35.36 | 15.218 | 0.128 | 42.6 |
| 5794185764514224512 | 46.47 | 15.531 | 0.168 | 44.8 |
| 5792684548884947072 | 47.39 | 16.886 | 0.565 | 44.2 |
| 5792684518826001408 | 49.08 | 13.476 | 0.032 | 55.2 |
| 5792684553185740928 | 49.17 | 17.116 | 0.697 | 46.4 |
| 5792684347027307008 | 50.48 | 15.561 | 0.172 | 54.8 |
| 5792684518826000896 | 52.86 | 15.681 | 0.191 | 60.4 |
| 5794185554054569856 | 55.03 | 17.267 | 0.800 | 55.8 |
| 5792684347027445120 | 55.22 | 16.618 | 0.443 | 59.0 |
| 5792684617604424064 | 55.68 | 17.504 | 0.992 | 53.2 |
| 5792684312667567744 | 59.84 | 13.035 | 0.024 | 67.8 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../download-receipts.json`, `../targeted-download-receipts.json`, `../gaia-geometry.json`, `../alias-audit.json`, `historical/diff_s39.json`, `historical/diff_s39.png`, `historical/gaia.json`, and `../helper-audit.md`. Original TESScut: `[local path omitted] (SHA256 in `../source-hashes.json`). Source code and retained evidence are listed in `../SHA256SUMS.json`.


Stable review key: R488. Public evidence files: [diff_s39.json](../../evidence/403410574/historical/diff_s39.json), [diff_s39.png](../../evidence/403410574/historical/diff_s39.png), [gaia.json](../../evidence/403410574/historical/gaia.json), [measurements.json](../../evidence/403410574/measurements.json), [raw-events.png](../../evidence/403410574/raw-events.png), [raw-windows.csv](../../evidence/403410574/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch08/INDEX.md). 
