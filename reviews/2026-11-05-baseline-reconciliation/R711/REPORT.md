# TIC 280950412 — PLAUSIBLE

Bounded physical review **COMPLETE**, ID R711. The sealed five-target queue position 4 is operational. Gaia DR3 source 5235048539475725696. Physical outcome and catalogue novelty are separate.

## Raw flux and cycle evidence

The sealed snapshot gives 8 QLP FITS receipts. `batch-shared/measure_raw.py` verified each SHA-256 and fitted representative quality-zero raw SAP windows with free centers. The weak phase panels are in `batch-shared/weak-phase-280950412.png` and diagnostic fits in `measurements.json`. The screen ephemeris located windows; its predictions are not timings.
No event passed the standard timing fit. A deliberately lower-threshold diagnostic in `batch-shared/weak-events-280950412.json` finds putative s11 BTJD 1603.60784 (1.28 ppt, local OOT scatter 0.61 ppt) and s64 BTJD 3061.50609 (1.16 ppt, scatter 2.15 ppt) minima. The s10 predicted window has no convincing deficit (0.23 ppt low-third against 1.85 ppt scatter), while s99 shows a broad baseline ramp. These are not accepted mid-times. The 64-cycle 22.77966-d quotient and screen 22.77774-d period are conditional aliases, not a measured ephemeris.

`batch-shared/coverage-alias.json` samples actual main and opposite-phase quality-zero windows, requiring central samples and bilateral sidebands. Incomplete or flagged predictions are not clean nulls. Main clean sample: s10/c0 0.2 ppt (scatter 0.8), s11/c1 0.8 ppt (scatter 0.8), s38/c34 0.3 ppt (scatter 0.8), s64/c65 0.8 ppt (scatter 1.8), s65/c66 0.1 ppt (scatter 2.1), s99/c109 0.1 ppt (scatter 4.0).
`batch-shared/sparse-aliases.json` tests integer-cycle alternatives with actual quality-zero central and bilateral sideband coverage. For the nominal 64-cycle 22.7797-d quotient, four windows are covered but none has local scatter below one-third of the putative 1.2-ppt depth. No tested alias is excluded by a sensitive clean null.

## Source and orbit checks

The s11/s64 custom TESScut reductions show 1×1/3×3/5×5 losses of 3.53/0.87/1.12 and 2.49/0.72/0.47 ppt, respectively. Strong aperture dependence and baseline uncertainty preclude a positive difference-image localization. The 60″ Gaia cone contains 169 sources, 57 of them conditionally capable at assumed 1.2 ppt under the G-band/full-throughput proxy; this is a capability screen, not evidence that all contaminate the aperture.
Gaia SB1 P = 22.78430874 ± 0.00669450 d, e = 0.3117, mass function 0.0700 solar masses. There is no accepted eclipse period to compare. The nearest edge-on conjunction to the unverified screen epoch is -4.958 d (-0.2176 phase), with source-specific Gaia covariance linear error 0.433 d. This is a descriptive geometry check, not an ownership probability.

## Catalogue, outcome and next check

No prior EB was identified in the completed seven-group queried catalogue scope. This is a catalogue statement only; a plausible physical outcome does not support a new-system claim. Catalogue evidence is `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv` and its source receipts. No exhaustive literature novelty claim is made.

**Physical outcome: PLAUSIBLE.** The two putative shallow dips are baseline- and aperture-dependent, with no reliable raw-event timing fit. All tested aliases lack sensitivity to a 1.2-ppt repeat; the screen conjunction is not a measured event. Severe crowding prevents source attribution.

**Next check:** Obtain a clean, sensitive repeat in a new TESS sector or ground-based time series before fitting an eclipse clock.

Alternative TESScut extraction uses the same photons as QLP, not another observing occasion. MAST QLP availability for the two sparse targets is documented in `batch-shared/helper-pixels/mast-availability.json`; no newer QLP sectors are listed.
