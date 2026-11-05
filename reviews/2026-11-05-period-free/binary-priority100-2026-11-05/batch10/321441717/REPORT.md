# T095 - TIC 321441717

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Two deep raw eclipses at 1921.7669 and 2611.8693 recur after 690.102 d. A shallower eclipse at 1907.3921 is a distinct kind. Twenty-four deep cycles would give 28.7543 d near Gaia 28.7717 d; a 72-cycle short harmonic predicts a visually absent deep event at 2631.0388, but neighboring 23/25-cycle aliases have no sensitive predicted primary windows. The shallow event cannot force a half phase without assuming the Gaia orbit.

Gaia selection orbit: P=28.771710 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 0.76-3.47 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 22: target WCS xy=(4.58,4.84), deficit peak xy=[5, 5], offset 0.46 pixel. A 3x3 sky-corrected custom aperture measures 86.3 ppt on the same observing occasion (7 core and 138 baseline cadences). There are 53 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 22 | 1907.3921 | 48.7 | 2.324 | 0.250 |
| 22 | 1921.7669 | 89.3 | 1.802 | 0.062 |
| 48 | 2611.8693 | 80.8 | 1.731 | 0.285 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Bounded integer-cycle coverage/null audit: lead-alias.json; tested 87 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [22, 48]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: The two deep occasions do not uniquely fix the cycle count. The shallow eclipse is 3.47 Gaia linear-sigma from nominal opposite conjunction, so Gaia-orbit association remains insecure. KSPSAP suppresses long dips; TESScut recovers one.
Next check: Measure another deep eclipse to establish the clock and test Gaia association.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T095); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.
