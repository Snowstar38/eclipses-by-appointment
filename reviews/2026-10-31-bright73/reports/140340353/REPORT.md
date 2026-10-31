# TIC 140340353: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 13 distinct eclipse events in selected sectors[33, 87]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 13 same-kind midtimes give P=3.3434088582 +/-0.0000031883d, reference eclipse epoch BTJD2203.1906137, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S33 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation0.867arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.174. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths43.911/42.702/41.059ppt, with 8 stacked events. QLP selected-kind fitted median45.287ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33322717610788810880, P=3.3440197736+/-0.0003574652d, e=0.098550, omega=327.8916deg. Closest edge-on conjunction offset-0.167185d (-0.049995phase), full-SB1-covariance linear propagated Gaia uncertainty0.161169d at the measured epoch. Near-Gaia-reference projected eclipse offset0.164542d (photometric period projection allowance0.001731d). The approximate central duration6.07h vs observed median3.22h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Thirteen narrow eclipses across S33/87 repeat coherently. No capable listed neighbor. Gaia conjunction offset-0.05phase (-0.167d) compared with full-covariance0.161d uncertainty: association is physically consistent within orbital-epoch uncertainty, without arbitrary phase veto.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 33 | 219 | 2203.1903722 | 0.003472 | 44.952 | used in ephemeris |
| 33 | 220 | 2206.5339597 | 0.003472 | 45.587 | used in ephemeris |
| 33 | 221 | 2209.8778085 | 0.003472 | 45.639 | used in ephemeris |
| 33 | 223 | 2216.5645577 | 0.003472 | 45.287 | used in ephemeris |
| 33 | 224 | 2219.9074408 | 0.003472 | 46.540 | used in ephemeris |
| 33 | 225 | 2223.2508490 | 0.003472 | 45.839 | used in ephemeris |
| 33 | 226 | 2226.5945579 | 0.003472 | 45.128 | used in ephemeris |
| 87 | 657 | 3667.6035206 | 0.001157 | 45.557 | used in ephemeris |
| 87 | 658 | 3670.9466228 | 0.001157 | 45.877 | used in ephemeris |
| 87 | 659 | 3674.2907028 | 0.001157 | 44.033 | used in ephemeris |
| 87 | 661 | 3680.9777823 | 0.001157 | 45.002 | used in ephemeris |
| 87 | 662 | 3684.3211172 | 0.001157 | 45.068 | used in ephemeris |
| 87 | 663 | 3687.6637723 | 0.001157 | 43.446 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s33.json, historical/diff_s33.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R404. [Deciding evidence](../../evidence/140340353/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/140340353/measurements.json), [raw eclipse plots](../../evidence/140340353/raw-events.png), [raw flux windows](../../evidence/140340353/raw-windows.csv), [Gaia geometry](../../analysis/batch07/gaia-geometry.json), [independent audit](../../analysis/batch07/helper-audit.md), [difference image](../../evidence/140340353/historical/diff_s33.png).
