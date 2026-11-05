# T096 - TIC 356733570

Physical verdict: **CONFIRMED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

The deep kind repeats at 1455.3169, 2478.5706 and 3228.9576 with selected cycles 0,30,52, giving 34.108492 d, near the Gaia 34.11518-d orbit. The shallow 8-9-ppt kind appears at 2181.1623, 2454.0263, 2488.1370, 2522.2480 and 3238.5280. Both kinds recur and are distinct. Raw and KSPSAP retain representative dips.

Gaia selection orbit: P=34.115181 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 0.33-0.40 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 43: target WCS xy=(4.40,4.10), deficit peak xy=[4, 4], offset 0.41 pixel. A 3x3 sky-corrected custom aperture measures 32.2 ppt on the same observing occasion (18 core and 126 baseline cadences). There are 53 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 5 | 1455.3169 | 27.3 | 0.344 | 0.042 |
| 32 | 2181.1623 | 7.5 | 0.338 | 0.014 |
| 42 | 2454.0263 | 7.5 | 0.358 | 0.021 |
| 43 | 2478.5706 | 28.9 | 0.341 | 0.021 |
| 43 | 2488.1370 | 7.7 | 0.349 | 0.021 |
| 44 | 2522.2480 | 8.0 | 0.353 | 0.028 |
| 70 | 3228.9576 | 27.4 | 0.340 | 0.002 |
| 71 | 3238.5280 | 7.5 | 0.342 | 0.002 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Selected same-kind timing artifact: lead-timing.json, P=34.10849161 d with explicit cycles and residuals. Its formal error is conditional on those selections.
Bounded integer-cycle coverage/null audit: lead-alias.json; tested 3 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [5, 32, 42, 43, 44, 70, 71]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: The stated period uncertainty is a selected-event scatter-inflated formal value; it does not include all reduction systematics.
Next check: No immediate physical check required in this bounded review; finish unresolved catalogue gates if novelty is needed.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T096); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.
