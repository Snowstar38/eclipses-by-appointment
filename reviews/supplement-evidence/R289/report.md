# TIC 201598744: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 14 distinct eclipse events in selected sectors[93, 104]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 14 same-kind midtimes give P=3.4086667035 ±0.0000083995d, reference eclipse epoch BTJD3830.7318892, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Unreliable fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S93 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation7.215arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.803. Capable neighbours: Gaia 6633731921030220032: 37.11 arcsec, G15.886, required fractional eclipse0.468; Gaia 6633638045927526528: 37.76 arcsec, G16.525, required fractional eclipse0.833; Gaia 6633684985627605248: 46.68 arcsec, G13.068, required fractional eclipse0.046; Gaia 6633684985627605376: 48.13 arcsec, G13.843, required fractional eclipse0.081; Gaia 6633638118945259264: 48.84 arcsec, G16.471, required fractional eclipse0.793; Gaia 6633731955389963776: 53.75 arcsec, G13.807, required fractional eclipse0.079
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths12.147/10.609/8.018ppt, with 8 stacked events. Historical event coordinates guide these stacks and are not newly measured midtimes. QLP selected-kind fitted median12.606ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36633731882372568576, P=3.4088296693±0.0003292291d, e=0.056446, omega=38.6510deg. Closest edge-on conjunction offset-0.084458d (-0.024776phase), full-SB1-covariance linear propagated Gaia uncertainty0.308497d at the measured epoch. Near-Gaia-reference projected eclipse offset0.080138d (photometric period projection allowance0.008483d). The approximate central duration3.94h vs observed median1.96h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Raw shallow eclipses recur in sectors93/104. Strong aperture dilution:1x1/3x3/5x5 depths12.15/10.61/8.02ppt. Deficit0.344pixel from target and closest capable catalogued neighbor1.63pixels from deficit favor target at TESS resolution. PSF-scaled residual0.803 is not a calibrated localization uncertainty.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 93 | 638 | 3830.7315945 | 0.001262 | 14.498 | usable; same-kind selection applies |
| 93 | 639 | 3834.1379008 | 0.001323 | 12.730 | usable; same-kind selection applies |
| 93 | 640 | 3837.5487973 | 0.001157 | 13.644 | usable; same-kind selection applies |
| 93 | 641 | 3840.9594548 | 0.001397 | 12.346 | usable; same-kind selection applies |
| 93 | 642 | 3844.3667858 | 0.001165 | 12.686 | usable; same-kind selection applies |
| 93 | 643 | 3847.7747315 | 0.001265 | 14.174 | usable; same-kind selection applies |
| 93 | 644 | 3851.1850801 | 0.001157 | 12.366 | usable; same-kind selection applies |
| 93 | 645 | 3854.5937586 | 0.001633 | 12.465 | usable; same-kind selection applies |
| 104 | 741 | 4181.8262152 | 0.001157 | 12.422 | usable; same-kind selection applies |
| 104 | 742 | 4185.2324238 | 0.001622 | 12.527 | usable; same-kind selection applies |
| 104 | 743 | 4188.6433377 | 0.001435 | 11.949 | usable; same-kind selection applies |
| 104 | 745 | 4195.4610324 | 0.001157 | 11.376 | usable; same-kind selection applies |
| 104 | 746 | 4198.8653100 | 0.001157 | 13.308 | usable; same-kind selection applies |
| 104 | 747 | 4202.2751695 | 0.001157 | 13.029 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s93.json, historical/diff_s93.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R289. [Deciding evidence](../../2026-10-31-magnitude60b/evidence/201598744) and [catalogue coverage](../../2026-10-31-magnitude60b/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
