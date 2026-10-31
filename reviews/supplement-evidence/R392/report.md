# TIC 76020303: CONFIRMED

Full bounded review: COMPLETE. Physical outcome and catalogue novelty are separate. Current section 2.7 five-check standard applied; historical screening is not itself admission evidence.

1. **Raw flux: pass.** 35 fitted event windows in sectors [43, 45, 72] were examined in raw-events.png and numeric raw-windows.csv. Repeated localized ingress/egress depressions and surrounding baseline were visually inspected; trapezoid fits alone are not the eclipse interpretation. QLP raw SAP_FLUX with quality zero is used for these measurements. Coverage requirements are in review_measure.py; uncovered/flagged windows are not clean nulls. At most three spread available sectors were initially selected; no mandatory all-event or all-sector analysis is implied.
2. **Measured timing: pass.** 17 same-kind measured centers give P = 3.7052792516 +/- 0.0000054871 d and reference epoch BTJD 2475.6703770. Epoch kind: Even historical half-period cycles; indistinguishable-depth primary/secondary identity ambiguous. Predicted historical centers only seed windows and cycle counts, not measured timings. Within-sector recurrence/parity tests are retained in alias-audit.json; this is not an exhaustive blind alias scan. Error meaning: Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Partial/singular fits remain documented and excluded; the epoch may denote a selected repeating eclipse rather than an independently established deeper primary.
3. **Source attribution: pass at TESS resolution.** Original cutout WCS/Gaia identity audited in pixel-audit.json. Saved sector 43 deficit-target distance 0.057 pixel; full deficit image examined against every flux-capable listed source. Capable neighbors: Gaia 3428849314988561024: separation 43.711 arcsec, required intrinsic fractional eclipse 0.9305, deficit distance 2.120 pixel; Gaia 3428849040110655872: separation 50.558 arcsec, required intrinsic fractional eclipse 0.4995, deficit distance 2.414 pixel; Gaia 3428849074470410880: separation 52.996 arcsec, required intrinsic fractional eclipse 0.3558, deficit distance 2.448 pixel Required intrinsic fractional eclipse and observed blended pixel fractional loss have different dilution and are not directly compared to exclude neighbors. The approximate G-band budget and saved 60 arcsec cone limit this check.
4. **Alternative reduction: pass.** Separately extracted background-subtracted target-centered TESScut 1x1/3x3/5x5 apertures show depths 63.661/57.191/40.992 ppt from 12 stacked events; current selected-kind QLP median 68.620 ppt. These are reductions of the same TESS photons, not independent observing occasions. Dilution, aperture differences and mixed primary/secondary stacks can change depth; no claim of equal intrinsic depths is made.
5. **Gaia orbital geometry: pass with limitations.** DR3 3428849104531235072, P = 3.7053469413 +/- 0.0001501581 d, e = 0.070651, omega = 327.6200 deg. Closest edge-on conjunction is offset -0.106060 d (-0.028623 phase), with full SB1 covariance linear propagated uncertainty 0.092846 d at measured epoch. Projection near Gaia reference gives offset -0.067950 d; photometric period projection allowance 0.003089 d excludes covariance and model systematics. Approximate central duration 6.80 h versus fitted median 4.33 h is an illustration using TIC radius/mass and a minimum-mass main-sequence companion, not a fitted geometry. No arbitrary sigma veto; gaia-geometry.json preserves all assumptions and both conjunctions.

**Deciding interpretation and limitations:** Near-equal alternating eclipses recur every 1.85264 d. Same-parity even events give the reported orbital period 3.705279 d, consistent with Gaia 3.705347 d. Photometry alone retains the half-period interpretation because parity depths are indistinguishable; Gaia supplies the orbital interpretation, not an unannounced alias replacement. Both conjunctions are plausible for the paired eclipses. The target is 0.057 pixel from deficit versus capable neighbors beyond 2.12 pixels.

**Next check:** Optional resolved photometry or spectroscopy for precision characterization.

Catalogue novelty: see central ../../catalogues/coverage-matrix.csv; this report does not establish exhaustive literature priority. Current observed repeats remove a single-cycle availability question; the short-baseline cases explicitly state their evidence.

| Sector | Historical photometric cycle | Measured midpoint BTJD | Timing input error d | Depth ppt | Timing status |
|---|---|---|---|---|---|
| 43 | 0 | 2475.6697589 | 0.0034726 | 67.665 | used |
| 43 | 1 | 2477.5236281 | 0.0034726 | 69.322 | other eclipse parity; excluded from same-kind ephemeris |
| 43 | 2 | 2479.3754730 | 0.0034726 | 68.964 | used |
| 43 | 3 | 2481.2282474 | 0.0034726 | 70.635 | other eclipse parity; excluded from same-kind ephemeris |
| 43 | 4 | 2483.0810813 | 0.0034726 | 67.395 | used |
| 43 | 5 | 2484.9336102 | 0.0034726 | 68.310 | other eclipse parity; excluded from same-kind ephemeris |
| 43 | 7 | 2488.6388780 | 0.0034726 | 69.566 | other eclipse parity; excluded from same-kind ephemeris |
| 43 | 8 | 2490.4903457 | 0.0034726 | 68.699 | used |
| 43 | 9 | 2492.3435930 | 0.0034726 | 68.698 | other eclipse parity; excluded from same-kind ephemeris |
| 43 | 10 | 2494.1962290 | 0.0034726 | 67.655 | used |
| 43 | 11 | 2496.0490936 | 0.0034726 | 72.071 | other eclipse parity; excluded from same-kind ephemeris |
| 43 | 12 | 2497.9021391 | 0.0034726 | 68.620 | used |
| 45 | 28 | 2527.5436132 | 0.0034724 | 69.909 | used |
| 45 | 29 | 2529.3964439 | 0.0034724 | 70.240 | other eclipse parity; excluded from same-kind ephemeris |
| 45 | 30 | 2531.2496872 | 0.0034724 | 69.897 | used |
| 45 | 31 | 2533.1019885 | 0.0034724 | 69.582 | other eclipse parity; excluded from same-kind ephemeris |
| 45 | 32 | 2534.9542965 | 0.0034724 | 69.811 | used |
| 45 | 33 | 2536.8078710 | 0.0034724 | 68.673 | other eclipse parity; excluded from same-kind ephemeris |
| 45 | 35 | 2540.5125340 | 0.0034724 | 69.639 | other eclipse parity; excluded from same-kind ephemeris |
| 45 | 36 | 2542.3653463 | 0.0034724 | 69.139 | used |
| 45 | 37 | 2544.2172234 | 0.0034724 | 68.207 | other eclipse parity; excluded from same-kind ephemeris |
| 45 | 38 | 2546.0698243 | 0.0034724 | 68.563 | used |
| 45 | 39 | 2547.9224540 | 0.0034724 | 70.204 | other eclipse parity; excluded from same-kind ephemeris |
| 45 | 40 | 2549.7802128 | 0.0034724 | 58.158 | used |
| 72 | 425 | 3263.0412498 | 0.0011575 | 68.936 | other eclipse parity; excluded from same-kind ephemeris |
| 72 | 426 | 3264.8940083 | 0.0011575 | 69.238 | used |
| 72 | 427 | 3266.7469286 | 0.0011575 | 68.077 | other eclipse parity; excluded from same-kind ephemeris |
| 72 | 428 | 3268.6031886 | 0.0011575 | 58.321 | used |
| 72 | 429 | 3270.4522278 | 0.0011575 | 70.801 | other eclipse parity; excluded from same-kind ephemeris |
| 72 | 430 | 3272.3048371 | 0.0011575 | 69.120 | used |
| 72 | 433 | 3277.8616510 | 0.0011575 | 68.759 | other eclipse parity; excluded from same-kind ephemeris |
| 72 | 434 | 3279.7153501 | 0.0011575 | 68.571 | used |
| 72 | 435 | 3281.5672412 | 0.0011575 | 67.446 | other eclipse parity; excluded from same-kind ephemeris |
| 72 | 436 | 3283.4202577 | 0.0011575 | 67.873 | used |
| 72 | 437 | 3285.2724572 | 0.0011575 | 66.604 | other eclipse parity; excluded from same-kind ephemeris |

Evidence (original source layout; use the public evidence links below for exported locations): measurements.json, raw-events.png, raw-windows.csv, historical/diff_s43.json, historical/diff_s43.png, historical/gaia.json; batch ../pixel-audit.json, ../alias-audit.json, ../gaia-geometry.json, ../helper-audit.md and ../SHA256SUMS.json. Raw cutout: [local path omitted] Historical extraction definitions: [local path omitted] and c3_sapdepth.py. Reused source hashes in source-hashes.json; no historical evidence overwritten.


Stable review key: R392. [Deciding evidence](../../2026-10-31-bright73/evidence/76020303) and [catalogue coverage](../../2026-10-31-bright73/catalogues/coverage-matrix.csv). The export manifest maps original hashes to sanitized files. Analysis scripts are archival and require the recorded external data; local paths are omitted.

Direct public evidence: [measured events](../../2026-10-31-bright73/evidence/76020303/measurements.json), [raw eclipse plots](../../2026-10-31-bright73/evidence/76020303/raw-events.png), [raw flux windows](../../2026-10-31-bright73/evidence/76020303/raw-windows.csv), [Gaia geometry](../../2026-10-31-bright73/analysis/batch06/gaia-geometry.json), [independent audit](../../2026-10-31-bright73/analysis/batch06/helper-audit.md), [difference image](../../2026-10-31-bright73/evidence/76020303/historical/diff_s43.png).
