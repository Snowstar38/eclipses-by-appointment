# TIC 76450330: CONFIRMED

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 17 timing-selected measured eclipses in sectors [93, 104]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=2.1332813704 d, fit error=0.0000038241 d, epoch BTJD 3830.9530096 (Deeper repeating eclipse; historical half-period parity 1). There are 10 consecutive within-sector same-kind cycle pairs. The inventory period was 2.13331 d and the historical SAP search branch was 1.0666548545 d. Deeper parity 1 of historical half-period cycles; consecutive same-kind events have orbital-cycle count one. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: favors target at TESS resolution.** Historical S66 TESScut deficit core is 4.40 arcsec from the target coordinate; peak pixel [7, 7] and target pixel [7, 7]. Fractional PSF model residual is 0.952, not a localization uncertainty. Capable Gaia neighbors: 45.6 arcsec, G=13.73, intrinsic-loss requirement ~0.13; 56.6 arcsec, G=15.96, intrinsic-loss requirement ~0.83. The full list and flux-budget calculation are in historical/diff_s66.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 23.47/17.15/7.81 ppt from 24 selected windows. Median selected QLP raw fit depth is 31.53 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 5918304478211801728 has P=2.1333285880 d and e=0.04973. Closest edge-on conjunction differs from the measured epoch by -0.03250 in phase (-0.06933 d); linear propagation of the source-specific full SB1 covariance gives 0.07043 d as a descriptive timing scale. The rough central-duration estimate is 6.24 h versus trapezoid median 3.47 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Strong alternating depths establish the 2.1333 d orbital cycle; the historical SAP 1.06665 d branch is the half-period. The deeper parity is fitted for the reported epoch.

**Next check.** Optional resolved photometry and spectroscopy for precision binary parameters; no missing bounded admission check.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 93 | 2039 | 3830.9503554 | 0.001244 | 30.84 | used |
| 93 | 2040 | 3832.0188593 | 0.001403 | 23.02 | other eclipse kind |
| 93 | 2041 | 3833.0874435 | 0.001157 | 38.33 | used |
| 93 | 2042 | 3834.1488187 | 0.001425 | 25.77 | other eclipse kind |
| 93 | 2043 | 3835.2217774 | 0.001351 | 32.71 | used |
| 93 | 2045 | 3837.3508688 | 0.001157 | 34.70 | used |
| 93 | 2046 | 3838.4181594 | 0.001330 | 25.12 | other eclipse kind |
| 93 | 2047 | 3839.4864046 | 0.001157 | 31.13 | used |
| 93 | 2048 | 3840.5553168 | 0.001157 | 22.95 | other eclipse kind |
| 93 | 2051 | 3843.7553337 | 0.001602 | 29.37 | used |
| 93 | 2052 | 3844.8200618 | 0.001520 | 24.12 | other eclipse kind |
| 93 | 2053 | 3845.8862230 | 0.001157 | 33.14 | used |
| 93 | 2054 | 3846.9531815 | 0.001265 | 23.20 | other eclipse kind |
| 93 | 2055 | 3848.0204345 | 0.001252 | 30.82 | used |
| 93 | 2056 | 3849.0899565 | 0.002583 | 19.85 | other eclipse kind |
| 93 | 2058 | 3851.2177570 | 0.001737 | 23.20 | other eclipse kind |
| 93 | 2059 | 3852.2846859 | 0.001157 | 31.88 | used |
| 93 | 2060 | 3853.3545826 | 0.001509 | 23.26 | other eclipse kind |
| 93 | 2061 | 3854.4187693 | 0.001342 | 32.23 | used |
| 104 | 2366 | 4179.7433388 | 0.002615 | 24.03 | other eclipse kind |
| 104 | 2367 | 4180.8106391 | 0.001157 | 31.56 | used |
| 104 | 2368 | 4181.8797986 | 0.001157 | 23.18 | other eclipse kind |
| 104 | 2369 | 4182.9451359 | 0.001157 | 31.53 | used |
| 104 | 2370 | 4184.0114345 | 0.001157 | 22.49 | other eclipse kind |
| 104 | 2372 | 4186.1448417 | 0.001169 | 22.25 | other eclipse kind |
| 104 | 2373 | 4187.2111476 | 0.001157 | 31.41 | used |
| 104 | 2374 | 4188.2772217 | 0.001360 | 23.53 | other eclipse kind |
| 104 | 2375 | 4189.3448112 | 0.001157 | 30.98 | used |
| 104 | 2376 | 4190.4097993 | 0.001374 | 22.70 | other eclipse kind |
| 104 | 2380 | 4194.6770309 | 0.001425 | 24.09 | other eclipse kind |
| 104 | 2381 | 4195.7440795 | 0.001157 | 32.82 | used |
| 104 | 2382 | 4196.8101891 | 0.001319 | 25.07 | other eclipse kind |
| 104 | 2384 | 4198.9436754 | 0.001157 | 23.39 | other eclipse kind |
| 104 | 2385 | 4200.0099345 | 0.001157 | 31.36 | used |
| 104 | 2386 | 4201.0779941 | 0.001157 | 22.29 | other eclipse kind |
| 104 | 2387 | 4202.1439058 | 0.001157 | 30.93 | used |
| 104 | 2388 | 4203.2101329 | 0.001157 | 23.48 | other eclipse kind |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s66.json, historical/diff_s66.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R441. Public evidence files: [diff_s66.json](../../evidence/76450330/historical/diff_s66.json), [diff_s66.png](../../evidence/76450330/historical/diff_s66.png), [gaia.json](../../evidence/76450330/historical/gaia.json), [measurements.json](../../evidence/76450330/measurements.json), [raw-events.png](../../evidence/76450330/raw-events.png), [raw-windows.csv](../../evidence/76450330/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
