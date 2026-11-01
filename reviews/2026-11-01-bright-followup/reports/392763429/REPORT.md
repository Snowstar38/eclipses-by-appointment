# TIC 392763429: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 24 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [13, 94, 103]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 2.4655285743 ± 0.0000030212 d and epoch BTJD 1658.86217686 (Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established). All timing-usable historical photometric cycles; no persistent unequal alternating pattern seen in representative events. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 13 deficit centroid is about 1.61 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 0 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\392763429\diff_s13.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S13 aperture photometry recovers 10 stacked events at 3x3 depth 73.91 ppt, versus median selected raw QLP fit depth 65.90 ppt. TESScut S13 and representative QLP S13 are reductions of the same TESS observations and share photons. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 6355496414811552128: orbital P = 2.465425911 d, e = 0.0483. Closest edge-on conjunction offset at the measured epoch is +0.0286 d (+0.0116 phase); linear full-NSS-covariance timing scale 0.0496 d. Approximate central duration 4.20 h versus measured median 3.67 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** S13/94/103 raw eclipses follow the same clock. A brief S103 depth doubling affects consecutive cycles, not stable odd/even alternation; its cause is unresolved. S13 difference image is target-centered with no capable Gaia neighbor within 60 arcsec.

**Next check:** Investigate the S103 depth discontinuity with aperture diagnostics.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 13 | 1 | 1658.8586557 | 0.010417 | 66.45 |
| 13 | 2 | 1661.3256533 | 0.010417 | 68.58 |
| 13 | 3 | 1663.7890780 | 0.010417 | 68.77 |
| 13 | 4 | 1666.2545928 | 0.010417 | 67.42 |
| 13 | 6 | 1671.1869404 | 0.010417 | 70.00 |
| 13 | 7 | 1673.6510554 | 0.010417 | 67.98 |
| 13 | 9 | 1678.5845727 | 0.010417 | 67.21 |
| 13 | 10 | 1681.0473863 | 0.010417 | 66.91 |
| 94 | 893 | 3858.1137926 | 0.001157 | 63.36 |
| 94 | 894 | 3860.5795276 | 0.001157 | 62.74 |
| 94 | 895 | 3863.0451407 | 0.001157 | 63.04 |
| 94 | 896 | 3865.5109645 | 0.001157 | 61.81 |
| 94 | 899 | 3872.9065859 | 0.001157 | 63.20 |
| 94 | 900 | 3875.3731737 | 0.001157 | 63.43 |
| 94 | 901 | 3877.8385592 | 0.001157 | 63.30 |
| 94 | 902 | 3880.3033415 | 0.001157 | 62.84 |
| 103 | 1013 | 4153.9778478 | 0.001157 | 125.72 |
| 103 | 1014 | 4156.4430929 | 0.001157 | 128.19 |
| 103 | 1016 | 4161.3737360 | 0.001157 | 128.82 |
| 103 | 1017 | 4163.8390246 | 0.001157 | 127.06 |
| 103 | 1018 | 4166.3038238 | 0.001157 | 62.23 |
| 103 | 1019 | 4168.7696539 | 0.001157 | 65.36 |
| 103 | 1021 | 4173.7004953 | 0.001157 | 65.11 |
| 103 | 1022 | 4176.1657093 | 0.001157 | 64.69 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\392763429\diff_s13.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R517. Public evidence files: [measurements.json](../../evidence/392763429/measurements.json), [raw-events.png](../../evidence/392763429/raw-events.png), [raw-windows.csv](../../evidence/392763429/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [392763429.png](../../analysis/continuation/batch01/helper/392763429.png)
