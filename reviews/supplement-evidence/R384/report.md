# TIC 9262715: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 7 distinct eclipse events in selected sectors[20, 47, 60]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=7.3625774772 +/-0.0000348536d, reference eclipse epoch BTJD1846.2999364, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S47 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.380arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.643. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths100.072/97.050/85.495ppt, with 4 stacked events. QLP selected-kind fitted median109.006ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR3923996517914746624, P=7.3632161676+/-0.0009799956d, e=0.069654, omega=157.7983deg. Closest edge-on conjunction offset-0.175911d (-0.023890phase), full-SB1-covariance linear propagated Gaia uncertainty0.198272d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.049450d (photometric period projection allowance0.006901d). The approximate central duration5.42h vs observed median3.68h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Seven deep repeated eclipses across sectors20/47/60, including sector47 consecutive cycles100-103. No capable listed neighbor.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 20 | 0 | 1846.2989112 | 0.010417 | 96.324 | used in ephemeris |
| 47 | 100 | 2582.5582853 | 0.003472 | 109.006 | used in ephemeris |
| 47 | 101 | 2589.9203232 | 0.003472 | 109.112 | used in ephemeris |
| 47 | 102 | 2597.2826705 | 0.003472 | 108.430 | used in ephemeris |
| 47 | 103 | 2604.6451631 | 0.003472 | 108.646 | used in ephemeris |
| 60 | 149 | 2943.3241963 | 0.001157 | 110.151 | used in ephemeris |
| 60 | 151 | 2958.0489055 | 0.001157 | 109.449 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s47.json, historical/diff_s47.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R384. [Deciding evidence](../../2026-10-31-bright73/evidence/9262715) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/9262715/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/9262715/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/9262715/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch05/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch05/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/9262715/historical/diff_s47.png).
