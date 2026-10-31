# TIC 394386248: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. This review applies current section2.7 and does not promote the historical screening label automatically.

1. **Raw events: pass.** Free eclipse-core fits to quality-zero raw QLP SAP_FLUX show 2 distinct eclipse events in selected sectors[81]. The raw-event plot and numeric raw-windows.csv were inspected. Broadly repeated morphology is retained even when individual shallow fits are noisy. Local baseline, free depth, center, duration and ingress were fitted with a linear baseline; QLP detrended flux is not used as the deciding raw check. Representative selection is at most three spread available QLP sectors, with coverage/window requirements recorded by the script. Uncovered or flagged windows were never called nulls.
2. **Eclipse timing: pass.** 2 same-kind midtimes give P=13.5773902434 +/-0.0016368077d, reference eclipse epoch BTJD3509.3712123, kind: Selected repeating eclipse; primary/secondary depth identity not established. No center-covariance fits were excluded. Historical event coordinates in difference-image JSON were predictions and are not used as measured timings. Cycle counts were seeded by historical photometric search period, then fit freely across the selected baseline. This is not a blind all-alias search. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated.
3. **Target attribution: pass at TESS image resolution.** Saved S40 deficit peak[7, 7] vs target pixel[7, 7]; deficit-target separation3.197arcsec. Full saved difference image, original cutout identity and capable neighbours were audited. PSF-scaled image fractional residual0.657. Capable neighbours: None within60arcsec under the approximate G-band flux-budget test.
4. **Alternative reduction: pass.** Background-subtracted target-centered TESScut aperture gives 1x1/3x3/5x5 depths81.223/81.035/77.614ppt, with 2 stacked events (flag2048 cores). QLP selected-kind fitted median77.740ppt. Sector40 is a separate TESS observing occasion from the measured sector81 QLP events; its custom extraction is not an independent telescope. Alternative reductions of any one exposure share photons. Dilution, aperture differences and, where relevant, mixed primary/secondary stacks prevent a claim of equal intrinsic depths.
5. **Gaia orbital geometry: pass with stated limitations.** DR32045837646305075072, P=13.5745185100+/-0.0023485600d, e=0.333088, omega=30.2864deg. Closest edge-on conjunction offset0.613972d (0.045230phase), full-SB1-covariance linear propagated Gaia uncertainty0.499331d at the measured epoch. Near-Gaia-reference projected eclipse offset-0.046526d (photometric period projection allowance0.376466d). The approximate central duration6.18h vs observed median4.46h permits noncentral geometry; this radius/minimum-mass estimate is not a detailed binary fit. Full covariance and assumptions are in gaia-geometry.json. No arbitrary sigma veto is used.

**Deciding limitations and interpretation:** Two consecutive quality-zero sector81 eclipses measure only a13.58d timing baseline, with formal/cadence period error0.00164d; no long-baseline precision asserted. Custom TESScut sector40 contains two further13.5769d-spaced raw repeats, all cores flag2048; these are flagged supportive recurrence, not clean nulls or precise timing points. Flagged difference image target offset0.15pixel with no capable neighbor under approximate flux screen. Flagged-image systematic and 9x9 residual0.657 limit localization; raw sector81 eclipses are unflagged.

**Next check:** Optional resolved photometry or updated spectroscopy for improved binary parameters; no missing bounded admission check.

Catalogue novelty: central seven-group result applies; see ../../catalogues/coverage-matrix.csv. A separate source in the search cone does not establish a target match. This physical report does not assert exhaustive literature priority.

Measured events (errors are the conservative fit inputs, not calibrated coverage):

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing error d | Fitted depth ppt | Timing status |
|---|---|---|---|---|---|
| 81 | 134 | 3509.3712123 | 0.001157 | 77.385 | selected |
| 81 | 135 | 3522.9486025 | 0.001157 | 78.095 | selected |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv; shared-qlp QLP FITS; historical/diff_s40_flag2048.json, historical/diff_s40_flag2048.png and historical/gaia.json; ../gaia-geometry.json; ../helper-audit.md; ../SHA256SUMS.json. Original cutout retained at [local path omitted] Historical pipeline definitions are diffstack.py and c3_sapdepth.py in the source sb1-scale tree. No historical evidence overwritten.


Stable review key: R311. [Deciding evidence](../../evidence/394386248/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.
