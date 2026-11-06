# TIC 180179209: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 9 distinct eclipse events in selected sectors[11, 65, 101]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=6.3122615616 ±0.0000079776d, reference eclipse epoch BTJD1601.6364849, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S64 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation4.874arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.815. Capable neighbours: Gaia 6054997992860786816: 16.65 arcsec, G14.888, required fractional eclipse0.454; Gaia 6054997997204150784: 28.39 arcsec, G14.393, required fractional eclipse0.296; Gaia 6054997962844403840: 34.00 arcsec, G15.410, required fractional eclipse0.722; Gaia 6054997928484667904: 34.34 arcsec, G14.207, required fractional eclipse0.253; Gaia 6054998164658275584: 35.63 arcsec, G12.723, required fractional eclipse0.081; Gaia 6054997924140107776: 37.07 arcsec, G14.060, required fractional eclipse0.224; Gaia 6054997928484660992: 40.14 arcsec, G14.685, required fractional eclipse0.381; Gaia 6054997928484659200: 41.13 arcsec, G14.017, required fractional eclipse0.216; Gaia 6054997928484664704: 42.76 arcsec, G15.405, required fractional eclipse0.718; Gaia 6054998233379003392: 54.73 arcsec, G15.640, required fractional eclipse0.887; Gaia 6054998164659490560: 59.57 arcsec, G15.708, required fractional eclipse0.942
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths23.099/18.880/11.766ppt, with 4 stacked events. QLP selected-kind fitted median24.572ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36054997992859584128, P=6.3121869210±0.0008826224d, e=0.294949, omega=289.1618deg. Closest edge-on conjunction offset0.000128d (0.000020phase), full-SB1-covariance linear propagated Gaia uncertainty0.168798d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.014203d (photometric period projection allowance0.001532d). The approximate central duration7.03h vs observed median5.45h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Crowded field: eleven capable neighbors, nearest16.6arcsec; deficit0.23pixel from target versus1.00pixel from nearest capable source. PSF residual0.82 limits localization precision; target-centered core supports attribution at TESS resolution. Final partial/singular sector101 fit excluded from timing.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 11 | 0 | 1601.6392042 | 0.010417 | 23.608 | used in ephemeris |
| 11 | 1 | 1607.9484964 | 0.010417 | 22.568 | used in ephemeris |
| 11 | 3 | 1620.5780545 | 0.010417 | 23.295 | used in ephemeris |
| 65 | 233 | 3072.3926234 | 0.001227 | 25.536 | used in ephemeris |
| 65 | 234 | 3078.7073291 | 0.001640 | 26.387 | used in ephemeris |
| 65 | 235 | 3085.0162053 | 0.001157 | 25.551 | used in ephemeris |
| 65 | 236 | 3091.3324864 | 0.001453 | 25.994 | used in ephemeris |
| 101 | 397 | 4107.6044410 | 0.001157 | 20.905 | used in ephemeris |
| 101 | 399 | 4120.2258125 | 83546.295765 | 19.042 | Singular or unidentifiable center covariance: formal timing uncertainty exceeds search duration; excluded from ephemeris. |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s64.json, historical/diff_s64.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R344. [Deciding evidence](../../evidence/180179209/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/180179209/measurements.json), [raw eclipse plots](../../evidence/180179209/raw-events.png), [raw flux windows](../../evidence/180179209/raw-windows.csv), [Gaia geometry](../../analysis/batch01/gaia-geometry.json), [independent audit](../../analysis/batch01/helper-audit.md), [difference image](../../evidence/180179209/historical/diff_s64.png).
