# TIC 399238907: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 5 distinct eclipse events in selected sectors[80]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=4.1443054573 ±0.0002790706d, reference eclipse epoch BTJD3480.3126460, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S80 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.732arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.329. Capable neighbours: Gaia 4468583068251428736: 16.59 arcsec, G14.439, required fractional eclipse0.537, pixel fractional loss0.03270235223204699; Gaia 4468582965172213888: 22.12 arcsec, G13.831, required fractional eclipse0.324, pixel fractional loss0.016929322145052952; Gaia 4468582969467512192: 23.01 arcsec, G14.622, required fractional eclipse0.628, pixel fractional loss0.016929322145052952; Gaia 4468583106906461184: 52.56 arcsec, G14.077, required fractional eclipse0.396, pixel fractional loss0.010143271811782536
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths34.251/31.049/29.498ppt, with 5 stacked events. QLP selected-kind fitted median42.314ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34468583068251428864, P=4.1442204144±0.0002752424d, e=0.053485, omega=202.9714deg. Closest edge-on conjunction offset0.076594d (0.018482phase), full-SB1-covariance linear propagated Gaia uncertainty0.214766d at the measured epoch. Near-Gaia-reference projected eclipse offset0.013152d (photometric period projection allowance0.208187d). The approximate central duration9.18h vs observed median7.03h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Only QLP sector80 is available in the shared availability receipt, containing five measured repeats. Queue4.14670d is the historical screening seed, not current Gaia period; full NSS4.144220414d agrees measured period. Sector80 pipeline timing offsets are an uncalibrated systematic. Four capable neighbors are offset from the target-centered lost-light core; closest16.6arcsec.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 80 | -1 | 3480.3136886 | 0.001157 | 42.314 | usable; same-kind selection applies |
| 80 | 0 | 3484.4556420 | 0.001157 | 41.193 | usable; same-kind selection applies |
| 80 | 2 | 3492.7452726 | 0.001157 | 41.471 | usable; same-kind selection applies |
| 80 | 3 | 3496.8904725 | 0.001157 | 42.956 | usable; same-kind selection applies |
| 80 | 4 | 3501.0341254 | 0.001157 | 43.541 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s80.json, historical/diff_s80.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R240. [Deciding evidence](../../evidence/399238907/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
