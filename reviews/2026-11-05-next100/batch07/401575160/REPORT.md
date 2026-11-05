# Q070 — TIC 401575160

**Physical verdict:** REFUTED. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

S27 2047.17 is a smooth decline after a sharp bright excursion near 2046.65, not a closed dip. S94 3867.58 is a long monotonic decline and 3875.07 has only 26% predicted-core coverage at the recurring gap feature. S101 4112.56 is another steep multi-day slope. Bright flags track level changes and crests. These profiles are unlike one another and lack ingress and egress around the selected centers.

## Timing, physics and source

No measured eclipse clock connects the selected features to Gaia SB2 P24.9437 d.

## Limits and next check

The selected eclipse interpretation is refuted; the origin of broad trends remains unassigned.

Require a complete isolated profile with stable baseline and repeat timing.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 8 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 4 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
