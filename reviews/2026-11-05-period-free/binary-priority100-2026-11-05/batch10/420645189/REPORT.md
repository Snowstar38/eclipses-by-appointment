# T091 - TIC 420645189

Physical verdict: **CONFIRMED**. Bounded review: **COMPLETE**. Catalogue novelty: **KNOWN**.

Two eclipse kinds recur in raw SAP. The deep 54-ppt class at BTJD 2001.0008, 2729.0102, 3311.4182 and 3457.0186 yields a 48.533875-d selected-event clock with cycles 0,15,27,30. Shallow events at 1837.4763, 2031.6106 and 3293.4966 are a separate class. The sector-59 retained feature is across a 1.63-d gap and is not used as timing evidence. A P/2=24.267-d harmonic predicts another ~54-ppt deep event in sector 26 at BTJD 2025.2678. The raw core has 12 uninterrupted cadences (93% expected coverage) and only a 1.0-ppt deficit; the right side is fully covered and the left side 62% covered. The plotted window excludes a comparable deep eclipse there, though it is not a strict three-band shallow-event null.

Gaia selection orbit: P=48.549921 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 0.05-0.64 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 52: target WCS xy=(4.13,4.08), deficit peak xy=[4, 4], offset 0.15 pixel. A 3x3 sky-corrected custom aperture measures 53.3 ppt on the same observing occasion (14 core and 130 baseline cadences). There are 54 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 19 | 1837.4763 | 4.2 | 0.240 | 0.042 |
| 25 | 2001.0008 | 46.1 | 0.270 | 0.062 |
| 26 | 2031.6106 | 4.1 | 0.256 | 0.042 |
| 52 | 2729.0102 | 47.8 | 0.268 | 0.014 |
| 59 | 2923.6032 | 1.1 | 1.179 | 1.632 |
| 73 | 3293.4966 | 3.8 | 0.267 | 0.002 |
| 73 | 3311.4182 | 46.0 | 0.268 | 0.002 |
| 79 | 3457.0186 | 47.0 | 0.267 | 0.005 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Selected same-kind timing artifact: lead-timing.json, P=48.53387501 d with explicit cycles and residuals. Its formal error is conditional on those selections.
Bounded integer-cycle coverage/null audit: lead-alias.json; tested 3 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [19, 25, 26, 52, 53, 59, 73, 79, 86]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
The primary Tarrants-Mendes Table 2 exact Gaia ID row calls TOI-1897 an EB, and sky/CATALOGUE.md records the two retired TOI signals. The positive known match takes precedence over failed other catalogue gates.
Limitation: Selected-event formal timing error excludes calibration and cycle-model uncertainty. The four VizieR catalogue gates remain unavailable, but an exact published EB identification resolves novelty.
Next check: No new-system claim; retain as a known EB recovery.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T091); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.

The P/2 targeted deep-eclipse null with actual core/side coverage and source hash is in lead-t091-half-null.json and lead-deciding-null-T091.png.