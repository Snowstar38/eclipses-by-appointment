# Q062 — TIC 219377638

**Physical verdict:** PLAUSIBLE. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

S13 near BTJD 1677.47 contains a roughly 1% U-shaped SAP depression with both sides observed and a matching same-photon KSPSAP shape. The nominal 0.12 d core has 71% of expected quality-zero samples, but the local event is wider than the detector core. The S13 1670.18 feature is a level change, S94 3874.87 has only 42% core and the shared sector-gap morphology, and S98 4002.51/4010.08 are slopes or steps beside gaps. These do not establish a second matching eclipse.

## Timing, physics and source

One eclipse-like occasion remains, so no period or primary assignment follows from the Gaia SB1 P24.2104 d. A current official MAST TESSCut sector query was run at both the sealed target coordinates and the known S13 FITS-header coordinates. It returned the same inventory, but omitted the verified S13 QLP sector in both cases. Thus this endpoint is demonstrably incomplete for this target; newer-sector availability remains unknown and no extra light-curve null is claimed.

## Limits and next check

The S13 trough could be an eclipse or another transient/extraction feature; source ownership and recurrence remain unproved. The alternate reduction uses the same photons. Current availability could not be established from the inconsistent TESSCut endpoint.

Acquire a second complete matching dip with stable baseline and localized pixels.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 12 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 5 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
