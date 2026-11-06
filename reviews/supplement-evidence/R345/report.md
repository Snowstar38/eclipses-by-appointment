# TIC 351335839: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 8 distinct eclipse events in selected sectors[13, 101, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=14.8399513286 ±0.0000448985d, reference eclipse epoch BTJD1655.6300072, kind: Deeper repeating eclipse; even half-period cycles. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S13 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.874arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.992. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths284.455/267.314/185.501ppt, with 4 stacked events. QLP selected-kind fitted median380.798ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36444110588084162688, P=14.8359991883±0.0022444509d, e=0.037964, omega=230.7166deg. Closest edge-on conjunction offset0.190357d (0.012831phase), full-SB1-covariance linear propagated Gaia uncertainty0.212663d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.145575d (photometric period projection allowance0.003816d). The approximate central duration7.04h vs observed median5.25h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unequal alternating eclipse depths establish doubled orbital period; deeper even historical cycles define ephemeris. Initial duration bound broadened to capture deepV morphology. Poor PSF residual0.99 limits detailed image modeling, but target-centered deficit and no capable listed neighbors support source. Mixed historical cutout stack cannot be equated to primary depth.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 13 | 0 | 1655.6297408 | 0.010417 | 400.937 | used in ephemeris |
| 13 | 2 | 1670.4699505 | 0.010417 | 412.438 | used in ephemeris |
| 13 | 3 | 1677.8970689 | 0.010417 | 174.146 | measured; excluded from primary fit (secondary) |
| 101 | 330 | 4104.2225387 | 0.001157 | 357.044 | used in ephemeris |
| 101 | 331 | 4111.6416208 | 0.001157 | 174.195 | measured; excluded from primary fit (secondary) |
| 101 | 332 | 4119.0613689 | 0.001157 | 360.659 | used in ephemeris |
| 104 | 341 | 4185.8404540 | 0.001157 | 166.111 | measured; excluded from primary fit (secondary) |
| 104 | 343 | 4200.6793647 | 0.001157 | 171.355 | measured; excluded from primary fit (secondary) |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s13.json, historical/diff_s13.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R345. [Deciding evidence](../../2026-10-31-bright73/evidence/351335839) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/351335839/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/351335839/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/351335839/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch01/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch01/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/351335839/historical/diff_s13.png).
