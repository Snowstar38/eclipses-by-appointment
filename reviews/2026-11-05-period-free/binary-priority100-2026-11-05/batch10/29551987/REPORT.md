# T099 - TIC 29551987

Physical verdict: **CONFIRMED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

A deep class appears at 1822.7651, 2916.8088 and 3291.0574; a shallower class at 1837.1432 and 2931.2046. The first two deep events give 28.79062 d over 38 cycles and the shallow pair gives 28.79109 d over 38 cycles. The sector-73 deep profile is observed through ingress, core and egress; its nearest 0.220-d gap falls after egress. Its fitted center differs from the two-kind prediction by 0.041 d, within a conservative 0.05-d center allowance. Adopt P=28.791 d with a conservative 0.001-d allowance, rather than the overprecise all-three formal fit. The P/2 alias maps deep and shallow events to the same kind despite their distinct persistent depths.

Gaia selection orbit: P=28.792787 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 0.47-1.19 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 59: target WCS xy=(4.88,4.68), deficit peak xy=[5, 5], offset 0.34 pixel. A 3x3 sky-corrected custom aperture measures 109.4 ppt on the same observing occasion (4 core and 1700 baseline cadences). There are 52 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 19 | 1822.7651 | 87.5 | 2.067 | 0.208 |
| 19 | 1837.1432 | 46.0 | 2.061 | 0.271 |
| 59 | 2916.8088 | 100.1 | 2.460 | 0.220 |
| 59 | 2931.2046 | 43.9 | 2.760 | 0.220 |
| 73 | 3291.0574 | 96.6 | 2.216 | 1.350 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Selected same-kind timing artifact: lead-timing.json, P=28.78953627 d with explicit cycles and residuals. Its formal error is conditional on those selections.
Bounded integer-cycle coverage/null audit: lead-alias.json; tested 3 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [19, 59, 73, 86]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: The 0.001-d period allowance is conservative, not a calibrated one-sigma error. Broad baseline gaps and slopes affect the sector-73 center; lead-t099-bounds.json records actual timing coverage and the 0.05-d bound.
Next check: Finish unavailable novelty catalogue gates before any new-system claim.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T099); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.

The adopted period and sector-73 conservative bound are in lead-t099-bounds.json. The selected three-deep-event fit in lead-timing.json is exploratory and is not the adopted ephemeris.