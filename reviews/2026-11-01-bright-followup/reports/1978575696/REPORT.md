# TIC 1978575696: CONFIRMED

**Full bounded review: COMPLETE.** Physical outcome and catalogue novelty are separate; historical screening was a queue label.

1. **Raw repeated events.** 9 measured, timing-usable raw QLP SAP_FLUX events in representative sectors [15, 57, 84]. Each local trapezoid has a free center, depth, duration and baseline. Predicted windows guided inspection; unobserved or flagged windows are not negative detections. See `measurements.json`, `raw-windows.csv` and `raw-events.png`.
2. **Timing and alias.** Same-kind midpoint fit gives P = 6.9721607271 ± 0.0000141450 d and epoch BTJD 1731.62698790 (Deeper repeating eclipse; even historical half-period cycles). Even historical half-period cycles only: deeper same-kind eclipses; odd cycles show shallower secondary. Within-sector recurrences and parity are in `../alias-audit.json`. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. This is a bounded alias check, not an exhaustive period search.
3. **Pixel attribution.** The alternative cutout sector 41 deficit centroid is about 0.23 arcsec from the Gaia target coordinate; this is not a calibrated localization uncertainty. 1 Gaia neighbors within 60 arcsec are bright enough under the approximate flux-budget test to produce the selected event. Neighbor intrinsic eclipse requirements are not compared directly with blended pixel fractional losses. Source: `[local path omitted] 5\made\sb1-scale\diffimg\1978575696\diff_s41.json`.
4. **Alternative reduction.** Separately extracted, target-centered TESScut S41 aperture photometry recovers 8 stacked events at 3x3 depth 20.84 ppt, versus median selected raw QLP fit depth 51.39 ppt. TESScut S41 and representative QLP sectors [15, 57, 84] are separate TESS observing occasions on the same instrument; their photons are distinct. Aperture dilution limits depth comparison.
5. **Gaia geometry.** DR3 source 2185260393630495488: orbital P = 6.973173120 d, e = 0.0210. Closest edge-on conjunction offset at the measured epoch is -0.1824 d (-0.0262 phase); linear full-NSS-covariance timing scale 0.1588 d. Approximate central duration 10.30 h versus measured median 4.92 h. This is a plausibility check using assumed TIC radius/minimum-mass companion, not a fitted eclipse model or sigma veto.

**Deciding interpretation and limitation:** Alternating raw depths identify the historical 3.486-day clock as half the orbital eclipse cycle. Deeper even cycles yield a measured 6.97216-day same-kind period, consistent with Gaia; S41 difference image favors the target. A capable G14.97 source at 23.9 arcsec is not favored by the target-centered deficit.

**Next check:** Optional resolved photometry and secondary-eclipse characterization.

Catalogue novelty: central seven-group coverage is in `../../shared-catalogues/coverage-matrix.csv`. A cone-source entry alone does not settle exact counterpart identity or priority.

| Sector | Historical cycle | Measured midpoint BTJD | Input timing error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 15 | 4 | 1731.6237758 | 0.010417 | 38.96 |
| 57 | 326 | 2854.1448650 | 0.001798 | 50.18 |
| 57 | 328 | 2861.1157163 | 0.001157 | 51.39 |
| 57 | 330 | 2868.0906737 | 0.004100 | 52.16 |
| 57 | 332 | 2875.0627901 | 0.001210 | 56.85 |
| 84 | 536 | 3586.2278709 | 0.003264 | 43.05 |
| 84 | 538 | 3593.1905433 | 0.001658 | 55.39 |
| 84 | 540 | 3600.1703801 | 0.003626 | 41.44 |
| 84 | 542 | 3607.1385708 | 0.001179 | 53.90 |

Evidence: `measurements.json`, `raw-windows.csv`, `raw-events.png`, `../alias-audit.json`, `../gaia-geometry.json`, `../download-receipts.json`, `[local path omitted] 5\made\sb1-scale\diffimg\1978575696\diff_s41.json`, its PNG and Gaia-neighbor table; source and artifact hashes are in `../SHA256SUMS.json`.


Stable review key: R518. Public evidence files: [measurements.json](../../evidence/1978575696/measurements.json), [raw-events.png](../../evidence/1978575696/raw-events.png), [raw-windows.csv](../../evidence/1978575696/raw-windows.csv). Batch-level audits and helper artifacts are linked in the batch index. Source and export hashes are in the manifest. FITS are not redistributed; source receipts retain hashes and acquisition records. Scripts are archival and may require original paths and external data.

[Batch evidence and audit index](../../analysis/continuation/batch01/INDEX.md). [1978575696.png](../../analysis/continuation/batch01/helper/1978575696.png)
