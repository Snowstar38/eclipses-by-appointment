# TIC 62337815: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. Current section 2.7 five-check standard applied; historical screening is not itself admission evidence.

1. **Raw flux: pass.** 4 fitted event windows in sectors [76, 83] were examined in raw-events.png and numeric raw-windows.csv. Repeated localized ingress/egress depressions and surrounding baseline were visually inspected; trapezoid fits alone are not the eclipse interpretation. QLP raw SAP_FLUX with quality zero is used for these measurements. Coverage requirements are in review_measure.py; uncovered/flagged windows are not clean nulls. At most three spread available sectors were initially selected; no mandatory all-event or all-sector analysis is implied.
2. **Measured timing: pass.** 4 same-kind measured centers give P = 11.5008928530 +/- 0.0000784016 d and reference epoch BTJD 3378.3037354. Epoch kind: Selected repeating eclipse; deeper/secondary identity not independently established. Predicted historical centers only seed windows and cycle counts, not measured timings. Within-sector recurrence/parity tests are retained in alias-audit.json; this is not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Partial/singular fits remain documented and excluded; the epoch may denote a selected repeating eclipse rather than an independently established deeper primary.
3. **Source attribution: pass at TESS resolution.** Original cutout WCS/Gaia identity audited in pixel-audit.json. Saved sector 55 deficit-target distance 0.249 pixel; full deficit image examined against every flux-capable listed source. Capable neighbors: Gaia 2166153703341315968: separation 12.253 arcsec, required intrinsic fractional eclipse 0.2344, deficit distance 0.833 pixel Required intrinsic fractional eclipse and observed blended pixel fractional loss have different dilution and are not directly compared to exclude neighbors. The approximate G-band budget and saved 60 arcsec cone limit this check.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut 1x1/3x3/5x5 apertures show depths 16.077/16.162/15.507 ppt from 2 stacked events; current selected-kind QLP median 20.247 ppt. These are reductions of the same TESS photons, not independent observing occasions. Dilution, aperture differences and mixed primary/secondary stacks can change depth; no claim of equal intrinsic depths is made.
5. **Gaia orbital geometry: pass with limitations.** DR3 2166153699041263360, P = 11.5003902549 +/- 0.0013799967 d, e = 0.048491, omega = 318.6830 deg. Closest edge-on conjunction is offset 0.067766 d (0.005892 phase), with full SB1 covariance linear propagated uncertainty 0.357581 d at measured epoch. Projection near Gaia reference gives offset -0.062910 d; photometric period projection allowance 0.020384 d excludes covariance and model systematics. Approximate central duration 7.79 h versus fitted median 3.44 h is an illustration using TIC radius/mass and a minimum-mass main-sequence companion, not a fitted geometry. No arbitrary sigma veto; gaia-geometry.json preserves all assumptions and both conjunctions.

**Deciding interpretation and limitations:** Four isolated flat-bottom eclipses in sectors 76/83 with consecutive cycles in each. The 12.25 arcsec capable neighbor is 0.833 pixel from the deficit versus target 0.249 pixel; full image favors target, with residual subpixel crowding limitation.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

Catalogue novelty: see central ../../catalogues/coverage-matrix.csv; this report does not establish exhaustive literature priority. Current observed repeats remove a single-cycle availability question; the short-baseline cases explicitly state their evidence.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing input error d | Depth ppt | Timing status |
|---|---|---|---|---|---|
| 76 | 144 | 3378.3030917 | 0.0015034 | 20.425 | used |
| 76 | 145 | 3389.8050547 | 0.0012106 | 20.069 | used |
| 83 | 160 | 3562.3182704 | 0.0011574 | 22.328 | used |
| 83 | 161 | 3573.8186563 | 0.0011574 | 19.705 | used |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s55.json, historical/diff_s55.png, historical/gaia.json; batch ../pixel-audit.json, ../alias-audit.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Raw cutout: [local path omitted] Historical extraction definitions: [local path omitted] and c3_sapdepth.py. Reused source hashes in source-hashes.json; no historical evidence overwritten.


Stable review key: R388. [Deciding evidence](../../evidence/62337815/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/62337815/measurements.json), [raw eclipse plots](../../evidence/62337815/raw-events.png), [raw flux windows](../../evidence/62337815/raw-windows.csv), [Gaia geometry](../../analysis/batch06/gaia-geometry.json), [independent audit](../../analysis/batch06/helper-audit.md), [difference image](../../evidence/62337815/historical/diff_s55.png).
