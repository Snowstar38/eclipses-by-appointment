# TIC 451086560: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 8 distinct eclipse events in selected sectors[10, 64, 100]. The representative raw-event plot and numeric raw-windows.csv were inspected. The raw morphology, ingress/egress and local baselines were inspected independently of fitted curves; target-specific interpretation follows below. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 7 same-kind midtimes give P=8.3004291559 +/-0.0000091255d, reference eclipse epoch BTJD1576.7194332, kind: Selected repeating eclipse; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S37 deficit peak[8, 7] vs target pixel[8, 7]; deficit-target separation2.006arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.985. Capable neighbours: Gaia 5346004174848323200: 32.54 arcsec, G13.548, required fractional eclipse0.780; Gaia 5346004106128831488: 59.25 arcsec, G8.021, required fractional eclipse0.155
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths68.641/16.758/6.125ppt, with 3 stacked events. QLP selected-kind fitted median151.848ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR35346004174848307712, P=8.2999349364+/-0.0006655746d, e=0.019055, omega=57.1282deg. Closest edge-on conjunction offset0.133686d (0.016107phase), full-SB1-covariance linear propagated Gaia uncertainty0.089273d at the measured epoch. Near-Gaia-reference projected eclipse offset0.063012d (photometric period projection allowance0.001305d). The approximate central duration8.37h vs observed median6.96h is a radius/minimum-mass illustration, not a detailed binary fit.  Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Deep flat-bottom eclipses repeat in S10/64/100. Partial S64 cycle179 ingress is excluded from timing. Aperture dilution and changing baseline can contribute to depth variation; deficit0.096pixel from target versus nearest capable neighbor1.679pixels. Adjacent S100 cycles directly test8.30d recurrence. A doubled orbital alias with equal eclipse kinds is not ruled out by parity alone; Gaia supports the retained branch.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 10 | 0 | 1576.7183031 | 0.010417 | 146.024 | used in ephemeris |
| 10 | 2 | 1593.3200517 | 0.010417 | 162.278 | used in ephemeris |
| 64 | 177 | 3045.8948798 | 0.001768 | 160.563 | used in ephemeris |
| 64 | 178 | 3054.1960875 | 0.001157 | 175.333 | used in ephemeris |
| 64 | 179 | 3062.5052542 | 0.002057 | 153.986 | Partial ingress coverage across gap; retained raw morphology but excluded timing. |
| 100 | 301 | 4075.1485308 | 0.001388 | 125.121 | used in ephemeris |
| 100 | 302 | 4083.4489310 | 0.001157 | 151.848 | used in ephemeris |
| 100 | 303 | 4091.7496016 | 0.001157 | 132.578 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s37.json, historical/diff_s37.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are [local path omitted] and [local path omitted] No historical evidence overwritten. Historical inventory G=12.0086; actual nested Gaia DR3 G=11.996699. All three are inside actual DR3 G11.5-12 despite inventory values above12; this preserves the inventory/DR3 distinction.


Stable review key: R408. [Deciding evidence](../../2026-10-31-bright73/evidence/451086560) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/451086560/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/451086560/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/451086560/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch08/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch08/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/451086560/historical/diff_s37.png).
