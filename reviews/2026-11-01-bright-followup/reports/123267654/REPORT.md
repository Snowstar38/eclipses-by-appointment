# TIC 123267654: CONFIRMED

Full bounded review: **COMPLETE**. This physical outcome is separate from catalogue novelty and from the historical screening label.

1. **Raw repeat:** 12 measured same-kind eclipses in representative QLP SAP_FLUX sectors [97, 104]; raw flux, quality filtering, fitted windows and plots are retained. Fitted periodic depressions alone would be insufficient: the inspected windows have recurring eclipse morphology. Predicted centers were search guides, never timing points. Flagged or unresolved windows are not clean nulls.
2. **Timing and aliases:** measured midpoints give P = 5.5559075318 ± 0.0000169590 d and reference BTJD 3939.0725724 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind within-sector counts and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check rather than a blind exhaustive search.
3. **Attribution:** historical S97 TESScut deficit lies 0.46 arcsec from the target coordinate; peak pixel [7, 8] and target pixel [7, 8]. Image-model fractional residual 0.060 is not a calibrated position error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic neighbor requirement is not the same as the blended pixel loss.
4. **Alternative reduction:** independent target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture extraction gives 135.68/133.72/133.25 ppt in 8 stacked events; selected QLP raw depth is 118.29 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution, event-kind mixing and temporal changes limit a direct depth comparison.
5. **Gaia geometry:** matched DR3 source 5018762885599910016 has SB1 period 5.5561122262 d, e = 0.07698. The closest edge-on conjunction differs from the measured eclipse epoch by -0.17143 d (-0.03085 phase); the linear propagated timing scale from source-specific full SB1 covariance is 0.25667 d. Rough central duration 4.65 h versus measured median 3.38 h uses TIC radius and a minimum-mass main-sequence companion; it is not a physical fit or a sigma veto.

**Deciding interpretation and limitations:** Twelve raw eclipses across S97/104, with consecutive cycles and consistent depths. The S97 cutout has a clean target-centered deficit. The selected earlier S3 QLP file supplied no usable midpoint; it is not treated as a null eclipse.

**Next check:** Optional resolved photometry or spectroscopy for precision binary parameters; no bounded admission check remains missing.

Catalogue novelty: the central seven-group check in ../../shared-catalogues/coverage-matrix.csv reports complete scoped coverage and no identified prior eclipsing-binary match for this exact target. This is not exhaustive priority and does not resolve embargoed identities.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 97 | 459 | 3939.0723654 | 0.001157 | 122.09 | used |
| 97 | 460 | 3944.6289202 | 0.001157 | 120.31 | used |
| 97 | 461 | 3950.1845485 | 0.001157 | 118.35 | used |
| 97 | 462 | 3955.7403975 | 0.001157 | 118.23 | used |
| 97 | 464 | 3966.8517920 | 0.001157 | 117.83 | used |
| 97 | 465 | 3972.4078429 | 0.001157 | 114.57 | used |
| 97 | 466 | 3977.9642012 | 0.001157 | 118.44 | used |
| 97 | 467 | 3983.5194413 | 0.001157 | 116.32 | used |
| 104 | 503 | 4183.5331930 | 0.001157 | 118.87 | used |
| 104 | 504 | 4189.0888142 | 0.001157 | 118.09 | used |
| 104 | 505 | 4194.6438920 | 0.001157 | 118.65 | used |
| 104 | 506 | 4200.1996719 | 0.001157 | 118.10 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json). Source code and retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R464. Public evidence files: [diff_s97.json](../../evidence/123267654/historical/diff_s97.json), [diff_s97.png](../../evidence/123267654/historical/diff_s97.png), [gaia.json](../../evidence/123267654/historical/gaia.json), [measurements.json](../../evidence/123267654/measurements.json), [raw-events.png](../../evidence/123267654/raw-events.png), [raw-windows.csv](../../evidence/123267654/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch06/INDEX.md). 
