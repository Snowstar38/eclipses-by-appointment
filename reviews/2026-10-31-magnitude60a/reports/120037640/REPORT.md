# TIC 120037640: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[93, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=3.6982624070 ±0.0000073790d, fitted ephemeris intercept at earliest retained cycle BTJD3833.6806832, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S66 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.736arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.697. Capable neighbours: Gaia 6651016827935020032: 34.86 arcsec, G14.449, required fractional eclipse0.290, pixel fractional loss0.016812257550119572; Gaia 6651016961075479552: 52.29 arcsec, G13.179, required fractional eclipse0.106, pixel fractional loss0.004252985656066122
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths22.768/22.273/20.123ppt, with 6 stacked events. QLP selected-kind fitted median24.000ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36651016862294758784, P=3.6985144102±0.0001310459d, e=0.061638, omega=94.3358deg. Closest edge-on conjunction offset-0.189153d (-0.051143phase), full-SB1-covariance linear propagated Gaia uncertainty0.110953d at the measured epoch. Near-Gaia-reference projected eclipse offset0.045461d (photometric period projection allowance0.006870d). The approximate central duration6.02h vs observed median3.18h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Actual-epoch Gaia offset -0.189d (phase -0.051) exceeds historical phase screen; near Gaia reference projected offset is +0.045d. Gaia period uncertainty accumulates over baseline. Low eccentricity0.062 and recurrence agreement support association without arbitrary sigma veto. Capable neighbors are34.9arcsec or farther and1.72pixel or farther from deficit vs0.178pixel target.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 93 | 588 | 3833.6805823 | 0.001157 | 24.254 | usable; same-kind selection applies |
| 93 | 589 | 3837.3767157 | 0.001157 | 27.400 | usable; same-kind selection applies |
| 93 | 590 | 3841.0781928 | 0.001157 | 24.054 | usable; same-kind selection applies |
| 93 | 591 | 3844.7766053 | 0.001157 | 24.000 | usable; same-kind selection applies |
| 93 | 592 | 3848.4751515 | 0.001157 | 25.596 | usable; same-kind selection applies |
| 93 | 593 | 3852.1707996 | 0.001157 | 24.088 | usable; same-kind selection applies |
| 104 | 682 | 4181.3174585 | 0.001157 | 21.477 | usable; same-kind selection applies |
| 104 | 684 | 4188.7144386 | 0.001157 | 21.612 | usable; same-kind selection applies |
| 104 | 686 | 4196.1096105 | 0.001157 | 21.936 | usable; same-kind selection applies |
| 104 | 687 | 4199.8089998 | 0.001157 | 21.263 | usable; same-kind selection applies |
| 104 | 688 | 4203.5066893 | 0.001157 | 22.784 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s66.json, historical/diff_s66.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R230. [Deciding evidence](../../evidence/120037640/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
