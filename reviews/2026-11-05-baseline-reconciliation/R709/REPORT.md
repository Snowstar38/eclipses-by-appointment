# TIC 70561926 — CONFIRMED

Bounded physical review **COMPLETE**, ID R709. The sealed five-target queue position 2 is operational. Gaia DR3 source 5637836688508288000. Physical outcome and catalogue novelty are separate.

## Raw flux and cycle evidence

The sealed snapshot gives 5 QLP FITS receipts. `batch-shared/measure_raw.py` verified each SHA-256 and fitted representative quality-zero raw SAP windows with free centers. Raw event panels and all fits are in `raw-events.png` and `measurements.json`. The screen ephemeris located windows; its predictions are not timings.
4 usable same-kind centers span cycles 0–103; adjacent-cycle anchor: no. Median realized trapezoid depth 15.34 ppt. The weighted fit gives P = 21.494190853 ± 0.000037811 d and selected-kind reference epoch BTJD 1523.06404178 ± 0.00323109 d at cycle 0. Center errors are max(formal covariance, half cadence), with scatter inflation if reduced χ² > 1; no model, pipeline or long-term systematic allowance is included.

| Sector | Cycle | Mid BTJD | Center error d | Depth ppt |
|---:|---:|---:|---:|---:|
| 8 | 0 | 1523.06427 | 0.010417 | 15.33 |
| 35 | 35 | 2275.35918 | 0.003472 | 15.83 |
| 62 | 69 | 3006.16354 | 0.001157 | 15.12 |
| 89 | 103 | 3736.96553 | 0.001157 | 15.35 |
The irregularly spaced four sectors fix the cycle count despite no adjacent pair: fitting s8→s35 as 35 cycles predicts s62/s89 within 0.0048 d, while 34 or 36 cycles miss s62 by 0.636 or 0.594 d. These are observed event-center residuals, not predicted-window nulls.

`batch-shared/coverage-alias.json` samples actual main and opposite-phase quality-zero windows, requiring central samples and bilateral sidebands. Incomplete or flagged predictions are not clean nulls. Main clean sample: s8/c0 15.3 ppt (scatter 0.5), s35/c35 15.9 ppt (scatter 1.2), s62/c69 15.8 ppt (scatter 1.4), s89/c103 15.1 ppt (scatter 1.4).

## Source and orbit checks

A separate background-subtracted TESScut extraction of the same TESS photons gives 1×1/3×3/5×5 aperture losses 16.31/15.94/15.13 ppt in sector 8. The positive difference peak is 0.044 pixel from the target, a descriptive offset rather than a calibrated localization likelihood. QLP alternative apertures are one pipeline and are not independent reduction.
The full 60″ Gaia census has 24 sources and 0 capable other source(s) using the minimum measured aperture loss, G-band flux as a TESS proxy and optimistic full throughput. Required fractions are **intrinsic neighbor eclipses**, not blended pixel deficits. No other Gaia source passes this optimistic capability test..
Gaia SB1 P = 21.53503235 ± 0.02439632 d, e = 0.2178, mass function 0.0011 solar masses. The raw fitted period differs by -0.040841 d. The nearest edge-on conjunction to the measured epoch is -1.392 d (-0.0646 phase), with source-specific Gaia covariance linear error 1.485 d. This is a descriptive geometry check, not an ownership probability.

## Catalogue, outcome and next check

VSX EA KELT KS22C028401 (OID 2213487), 0.30″ from the selected Gaia source, has P = 21.49257 d. The Gaia cone contains no second source within 2″ and the raw 21.49419-d clock agrees closely: target association is strongly supported and this is a **known recovery**, resolving the matrix identity alert. Catalogue evidence is `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv` and its source receipts. No exhaustive literature novelty claim is made.

**Physical outcome: CONFIRMED.** The Gaia period differs from the eclipse fit by 0.04084 d (1.67 Gaia quoted standard errors), and the closest conjunction is 1.39 d away with 1.48 d source-specific linear covariance uncertainty. The exact VSX counterpart is a known EB.

**Next check:** Compare a new timed eclipse and radial velocities with the Gaia orbit and VSX ephemeris.

Alternative TESScut extraction uses the same photons as QLP, not another observing occasion. MAST QLP availability for the two sparse targets is documented in `batch-shared/helper-pixels/mast-availability.json`; no newer QLP sectors are listed.
