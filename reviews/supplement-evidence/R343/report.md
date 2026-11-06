# TIC 14291901: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 11 distinct eclipse events in selected sectors[42, 44, 71]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=5.9988293272 ±0.0000112890d, reference eclipse epoch BTJD2448.4020518, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S43 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation0.978arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.047. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths40.282/39.535/39.267ppt, with 3 stacked events. QLP selected-kind fitted median43.443ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR350221915880732288, P=5.9990825867±0.0004188713d, e=0.004308, omega=257.5851deg. Closest edge-on conjunction offset-0.108901d (-0.018153phase), full-SB1-covariance linear propagated Gaia uncertainty0.155500d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.022033d (photometric period projection allowance0.003872d). The approximate central duration4.74h vs observed median2.89h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipses at multiple successive cycles; Gaia conjunction offset retained with propagated orbit covariance and radius/model limitations.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 42 | 0 | 2448.4016012 | 0.003473 | 41.196 | used in ephemeris |
| 42 | 1 | 2454.4008384 | 0.003473 | 41.540 | used in ephemeris |
| 42 | 3 | 2466.3991292 | 0.003473 | 41.887 | used in ephemeris |
| 44 | 9 | 2502.3911272 | 0.003472 | 44.937 | used in ephemeris |
| 44 | 10 | 2508.3902582 | 0.003472 | 43.827 | used in ephemeris |
| 44 | 11 | 2514.3895396 | 0.003472 | 44.107 | used in ephemeris |
| 44 | 12 | 2520.3880726 | 0.003472 | 43.706 | used in ephemeris |
| 71 | 132 | 3240.2473673 | 0.001157 | 42.743 | used in ephemeris |
| 71 | 133 | 3246.2461485 | 0.001157 | 42.758 | used in ephemeris |
| 71 | 134 | 3252.2454786 | 0.001157 | 43.443 | used in ephemeris |
| 71 | 135 | 3258.2440673 | 0.001157 | 43.849 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s43.json, historical/diff_s43.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R343. [Deciding evidence](../../2026-10-31-bright73/evidence/14291901) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/14291901/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/14291901/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/14291901/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch01/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch01/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/14291901/historical/diff_s43.png).
