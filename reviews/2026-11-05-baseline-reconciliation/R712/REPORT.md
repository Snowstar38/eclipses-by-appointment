# TIC 188908998 — PLAUSIBLE

Bounded physical review **COMPLETE**, ID R712. The sealed five-target queue position 5 is operational. Gaia DR3 source 1889426452191954176. Physical outcome and catalogue novelty are separate.

## Raw flux and cycle evidence

The sealed snapshot gives 2 QLP FITS receipts. `batch-shared/measure_raw.py` verified each SHA-256 and fitted representative quality-zero raw SAP windows with free centers. Raw event panels and all fits are in `raw-events.png` and `measurements.json`. The screen ephemeris located windows; its predictions are not timings.
2 usable same-kind centers span cycles 0–32; adjacent-cycle anchor: no. Median realized trapezoid depth 20.04 ppt. The weighted fit gives P = 22.704728116 ± 0.000061101 d and selected-kind reference epoch BTJD 2847.87330010 ± 0.00126054 d at cycle 0. Center errors are max(formal covariance, half cadence), with scatter inflation if reduced χ² > 1; no model, pipeline or long-term systematic allowance is included.

| Sector | Cycle | Mid BTJD | Center error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 56 | 0 | 2847.87330 | 0.001261 | 18.39 |
| 83 | 32 | 3574.42460 | 0.001495 | 21.69 |

`batch-shared/coverage-alias.json` samples actual main and opposite-phase quality-zero windows, requiring central samples and bilateral sidebands. Incomplete or flagged predictions are not clean nulls. Main clean sample: s56/c0 18.8 ppt (scatter 1.5), s83/c32 21.3 ppt (scatter 1.6).
`batch-shared/sparse-aliases.json` tests integer-cycle alternatives with actual quality-zero central and bilateral sideband coverage. The 31-cycle (23.4371 d) alternative has no sensitive intermediate window, as does the 32-cycle (22.7047 d) candidate; 33 cycles has one sensitive null. Thus Gaia agreement does not itself measure the cycle count.

## Source and orbit checks

A separate background-subtracted TESScut extraction of the same TESS photons gives 1×1/3×3/5×5 aperture losses 18.30/17.98/17.01 ppt in sector 56. The positive difference peak is 0.105 pixel from the target, a descriptive offset rather than a calibrated localization likelihood. QLP alternative apertures are one pipeline and are not independent reduction.
The full 60″ Gaia census has 15 sources and 2 capable other source(s) using the minimum measured aperture loss, G-band flux as a TESS proxy and optimistic full throughput. Required fractions are **intrinsic neighbor eclipses**, not blended pixel deficits. 1889473387594563968 at 29.27″ requires 0.654; 1889426383472478848 at 41.12″ requires 0.232.
Gaia SB1 P = 22.69849206 ± 0.00397110 d, e = 0.0980, mass function 0.2195 solar masses. The raw fitted period differs by +0.006236 d. The nearest edge-on conjunction to the measured epoch is +0.752 d (+0.0331 phase), with source-specific Gaia covariance linear error 0.509 d. This is a descriptive geometry check, not an ownership probability.

## Catalogue, outcome and next check

No prior EB was identified in the completed seven-group queried catalogue scope. This is a catalogue statement only; a plausible physical outcome does not support a new-system claim. Catalogue evidence is `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv` and its source receipts. No exhaustive literature novelty claim is made.

**Physical outcome: PLAUSIBLE.** Only two raw same-kind events, 32 putative cycles apart, have usable centers. The neighboring 31-cycle alias has no sensitive intermediate coverage, so the integer period is untested; two capable Gaia neighbors remain.

**Next check:** Observe a clean predicted eclipse to distinguish the 31- and 32-cycle aliases and localize the source.

Alternative TESScut extraction uses the same photons as QLP, not another observing occasion. MAST QLP availability for the two sparse targets is documented in `batch-shared/helper-pixels/mast-availability.json`; no newer QLP sectors are listed.
