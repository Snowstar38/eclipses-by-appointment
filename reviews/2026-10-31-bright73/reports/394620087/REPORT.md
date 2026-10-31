# TIC 394620087: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 5 distinct eclipse events in selected sectors[54, 81]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=6.8947331077 +/-0.0000236096d, reference eclipse epoch BTJD2771.8036128, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S40 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.578arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.547. Capable neighbours: Gaia 2045989451938846336: 30.87 arcsec, G13.589, required fractional eclipse0.594
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths101.759/96.507/82.787ppt, with 2 stacked events. QLP selected-kind fitted median104.974ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32045989413267218816, P=6.8950679495+/-0.0005730378d, e=0.015067, omega=339.7470deg. Closest edge-on conjunction offset-0.094934d (-0.013768phase), full-SB1-covariance linear propagated Gaia uncertainty0.216787d at the measured epoch. Near-Gaia-reference projected eclipse offset0.020921d (photometric period projection allowance0.008169d). The approximate central duration7.07h vs observed median5.28h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Five deep repeated eclipses across sectors54/81, including consecutive cycles266/267. Target deficit0.123pixel versus capable neighbor1.436pixels.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 54 | 157 | 2771.8032357 | 0.003472 | 103.783 | used in ephemeris |
| 54 | 159 | 2785.5933979 | 0.003472 | 102.695 | used in ephemeris |
| 81 | 264 | 3509.5403160 | 0.001157 | 104.974 | used in ephemeris |
| 81 | 266 | 3523.3295217 | 0.001157 | 109.417 | used in ephemeris |
| 81 | 267 | 3530.2240002 | 0.001157 | 109.299 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s40.json, historical/diff_s40.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R385. [Deciding evidence](../../evidence/394620087/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/394620087/measurements.json), [raw eclipse plots](../../evidence/394620087/raw-events.png), [raw flux windows](../../evidence/394620087/raw-windows.csv), [Gaia geometry](../../analysis/batch05/gaia-geometry.json), [independent audit](../../analysis/batch05/helper-audit.md), [difference image](../../evidence/394620087/historical/diff_s40.png).
