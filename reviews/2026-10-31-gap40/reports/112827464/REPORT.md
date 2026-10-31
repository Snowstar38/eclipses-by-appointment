# TIC 112827464: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[67, 94]. The lead inspected raw-event plots and numeric fitting summaries. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=3.4225952625 ±0.0000046565d, reference primary epoch BTJD3129.3941410. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using quadrature-free conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage.
3. **Target attribution: pass at TESS image resolution.** Historical S27 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation3.053arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.582. Capable neighbours: Gaia 6744219263229275136: 30.53 arcsec, G12.650, required fractional eclipse0.115, pixel fractional loss0.003067157147837522
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths30.267/25.168/18.244ppt, with 6 stacked events. QLP primary fitted median33.456ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36744219095727246720, P=3.4231233978±0.0002361926d, e=0.285125, omega=17.3840deg. Closest edge-on conjunction offset-0.215585d (-0.062979phase), full-SB1-covariance linear propagated Gaia uncertainty0.164184d at the measured epoch. Near-Gaia-reference projected eclipse offset0.207452d (photometric period projection allowance0.003730d). The approximate central duration4.26h vs observed median3.16h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Raw local baseline slopes are fitted explicitly. One capable neighbour is separated from the target-centered deficit; no calibrated centroid confidence ellipse. Gaia nominal phase offset0.063 and period drift remain explicit; full covariance and near-reference projection support association without arbitrary sigma veto.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt |
|---|---|---|---|---|
| 67 | 429 | 3129.3942573 | 0.001234 | 33.456 |
| 67 | 430 | 3132.8170306 | 0.001228 | 35.886 |
| 67 | 431 | 3136.2390573 | 0.001157 | 36.061 |
| 67 | 433 | 3143.0839208 | 0.001593 | 33.598 |
| 67 | 434 | 3146.5078492 | 0.002025 | 32.273 |
| 67 | 435 | 3149.9296258 | 0.002634 | 34.225 |
| 94 | 642 | 3858.4072081 | 0.001496 | 29.223 |
| 94 | 643 | 3861.8296391 | 0.001461 | 29.723 |
| 94 | 644 | 3865.2519654 | 0.001893 | 31.535 |
| 94 | 646 | 3872.0962772 | 0.002724 | 31.051 |
| 94 | 648 | 3878.9425497 | 0.001990 | 34.643 |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../../shared-qlp/QLP FITS; historical/diff_s27.json, historical/diff_s27.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R193. [Deciding evidence](../../evidence/112827464/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
