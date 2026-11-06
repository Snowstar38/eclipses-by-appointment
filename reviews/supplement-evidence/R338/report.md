# TIC 346865542: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 4 distinct eclipse events in selected sectors[42, 43, 70]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=12.0441549925 ±0.0000365340d, reference eclipse epoch BTJD2449.5432269, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S42 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation0.666arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.080. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths60.315/59.572/57.677ppt, with 2 stacked events. QLP selected-kind fitted median67.432ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32565456430589727488, P=12.0444654688±0.0006823424d, e=0.460253, omega=166.0696deg. Closest edge-on conjunction offset-0.081524d (-0.006769phase), full-SB1-covariance linear propagated Gaia uncertainty0.149158d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.028433d (photometric period projection allowance0.006247d). The approximate central duration6.28h vs observed median3.82h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four deep isolated eclipses test within-sector recurrence and long-baseline cycle count. Aperture dilution retained; fitted depths are not intrinsic.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 42 | 0 | 2449.5431115 | 0.003472 | 67.360 | used in ephemeris |
| 42 | 1 | 2461.5874220 | 0.003472 | 68.615 | used in ephemeris |
| 43 | 4 | 2497.7199278 | 0.003472 | 67.503 | used in ephemeris |
| 70 | 65 | 3232.4133008 | 0.001157 | 63.445 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s42.json, historical/diff_s42.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R338. [Deciding evidence](../../2026-10-31-bright73/evidence/346865542) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/346865542/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/346865542/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/346865542/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch01/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch01/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/346865542/historical/diff_s42.png).
