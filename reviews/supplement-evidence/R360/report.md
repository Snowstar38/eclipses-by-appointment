# TIC 178199444: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 3 distinct eclipse events in selected sectors[31]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 3 same-kind midtimes give P=6.5485022540 ±0.0016073438d, reference eclipse epoch BTJD2149.2179543, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S31 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation1.857arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.964. Capable neighbours: Gaia 5087572522289602944: 59.59 arcsec, G14.889, required fractional eclipse0.700
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths36.052/32.012/21.556ppt, with 4 stacked events. QLP selected-kind fitted median40.179ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35087572625368816896, P=6.5478351785±0.0003587164d, e=0.006130, omega=71.8319deg. Closest edge-on conjunction offset-0.031815d (-0.004859phase), full-SB1-covariance linear propagated Gaia uncertainty0.111501d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.211258d (photometric period projection allowance0.432375d). The approximate central duration4.44h vs observed median2.31h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Three raw events in sector31 include consecutive cycles110/111 and a two-cycle separation108/110. Single selected sector supplies repeated cycles; this is not a single-event case.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 31 | 108 | 2149.2174819 | 0.003472 | 40.179 | used in ephemeris |
| 31 | 110 | 2162.3163759 | 0.003472 | 40.647 | used in ephemeris |
| 31 | 111 | 2168.8625163 | 0.003472 | 39.168 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s31.json, historical/diff_s31.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R360. [Deciding evidence](../../2026-10-31-bright73/evidence/178199444) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/178199444/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/178199444/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/178199444/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch03/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch03/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/178199444/historical/diff_s31.png).
