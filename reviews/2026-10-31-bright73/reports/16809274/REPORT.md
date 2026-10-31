# TIC 16809274: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free trapezoid fits to quality-zero raw QLP SAP_FLUX contain 8 distinct eclipse events in selected sectors[15, 82, 83]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local linear baseline, free depth, center, duration and ingress were fitted; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 5 same-kind midtimes give P=14.7258719722 Ã‚+/-0.0000898281d, reference eclipse epoch BTJD1714.5124553, kind: Shallower repeating eclipse, even historical half-period cycles; not asserted to be deeper primary. Partial or singular center-covariance fits flagged timing_usable=false are excluded from ephemeris and remain documented in measurements.json. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Historical S56 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.360arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.958. Capable neighbours: Gaia 1897254734463908352: 24.02 arcsec, G13.330, required fractional eclipse0.305
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths55.552/50.247/40.055ppt, with 4 stacked events. QLP selected-kind fitted median58.352ppt. This separately extracted cutout is an alternative reduction of the same TESS photons, not independent observing occasions. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR31897254730167270528, P=14.7287368632Ã‚+/-0.0029848195d, e=0.026585, omega=301.3580deg. Closest edge-on conjunction offset-0.254052d (-0.017249phase), full-SB1-covariance linear propagated Gaia uncertainty0.301075d at the measured epoch. Near-Gaia-reference projected eclipse offset0.003788d (photometric period projection allowance0.008085d). The approximate central duration15.06h vs observed median14.83h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Persistent unequal alternating eclipses establish doubled orbital period relative to historical SAP half-period7.363d. Even historical cycles are the shallower event; only those five measured events define the ephemeris, explicitly not called deeper primary. Odd deeper events remain in raw evidence. Capable neighbor1.046pixels from deficit versus target0.160pixel; target core favors attribution. Historical cutout stack mixes eclipse kinds.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 15 | 0 | 1714.5126228 | 0.010417 | 57.733 | used in ephemeris |
| 15 | 2 | 1729.2368375 | 0.010417 | 56.147 | used in ephemeris |
| 82 | 248 | 3540.5240558 | 0.002026 | 61.879 | used in ephemeris |
| 82 | 249 | 3547.9459064 | 0.001157 | 86.665 | measured; excluded from selected shallower-eclipse fit (deeper event) |
| 82 | 250 | 3555.2462222 | 0.001157 | 61.825 | used in ephemeris |
| 83 | 251 | 3562.6712971 | 0.001514 | 80.932 | measured; excluded from selected shallower-eclipse fit (deeper event) |
| 83 | 252 | 3569.9665978 | 0.002939 | 58.352 | used in ephemeris |
| 83 | 253 | 3577.3971027 | 0.001157 | 80.492 | measured; excluded from selected shallower-eclipse fit (deeper event) |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, shared-qlp QLP FITS; historical/diff_s56.json, historical/diff_s56.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R365. [Deciding evidence](../../evidence/16809274/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/16809274/measurements.json), [raw eclipse plots](../../evidence/16809274/raw-events.png), [raw flux windows](../../evidence/16809274/raw-windows.csv), [Gaia geometry](../../analysis/batch03/gaia-geometry.json), [independent audit](../../analysis/batch03/helper-audit.md), [difference image](../../evidence/16809274/historical/diff_s56.png).
