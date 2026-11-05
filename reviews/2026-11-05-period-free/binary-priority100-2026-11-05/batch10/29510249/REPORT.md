# T097 - TIC 29510249

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Two ~225-ppt raw primary-like eclipses occur at 1559.4177 and 2275.4556, 716.038 d apart. A partly covered shallower ~56-ppt event near 3737.73 is a third, opposite-kind candidate, but its center is insecure. Twelve cycles would give 59.6698 d near Gaia 59.6703 d; 36/48/60-cycle short harmonics have actual flat predicted primary windows, while neighboring 11/13-cycle aliases remain without sensitive nulls. One opposite-kind event cannot independently select the 12-cycle count.

Gaia selection orbit: P=59.670259 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 0.29-0.83 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 35: target WCS xy=(4.39,4.22), deficit peak xy=[4, 4], offset 0.45 pixel. A 3x3 sky-corrected custom aperture measures 229.9 ppt on the same observing occasion (20 core and 347 baseline cadences). There are 52 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 9 | 1559.4177 | 209.2 | 1.494 | 0.542 |
| 35 | 2275.4556 | 213.1 | 1.511 | 0.181 |
| 89 | 3737.7306 | 55.6 | 2.179 | 1.958 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Bounded integer-cycle coverage/null audit: lead-alias.json; tested 65 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [8, 9, 35, 36, 62, 89]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: The sector-89 shallow event is partly gapped and cannot supply a precision midpoint. Sector 62 is an unusable negative-target-pixel cutout, not a null. Orbital period and Gaia association are not established.
Next check: Time an additional fully covered primary to distinguish neighboring cycle counts.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T097); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.

Sector-62 supplemental cutout and its source hash: lead-s62-audit.json. The target pixel median is negative, so it contributes no sensitive null.