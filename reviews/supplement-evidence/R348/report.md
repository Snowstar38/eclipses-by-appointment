# TIC 142932503: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 3 distinct eclipse events in selected sectors[14, 47, 75]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 same-kind midtimes give P=18.6886141507 ±0.0000723224d, reference eclipse epoch BTJD1699.2030487, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json; for142932503 the three separated centers, integer-count scan and clean submultiple tests are in helper/alias142.py and helper audit. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S14 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.808arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.433. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths154.268/153.320/151.562ppt, with 1 stacked events. QLP selected-kind fitted median170.639ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31061670668091476480, P=18.6878640883±0.0038143874d, e=0.507144, omega=148.4350deg. Closest edge-on conjunction offset0.027089d (0.001450phase), full-SB1-covariance linear propagated Gaia uncertainty0.325945d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.025415d (photometric period projection allowance0.005063d). The approximate central duration5.60h vs observed median4.19h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Three separated measured eclipses at cycles0,48,89. Independent integer-count scan1-25d finds unique near18.69d fit; clean sector47 nulls reject identical deep events at divisors2,3,4. This is bounded alias evidence, not exhaustive all-period exclusion.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 14 | 0 | 1699.2078766 | 0.010416 | 158.588 | included timing center |
| 47 | 48 | 2596.2553634 | 0.003472 | 176.201 | included timing center |
| 75 | 89 | 3362.4897779 | 0.001157 | 170.639 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s14.json, historical/diff_s14.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R348. [Deciding evidence](../../2026-10-31-bright73/evidence/142932503) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/142932503/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/142932503/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/142932503/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch02/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch02/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/142932503/historical/diff_s14.png).
