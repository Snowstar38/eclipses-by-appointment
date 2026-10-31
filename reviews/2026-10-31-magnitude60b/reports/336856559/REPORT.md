# TIC 336856559: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 13 distinct eclipse events in selected sectors[66, 103]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 13 same-kind midtimes give P=2.9097059074 ±0.0000018140d, reference eclipse epoch BTJD3098.6256467, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S103 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation4.441arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.937. Capable neighbours: Gaia 5969863533437354240: 45.91 arcsec, G9.994, required fractional eclipse0.170
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths99.668/54.231/27.297ppt, with 8 stacked events. QLP selected-kind fitted median124.260ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35969863529078398848, P=2.9097381651±0.0001997714d, e=0.101456, omega=131.0731deg. Closest edge-on conjunction offset-0.035368d (-0.012155phase), full-SB1-covariance linear propagated Gaia uncertainty0.195472d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.005336d (photometric period projection allowance0.001689d). The approximate central duration4.67h vs observed median3.37h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Strong aperture dilution: cutout1/3/5 depths99.7/54.2/27.3ppt; QLP sectors66/103 differ. Deficit0.211pixel from target, bright capable neighbor2.26pixels from deficit favors target. Depths are pipeline/aperture dependent, not intrinsic.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 66 | 504 | 3098.6262889 | 0.001157 | 149.901 | usable; same-kind selection applies |
| 66 | 505 | 3101.5347270 | 0.001157 | 152.075 | usable; same-kind selection applies |
| 66 | 506 | 3104.4448759 | 0.001157 | 149.438 | usable; same-kind selection applies |
| 66 | 509 | 3113.1741657 | 0.001157 | 149.144 | usable; same-kind selection applies |
| 66 | 510 | 3116.0840417 | 0.001157 | 151.414 | usable; same-kind selection applies |
| 103 | 867 | 4154.8493451 | 0.001157 | 122.891 | usable; same-kind selection applies |
| 103 | 868 | 4157.7592234 | 0.001157 | 123.057 | usable; same-kind selection applies |
| 103 | 869 | 4160.6686202 | 0.001157 | 117.136 | usable; same-kind selection applies |
| 103 | 870 | 4163.5779190 | 0.001157 | 131.159 | usable; same-kind selection applies |
| 103 | 871 | 4166.4872588 | 0.001157 | 124.260 | usable; same-kind selection applies |
| 103 | 872 | 4169.3972923 | 0.001157 | 123.971 | usable; same-kind selection applies |
| 103 | 873 | 4172.3068993 | 0.001157 | 115.232 | usable; same-kind selection applies |
| 103 | 874 | 4175.2163536 | 0.001157 | 122.496 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s103.json, historical/diff_s103.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R277. [Deciding evidence](../../evidence/336856559/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
