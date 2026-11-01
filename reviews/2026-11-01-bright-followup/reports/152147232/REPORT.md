# TIC 152147232: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 15 timing-usable measured centers in sectors [10, 63, 100]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 4.2135536598 ± 0.0000034278 d and reference epoch BTJD 1572.7251990 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 10 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 37 TESScut difference image puts the deficit 0.69 arcsec from the target coordinate; peak [7, 8] versus target pixel [8, 8]. Image-model fractional residual 0.531 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 5395959695358663040 (2.69 arcsec, G 15.822, intrinsic loss approx. 0.216); Gaia 5395959695356170624 (15.98 arcsec, G 16.524, intrinsic loss approx. 0.407); Gaia 5395959386121017472 (23.16 arcsec, G 14.509, intrinsic loss approx. 0.069); Gaia 5395959695358664832 (31.29 arcsec, G 16.245, intrinsic loss approx. 0.316); Gaia 5395959764078141952 (46.20 arcsec, G 14.642, intrinsic loss approx. 0.077); Gaia 5395959489200231936 (52.26 arcsec, G 15.438, intrinsic loss approx. 0.154). Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 5.19/4.77/3.58 ppt in 6 stacked historical events; representative QLP raw median fit depth is 6.70 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 5395959695358663296 has SB1 P = 4.2132911086 d and e = 0.09094. Closest edge-on conjunction offset is -0.03876 d (-0.00920 phase), with 0.37454 d linearly propagated full source-specific SB1 covariance. Rough central duration 4.84 h versus observed median fit 3.35 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** Fifteen raw repeats include many within-sector pairs. A capable 2.7 arcsec Gaia neighbor shares the TESS core and cannot be resolved.

**Next check:** Resolved eclipse photometry or multi-source PSF localization of the 2.7 arcsec pair.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 10 | 0 | 1572.7224256 | 0.010417 | 7.07 | used |
| 10 | 2 | 1581.1488039 | 0.010417 | 7.22 | used |
| 10 | 4 | 1589.5721707 | 0.010417 | 6.40 | used |
| 63 | 343 | 3017.9727299 | 0.001818 | 7.87 | used |
| 63 | 344 | 3022.1868246 | 0.002043 | 7.09 | used |
| 63 | 345 | 3026.4021096 | 0.001357 | 6.70 | used |
| 63 | 346 | 3030.6159883 | 0.001675 | 6.81 | used |
| 63 | 347 | 3034.8274841 | 0.001542 | 7.44 | used |
| 63 | 348 | 3039.0432524 | 0.002049 | 6.52 | used |
| 100 | 594 | 4075.5762282 | 0.001268 | 6.27 | used |
| 100 | 595 | 4079.7915930 | 0.001251 | 6.81 | used |
| 100 | 596 | 4084.0038984 | 0.001917 | 6.62 | used |
| 100 | 597 | 4088.2146792 | 0.001852 | 6.67 | used |
| 100 | 598 | 4092.4283531 | 0.001173 | 6.28 | used |
| 100 | 599 | 4096.6444202 | 0.001402 | 6.62 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s37.json, historical/diff_s37.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R434. Public evidence files: [diff_s37.json](../../evidence/152147232/historical/diff_s37.json), [diff_s37.png](../../evidence/152147232/historical/diff_s37.png), [gaia.json](../../evidence/152147232/historical/gaia.json), [measurements.json](../../evidence/152147232/measurements.json), [raw-events.png](../../evidence/152147232/raw-events.png), [raw-windows.csv](../../evidence/152147232/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
