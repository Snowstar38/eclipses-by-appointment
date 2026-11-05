# TIC 257992903 — PROBABLE

Bounded physical review **COMPLETE**, ID R708. The sealed five-target queue position 1 is operational. Gaia DR3 source 5644757117781650560. Physical outcome and catalogue novelty are separate.

## Raw flux and cycle evidence

The sealed snapshot gives 5 QLP FITS receipts. `batch-shared/measure_raw.py` verified each SHA-256 and fitted representative quality-zero raw SAP windows with free centers. Raw event panels and all fits are in `raw-events.png` and `measurements.json`. The screen ephemeris located windows; its predictions are not timings.
5 usable same-kind centers span cycles 0–106; adjacent-cycle anchor: yes. Median realized trapezoid depth 40.08 ppt. The weighted fit gives P = 20.587598859 ± 0.000033973 d and selected-kind reference epoch BTJD 1524.55598079 ± 0.00280634 d at cycle 0. Center errors are max(formal covariance, half cadence), with scatter inflation if reduced χ² > 1; no model, pipeline or long-term systematic allowance is included.

| Sector | Cycle | Mid BTJD | Center error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 8 | 0 | 1524.55704 | 0.010417 | 39.84 |
| 34 | 35 | 2245.12306 | 0.003472 | 40.08 |
| 61 | 70 | 2965.68777 | 0.001157 | 40.62 |
| 61 | 71 | 2986.27534 | 0.001157 | 40.57 |
| 88 | 106 | 3706.84161 | 0.001157 | 39.84 |

`batch-shared/coverage-alias.json` samples actual main and opposite-phase quality-zero windows, requiring central samples and bilateral sidebands. Incomplete or flagged predictions are not clean nulls. Main clean sample: s8/c0 38.3 ppt (scatter 0.9), s34/c35 39.0 ppt (scatter 1.3), s61/c70 39.2 ppt (scatter 2.1), s61/c71 39.3 ppt (scatter 1.8), s88/c106 38.4 ppt (scatter 2.1).

## Source and orbit checks

A separate background-subtracted TESScut extraction of the same TESS photons gives 1×1/3×3/5×5 aperture losses 41.95/44.15/43.52 ppt in sector 8. The positive difference peak is 0.071 pixel from the target, a descriptive offset rather than a calibrated localization likelihood. QLP alternative apertures are one pipeline and are not independent reduction.
The full 60″ Gaia census has 60 sources and 2 capable other source(s) using the minimum measured aperture loss, G-band flux as a TESS proxy and optimistic full throughput. Required fractions are **intrinsic neighbor eclipses**, not blended pixel deficits. 5644757049062168832 at 47.26″ requires 0.934; 5644757049062165888 at 54.64″ requires 0.256.
Gaia SB1 P = 20.58983366 ± 0.00788580 d, e = 0.5732, mass function 0.0444 solar masses. The raw fitted period differs by -0.002235 d. The nearest edge-on conjunction to the measured epoch is -0.290 d (-0.0141 phase), with source-specific Gaia covariance linear error 0.726 d. This is a descriptive geometry check, not an ownership probability.

## Catalogue, outcome and next check

Exact prior EB identification in IJspeert et al. (2024): known recovery in the completed seven-group catalogue scope. Catalogue evidence is `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv` and its source receipts. No exhaustive literature novelty claim is made.

**Physical outcome: PROBABLE.** Two Gaia neighbors at 47.26 and 54.64 arcsec remain capable under an optimistic G-band/full-capture screen; the target-like pixel deficit does not calibrate source ownership.

**Next check:** Higher-resolution photometry during a predicted event to identify the eclipsing Gaia source.

Alternative TESScut extraction uses the same photons as QLP, not another observing occasion. MAST QLP availability for the two sparse targets is documented in `batch-shared/helper-pixels/mast-availability.json`; no newer QLP sectors are listed.
