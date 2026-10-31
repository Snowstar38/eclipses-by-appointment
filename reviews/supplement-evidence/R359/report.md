# TIC 48870240: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 6 distinct eclipse events in selected sectors[91]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 6 same-kind midtimes give P=2.7256354375 Ã‚+/-0.0001582455d, reference eclipse epoch BTJD3777.6561442, kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S91 deficit peak[7, 8] vs target pixel[7, 8]; deficit-target separation1.173arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.595. Capable neighbours: Gaia 6248866704865905536: 29.16 arcsec, G11.866, required fractional eclipse0.079
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths32.789/20.566/17.718ppt, with 7 stacked events. QLP selected-kind fitted median37.000ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR36248866322608821248, P=2.7257434900Ã‚+/-0.0002657921d, e=0.047898, omega=356.3095deg. Closest edge-on conjunction offset-0.069254d (-0.025408phase), full-SB1-covariance linear propagated Gaia uncertainty0.334151d at the measured epoch. Near-Gaia-reference projected eclipse offset0.065055d (photometric period projection allowance0.196699d). The approximate central duration4.18h vs observed median3.87h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Six measured raw events in sector91 include four successive cycles5-8 and the cycle0/1 pair, establishing recurrence. Capable neighbor1.39pixels from deficit versus target0.056pixel; target core favors attribution.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 91 | 0 | 3777.6564539 | 0.001157 | 36.662 | used in ephemeris |
| 91 | 1 | 3780.3814365 | 0.001157 | 36.331 | used in ephemeris |
| 91 | 5 | 3791.2846138 | 0.001157 | 37.322 | used in ephemeris |
| 91 | 6 | 3794.0090677 | 0.001157 | 36.677 | used in ephemeris |
| 91 | 7 | 3796.7364181 | 0.001157 | 37.388 | used in ephemeris |
| 91 | 8 | 3799.4610321 | 0.001157 | 38.699 | used in ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s91.json, historical/diff_s91.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R359. [Deciding evidence](../../2026-10-31-bright73/evidence/48870240) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/48870240/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/48870240/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/48870240/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch03/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch03/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/48870240/historical/diff_s91.png).
