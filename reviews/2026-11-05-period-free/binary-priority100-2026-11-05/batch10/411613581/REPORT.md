# T093 - TIC 411613581

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Two deep flat-bottomed raw eclipses recur at 2312.9773 and 3044.2421, 731.265 d apart. A sector-10 partial low state may be a third occasion but cannot supply a center; a sector-38 shallower eclipse is of the opposite kind. Thirteen cycles would give 56.25114 d, near Gaia 56.2262 d, but neighboring 12- and 14-cycle counts have no sensitive predicted primary windows in the available data. The opposite-kind phase constrains the clock only if the Gaia orbit and its eccentricity are assumed. Shorter 39/65-cycle harmonics have visually flat covered predicted deep windows.

Gaia selection orbit: P=56.226200 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 1.67-2.00 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 37: target WCS xy=(4.72,4.41), deficit peak xy=[5, 4], offset 0.50 pixel. A 3x3 sky-corrected custom aperture measures 82.2 ppt on the same observing occasion (16 core and 561 baseline cadences). There are 52 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 10 | 1580.9892 | 75.7 | 0.991 | 0.229 |
| 37 | 2312.9773 | 82.7 | 2.436 | 0.014 |
| 38 | 2341.1071 | 17.6 | 2.417 | 0.021 |
| 64 | 3044.2421 | 86.1 | 2.445 | 0.220 |
| 99 | 4050.8467 | 4.9 | 4.238 | 0.269 |
| 99 | 4067.7162 | 1.5 | 1.138 | 0.252 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Selected same-kind timing artifact: lead-timing.json, P=56.25114048 d with explicit cycles and residuals. Its formal error is conditional on those selections. This is not an adopted orbital period.
Bounded integer-cycle coverage/null audit: lead-alias.json; tested 73 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [10, 11, 37, 38, 64, 99, 100, 101]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: The integer cycle count and an eclipse-derived orbital period remain unresolved. The sector-10 partial state cannot time a cycle. QLP KSPSAP suppresses the long event; the independent TESScut aperture recovers it.
Next check: Measure another full deep eclipse or obtain an independent period constraint. The 56.25114-d value remains conditional only.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T093); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.
