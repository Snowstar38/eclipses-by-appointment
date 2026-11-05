# Q064 — TIC 339768963

**Physical verdict:** REFUTED. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

S90 3759.63 is a weak broad undulation, S94 3874.90 has 27% of the predicted core across the common sector-gap feature, and S97 3954.71 is a one-sided decline/recovery beside a gap. S9 and S62 bright flags are broad baseline changes. Full raw context in the other 23 sectors does not show a matching closed eclipse profile.

## Timing, physics and source

The three selected dip timings do not yield a measured repeat period for Gaia SB1 P25.8876 d.

## Limits and next check

The selected morphology is refuted; a separate low-amplitude event elsewhere is not excluded.

Seek a continuous isolated ingress, bottom, and egress before timing or source attribution.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 26 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 3 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
