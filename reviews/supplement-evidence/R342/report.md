# TIC 274578846: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 5 distinct eclipse events in selected sectors[23, 53, 84]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=12.9678602618 Ã‚+/-0.0000360930d, reference eclipse epoch BTJD1931.6480036, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S23 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation3.183arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.412. Capable neighbours: Gaia 1413834278144873728: 28.85 arcsec, G12.494, required fractional eclipse0.138
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths37.663/31.396/28.856ppt, with 2 stacked events. QLP selected-kind fitted median45.643ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31413834312504612352, P=12.9670803122Ã‚+/-0.0021571855d, e=0.248242, omega=61.1714deg. Closest edge-on conjunction offset0.089513d (0.006903phase), full-SB1-covariance linear propagated Gaia uncertainty0.291273d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.003301d (photometric period projection allowance0.004295d). The approximate central duration6.01h vs observed median3.94h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Same-kind repeat within sector53 and84 secures long-baseline cycle count. Modest aperture/sector depth differences retained.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 23 | 0 | 1931.6472336 | 0.010417 | 41.906 | used in ephemeris |
| 53 | 63 | 2748.6237263 | 0.003472 | 45.643 | used in ephemeris |
| 53 | 64 | 2761.5907438 | 0.003472 | 45.459 | used in ephemeris |
| 84 | 128 | 3591.5337707 | 0.001157 | 47.966 | used in ephemeris |
| 84 | 129 | 3604.5023100 | 0.001157 | 47.698 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s23.json, historical/diff_s23.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R342. [Deciding evidence](../../2026-10-31-bright73/evidence/274578846) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/274578846/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/274578846/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/274578846/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch01/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch01/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/274578846/historical/diff_s23.png).
