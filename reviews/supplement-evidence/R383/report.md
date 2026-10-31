# TIC 283635479: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 4 distinct eclipse events in selected sectors[17, 57, 84]. The representative raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 4 same-kind midtimes give P=12.4540146131 +/-0.0000236056d, reference eclipse epoch BTJD1768.3738400, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S17 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation4.322arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.653. Capable neighbours: Gaia 1996693191697286144: 38.43 arcsec, G11.906, required fractional eclipse0.234
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths118.799/99.677/70.809ppt, with 2 stacked events. QLP selected-kind fitted median125.079ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31996693191697283712, P=12.4547731122+/-0.0018532069d, e=0.172986, omega=141.3381deg. Closest edge-on conjunction offset-0.206500d (-0.016580phase), full-SB1-covariance linear propagated Gaia uncertainty0.254473d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.122307d (photometric period projection allowance0.002620d). The approximate central duration5.52h vs observed median3.96h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Four repeated deep eclipses across sectors17/57/84; sector84 consecutive cycles146/147 test integer recurrence. Target deficit0.206pixel versus capable neighbor1.714pixels.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 17 | 0 | 1768.3741759 | 0.010417 | 123.098 | used in ephemeris |
| 57 | 89 | 2876.7811212 | 0.001157 | 127.880 | used in ephemeris |
| 84 | 146 | 3586.6604921 | 0.001157 | 125.032 | used in ephemeris |
| 84 | 147 | 3599.1134849 | 0.001157 | 125.126 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s17.json, historical/diff_s17.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R383. [Deciding evidence](../../2026-10-31-bright73/evidence/283635479) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/283635479/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/283635479/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/283635479/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch05/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch05/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/283635479/historical/diff_s17.png).
