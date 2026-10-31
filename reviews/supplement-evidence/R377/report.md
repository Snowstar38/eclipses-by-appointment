# TIC 66787531: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 6 distinct eclipse events in selected sectors[76, 84]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=8.4698323955 +/-0.0000408947d, reference eclipse epoch BTJD3372.5340791, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S57 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation4.885arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.438. Capable neighbours: Gaia 1985288988373538176: 29.23 arcsec, G16.005, required fractional eclipse0.649; Gaia 1985288610416416640: 50.84 arcsec, G15.933, required fractional eclipse0.608; Gaia 1985291565353912576: 51.60 arcsec, G15.706, required fractional eclipse0.496
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths14.138/14.120/13.460ppt, with 3 stacked events. QLP selected-kind fitted median16.163ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31985288988373538432, P=8.4702687962+/-0.0005995472d, e=0.283327, omega=345.7269deg. Closest edge-on conjunction offset-0.194463d (-0.022958phase), full-SB1-covariance linear propagated Gaia uncertainty0.221120d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.040850d (photometric period projection allowance0.014395d). The approximate central duration6.26h vs observed median2.26h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated isolated eclipses; deficit0.233pixel from target versus nearest capable neighbor1.675pixels. Aperture dilution limits intrinsic depth.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 76 | 192 | 3372.5337087 | 0.001432 | 16.326 | used in ephemeris |
| 76 | 193 | 3381.0030530 | 0.001689 | 20.131 | used in ephemeris |
| 76 | 194 | 3389.4745364 | 0.001258 | 16.966 | used in ephemeris |
| 84 | 218 | 3592.7502013 | 0.001157 | 15.806 | used in ephemeris |
| 84 | 219 | 3601.2188247 | 0.001157 | 15.999 | used in ephemeris |
| 84 | 220 | 3609.6896101 | 0.001157 | 14.520 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s57.json, historical/diff_s57.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R377. [Deciding evidence](../../2026-10-31-bright73/evidence/66787531) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/66787531/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/66787531/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/66787531/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch05/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch05/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/66787531/historical/diff_s57.png).
