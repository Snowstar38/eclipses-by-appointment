# TIC 337881909: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 9 distinct eclipse events in selected sectors[13, 93, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 9 same-kind midtimes give P=9.6174021260 Ã‚+/-0.0000203371d, reference eclipse epoch BTJD1661.0486137, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S13 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation1.252arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.828. Capable neighbours: Gaia 6724638855242197120: 17.77 arcsec, G14.446, required fractional eclipse0.193; Gaia 6724638820882453888: 21.65 arcsec, G16.246, required fractional eclipse0.952; Gaia 6724638889601940224: 21.89 arcsec, G15.135, required fractional eclipse0.351; Gaia 6724638820882457984: 26.79 arcsec, G15.128, required fractional eclipse0.349; Gaia 6724638923961681280: 27.11 arcsec, G15.629, required fractional eclipse0.545; Gaia 6724638820882447232: 47.87 arcsec, G16.037, required fractional eclipse0.788; Gaia 6724638850925800064: 52.52 arcsec, G16.080, required fractional eclipse0.819; Gaia 6724638649083749760: 58.15 arcsec, G15.084, required fractional eclipse0.336
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths13.705/13.040/11.404ppt, with 3 stacked events. QLP selected-kind fitted median13.400ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36724638885282158720, P=9.6159030557Ã‚+/-0.0037502071d, e=0.245757, omega=215.8197deg. Closest edge-on conjunction offset0.007154d (0.000744phase), full-SB1-covariance linear propagated Gaia uncertainty0.532172d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.190723d (photometric period projection allowance0.002684d). The approximate central duration9.33h vs observed median8.77h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Crowded field: eight capable neighbors, nearest17.8arcsec; deficit0.06pixel from target versus0.80pixel from nearest capable source. Target-centered core favors target, but highPSF fractional residual0.83 limits precise localization. No calibrated errors or resolved binary parameters claimed.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 13 | 0 | 1661.0430448 | 0.010416 | 13.173 | used in ephemeris |
| 13 | 1 | 1670.6620979 | 0.010416 | 13.492 | used in ephemeris |
| 13 | 2 | 1680.2756262 | 0.010416 | 13.400 | used in ephemeris |
| 93 | 226 | 3834.5824036 | 0.001608 | 14.514 | used in ephemeris |
| 93 | 227 | 3844.2025253 | 0.002441 | 14.350 | used in ephemeris |
| 93 | 228 | 3853.8174251 | 0.002353 | 13.545 | used in ephemeris |
| 104 | 262 | 4180.8071992 | 0.001157 | 12.689 | used in ephemeris |
| 104 | 263 | 4190.4246764 | 0.001823 | 11.171 | used in ephemeris |
| 104 | 264 | 4200.0424811 | 0.001157 | 12.016 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s13.json, historical/diff_s13.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R341. [Deciding evidence](../../2026-10-31-bright73/evidence/337881909) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/337881909/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/337881909/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/337881909/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch01/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch01/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/337881909/historical/diff_s13.png).
