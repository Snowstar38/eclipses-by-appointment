# TIC 161823655: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[15, 51, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=11.6070592589 +/-0.0000733037d, reference eclipse epoch BTJD1713.7278770, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S16 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation1.147arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.153. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths64.990/64.779/63.789ppt, with 2 stacked events. QLP selected-kind fitted median67.139ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31625985493400507648, P=11.6063345473+/-0.0017583299d, e=0.067125, omega=257.8654deg. Closest edge-on conjunction offset0.085945d (0.007405phase), full-SB1-covariance linear propagated Gaia uncertainty0.256699d at the measured epoch. Near-Gaia-reference projected eclipse offset0.003328d (photometric period projection allowance0.008357d). The approximate central duration7.97h vs observed median7.18h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Five measured events over three sectors, including adjacent same-kind repeats. Raw sector85 has changing baselines but clear narrow core; depth variation alone is not established astrophysically. No capable neighbor under approximate Gaia flux-budget screen.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | 0 | 1713.7302715 | 0.010416 | 66.681 | usable; same-kind selection applies |
| 51 | 85 | 2700.3271109 | 0.003472 | 67.562 | usable; same-kind selection applies |
| 51 | 86 | 2711.9348250 | 0.003472 | 67.887 | usable; same-kind selection applies |
| 85 | 164 | 3617.2891575 | 0.001157 | 67.139 | usable; same-kind selection applies |
| 85 | 165 | 3628.8891688 | 0.001157 | 64.618 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s16.json, historical/diff_s16.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R298. [Deciding evidence](../../evidence/161823655/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
