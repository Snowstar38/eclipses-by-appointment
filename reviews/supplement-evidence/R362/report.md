# TIC 167923097: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 5 distinct eclipse events in selected sectors[9, 62, 100]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=15.9435356330 Ã‚+/-0.0000166784d, reference eclipse epoch BTJD1560.4521364, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S35 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation9.287arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.537. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths226.324/220.069/212.394ppt, with 2 stacked events. QLP selected-kind fitted median241.112ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35466449351454905216, P=15.9431608845Ã‚+/-0.0084437670d, e=0.133116, omega=261.7914deg. Closest edge-on conjunction offset-0.439652d (-0.027576phase), full-SB1-covariance linear propagated Gaia uncertainty0.577385d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.467008d (photometric period projection allowance0.001218d). The approximate central duration6.93h vs observed median5.11h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated V eclipses in sectors9/62/100; aperture differences and0.44pixel deficit offset retained; no capable listed neighbor.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 9 | 0 | 1560.4515699 | 0.010417 | 241.112 | used in ephemeris |
| 62 | 90 | 2995.3704457 | 0.001157 | 253.285 | used in ephemeris |
| 62 | 91 | 3011.3137913 | 0.001157 | 253.640 | used in ephemeris |
| 100 | 158 | 4079.5307793 | 0.001157 | 217.623 | used in ephemeris |
| 100 | 159 | 4095.4742815 | 0.001157 | 220.461 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s35.json, historical/diff_s35.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R362. [Deciding evidence](../../2026-10-31-bright73/evidence/167923097) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/167923097/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/167923097/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/167923097/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch03/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch03/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/167923097/historical/diff_s35.png).
