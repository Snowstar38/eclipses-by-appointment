# TIC 457003443: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. Current section 2.7 five-check standard applied; historical screening is not itself admission evidence.

1. **Raw flux: pass.** 13 fitted event windows in sectors [43, 45, 72] were examined in raw-events.png and numeric raw-windows.csv. Repeated localized ingress/egress depressions and surrounding baseline were visually inspected; trapezoid fits alone are not the eclipse interpretation. QLP raw SAP_FLUX with quality zero is used for these measurements. Coverage requirements are in review_measure.py; uncovered/flagged windows are not clean nulls. At most three spread available sectors were initially selected; no mandatory all-event or all-sector analysis is implied.
2. **Measured timing: pass.** 13 same-kind measured centers give P = 4.6443443385 +/- 0.0000089036 d and reference epoch BTJD 2479.0598944. Epoch kind: Selected repeating eclipse; deeper/secondary identity not independently established. Predicted historical centers only seed windows and cycle counts, not measured timings. Within-sector recurrence/parity tests are retained in alias-audit.json; this is not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Partial/singular fits remain documented and excluded; the epoch may denote a selected repeating eclipse rather than an independently established deeper primary.
3. **Source attribution: pass at TESS resolution.** Original cutout WCS/Gaia identity audited in pixel-audit.json. Saved sector 43 deficit-target distance 0.218 pixel; full deficit image examined against every flux-capable listed source. Capable neighbors: Gaia 3379491619541073280: separation 29.470 arcsec, required intrinsic fractional eclipse 0.2631, deficit distance 1.708 pixel; Gaia 3379493092713030656: separation 43.785 arcsec, required intrinsic fractional eclipse 0.1467, deficit distance 2.360 pixel; Gaia 3379491580884499072: separation 45.533 arcsec, required intrinsic fractional eclipse 0.3374, deficit distance 2.052 pixel; Gaia 3379491516461860608: separation 49.600 arcsec, required intrinsic fractional eclipse 0.2856, deficit distance 2.277 pixel; Gaia 3379493028290345728: separation 51.857 arcsec, required intrinsic fractional eclipse 0.0408, deficit distance 2.845 pixel Required intrinsic fractional eclipse and observed blended pixel fractional loss have different dilution and are not directly compared to exclude neighbors. The approximate G-band budget and saved 60 arcsec cone limit this check.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut 1x1/3x3/5x5 apertures show depths 8.270/8.372/7.000 ppt from 6 stacked events; current selected-kind QLP median 9.585 ppt. These are reductions of the same TESS photons, not independent observing occasions. Dilution, aperture differences and mixed primary/secondary stacks can change depth; no claim of equal intrinsic depths is made.
5. **Gaia orbital geometry: pass with limitations.** DR3 3379491615243515392, P = 4.6449635222 +/- 0.0019033067 d, e = 0.097546, omega = 281.9464 deg. Closest edge-on conjunction is offset -0.132312 d (-0.028485 phase), with full SB1 covariance linear propagated uncertainty 0.925255 d at measured epoch. Projection near Gaia reference gives offset 0.146321 d; photometric period projection allowance 0.004007 d excludes covariance and model systematics. Approximate central duration 7.92 h versus fitted median 4.14 h is an illustration using TIC radius/mass and a minimum-mass main-sequence companion, not a fitted geometry. No arbitrary sigma veto; gaia-geometry.json preserves all assumptions and both conjunctions.

**Deciding interpretation and limitations:** Repeated isolated flat-bottom shallow eclipses across sectors 43/45/72. Full deficit image favors target at 0.218 pixel; capable neighbors are at least 1.708 pixels away. Aperture dilution and baseline variability limit depth interpretation.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

Catalogue novelty: see central ../../catalogues/coverage-matrix.csv; this report does not establish exhaustive literature priority. Current observed repeats remove a single-cycle availability question; the short-baseline cases explicitly state their evidence.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing input error d | Depth ppt | Timing status |
|---|---|---|---|---|---|
| 43 | 0 | 2479.0625871 | 0.0034726 | 9.552 | used |
| 43 | 1 | 2483.7041251 | 0.0034726 | 8.606 | used |
| 43 | 2 | 2488.3491318 | 0.0034726 | 9.154 | used |
| 43 | 3 | 2492.9908462 | 0.0034726 | 9.107 | used |
| 43 | 4 | 2497.6374866 | 0.0034726 | 8.975 | used |
| 45 | 11 | 2530.1479548 | 0.0034725 | 9.448 | used |
| 45 | 12 | 2534.7972437 | 0.0034725 | 9.810 | used |
| 45 | 14 | 2544.0750911 | 0.0034725 | 9.629 | used |
| 45 | 15 | 2548.7237772 | 0.0034725 | 9.585 | used |
| 72 | 169 | 3263.9537807 | 0.0017904 | 10.407 | used |
| 72 | 170 | 3268.5973875 | 0.0018398 | 9.784 | used |
| 72 | 172 | 3277.8889397 | 0.0019366 | 9.990 | used |
| 72 | 173 | 3282.5312831 | 0.0016369 | 9.589 | used |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s43.json, historical/diff_s43.png, historical/gaia.json; batch ../pixel-audit.json, ../alias-audit.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Raw cutout: [local path omitted] Historical extraction definitions: [local path omitted] and c3_sapdepth.py. Reused source hashes in source-hashes.json; no historical evidence overwritten.


Stable review key: R391. [Deciding evidence](../../evidence/457003443/) and [catalogue coverage](../../catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../evidence/457003443/measurements.json), [raw eclipse plots](../../evidence/457003443/raw-events.png), [raw flux windows](../../evidence/457003443/raw-windows.csv), [Gaia geometry](../../analysis/batch06/gaia-geometry.json), [independent audit](../../analysis/batch06/helper-audit.md), [difference image](../../evidence/457003443/historical/diff_s43.png).
