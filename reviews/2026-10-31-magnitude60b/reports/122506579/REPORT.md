# TIC 122506579: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors[97]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=6.9345089138 ±0.0002217831d, reference eclipse epoch BTJD3939.4721930, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S97 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation0.972arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.187. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths14.430/13.648/13.226ppt, with 7 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median12.939ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35067148750205866240, P=6.9335988748±0.0005002026d, e=0.004443, omega=329.5125deg. Closest edge-on conjunction offset0.607534d (0.087622phase), full-SB1-covariance linear propagated Gaia uncertainty0.259233d at the measured epoch. Near-Gaia-reference projected eclipse offset0.141594d (photometric period projection allowance0.113553d). The approximate central duration5.63h vs observed median2.26h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated shallow eclipses in sector97. Gaia orbit is nearly circular (e0.00444), so periastron/omega parameterization is weak; measured eclipse falls0.60753d (phase0.08762) from nearer nominal edge-on conjunction versus full-covariance linear allowance0.25923d. Other conjunction is2.87617d away. Near-reference projected offset0.14159d with photometric period projection allowance0.11355d; photometric P differs from Gaia by0.000910d versus Gaia error0.000500d. Retain mild orbit/timing tension, no arbitrary sigma veto or forced alias. Approximate central duration5.63h vs observed2.26h permits grazing/noncentral eclipse. Updated orbital solution would sharpen association.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 97 | 368 | 3939.4723816 | 0.001157 | 13.165 | usable; same-kind selection applies |
| 97 | 369 | 3946.4056957 | 0.001157 | 12.910 | usable; same-kind selection applies |
| 97 | 370 | 3953.3425790 | 0.001157 | 12.788 | usable; same-kind selection applies |
| 97 | 371 | 3960.2740933 | 0.001157 | 12.069 | usable; same-kind selection applies |
| 97 | 372 | 3967.2119089 | 0.001157 | 13.053 | usable; same-kind selection applies |
| 97 | 373 | 3974.1444079 | 0.001157 | 12.939 | usable; same-kind selection applies |
| 97 | 375 | 3988.0134806 | 0.001157 | 13.126 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s97.json, historical/diff_s97.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R288. [Deciding evidence](../../evidence/122506579/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
