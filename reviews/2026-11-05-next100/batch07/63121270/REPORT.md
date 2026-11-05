# Q069 — TIC 63121270

**Physical verdict:** REFUTED. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

S14 is dominated by a tens-of-percent evolving baseline with rapid oscillations, a major level transition near BTJD 1696, and strong bright crests. Selected S14 minima at 1694.49/1704.41/1705.41/1708.49 have different local shapes and ride the larger variation. S40/S41/S54/S55/S74/S75/S81/S82 show changing broad waves; S41 2422/2427 minima are several days wide and not the S14 shape. The alternate same-photon reductions damp some broad components but cannot by themselves identify the physical variable.

## Timing, physics and source

No discrete, repeated same-kind eclipse centers or alias-tested clock link these shapes to Gaia SB1 P20.9272 d.

## Limits and next check

The selected eclipse interpretation is refuted; the large-amplitude variability remains an interesting separate classification problem.

Use independent aperture photometry to classify the strong variable signal.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 9 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 6 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
