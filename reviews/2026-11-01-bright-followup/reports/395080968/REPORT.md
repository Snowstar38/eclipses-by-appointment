# TIC 395080968: PROBABLE

Full bounded review: **COMPLETE**. Physical outcome and catalogue novelty are separate. This report reviews the frozen batch04 target; historical screening is not an admission verdict.

1. **Raw events.** Quality-zero QLP SAP_FLUX shows 17 timing-selected measured eclipses in sectors [16, 76, 84]. Local trapezoid fits allow free centers and baseline. Predicted windows are search guides only; flagged or sparsely sampled windows are not null detections. Numeric windows and the raw plot retain the evidence.
2. **Timing and aliases.** Measured same-kind centers give P=3.6265035299 d, fit error=0.0000164528 d, epoch BTJD 1740.3942050 (Deeper repeating eclipse; historical half-period parity 0). There are 12 consecutive within-sector same-kind cycle pairs. The inventory period was 3.62651 d and the historical SAP search branch was 1.8132553250 d. Deeper parity 0 of historical half-period cycles; consecutive same-kind events have orbital-cycle count one. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The fit error is not calibrated total uncertainty. This bounded alias check is not an exhaustive blind period search.
3. **Pixel attribution: unresolved at TESS resolution.** Historical S56 TESScut deficit core is 4.65 arcsec from the target coordinate; peak pixel [7, 7] and target pixel [7, 7]. Fractional PSF model residual is 0.982, not a localization uncertainty. Capable Gaia neighbors: 6.3 arcsec, G=16.71, intrinsic-loss requirement ~0.75; 11.9 arcsec, G=16.91, intrinsic-loss requirement ~0.91; 35.7 arcsec, G=16.98, intrinsic-loss requirement ~0.96; 38.5 arcsec, G=15.37, intrinsic-loss requirement ~0.23; 40.1 arcsec, G=16.38, intrinsic-loss requirement ~0.56; 5 further capable sources in the 60 arcsec list. The full list and flux-budget calculation are in historical/diff_s56.json; the original cutout and stacked image are retained and hashed.
4. **Alternative reduction.** A target-centered, background-subtracted TESScut extraction gives 1x1/3x3/5x5 stacked depths 5.29/2.22/0.65 ppt from 14 selected windows. Median selected QLP raw fit depth is 18.54 ppt. Aperture dilution, event-kind mixing and model residuals limit direct depth comparisons. QLP and TESScut products for the same sector share photons; distinct sectors are separate observing occasions with the same instrument.
5. **Gaia orbit.** The matched DR3 NSS source 2171489770715391616 has P=3.6264741663 d and e=0.06738. Closest edge-on conjunction differs from the measured epoch by -0.00711 in phase (-0.02580 d); linear propagation of the source-specific full SB1 covariance gives 0.07572 d as a descriptive timing scale. The rough central-duration estimate is 8.38 h versus trapezoid median 3.11 h; these assume a TIC radius and minimum-mass main-sequence companion and are not a full geometry fit or a sigma gate.

**Deciding interpretation and limitation.** Alternating depths support the 3.6265 d orbital period, but raw fits scatter strongly and residuals reach 75 min. The S56 alternative aperture stack mixes eclipse kinds; its depth is not an intrinsic primary depth. Capable neighbors at 6.3 and 11.9 arcsec share the TESS image core and the image-model residual is 0.982, so source attribution and precision ephemeris remain limited.

**Next check.** Resolved eclipse photometry or multi-source PRF localization for source attribution.

Catalogue novelty is evaluated centrally against seven scoped groups in ../../shared-catalogues/coverage-matrix.csv. This physical review does not assert exhaustive literature priority.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Input timing error d | Fitted depth ppt | Timing status |
|---|---:|---:|---:|---:|---|
| 16 | 0 | 1740.4068340 | 0.010417 | 17.23 | used |
| 16 | 1 | 1742.1753092 | 0.010417 | 15.29 | other eclipse kind |
| 16 | 2 | 1744.0135012 | 0.010417 | 21.36 | used |
| 16 | 7 | 1753.0596536 | 0.019758 | 5.08 | other eclipse kind |
| 16 | 8 | 1754.8942611 | 0.010417 | 21.08 | used |
| 16 | 9 | 1756.6989109 | 0.010417 | 9.32 | other eclipse kind |
| 16 | 11 | 1760.3374561 | 0.016615 | 7.57 | other eclipse kind |
| 76 | 898 | 3368.7464702 | 0.014812 | 16.95 | used |
| 76 | 899 | 3370.4767960 | 0.003860 | 7.00 | other eclipse kind |
| 76 | 900 | 3372.3198869 | 0.010680 | 18.60 | used |
| 76 | 902 | 3375.9517373 | 0.005173 | 22.92 | used |
| 76 | 903 | 3377.7228961 | 0.008759 | 16.70 | other eclipse kind |
| 76 | 904 | 3379.5664159 | 0.005774 | 30.89 | used |
| 76 | 906 | 3383.2096794 | 0.005946 | 20.55 | used |
| 76 | 907 | 3385.0113163 | 0.007454 | 8.18 | other eclipse kind |
| 76 | 908 | 3386.8231146 | 0.004738 | 17.53 | used |
| 76 | 909 | 3388.6222925 | 0.003181 | 54.45 | other eclipse kind |
| 76 | 910 | 3390.4504345 | 0.004672 | 14.95 | used |
| 76 | 911 | 3392.2404815 | 0.004192 | 46.66 | other eclipse kind |
| 76 | 912 | 3394.0765956 | 0.005304 | 26.55 | used |
| 84 | 1018 | 3586.2803727 | 0.004857 | 20.02 | used |
| 84 | 1019 | 3588.0793575 | 0.007339 | 11.74 | other eclipse kind |
| 84 | 1020 | 3589.9091733 | 0.004168 | 18.54 | used |
| 84 | 1021 | 3591.7124273 | 0.008708 | 11.84 | other eclipse kind |
| 84 | 1022 | 3593.5427983 | 0.004557 | 16.65 | used |
| 84 | 1023 | 3595.3238697 | 0.010836 | 10.53 | other eclipse kind |
| 84 | 1025 | 3598.9485479 | 0.005482 | 15.84 | other eclipse kind |
| 84 | 1026 | 3600.7852493 | 0.003297 | 15.68 | used |
| 84 | 1027 | 3602.5784254 | 0.006899 | 9.21 | other eclipse kind |
| 84 | 1028 | 3604.4200775 | 0.003981 | 18.16 | used |
| 84 | 1029 | 3606.2246957 | 0.008835 | 8.32 | other eclipse kind |
| 84 | 1030 | 3608.0478675 | 0.003847 | 16.65 | used |
| 84 | 1031 | 3609.8369787 | 0.007819 | 8.31 | other eclipse kind |

Evidence: measurements.json, raw-windows.csv, raw-events.png, ../download-receipts.json, ../alias-audit.json, ../gaia-geometry.json, historical/diff_s56.json, historical/diff_s56.png, historical/gaia.json, original TESScut [local path omitted] and ../helper-audit.md. The original cutout and source files are SHA-256 recorded in ../source-hashes.json and ../SHA256SUMS.json.


Stable review key: R449. Public evidence files: [diff_s56.json](../../evidence/395080968/historical/diff_s56.json), [diff_s56.png](../../evidence/395080968/historical/diff_s56.png), [gaia.json](../../evidence/395080968/historical/gaia.json), [measurements.json](../../evidence/395080968/measurements.json), [raw-events.png](../../evidence/395080968/raw-events.png), [raw-windows.csv](../../evidence/395080968/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/original/batch04/INDEX.md). 
