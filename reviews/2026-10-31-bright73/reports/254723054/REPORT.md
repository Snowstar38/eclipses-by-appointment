# TIC 254723054: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 7 distinct eclipse events in selected sectors[12, 65, 103]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=13.8861420099 ±0.0000226421d, reference eclipse epoch BTJD1636.3604759, kind: Deeper repeating eclipse; even half-period cycles. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. Local recurrence where covered and alternating depths are recorded in alias-audit.json. No exhaustive blind search claimed. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S65 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.094arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.384. Capable neighbours: Gaia 5987885181823038720: 19.91 arcsec, G14.701, required fractional eclipse0.629
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths24.441/23.551/24.559ppt, with 3 stacked events. QLP selected-kind fitted median40.985ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35987885143131649280, P=13.8892341157±0.0021777940d, e=0.042019, omega=326.0764deg. Closest edge-on conjunction offset-0.077217d (-0.005560phase), full-SB1-covariance linear propagated Gaia uncertainty0.194146d at the measured epoch. Near-Gaia-reference projected eclipse offset0.201072d (photometric period projection allowance0.002038d). The approximate central duration13.11h vs observed median12.03h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Stable alternating depths establish doubled orbital period. Four deeper even historical half-period events alone define ephemeris; historical cutout stack mixes both kinds. Nearest capable neighbor is0.883pixel from deficit versus target0.100pixel; target favored at image resolution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 12 | 0 | 1636.3511235 | 0.010417 | 41.715 | included timing center |
| 12 | 2 | 1650.2375152 | 0.010417 | 37.047 | included timing center |
| 65 | 207 | 3073.5780045 | 0.001468 | 16.704 | usable center; excluded opposite eclipse kind |
| 65 | 208 | 3080.5197751 | 0.001157 | 48.266 | included timing center |
| 65 | 209 | 3087.4565207 | 0.001633 | 16.834 | usable center; excluded opposite eclipse kind |
| 103 | 363 | 4156.6930015 | 0.002959 | 14.142 | usable center; excluded opposite eclipse kind |
| 103 | 364 | 4163.6377848 | 0.001542 | 40.255 | included timing center |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s65.json, historical/diff_s65.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R354. [Deciding evidence](../../evidence/254723054/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/254723054/measurements.json), [raw eclipse plots](../../evidence/254723054/raw-events.png), [raw flux windows](../../evidence/254723054/raw-windows.csv), [Gaia geometry](../../analysis/batch02/gaia-geometry.json), [independent audit](../../analysis/batch02/helper-audit.md), [difference image](../../evidence/254723054/historical/diff_s65.png).
