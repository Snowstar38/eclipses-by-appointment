# Q063 — TIC 25194865

**Physical verdict:** REFUTED. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

Across 42 cached sectors the raw SAP curve repeatedly rises and falls over several days at variable amplitude and phase. The 34 selected dip flags sample broad wave minima, slopes and sector transitions, with bright flags on wave crests. S98 dips at 4010.65 and 4025.30 are broad evolving troughs, not the same narrow repeated event. S94 3874.87 lies at the shared gap feature and covers only 46% of its nominal core. KSPSAP and other same-photon reductions alter the waves, so their physical cause remains open.

## Timing, physics and source

No measured discrete same-kind eclipse centers, depth profile or alias-tested clock connects the waves to Gaia SB1 P52.3424 d.

## Limits and next check

This refutes the selected repeat-sector eclipse interpretation, not the existence of stellar variability or every possible weak eclipse.

Characterize the broad variability with an independent target-centered extraction if its source is of interest.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 42 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 34 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
