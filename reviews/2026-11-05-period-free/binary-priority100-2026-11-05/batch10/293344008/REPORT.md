# T094 - TIC 293344008

Physical verdict: **PLAUSIBLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Two clean ~45-ppt raw events occur at 2478.7621 (s43) and 3215.7910 (s70), separated by 737.0289 d. Their similarly shaped profiles support recurrence, and an independent TESScut aperture recovers the s43 event. The Gaia-near 18-cycle period would be 40.9461 d, but the bounded tests of 12-35 cycles found no sufficiently covered intervening predicted primary window; several aliases remain open.

Gaia selection orbit: P=40.932431 d, SB1. The nearest nominal conjunction to the retained screening window differs by +0.0169 Gaia cycles. This is a screening comparison, not an eclipse-derived period or source attribution.

## Source and reduction

TESScut sector 43: target WCS xy=(4.39,4.65), deficit peak xy=[4, 5], offset 0.52 pixel. A 3x3 sky-corrected custom aperture measures 46.7 ppt on the same observing occasion (20 core and 184 baseline cadences). There are 51 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 43 | 2478.7621 | 32.5 | 0.793 | 0.028 |
| 70 | 3215.7910 | 33.4 | 0.789 | 0.220 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Bounded integer-cycle coverage/null audit: lead-alias.json; tested 24 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [42, 43, 70]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: The long gap leaves the orbital period and Gaia orbit association insecure. Tesscut currently lists only sectors 42, 43 and 70; there is no later available sector.
Next check: Measure a third same-kind eclipse or get an independent period constraint.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T094); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.
