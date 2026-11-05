# T098 - TIC 117404582

Physical verdict: **CONFIRMED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**.

Two eclipse kinds each recur: deep at 1795.4125 and 2908.5573 (~30 ppt), shallow at 1805.0055 and 2883.4018 (~16-18 ppt). Both same-kind separations select a 34.786-d clock near Gaia 34.7799 d; the relative phases distinguish the kinds. Additional s58/s86 retained features are not used as clock points. The P/2=17.3929-d alias predicts a deep eclipse at BTJD 1812.8054 in fully covered sector-18 raw SAP, where the light curve is flat through the expected 1.14-d core. Deep and shallow pairs independently give 34.78577 and 34.78698 d; adopt P=34.786 d with a conservative 0.002-d allowance. The selected clock also matches the eccentric Gaia conjunction spacing.

Gaia selection orbit: P=34.779925 d, SB1. Measured raw eclipse centers were compared against both edge-on Gaia conjunction kinds using the source-specific NSS covariance: nearest-conjunction absolute offsets span 0.93-1.50 propagated Gaia sigma across the selected events. Per-event measured times, predicted times, kinds, cycles and uncertainties are in lead-event-geometry.json. This conditional comparison alone cannot fix an unmeasured eclipse cycle count or source relationship.

## Source and reduction

TESScut sector 18: target WCS xy=(4.02,4.75), deficit peak xy=[4, 5], offset 0.25 pixel. A 3x3 sky-corrected custom aperture measures 29.9 ppt on the same observing occasion (7 core and 88 baseline cadences). There are 53 valid positive sky pixels. Gaia capable-neighbor list is in helper-pixel-audit.json; bandpass flux ratios alone are not attribution. This independently extracts the same photons; it is not another observing occasion.

## Raw observations

| Sector | Fitted center BTJD | Raw core deficit ppt | Fitted duration d | Local max gap d |
|---:|---:|---:|---:|---:|
| 18 | 1795.4125 | 33.1 | 1.157 | 0.042 |
| 18 | 1805.0055 | 17.9 | 0.945 | 0.125 |
| 58 | 2883.4018 | 13.4 | 0.953 | 0.002 |
| 58 | 2896.7831 | 4.3 | 1.643 | 0.333 |
| 58 | 2908.5573 | 23.8 | 1.135 | 0.005 |
| 86 | 3648.9617 | 7.0 | 0.399 | 0.007 |

These are period-free retained-window fits for inspection; a flag or fitted midpoint alone is not proof of an eclipse. Raw panels and complete source SHA256 values are in lead-raw-*.png and lead-numeric.json. Actual finite quality-zero cadence and endpoints are retained in its coverage array.

## Timing, catalogue, and limits

Selected same-kind timing artifact: lead-timing.json, P=34.78577420 d with explicit cycles and residuals. Its formal error is conditional on those selections.
Bounded integer-cycle coverage/null audit: lead-alias.json; tested 3 aliases, with each actual core and side-band cadence audit saved. Deciding shorter-alias windows were also plotted in lead-deciding-null-*.png; the numeric screen alone is not a physical veto.
Current Tesscut footprint query returns sectors [18, 58, 86]. This is sector availability, not an assertion that all have usable raw QLP files or sensitive eclipse windows.
Shared catalogue novelty gates remain unknown.
Limitation: The 0.002-d allowance covers the difference between two kind-specific pair periods; it is conservative, not calibrated one-sigma precision. KSPSAP suppresses broad dips; TESScut custom aperture confirms a representative event.
Next check: Finish unavailable novelty catalogues before any new-system claim.

## Provenance

Source packet: [local-path-redacted]
Shared catalogue evidence: [local-path-redacted] (row T098); shared 120-arcsec Gaia neighbor query and source receipts are in shared-catalogues.
Independent TESScut receipt: [local-path-redacted] The cached QLP FITS and SHA256 values used here are enumerated in lead-numeric.json.

The adopted conservative two-kind clock and P/2 test are in lead-t098-bounds.json. The deep-only selected formal fit in lead-timing.json is not the adopted uncertainty.