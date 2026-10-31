# TIC 35635884: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[33, 87]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=5.5005487862 +/-0.0000107720d, reference eclipse epoch BTJD2203.8207426, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Deciding S33 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.630arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.454. Capable neighbours: Gaia 2946315752238013696: 47.20 arcsec, G13.768, required fractional eclipse0.566, pixel fractional loss0.009677394392040716
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths116.027/108.058/81.954ppt, with 4 stacked events. QLP selected-kind fitted median117.741ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32946315369981174784, P=5.5005719282+/-0.0003916036d, e=0.166765, omega=78.6462deg. Closest edge-on conjunction offset-0.008812d (-0.001602phase), full-SB1-covariance linear propagated Gaia uncertainty0.131948d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.001175d (photometric period projection allowance0.003555d). The approximate central duration4.36h vs observed median3.34h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Eight repeated raw eclipses across three sectors; capable neighbor47.20arcsec is distinct from deficit core. Raw114-129ppt vs cutout116/108/82ppt show aperture and sector dilution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 33 | 133 | 2203.8209106 | 0.003472 | 120.424 | usable; same-kind selection applies |
| 33 | 134 | 2209.3211757 | 0.003472 | 120.554 | usable; same-kind selection applies |
| 33 | 136 | 2220.3222756 | 0.003472 | 117.370 | usable; same-kind selection applies |
| 33 | 137 | 2225.8228566 | 0.003472 | 120.238 | usable; same-kind selection applies |
| 87 | 399 | 3666.9680740 | 0.001157 | 113.143 | usable; same-kind selection applies |
| 87 | 400 | 3672.4681274 | 0.001157 | 114.903 | usable; same-kind selection applies |
| 87 | 402 | 3683.4645546 | 0.001157 | 118.111 | usable; same-kind selection applies |
| 87 | 403 | 3688.9705292 | 0.001157 | 114.055 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s33.json, historical/diff_s33.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] For TIC407207285 the deciding revised cutout is revised-cutout/diff_revised-long-window.json and .png; historical extraction remains for comparison. Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R266. [Deciding evidence](../../evidence/35635884/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
