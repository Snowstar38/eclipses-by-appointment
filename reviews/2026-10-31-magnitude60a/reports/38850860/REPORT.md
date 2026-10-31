# TIC 38850860: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 8 distinct eclipse events in selected sectors[27, 68, 96]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 8 same-kind midtimes give P=8.4145931953 Ãƒâ€šÃ‚±0.0000081269d, reference eclipse epoch BTJD2042.7168402, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S27 deficit peak[8, 8] vs target pixel[8, 8]; deficit-target separation1.214arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.190. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths31.055/30.538/29.006ppt, with 3 stacked events. QLP selected-kind fitted median30.158ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR34702435241420083712, P=8.4129097571Ãƒâ€šÃ‚±0.0020308000d, e=0.169799, omega=71.4874deg. Closest edge-on conjunction offset-0.092244d (-0.010965phase), full-SB1-covariance linear propagated Gaia uncertainty0.475998d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.423882d (photometric period projection allowance0.001601d). The approximate central duration3.97h vs observed median3.76h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Eight measured repeats across three sectors. No capable catalogued neighbor; target-centered deficit. Raw depth26-31ppt varies by extraction/sector.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 27 | 0 | 2042.7164086 | 0.003472 | 30.060 | usable; same-kind selection applies |
| 27 | 1 | 2051.1315095 | 0.003472 | 30.882 | usable; same-kind selection applies |
| 27 | 2 | 2059.5465702 | 0.003472 | 30.280 | usable; same-kind selection applies |
| 68 | 134 | 3170.2726330 | 0.001157 | 30.256 | usable; same-kind selection applies |
| 68 | 135 | 3178.6865601 | 0.001157 | 31.201 | usable; same-kind selection applies |
| 96 | 222 | 3910.7567478 | 0.001157 | 26.599 | usable; same-kind selection applies |
| 96 | 223 | 3919.1708937 | 0.001157 | 26.586 | usable; same-kind selection applies |
| 96 | 224 | 3927.5857628 | 0.001157 | 26.089 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s27.json, historical/diff_s27.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R244. [Deciding evidence](../../evidence/38850860/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
