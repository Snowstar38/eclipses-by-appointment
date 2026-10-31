# TIC 238857132: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 21 distinct eclipse events in selected sectors[19, 59, 86]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=4.1681777841 ±0.0000043833d, reference eclipse epoch BTJD1819.0960960, kind: Deeper primary (even half-period cycles). Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S59 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation1.364arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.500. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths102.438/99.296/95.399ppt, with 12 stacked events. QLP selected-kind fitted median145.901ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3179205929877639680, P=4.1679867378±0.0002603474d, e=0.021003, omega=258.5500deg. Closest edge-on conjunction offset0.077346d (0.018557phase), full-SB1-covariance linear propagated Gaia uncertainty0.096978d at the measured epoch. Near-Gaia-reference projected eclipse offset0.011818d (photometric period projection allowance0.001503d). The approximate central duration7.74h vs observed median5.00h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses approximately75/147ppt establish doubled orbital period. Even half-period cycles are deeper primaries and alone define ephemeris. Historical cutout mixes eclipse kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 19 | 0 | 1819.0960855 | 0.010417 | 144.979 | usable; same-kind selection applies |
| 19 | 3 | 1825.3565265 | 0.010417 | 66.421 | usable; same-kind selection applies |
| 19 | 4 | 1827.4361486 | 0.010417 | 130.797 | usable; same-kind selection applies |
| 19 | 9 | 1837.8573728 | 0.010417 | 62.025 | usable; same-kind selection applies |
| 59 | 525 | 2913.2424422 | 0.001157 | 78.780 | usable; same-kind selection applies |
| 59 | 526 | 2915.3273027 | 0.001157 | 145.590 | usable; same-kind selection applies |
| 59 | 527 | 2917.4112655 | 0.001157 | 74.574 | usable; same-kind selection applies |
| 59 | 528 | 2919.4950535 | 0.001157 | 146.996 | usable; same-kind selection applies |
| 59 | 529 | 2921.5794780 | 0.001157 | 73.944 | usable; same-kind selection applies |
| 59 | 531 | 2925.7483054 | 0.001157 | 76.121 | usable; same-kind selection applies |
| 59 | 532 | 2927.8315850 | 0.001157 | 148.491 | usable; same-kind selection applies |
| 59 | 533 | 2929.9158391 | 0.001157 | 75.967 | usable; same-kind selection applies |
| 59 | 534 | 2931.9991674 | 0.001157 | 148.551 | usable; same-kind selection applies |
| 59 | 535 | 2934.0837257 | 0.001157 | 75.886 | usable; same-kind selection applies |
| 59 | 536 | 2936.1673412 | 0.001157 | 147.335 | usable; same-kind selection applies |
| 86 | 874 | 3640.5897800 | 0.001157 | 146.991 | usable; same-kind selection applies |
| 86 | 876 | 3644.7581530 | 0.001157 | 145.901 | usable; same-kind selection applies |
| 86 | 877 | 3646.8426710 | 0.001157 | 75.747 | usable; same-kind selection applies |
| 86 | 878 | 3648.9258390 | 0.001157 | 144.066 | usable; same-kind selection applies |
| 86 | 883 | 3659.3478677 | 0.001157 | 73.359 | usable; same-kind selection applies |
| 86 | 884 | 3661.4308826 | 0.001157 | 145.028 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s59.json, historical/diff_s59.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R222. [Deciding evidence](../../evidence/238857132/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
