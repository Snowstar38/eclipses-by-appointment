# TIC 143467555: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 22 distinct eclipse events in selected sectors[19, 59, 86]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 13 same-kind midtimes give P=4.2735185639 +/-0.0000041911d, reference eclipse epoch BTJD1820.1507383, kind: Deeper eclipse; odd historical half-period cycles. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S59 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation4.348arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.339. Capable neighbours: Gaia 177237602207452544: 30.18 arcsec, G13.098, required fractional eclipse0.536
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths105.058/86.319/73.841ppt, with 11 stacked events. QLP selected-kind fitted median162.430ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3177237602207451008, P=4.2735828118+/-0.0002613483d, e=0.016118, omega=94.3267deg. Closest edge-on conjunction offset-0.015015d (-0.003513phase), full-SB1-covariance linear propagated Gaia uncertainty0.072119d at the measured epoch. Near-Gaia-reference projected eclipse offset0.006508d (photometric period projection allowance0.001404d). The approximate central duration4.96h vs observed median3.70h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating depths persist across S19/59/86: odd deeper events about145/167/162ppt versus even76/82/84ppt. Only13 odd deeper measured events define4.27351856d orbital period; half-period aliases are rejected by persistent parity morphology. Target deficit0.207pixel; mixed-kind historical difference stack still locates the signal.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 19 | 1 | 1820.1515257 | 0.010417 | 145.111 | used in ephemeris |
| 19 | 3 | 1824.4234335 | 0.010417 | 144.987 | used in ephemeris |
| 19 | 4 | 1826.5613202 | 0.010417 | 81.624 | measured; excluded secondary event |
| 19 | 6 | 1830.8371340 | 0.010417 | 70.159 | measured; excluded secondary event |
| 19 | 7 | 1832.9731222 | 0.010417 | 156.774 | used in ephemeris |
| 59 | 512 | 2912.0338269 | 0.001157 | 84.175 | measured; excluded secondary event |
| 59 | 513 | 2914.1715086 | 0.001157 | 166.425 | used in ephemeris |
| 59 | 514 | 2916.3075708 | 0.001157 | 81.877 | measured; excluded secondary event |
| 59 | 515 | 2918.4450150 | 0.001157 | 167.197 | used in ephemeris |
| 59 | 516 | 2920.5820861 | 0.001157 | 78.611 | measured; excluded secondary event |
| 59 | 519 | 2926.9921263 | 0.001157 | 167.430 | used in ephemeris |
| 59 | 520 | 2929.1290645 | 0.001157 | 82.458 | measured; excluded secondary event |
| 59 | 521 | 2931.2656587 | 0.001157 | 167.260 | used in ephemeris |
| 59 | 522 | 2933.4021701 | 0.001157 | 85.244 | measured; excluded secondary event |
| 59 | 523 | 2935.5388296 | 0.001157 | 168.958 | used in ephemeris |
| 86 | 853 | 3640.6693219 | 0.001157 | 161.944 | used in ephemeris |
| 86 | 855 | 3644.9431665 | 0.001157 | 162.051 | used in ephemeris |
| 86 | 856 | 3647.0791881 | 0.001157 | 82.834 | measured; excluded secondary event |
| 86 | 857 | 3649.2168370 | 0.001157 | 162.340 | used in ephemeris |
| 86 | 859 | 3653.4906809 | 0.001157 | 163.215 | used in ephemeris |
| 86 | 862 | 3659.9001930 | 0.001157 | 84.565 | measured; excluded secondary event |
| 86 | 863 | 3662.0369654 | 0.001157 | 162.430 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s59.json, historical/diff_s59.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R405. [Deciding evidence](../../evidence/143467555/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/143467555/measurements.json), [raw eclipse plots](../../evidence/143467555/raw-events.png), [raw flux windows](../../evidence/143467555/raw-windows.csv), [Gaia geometry](../../analysis/batch07/gaia-geometry.json), [independent audit](../../analysis/batch07/helper-audit.md), [difference image](../../evidence/143467555/historical/diff_s59.png).
