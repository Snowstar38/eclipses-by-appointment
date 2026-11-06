# TIC 157850336: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 4 distinct eclipse events in selected sectors[14, 81]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=14.9033560025 ±0.0000664269d, reference eclipse epoch BTJD1683.7854476, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S14 deficit peak[8, 1] vs target pixel[7, 7]; deficit-target separation1.384arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.981. Capable neighbours: Gaia 2098520337930119552: 51.05 arcsec, G15.628, required fractional eclipse0.622
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths17.846/16.645/13.145ppt, with 2 stacked events. QLP selected-kind fitted median17.411ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32098520303570374016, P=14.9046473566±0.0047076703d, e=0.280777, omega=94.9536deg. Closest edge-on conjunction offset-0.095974d (-0.006439phase), full-SB1-covariance linear propagated Gaia uncertainty0.356126d at the measured epoch. Near-Gaia-reference projected eclipse offset0.016374d (photometric period projection allowance0.005779d). The approximate central duration6.79h vs observed median6.90h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipses and successive raw cycles secure recurrence; target deficit0.066pixel versus capable neighbor2.53pixels. Aperture dilution retained.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 14 | -1 | 1683.7801863 | 0.010417 | 17.450 | used in ephemeris |
| 14 | 0 | 1698.6933446 | 0.010417 | 15.321 | used in ephemeris |
| 81 | 122 | 3516.8993945 | 0.001157 | 17.372 | used in ephemeris |
| 81 | 123 | 3531.8004421 | 0.001157 | 18.824 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s14.json, historical/diff_s14.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R357. [Deciding evidence](../../evidence/157850336/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/157850336/measurements.json), [raw eclipse plots](../../evidence/157850336/raw-events.png), [raw flux windows](../../evidence/157850336/raw-windows.csv), [Gaia geometry](../../analysis/batch03/gaia-geometry.json), [independent audit](../../analysis/batch03/helper-audit.md), [difference image](../../evidence/157850336/historical/diff_s14.png).
