# TIC 409935170: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 16 distinct eclipse events in selected sectors[13, 94, 103]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=8.7039814271 ±0.0000183962d, reference eclipse epoch BTJD1655.8339615, kind: Deeper repeating eclipse; even half-period cycles. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S94 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.121arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.184. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths129.075/126.963/119.540ppt, with 6 stacked events. QLP selected-kind fitted median135.909ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36422380841001518848, P=8.7056187340±0.0007330769d, e=0.021485, omega=165.0639deg. Closest edge-on conjunction offset-0.194825d (-0.022379phase), full-SB1-covariance linear propagated Gaia uncertainty0.106030d at the measured epoch. Near-Gaia-reference projected eclipse offset0.044222d (photometric period projection allowance0.002686d). The approximate central duration9.09h vs observed median7.60h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating depths within sectors establish doubled orbital period even though across-sector pooled depths overlap. Even half-period cycles alone define deeper-eclipse timing. Historical cutout mixes kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 13 | 0 | 1655.8300360 | 0.010417 | 145.432 | usable; same-kind selection applies |
| 13 | 1 | 1660.0610314 | 0.010417 | 121.233 | usable; same-kind selection applies |
| 13 | 2 | 1664.5343687 | 0.010417 | 160.466 | usable; same-kind selection applies |
| 13 | 4 | 1673.2354553 | 0.010417 | 163.291 | usable; same-kind selection applies |
| 13 | 5 | 1677.4663082 | 0.010417 | 134.616 | usable; same-kind selection applies |
| 94 | 506 | 3857.9434991 | 0.001157 | 134.902 | usable; same-kind selection applies |
| 94 | 507 | 3862.1728628 | 0.001157 | 117.366 | usable; same-kind selection applies |
| 94 | 508 | 3866.6445909 | 0.001157 | 136.915 | usable; same-kind selection applies |
| 94 | 509 | 3870.8770563 | 0.001157 | 117.821 | usable; same-kind selection applies |
| 94 | 510 | 3875.3490234 | 0.001157 | 134.251 | usable; same-kind selection applies |
| 94 | 511 | 3879.5810360 | 0.001157 | 114.162 | usable; same-kind selection applies |
| 103 | 574 | 4153.8766805 | 0.001157 | 127.455 | usable; same-kind selection applies |
| 103 | 575 | 4158.1078217 | 0.001157 | 108.562 | usable; same-kind selection applies |
| 103 | 576 | 4162.5793538 | 0.001157 | 129.196 | usable; same-kind selection applies |
| 103 | 577 | 4166.8113257 | 0.001157 | 108.638 | usable; same-kind selection applies |
| 103 | 579 | 4175.5148085 | 0.001157 | 111.024 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s94.json, historical/diff_s94.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R285. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/409935170) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
