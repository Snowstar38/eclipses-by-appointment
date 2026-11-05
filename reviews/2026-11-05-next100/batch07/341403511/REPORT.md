# Q066 — TIC 341403511

**Physical verdict:** REFUTED. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

The S94 3874.874 selected core is 27% covered at the recurring shared gap feature; S94 3869.583 covers 53% beside a large level step. S101 4113.264 covers 48% and S103 4165.045 covers 41%, each clipped by a segment edge. Their local shapes are sloping baselines or one-sided recoveries, not full repeated U-shaped events.

## Timing, physics and source

No measured eclipse center sequence can be related to Gaia SB1 P41.3473 d.

## Limits and next check

The selected repeat-sector evidence is refuted; unrelated variability remains possible.

Require a fully observed event away from segment boundaries, then independent pixels.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 5 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 4 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
