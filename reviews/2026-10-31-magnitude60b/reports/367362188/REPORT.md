# TIC 367362188: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 14 distinct eclipse events in selected sectors[19, 59, 86]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a linear baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 14 same-kind midtimes give P=3.8453405155 +/-0.0000036346d, reference eclipse epoch BTJD1818.1697582, kind: Selected repeating eclipse; primary/secondary depth identity not established. No center-covariance fits were excluded. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S44 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation4.492arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.754. Capable neighbours: Gaia 185367425540565760: 30.23 arcsec, G14.918, required fractional eclipse0.744
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths53.953/50.016/40.001ppt, with 6 stacked events (quality-zero data). QLP selected-kind fitted median54.935ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3185367421242800768, P=3.8451064321+/-0.0003851350d, e=0.091429, omega=237.6746deg. Closest edge-on conjunction offset-0.022555d (-0.005866phase), full-SB1-covariance linear propagated Gaia uncertainty0.145341d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.109634d (photometric period projection allowance0.001352d). The approximate central duration5.04h vs observed median3.89h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Fourteen raw eclipses across three sectors include consecutive cycles285/286 and multiple later repeats. Target deficit0.214pixel versus capable neighbor1.71pixels; depth and timing remain finite-cadence/model-dependent.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 19 | 0 | 1818.1703500 | 0.010417 | 56.729 | selected |
| 19 | 1 | 1822.0151147 | 0.010417 | 54.705 | selected |
| 19 | 5 | 1837.3985928 | 0.010417 | 56.032 | selected |
| 59 | 285 | 2914.0918565 | 0.001157 | 55.760 | selected |
| 59 | 286 | 2917.9370382 | 0.001157 | 55.820 | selected |
| 59 | 287 | 2921.7827785 | 0.001157 | 54.819 | selected |
| 59 | 288 | 2925.6275834 | 0.001157 | 55.550 | selected |
| 59 | 289 | 2929.4731676 | 0.001157 | 54.927 | selected |
| 59 | 290 | 2933.3184088 | 0.001157 | 56.487 | selected |
| 86 | 473 | 3637.0160542 | 0.001157 | 54.286 | selected |
| 86 | 474 | 3640.8614157 | 0.001157 | 54.300 | selected |
| 86 | 475 | 3644.7065511 | 0.001157 | 53.565 | selected |
| 86 | 476 | 3648.5521141 | 0.001157 | 54.583 | selected |
| 86 | 479 | 3660.0871330 | 0.001157 | 54.943 | selected |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; shared-qlp QLP FITS; historical/diff_s44.json, historical/diff_s44.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R316. [Deciding evidence](../../evidence/367362188/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
