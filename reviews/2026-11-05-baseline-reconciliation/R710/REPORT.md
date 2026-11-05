# TIC 380395732 — PROBABLE

Bounded physical review **COMPLETE**, ID R710. The sealed five-target queue position 3 is operational. Gaia DR3 source 5811126180682231040. Physical outcome and catalogue novelty are separate.

## Raw flux and cycle evidence

The sealed snapshot gives 7 QLP FITS receipts. `batch-shared/measure_raw.py` verified each SHA-256 and fitted representative quality-zero raw SAP windows with free centers. Raw event panels and all fits are in `raw-events.png` and `measurements.json`. The screen ephemeris located windows; its predictions are not timings.
5 usable same-kind centers span cycles 0–120; adjacent-cycle anchor: yes. Median realized trapezoid depth 31.18 ppt. The weighted fit gives P = 20.740076256 ± 0.000027345 d and selected-kind reference epoch BTJD 1644.99901738 ± 0.00261799 d at cycle 0. Center errors are max(formal covariance, half cadence), with scatter inflation if reduced χ² > 1; no model, pipeline or long-term systematic allowance is included.

| Sector | Cycle | Mid BTJD | Center error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 12 | 0 | 1645.00019 | 0.010417 | 29.46 |
| 13 | 1 | 1665.73916 | 0.010416 | 31.18 |
| 39 | 35 | 2370.90308 | 0.003472 | 32.16 |
| 66 | 71 | 3117.54413 | 0.001157 | 32.65 |
| 102 | 120 | 4133.80830 | 0.001157 | 27.15 |

`batch-shared/coverage-alias.json` samples actual main and opposite-phase quality-zero windows, requiring central samples and bilateral sidebands. Incomplete or flagged predictions are not clean nulls. Main clean sample: s12/c0 22.4 ppt (scatter 2.0), s13/c1 25.9 ppt (scatter 0.4), s39/c35 28.5 ppt (scatter 1.2), s66/c71 29.0 ppt (scatter 2.3), s102/c120 22.7 ppt (scatter 1.7).

## Source and orbit checks

A separate background-subtracted TESScut extraction of the same TESS photons gives 1×1/3×3/5×5 aperture losses 27.57/22.35/16.96 ppt in sector 13. The positive difference peak is 0.074 pixel from the target, a descriptive offset rather than a calibrated localization likelihood. QLP alternative apertures are one pipeline and are not independent reduction.
The full 60″ Gaia census has 47 sources and 2 capable other source(s) using the minimum measured aperture loss, G-band flux as a TESS proxy and optimistic full throughput. Required fractions are **intrinsic neighbor eclipses**, not blended pixel deficits. 5811126936596484864 at 52.68″ requires 0.651; 5811126554335380608 at 39.52″ requires 0.046.
Gaia SB1 P = 20.74270607 ± 0.00419563 d, e = 0.3663, mass function 0.1527 solar masses. The raw fitted period differs by -0.002630 d. The nearest edge-on conjunction to the measured epoch is -0.079 d (-0.0038 phase), with source-specific Gaia covariance linear error 0.276 d. This is a descriptive geometry check, not an ownership probability.

## Catalogue, outcome and next check

Exact prior EB identification in IJspeert et al. (2024): known recovery in the completed seven-group catalogue scope. Catalogue evidence is `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv` and its source receipts. No exhaustive literature novelty claim is made.

**Physical outcome: PROBABLE.** Two Gaia neighbors at 39.52 and 52.68 arcsec remain capable under an optimistic G-band/full-capture screen. The 5×5 pixel loss is diluted relative to the 1×1; source ownership needs higher spatial resolution.

**Next check:** Higher-resolution event photometry of the target and capable neighbors.

Alternative TESScut extraction uses the same photons as QLP, not another observing occasion. MAST QLP availability for the two sparse targets is documented in `batch-shared/helper-pixels/mast-availability.json`; no newer QLP sectors are listed.
