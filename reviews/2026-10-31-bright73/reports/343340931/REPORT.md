# TIC 343340931: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 9 distinct eclipse events in selected sectors[12, 93, 103]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=6.1520562408 +/-0.0000181837d, reference eclipse epoch BTJD1630.7654348, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: unresolved after check.** Historical S13 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation3.996arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.153. Capable neighbours: Gaia 5801411754927216640: 2.88 arcsec, G14.241, required fractional eclipse0.205
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths21.316/20.867/20.807ppt, with 4 stacked events. QLP selected-kind fitted median20.390ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35801411754927217024, P=6.1527422755+/-0.0006366165d, e=0.140362, omega=312.4429deg. Closest edge-on conjunction offset-0.155060d (-0.025202phase), full-SB1-covariance linear propagated Gaia uncertainty0.137697d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.016481d (photometric period projection allowance0.003673d). The approximate central duration4.79h vs observed median9.82h is a radius/minimum-mass illustration, not a detailed binary fit. TIC radius/mass are unavailable for this target; the solar fallback is not a physical duration constraint. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Attribution remains unresolved: capable neighbor only2.879arcsec from target, required intrinsic eclipse0.205; deficit distances0.190pixel to target and0.282pixel to neighbor are insufficient to distinguish these sources reliably. TIC mass/radius absent; approximate solar-fallback duration4.79h cannot constrain observed9.82h. Gaia association remains possible; source assignment needs resolved photometry.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of this signal.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 12 | 0 | 1630.7613410 | 0.010417 | 20.390 | used in ephemeris |
| 12 | 1 | 1636.9100316 | 0.010417 | 19.672 | used in ephemeris |
| 12 | 3 | 1649.2165764 | 0.010417 | 20.254 | used in ephemeris |
| 93 | 358 | 3833.2017649 | 0.001157 | 23.512 | used in ephemeris |
| 93 | 359 | 3839.3553771 | 0.001157 | 23.355 | used in ephemeris |
| 93 | 360 | 3845.5052080 | 0.001157 | 22.784 | used in ephemeris |
| 93 | 361 | 3851.6579128 | 0.001157 | 23.029 | used in ephemeris |
| 103 | 410 | 4153.1062442 | 0.001157 | 18.409 | used in ephemeris |
| 103 | 411 | 4159.2693171 | 0.003821 | 17.983 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s13.json, historical/diff_s13.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R380. [Deciding evidence](../../evidence/343340931/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/343340931/measurements.json), [raw eclipse plots](../../evidence/343340931/raw-events.png), [raw flux windows](../../evidence/343340931/raw-windows.csv), [Gaia geometry](../../analysis/batch05/gaia-geometry.json), [independent audit](../../analysis/batch05/helper-audit.md), [difference image](../../evidence/343340931/historical/diff_s13.png).
