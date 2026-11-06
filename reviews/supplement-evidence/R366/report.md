# TIC 279065540: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 9 distinct eclipse events in selected sectors[58, 85]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=5.2403431586 ±0.0000058932d, reference eclipse epoch BTJD2883.0673999, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S58 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation5.250arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.844. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths213.830/201.663/167.136ppt, with 6 stacked events. QLP selected-kind fitted median216.202ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3430965367901091456, P=5.2403509794±0.0002055046d, e=0.240755, omega=135.7897deg. Closest edge-on conjunction offset0.000412d (0.000079phase), full-SB1-covariance linear propagated Gaia uncertainty0.104181d at the measured epoch. Near-Gaia-reference projected eclipse offset0.004135d (photometric period projection allowance0.002805d). The approximate central duration5.07h vs observed median3.31h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated isolated eclipses across sectors58/85; no capable listed neighbor. Aperture dilution retained.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 58 | 208 | 2883.0671535 | 0.001157 | 214.898 | used in ephemeris |
| 58 | 209 | 2888.3079418 | 0.001157 | 215.743 | used in ephemeris |
| 58 | 210 | 2893.5480362 | 0.001157 | 215.478 | used in ephemeris |
| 58 | 211 | 2898.7887838 | 0.001157 | 215.383 | used in ephemeris |
| 58 | 212 | 2904.0285397 | 0.001157 | 216.202 | used in ephemeris |
| 58 | 213 | 2909.2690821 | 0.001157 | 218.223 | used in ephemeris |
| 85 | 348 | 3616.7153682 | 0.001157 | 219.016 | used in ephemeris |
| 85 | 349 | 3621.9565974 | 0.001157 | 220.389 | used in ephemeris |
| 85 | 351 | 3632.4357426 | 0.001157 | 220.593 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s58.json, historical/diff_s58.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R366. [Deciding evidence](../../2026-10-31-bright73/evidence/279065540) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/279065540/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/279065540/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/279065540/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch03/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch03/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/279065540/historical/diff_s58.png).
