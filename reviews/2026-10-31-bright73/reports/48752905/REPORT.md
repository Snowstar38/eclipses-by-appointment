# TIC 48752905: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 52 distinct eclipse events in selected sectors[33, 87]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 25 same-kind midtimes give P=1.7220909305 ±0.0000011993d, reference eclipse epoch BTJD2202.7901470, kind: Deeper repeating eclipse; even half-period cycles. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S33 deficit peak[8, 8] vs target pixel[7, 8]; deficit-target separation1.683arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.221. Capable neighbours: Gaia 2926491213995591296: 40.26 arcsec, G15.750, required fractional eclipse0.855; Gaia 2926491351434540160: 40.72 arcsec, G13.776, required fractional eclipse0.155; Gaia 2926491042196899200: 47.18 arcsec, G15.412, required fractional eclipse0.632
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths25.065/24.019/21.698ppt, with 28 stacked events. QLP selected-kind fitted median37.566ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32926491244053139712, P=1.7220692438±0.0000166135d, e=0.015301, omega=141.9089deg. Closest edge-on conjunction offset0.026703d (0.015506phase), full-SB1-covariance linear propagated Gaia uncertainty0.018956d at the measured epoch. Near-Gaia-reference projected eclipse offset0.003867d (photometric period projection allowance0.001263d). The approximate central duration4.35h vs observed median2.24h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipses establish doubled period relative to historical SAP half-period. Deeper even historical cycles alone define epoch and orbital timing; mixed historical cutout stack is not a same-kind depth measurement.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 33 | 851 | 2201.9314905 | 0.003472 | 18.650 | measured; excluded from primary fit (secondary) |
| 33 | 852 | 2202.7893974 | 0.003472 | 38.298 | used in ephemeris |
| 33 | 853 | 2203.6511250 | 0.003472 | 18.214 | measured; excluded from primary fit (secondary) |
| 33 | 854 | 2204.5118227 | 0.003472 | 41.100 | used in ephemeris |
| 33 | 855 | 2205.3726943 | 0.003472 | 20.597 | measured; excluded from primary fit (secondary) |
| 33 | 856 | 2206.2344529 | 0.003472 | 36.151 | used in ephemeris |
| 33 | 857 | 2207.0949678 | 0.003472 | 20.597 | measured; excluded from primary fit (secondary) |
| 33 | 858 | 2207.9549409 | 0.003472 | 36.463 | used in ephemeris |
| 33 | 859 | 2208.8172361 | 0.003472 | 18.513 | measured; excluded from primary fit (secondary) |
| 33 | 860 | 2209.6795282 | 0.003472 | 36.596 | used in ephemeris |
| 33 | 861 | 2210.5392888 | 0.003472 | 20.109 | measured; excluded from primary fit (secondary) |
| 33 | 862 | 2211.4000198 | 0.003472 | 36.405 | used in ephemeris |
| 33 | 863 | 2212.2629854 | 0.003472 | 19.326 | measured; excluded from primary fit (secondary) |
| 33 | 864 | 2213.1232831 | 0.003472 | 37.366 | used in ephemeris |
| 33 | 867 | 2215.7066632 | 0.003472 | 18.369 | measured; excluded from primary fit (secondary) |
| 33 | 868 | 2216.5670950 | 0.003472 | 36.338 | used in ephemeris |
| 33 | 869 | 2217.4281851 | 0.003472 | 17.666 | measured; excluded from primary fit (secondary) |
| 33 | 870 | 2218.2895162 | 0.003472 | 37.164 | used in ephemeris |
| 33 | 871 | 2219.1522256 | 0.003472 | 19.003 | measured; excluded from primary fit (secondary) |
| 33 | 872 | 2220.0111150 | 0.003472 | 35.985 | used in ephemeris |
| 33 | 873 | 2220.8722004 | 0.003472 | 17.851 | measured; excluded from primary fit (secondary) |
| 33 | 875 | 2222.5969952 | 0.003472 | 19.897 | measured; excluded from primary fit (secondary) |
| 33 | 876 | 2223.4557585 | 0.003472 | 36.141 | used in ephemeris |
| 33 | 877 | 2224.3158238 | 0.003472 | 17.879 | measured; excluded from primary fit (secondary) |
| 33 | 878 | 2225.1776472 | 0.003472 | 37.015 | used in ephemeris |
| 33 | 879 | 2226.0382563 | 0.003472 | 17.382 | measured; excluded from primary fit (secondary) |
| 33 | 880 | 2226.8993957 | 0.003472 | 37.341 | used in ephemeris |
| 87 | 2551 | 3665.7062363 | 0.001973 | 16.809 | measured; excluded from primary fit (secondary) |
| 87 | 2552 | 3666.5673389 | 0.001157 | 38.467 | used in ephemeris |
| 87 | 2553 | 3667.4268908 | 0.001375 | 18.654 | measured; excluded from primary fit (secondary) |
| 87 | 2554 | 3668.2885280 | 0.001157 | 37.217 | used in ephemeris |
| 87 | 2555 | 3669.1488583 | 0.001157 | 18.590 | measured; excluded from primary fit (secondary) |
| 87 | 2556 | 3670.0111680 | 0.001157 | 37.626 | used in ephemeris |
| 87 | 2557 | 3670.8721219 | 0.001258 | 18.570 | measured; excluded from primary fit (secondary) |
| 87 | 2558 | 3671.7337316 | 0.001157 | 38.217 | used in ephemeris |
| 87 | 2559 | 3672.5964494 | 0.001352 | 18.699 | measured; excluded from primary fit (secondary) |
| 87 | 2560 | 3673.4556201 | 0.001157 | 38.481 | used in ephemeris |
| 87 | 2561 | 3674.3174168 | 0.001491 | 17.810 | measured; excluded from primary fit (secondary) |
| 87 | 2562 | 3675.1784426 | 0.001157 | 38.433 | used in ephemeris |
| 87 | 2563 | 3676.0397348 | 0.001369 | 18.937 | measured; excluded from primary fit (secondary) |
| 87 | 2567 | 3679.4829622 | 0.002117 | 15.928 | measured; excluded from primary fit (secondary) |
| 87 | 2568 | 3680.3436343 | 0.001157 | 39.680 | used in ephemeris |
| 87 | 2569 | 3681.2060437 | 0.001391 | 17.966 | measured; excluded from primary fit (secondary) |
| 87 | 2570 | 3682.0671908 | 0.001157 | 39.473 | used in ephemeris |
| 87 | 2571 | 3682.9268450 | 0.001523 | 17.770 | measured; excluded from primary fit (secondary) |
| 87 | 2572 | 3683.7888215 | 0.001157 | 39.372 | used in ephemeris |
| 87 | 2573 | 3684.6510309 | 0.001812 | 16.907 | measured; excluded from primary fit (secondary) |
| 87 | 2574 | 3685.5104438 | 0.001157 | 38.125 | used in ephemeris |
| 87 | 2575 | 3686.3737709 | 0.001689 | 16.623 | measured; excluded from primary fit (secondary) |
| 87 | 2576 | 3687.2327691 | 0.001157 | 37.566 | used in ephemeris |
| 87 | 2577 | 3688.0944441 | 0.001906 | 18.420 | measured; excluded from primary fit (secondary) |
| 87 | 2578 | 3688.9546417 | 0.001157 | 38.316 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s33.json, historical/diff_s33.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R340. [Deciding evidence](../../evidence/48752905/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/48752905/measurements.json), [raw eclipse plots](../../evidence/48752905/raw-events.png), [raw flux windows](../../evidence/48752905/raw-windows.csv), [Gaia geometry](../../analysis/batch01/gaia-geometry.json), [independent audit](../../analysis/batch01/helper-audit.md), [difference image](../../evidence/48752905/historical/diff_s33.png).
