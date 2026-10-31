# TIC 128460489: PROBABLE

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX show 11 distinct eclipse events in selected sectors[7, 34, 88]. The raw-event plot and numeric raw-windows.csv were inspected. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 11 same-kind midtimes give P=6.3628732011 Ãƒâ€šÃ‚±0.0000073187d, reference eclipse epoch BTJD1493.6722577, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: unresolved after check.** Historical S7 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation5.679arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.317. Capable neighbours: Gaia 5600259057572857856: 11.02 arcsec, G14.307, required fractional eclipse0.254, pixel fractional loss0.020584271802751925; Gaia 5600259091932595584: 37.61 arcsec, G13.736, required fractional eclipse0.160, pixel fractional loss0.00852574510837417; Gaia 5600258988853381376: 41.92 arcsec, G13.394, required fractional eclipse0.123, pixel fractional loss0.002302554160844853; Gaia 5600258885774167040: 59.41 arcsec, G15.688, required fractional eclipse0.845, pixel fractional loss0.007786925055711405
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths20.584/19.674/17.212ppt, with 4 stacked events. QLP selected-kind fitted median26.324ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35600259057572857984, P=6.3633869971Ãƒâ€šÃ‚±0.0004569123d, e=0.017282, omega=333.8953deg. Closest edge-on conjunction offset-0.069923d (-0.010988phase), full-SB1-covariance linear propagated Gaia uncertainty0.086227d at the measured epoch. Near-Gaia-reference projected eclipse offset0.019477d (photometric period projection allowance0.001273d). The approximate central duration8.56h vs observed median3.68h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Unresolved attribution after completed check: capable Gaia5600259057572857856 neighbor11.02arcsec away requires25.4percent intrinsic eclipse and shares rounded TESS pixel with target. Deficit centroid is0.270pixel from target and0.516pixel from neighbor, favoring target but without calibrated uncertainty sufficient to exclude neighbor. Local blended pixel loss cannot exclude that neighbor. Retain probable for target pending resolved photometry or multi-source PRF localization.

**Next check:** Resolved eclipse photometry or multi-source PRF localization of this signal.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 7 | 0 | 1493.6722444 | 0.010417 | 22.360 | usable; same-kind selection applies |
| 7 | 1 | 1500.0353892 | 0.010417 | 24.308 | usable; same-kind selection applies |
| 7 | 2 | 1506.3993270 | 0.010417 | 23.012 | usable; same-kind selection applies |
| 34 | 116 | 2231.7657675 | 0.003472 | 25.015 | usable; same-kind selection applies |
| 34 | 117 | 2238.1283990 | 0.003472 | 29.085 | usable; same-kind selection applies |
| 34 | 118 | 2244.4907224 | 0.003472 | 27.235 | usable; same-kind selection applies |
| 34 | 119 | 2250.8542640 | 0.003472 | 26.625 | usable; same-kind selection applies |
| 88 | 346 | 3695.2272142 | 0.001157 | 26.324 | usable; same-kind selection applies |
| 88 | 347 | 3701.5884641 | 0.001157 | 25.638 | usable; same-kind selection applies |
| 88 | 348 | 3707.9517291 | 0.001157 | 27.144 | usable; same-kind selection applies |
| 88 | 349 | 3714.3153850 | 0.001157 | 26.796 | usable; same-kind selection applies |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, ../identity-check.json, shared-qlp QLP FITS; historical/diff_s07.json, historical/diff_s07.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R246. [Deciding evidence](../../evidence/128460489/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
