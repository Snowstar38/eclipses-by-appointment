# T092 - TIC 212431520

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Sector 81 contains a deep ~180-ppt event near 3512.516 and a weaker, partly gapped event near 3531.965, 19.449 d later. These are unequal and cannot count as two same-kind repetitions. The sector-54 retained windows at 2772-2788 sit on sloping, wavy raw variability and fail as independent eclipse repeats. The two sector-81 events do not establish a unique period or the Gaia 33.294-d clock.

Gaia selection orbit: P=33.293973 d, SB1. The nearest nominal conjunction to the retained screening window differs by +0.0825 Gaia cycles. This is a screening comparison, not an eclipse-derived period or source attribution.

## Source and reduction

TESScut sector 81: target WCS xy=(4.83,4.84), deficit peak xy=[5, 5], offset 0.23 pixel. A 3x3 sky-corrected custom aperture measures 104.7 ppt on the same observing occasion (61 core and 475 baseline cadences). There are 53 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 54 | 2772.3577 | 11.6 | 0.405 | 0.035 |
| 54 | 2773.3595 | 7.2 | 0.507 | 0.042 |
| 54 | 2787.3839 | 22.4 | 0.428 | 0.042 |
| 54 | 2788.3806 | 14.7 | 0.507 | 0.042 |
| 81 | 3512.5162 | 132.0 | 0.830 | 0.222 |
| 81 | 3531.9648 | 52.6 | 0.587 | 0.350 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Bounded integer-cycle coverage/null audit: lead-alias.json; tested 7 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [54, 81]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue tests show no positive EB match; four VizieR gates are unknown.
Limitation: The first sector-81 event has a bright Gaia neighbor 35.8 arcsec away. Its positive difference moment lies 0.047 pixel from the target and 1.65 pixels from that neighbor, favoring the target without a calibrated PRF fit. No same-kind recurrence or secure clock.
Next check: Obtain another target-resolved event to determine which eclipse kind repeats and its period.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T092); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.
