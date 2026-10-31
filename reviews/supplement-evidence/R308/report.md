# TIC 363534683: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 10 distinct eclipse events in selected sectors[9, 36, 90]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a linear baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 10 same-kind midtimes give P=5.2864321424 +/-0.0000069133d, reference eclipse epoch BTJD1544.7583809, kind: Selected repeating eclipse; primary/secondary depth identity not established. No center-covariance fits were excluded. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S64 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation2.618arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.574. Capable neighbours: Gaia 5249644487609641344: 35.96 arcsec, G14.329, required fractional eclipse0.979
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths141.125/129.722/106.222ppt, with 5 stacked events (quality-zero data). QLP selected-kind fitted median144.520ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35249644448937154816, P=5.2864401901+/-0.0005018875d, e=0.048633, omega=239.4062deg. Closest edge-on conjunction offset-0.037278d (-0.007052phase), full-SB1-covariance linear propagated Gaia uncertainty0.097256d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.035516d (photometric period projection allowance0.001514d). The approximate central duration5.35h vs observed median4.27h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Ten raw eclipses across three sectors include adjacent repeats. Target deficit0.125pixel versus capable neighbor1.78pixels. Sector depths vary through aperture dilution; no claim of intrinsic constancy.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 9 | -1 | 1544.7580741 | 0.010417 | 129.425 | selected |
| 9 | 3 | 1565.9039421 | 0.010417 | 128.174 | selected |
| 36 | 139 | 2284.8591393 | 0.003472 | 148.482 | selected |
| 36 | 140 | 2290.1449691 | 0.003472 | 147.631 | selected |
| 36 | 142 | 2300.7183070 | 0.003472 | 143.991 | selected |
| 90 | 416 | 3749.2008153 | 0.001157 | 145.199 | selected |
| 90 | 417 | 3754.4871767 | 0.001157 | 144.947 | selected |
| 90 | 418 | 3759.7732248 | 0.001157 | 144.401 | selected |
| 90 | 419 | 3765.0599998 | 0.001157 | 144.640 | selected |
| 90 | 420 | 3770.3460272 | 0.001157 | 142.955 | selected |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; shared-qlp QLP FITS; historical/diff_s64.json, historical/diff_s64.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R308. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/363534683) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
