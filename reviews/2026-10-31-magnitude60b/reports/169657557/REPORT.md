# TIC 169657557: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 29 distinct eclipse events in selected sectors[61, 88]. The raw-event plot and numeric raw-windows.csv were inspected. The raw-windows.csv retains the initial broad linear model; deciding narrow-core fits and timings are in quadratic-core.json/png and measurements.json. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a quadratic baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 29 same-kind midtimes give P=1.4973843851 +/-0.0000030799d, reference eclipse epoch BTJD2965.1431096, kind: Narrow eclipse core atop broad phase modulation; physical primary identity unestablished. No center-covariance fits were excluded. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S88 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation2.086arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.505. Capable neighbours: Gaia 3036481615590722176: 29.04 arcsec, G12.512, required fractional eclipse0.037; Gaia 3036481615590722304: 30.71 arcsec, G16.598, required fractional eclipse0.957; Gaia 3036528443615800960: 49.79 arcsec, G14.030, required fractional eclipse0.104; Gaia 3036481512511513216: 55.32 arcsec, G15.668, required fractional eclipse0.415; Gaia 3036481615590721408: 55.33 arcsec, G16.556, required fractional eclipse0.920; Gaia 3036481478151775744: 56.40 arcsec, G13.060, required fractional eclipse0.051; Gaia 3036481443792033920: 57.17 arcsec, G14.265, required fractional eclipse0.125; Gaia 3036481409432298368: 57.87 arcsec, G16.577, required fractional eclipse0.938
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths17.702/13.538/9.801ppt, with 15 stacked events (quality-zero data). QLP selected-kind fitted median16.335ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR33036481512511509632, P=1.4974373957+/-0.0000740271d, e=0.111978, omega=21.7640deg. Closest edge-on conjunction offset-0.042512d (-0.028390phase), full-SB1-covariance linear propagated Gaia uncertainty0.137602d at the measured epoch. Near-Gaia-reference projected eclipse offset0.048667d (photometric period projection allowance0.005297d). The approximate central duration4.45h vs observed median2.41h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Broad phase modulation surrounds a sharper eclipse core. Quadratic-baseline narrow-core fit replaces the broad linear-baseline timing/depth model; core depth16.34ppt and duration2.41h are model-dependent. Earlier broad-model period agrees within formal errors. Target deficit0.099pixel, closest capable neighbor1.41pixels; all capable sources checked geometrically. No calibrated centroid uncertainty.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 61 | 983 | 2965.1476881 | 0.002419 | 18.733 | selected |
| 61 | 984 | 2966.6365462 | 0.002810 | 14.874 | selected |
| 61 | 985 | 2968.1431215 | 0.002184 | 15.142 | selected |
| 61 | 987 | 2971.1281557 | 0.003943 | 18.583 | selected |
| 61 | 988 | 2972.6309835 | 0.002054 | 16.335 | selected |
| 61 | 989 | 2974.1244091 | 0.002184 | 16.403 | selected |
| 61 | 991 | 2977.1249005 | 0.004182 | 16.513 | selected |
| 61 | 992 | 2978.6114077 | 0.004062 | 14.097 | selected |
| 61 | 993 | 2980.1139928 | 0.003655 | 16.080 | selected |
| 61 | 994 | 2981.6145236 | 0.003681 | 18.270 | selected |
| 61 | 995 | 2983.1078798 | 0.003846 | 16.361 | selected |
| 61 | 996 | 2984.6198193 | 0.004447 | 14.869 | selected |
| 61 | 997 | 2986.1067020 | 0.001876 | 20.601 | selected |
| 61 | 998 | 2987.5907552 | 0.005203 | 9.619 | selected |
| 88 | 1470 | 3694.3723254 | 0.003593 | 12.287 | selected |
| 88 | 1471 | 3695.8593781 | 0.003299 | 13.535 | selected |
| 88 | 1472 | 3697.3658519 | 0.002383 | 15.136 | selected |
| 88 | 1473 | 3698.8589370 | 0.002788 | 17.388 | selected |
| 88 | 1474 | 3700.3562855 | 0.002571 | 15.531 | selected |
| 88 | 1475 | 3701.8600297 | 0.003675 | 14.452 | selected |
| 88 | 1476 | 3703.3513601 | 0.001696 | 19.675 | selected |
| 88 | 1477 | 3704.8579194 | 0.003987 | 13.193 | selected |
| 88 | 1478 | 3706.3428245 | 0.004063 | 17.047 | selected |
| 88 | 1479 | 3707.8463010 | 0.001981 | 18.762 | selected |
| 88 | 1480 | 3709.3408970 | 0.004171 | 15.776 | selected |
| 88 | 1481 | 3710.8508522 | 0.003222 | 16.539 | selected |
| 88 | 1482 | 3712.3382359 | 0.002425 | 20.943 | selected |
| 88 | 1483 | 3713.8337482 | 0.004714 | 14.454 | selected |
| 88 | 1484 | 3715.3332414 | 0.001475 | 22.483 | selected |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; quadratic-core.json/png and broad-linear-model.json; shared-qlp QLP FITS; historical/diff_s88.json, historical/diff_s88.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R307. [Deciding evidence](../../evidence/169657557/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
