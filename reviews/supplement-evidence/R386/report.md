# TIC 443900773: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 8 distinct eclipse events in selected sectors[7, 46, 88]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=9.3257982069 +/-0.0000153302d, reference eclipse epoch BTJD1496.6547499, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S7 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.805arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.082. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths351.148/350.810/345.926ppt, with 3 stacked events. QLP selected-kind fitted median379.302ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3649664385352561664, P=9.3257311444+/-0.0008100741d, e=0.014226, omega=280.9488deg. Closest edge-on conjunction offset0.022938d (0.002460phase), full-SB1-covariance linear propagated Gaia uncertainty0.121549d at the measured epoch. Near-Gaia-reference projected eclipse offset0.014958d (photometric period projection allowance0.001824d). The approximate central duration5.30h vs observed median4.31h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep repeated flat-bottom eclipses across sectors7/46/88; no capable listed neighbor. Fitted depths differ by aperture and sector; no detailed binary characterization.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 7 | 0 | 1496.6530390 | 0.010417 | 349.261 | used in ephemeris |
| 7 | 1 | 1505.9832182 | 0.010417 | 333.251 | used in ephemeris |
| 46 | 114 | 2559.7954116 | 0.003472 | 390.319 | used in ephemeris |
| 46 | 115 | 2569.1217730 | 0.003472 | 387.013 | used in ephemeris |
| 46 | 116 | 2578.4472772 | 0.003472 | 386.179 | used in ephemeris |
| 88 | 236 | 3697.5428520 | 0.001157 | 379.586 | used in ephemeris |
| 88 | 237 | 3706.8690316 | 0.001157 | 378.635 | used in ephemeris |
| 88 | 238 | 3716.1948982 | 0.001157 | 379.018 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s07.json, historical/diff_s07.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R386. [Deciding evidence](../../2026-10-31-bright73/evidence/443900773) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/443900773/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/443900773/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/443900773/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch05/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch05/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/443900773/historical/diff_s07.png).
