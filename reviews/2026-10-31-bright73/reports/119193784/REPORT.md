# TIC 119193784: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 4 distinct eclipse events in selected sectors[50, 91]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: conditional orbital alias.** 4 same-kind midtimes give P=10.4453149260 +/-0.0000244041d, reference eclipse epoch BTJD2669.7487457, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S50 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation4.008arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.570. Capable neighbours: Gaia 3645530720010524672: 41.07 arcsec, G12.275, required fractional eclipse0.268
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths112.056/101.074/78.404ppt, with 2 stacked events. QLP selected-kind fitted median122.868ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33645530788730001280, P=10.4445071004+/-0.0023469310d, e=0.204078, omega=254.9518deg. Closest edge-on conjunction offset0.062988d (0.006031phase), full-SB1-covariance linear propagated Gaia uncertainty0.556629d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.113118d (photometric period projection allowance0.005320d). The approximate central duration6.07h vs observed median4.30h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four deep V-shaped/truncated-bottom events across S50/91, all odd historical10.445d cycles. Intermediate cycles0 and106 have zero quality-zero points within0.2d (42 and173 flagged points respectively), so neither is a clean null. Available QLP inventory lists only S50/91. Two20.8906d-separated pairs establish real repetition, but10.4453149d period is conditional on the Gaia-informed cycle count;20.8906d and integer-count aliases are not independently rejected. This missing orbital-alias check retains PROBABLE despite completed bounded inspection. Target deficit0.191pixel versus capable neighbor2.279pixels; dilution limits intrinsic depth.

**Next check:** Obtain clean intermediate-cycle photometry to distinguish10.445d from20.8906d orbital aliases.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 50 | -1 | 2669.7487060 | 0.003472 | 125.471 | used in conditional ephemeris |
| 50 | 1 | 2690.6394133 | 0.003472 | 125.744 | used in conditional ephemeris |
| 91 | 105 | 3776.9521434 | 0.001157 | 120.265 | used in conditional ephemeris |
| 91 | 107 | 3797.8427424 | 0.001157 | 119.358 | used in conditional ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s50.json, historical/diff_s50.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten.


Stable review key: R397. [Deciding evidence](../../evidence/119193784/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/119193784/measurements.json), [raw eclipse plots](../../evidence/119193784/raw-events.png), [raw flux windows](../../evidence/119193784/raw-windows.csv), [Gaia geometry](../../analysis/batch07/gaia-geometry.json), [independent audit](../../analysis/batch07/helper-audit.md), [difference image](../../evidence/119193784/historical/diff_s50.png).
