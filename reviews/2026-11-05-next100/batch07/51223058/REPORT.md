# Q067 — TIC 51223058

**Physical verdict:** NON_ECLIPSE_VARIABLE. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

S54/S55/S81 show smooth multi-day troughs and asymmetric recoveries near BTJD 2778, 2799, 2820 and 3527. The SAP trough width is several days, with changing local slope; S54/S55 KSPSAP suppresses much of it, but that same-photon reduction alone is not artifact proof. This is the independently studied HD 193389 heartbeat H1: earlier Fable vet8 raw, TESS-SPOC, pixel and tidal-model analysis found recurring periastron-linked modulation and no fitted eclipse component at the claimed depth.

## Timing, physics and source

The local prior analysis favors equilibrium-tide heartbeat modulation on Gaia SB1 P20.79663 d; the trough occurs after predicted A conjunction. It is not a repeated occultation. This batch independently verifies raw morphology, rather than claiming a new EB.

## Limits and next check

The positive non-eclipse classification recovers prior heartbeat H1 in the existing paper rather than claiming a new variable; no isolated eclipse is supported at the selected depth. EB novelty remains separate from that heartbeat result.

Retain as heartbeat H1 in the non-eclipse catalogue; no new EB claim.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 3 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 4 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
