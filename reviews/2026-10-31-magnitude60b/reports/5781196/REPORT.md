# TIC 5781196: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 2 distinct eclipse events in selected sectors[36, 99]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 2 same-kind midtimes give P=11.0017719770 ±0.0000228750d, reference eclipse epoch BTJD2289.0187466, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S89 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation5.093arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.441. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths215.498/201.534/157.504ppt, with 3 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median202.989ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35435847468956665856, P=11.0028295172±0.0015099322d, e=0.570356, omega=115.9229deg. Closest edge-on conjunction offset-0.189598d (-0.017232phase), full-SB1-covariance linear propagated Gaia uncertainty0.272145d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.006644d (photometric period projection allowance0.003957d). The approximate central duration2.79h vs observed median2.30h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Two precisely fitted deep events in sectors36/99 are supplemented by helper raw sector89 THREE adjacent repeated eclipses near BTJD3719/3730/3741 separated by11.0018d. Those actual raw repeats test long-baseline integer-cycle aliases; they are not predicted centers used as measured timings. Strong aperture/sector dilution differences remain; no capable catalogued neighbor within60arcsec.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 36 | 70 | 2289.0187466 | 0.003472 | 223.722 | usable; same-kind selection applies |
| 99 | 230 | 4049.3022629 | 0.001157 | 182.256 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s89.json, historical/diff_s89.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R295. [Deciding evidence](../../evidence/5781196/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
