# TIC 135362193: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 7 distinct eclipse events in selected sectors[53, 80]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=4.6690140750 Ã‚+/-0.0000131496d, reference eclipse epoch BTJD2745.7473584, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S79 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation2.323arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.232. Capable neighbours: Gaia 4577603498730811008: 18.91 arcsec, G16.165, required fractional eclipse0.691; Gaia 4577603498730962560: 22.88 arcsec, G14.835, required fractional eclipse0.211
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths10.151/10.284/10.166ppt, with 4 stacked events. QLP selected-kind fitted median11.442ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34577603498730812672, P=4.6688816715Ã‚+/-0.0002208323d, e=0.038599, omega=117.5167deg. Closest edge-on conjunction offset0.046153d (0.009885phase), full-SB1-covariance linear propagated Gaia uncertainty0.103629d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.020711d (photometric period projection allowance0.006641d). The approximate central duration5.44h vs observed median2.09h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Shallow repeated eclipses across sectors53/80; capable neighbors at18.9/22.9arcsec lie0.91/1.06pixel from deficit versus target0.11pixel. Target-centered core supports attribution at TESS resolution; no calibrated localization errors. Sector80 pipeline offsets remain systematic uncertainty.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 53 | 157 | 2745.7456293 | 0.003472 | 11.442 | used in ephemeris |
| 53 | 159 | 2755.0862173 | 0.003472 | 11.451 | used in ephemeris |
| 53 | 160 | 2759.7550782 | 0.003472 | 13.447 | used in ephemeris |
| 80 | 315 | 3483.4527319 | 0.001157 | 10.709 | used in ephemeris |
| 80 | 317 | 3492.7899207 | 0.001157 | 12.037 | used in ephemeris |
| 80 | 318 | 3497.4577896 | 0.001157 | 11.157 | used in ephemeris |
| 80 | 319 | 3502.1270379 | 0.001157 | 10.871 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s79.json, historical/diff_s79.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R337. [Deciding evidence](../../evidence/135362193/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/135362193/measurements.json), [raw eclipse plots](../../evidence/135362193/raw-events.png), [raw flux windows](../../evidence/135362193/raw-windows.csv), [Gaia geometry](../../analysis/batch01/gaia-geometry.json), [independent audit](../../analysis/batch01/helper-audit.md), [difference image](../../evidence/135362193/historical/diff_s79.png).
