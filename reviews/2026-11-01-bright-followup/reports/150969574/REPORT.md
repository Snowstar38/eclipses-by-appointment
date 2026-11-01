# TIC 150969574: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are recorded separately. The historical screening label is not an admission verdict.

1. **Raw repeated events: pass.** Quality-zero QLP SAP_FLUX contains 8 timing-usable measured eclipses in representative sectors [57, 84]. The raw plot and numeric windows retain the light-curve evidence. Local trapezoids have free centers, depths, durations and baselines. Predicted times guided windows only. Flagged or uncovered intervals are not null detections.
2. **Measured timing and alias: pass.** 8 actual midpoints yield P = 6.0463235428 ± 0.0000070222 d and reference epoch BTJD 2859.5530800 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). Same-kind cycle counts, within-sector repeats and parity are in ../alias-audit.json. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive blind all-period search.
3. **Source attribution: favors target at TESS image resolution.** Historical sector 84 cutout puts the deficit 1.35 arcsec from the target coordinate; peak [7, 7] versus target pixel [7, 7]. Image-model fractional residual 0.031; this is not a calibrated localization error. Capable Gaia neighbors: None within 60 arcsec under the approximate G-band flux budget. The intrinsic requirement uses an approximate flux budget and is not compared directly with a blended pixel fractional loss.
4. **Alternative reduction: pass.** Target-centered background-subtracted TESScut 1x1/3x3/5x5 aperture depths are 35.85/36.10/35.95 ppt in 4 stacked events; median selected QLP raw fit depth 35.32 ppt. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument. Aperture dilution and any mixed event kinds limit depth comparisons.
5. **Gaia geometry: consistent within descriptive limits.** Matched DR3 source 2799480161937494912 has orbital P = 6.0462607078 d, e = 0.08689; closest edge-on conjunction offset at the measured epoch is 0.12220 d (0.02021 phase), with 0.45776 d linearly propagated full-SB1-covariance timing error. The rough central duration is 4.48 h versus observed median 4.08 h; assumed TIC radius and minimum-mass companion are not a full fit. Geometry supports physical plausibility without an arbitrary sigma veto or proof of which unresolved neighbor eclipses.

**Deciding interpretation and limitation:** Eight repeated raw eclipses S57/84; target-centered difference core and no capable Gaia neighbor under the brightness screen.

**Next check:** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result is in ../../shared-catalogues/coverage-matrix.csv. A cone-source entry alone does not establish an exact target match or exhaustive priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 57 | 0 | 2859.5525475 | 0.001157 | 35.04 | used |
| 57 | 2 | 2871.6459482 | 0.001157 | 35.14 | used |
| 57 | 3 | 2877.6923742 | 0.001157 | 35.59 | used |
| 84 | 120 | 3585.1115748 | 0.001157 | 35.53 | used |
| 84 | 121 | 3591.1585797 | 0.001157 | 35.07 | used |
| 84 | 122 | 3597.2047197 | 0.001157 | 35.02 | used |
| 84 | 123 | 3603.2507075 | 0.001157 | 35.51 | used |
| 84 | 124 | 3609.2971671 | 0.001157 | 35.66 | used |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../gaia-geometry.json, ../alias-audit.json, historical/diff_s84.json, historical/diff_s84.png, historical/gaia.json and ../helper-audit.md. Original TESScut binary: [local path omitted] (hash in ../source-hashes.json).  Source code and all retained evidence are covered by ../SHA256SUMS.json.


Stable review key: R418. Public evidence files: [diff_s84.json](../../evidence/150969574/historical/diff_s84.json), [diff_s84.png](../../evidence/150969574/historical/diff_s84.png), [gaia.json](../../evidence/150969574/historical/gaia.json), [measurements.json](../../evidence/150969574/measurements.json), [raw-events.png](../../evidence/150969574/raw-events.png), [raw-windows.csv](../../evidence/150969574/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch01/INDEX.md). 
