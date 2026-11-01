# TIC 66281997: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate.

1. **Raw evidence.** Quality-zero QLP SAP_FLUX contains 8 timing-usable measured centers in sectors [56, 57, 76, 77, 83, 84]. Local trapezoids fit free centers, depths, durations and baselines. Raw plots and windows retain the evidence. Predicted centers guided extraction only; flagged or uncovered windows are not null detections. Representative morphology shows repeated eclipses.
2. **Timing and aliases.** Measured centers yield P = 16.1669963889 ± 0.0000470947 d and reference epoch BTJD 2840.7742919 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). There are 2 within-sector adjacent same-kind pairs (../alias-audit.json). Measured centers and same-kind pairs support the bounded period and alias check. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This formal error is not total calibrated uncertainty or an exhaustive alias search.
3. **Source attribution.** Historical sector 57 TESScut difference image puts the deficit 9.07 arcsec from the target coordinate; peak [7, 8] versus target pixel [7, 8]. Image-model fractional residual 0.659 is not a localization error. Capable Gaia neighbors within 60 arcsec: Gaia 1988346111733826048 (21.78 arcsec, G 16.847, intrinsic loss approx. 0.477); Gaia 1988346180453300224 (28.72 arcsec, G 14.216, intrinsic loss approx. 0.047); Gaia 1988344634265076480 (42.81 arcsec, G 15.709, intrinsic loss approx. 0.171); Gaia 1988346111733827840 (51.33 arcsec, G 16.147, intrinsic loss approx. 0.253); Gaia 1988346936367541632 (53.51 arcsec, G 15.384, intrinsic loss approx. 0.128); Gaia 1988344634265076608 (54.24 arcsec, G 17.139, intrinsic loss approx. 0.622); Gaia 1988346146093565824 (56.84 arcsec, G 14.496, intrinsic loss approx. 0.060). Intrinsic-loss requirements use an approximate flux budget and cannot be equated to blended pixel loss.
4. **Alternative reduction.** Background-subtracted TESScut 1x1/3x3/5x5 target apertures yield 6.83/6.71/5.38 ppt in 2 stacked historical events; representative QLP raw median fit depth is 5.95 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and event choice limit depth comparisons.
5. **Gaia geometry.** Matched DR3 source 1988346180453301632 has SB1 P = 16.1641569409 d and e = 0.40209. Closest edge-on conjunction offset is 0.43325 d (0.02680 phase), with 0.51578 d linearly propagated full source-specific SB1 covariance. Rough central duration 7.71 h versus observed median fit 2.48 h assumes TIC radius and a minimum-mass main-sequence companion, not a full binary model. Agreement is not source proof.

**Interpretation and limitation:** Eight usable raw centers lie in six sectors after all eight archived QLP sectors were examined; they include adjacent S56/S57 and S76/S77 cycles. The historical S57 deficit lies 9.1 arcsec from the target, toward a capable G16.8 star 21.8 arcsec away. Noisy pixels and other capable neighbors prevent unique attribution.

**Next check:** Independent high-resolution eclipse photometry or multi-source PSF localization of the crowded deficit core.

Catalogue novelty: central seven-group result is ../../shared-catalogues/coverage-matrix.csv. A cone source alone is not an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 56 | 68 | 2840.7728335 | 0.002230 | 5.77 | used |
| 57 | 69 | 2856.9441832 | 0.002354 | 5.64 | used |
| 57 | 70 | 2873.1056462 | 0.002773 | 5.92 | used |
| 76 | 101 | 3374.2961244 | 392421.524476 | 5.60 | excluded: Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris. |
| 76 | 102 | 3390.4556240 | 0.003173 | 6.61 | used |
| 77 | 103 | 3406.6183094 | 0.002544 | 6.55 | used |
| 77 | 104 | 3422.7876011 | 0.002693 | 5.96 | used |
| 83 | 113 | 3568.2897722 | 0.003193 | 5.94 | used |
| 84 | 115 | 3600.6209460 | 0.002463 | 6.07 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s57.json, historical/diff_s57.png, historical/gaia.json and ../helper-audit.md. Original TESScut: [local path omitted] (SHA256 in ../source-hashes.json). Retained artifacts are in ../SHA256SUMS.json.


Stable review key: R436. Public evidence files: [diff_s57.json](../../evidence/66281997/historical/diff_s57.json), [diff_s57.png](../../evidence/66281997/historical/diff_s57.png), [gaia.json](../../evidence/66281997/historical/gaia.json), [measurements.json](../../evidence/66281997/measurements.json), [raw-events.png](../../evidence/66281997/raw-events.png), [raw-windows.csv](../../evidence/66281997/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch03/INDEX.md). 
