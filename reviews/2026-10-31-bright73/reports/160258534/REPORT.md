# TIC 160258534: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 7 distinct eclipse events in selected sectors[15, 56, 83]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=7.7049863920 ±0.0000097839d, reference eclipse epoch BTJD1730.5945848, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S55 deficit peak[8, 7] vs target pixel[7, 7]; deficit-target separation1.654arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.519. Capable neighbours: Gaia 1951244157007311360: 49.79 arcsec, G13.296, required fractional eclipse0.491; Gaia 1951244569324172288: 53.83 arcsec, G13.622, required fractional eclipse0.628
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths89.365/86.649/69.479ppt, with 3 stacked events. QLP selected-kind fitted median96.211ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31951244534964478720, P=7.7037472107±0.0008325053d, e=0.045926, omega=218.2302deg. Closest edge-on conjunction offset0.215587d (0.027985phase), full-SB1-covariance linear propagated Gaia uncertainty0.179708d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.000030d (photometric period projection allowance0.001702d). The approximate central duration4.74h vs observed median3.64h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Repeated eclipses across sectors15/56/83; capable neighbors2.51/2.73pixels from deficit versus target0.079pixel. Pixel core supports target at TESS resolution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | 2 | 1730.5844469 | 0.010417 | 99.373 | used in ephemeris |
| 56 | 145 | 2832.4076921 | 0.001157 | 96.211 | used in ephemeris |
| 56 | 146 | 2840.1125037 | 0.001157 | 96.537 | used in ephemeris |
| 56 | 147 | 2847.8179997 | 0.001157 | 98.588 | used in ephemeris |
| 83 | 240 | 3564.3811879 | 0.001157 | 95.605 | used in ephemeris |
| 83 | 241 | 3572.0863352 | 0.001157 | 96.052 | used in ephemeris |
| 83 | 242 | 3579.7912800 | 0.001157 | 95.350 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s55.json, historical/diff_s55.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R364. [Deciding evidence](../../evidence/160258534/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/160258534/measurements.json), [raw eclipse plots](../../evidence/160258534/raw-events.png), [raw flux windows](../../evidence/160258534/raw-windows.csv), [Gaia geometry](../../analysis/batch03/gaia-geometry.json), [independent audit](../../analysis/batch03/helper-audit.md), [difference image](../../evidence/160258534/historical/diff_s55.png).
