# Q065 — TIC 312243976

**Physical verdict:** REFUTED. **EB novelty:** UNKNOWN. **Review completion:** COMPLETE.

## Raw evidence

All eight sectors show continuing roughly day-scale oscillations with changing amplitude and sharper bright crests. The 27 dip flags sit at the oscillation troughs and the 16 bright flags at crests; S14/S15/S41/S54/S55/S75/S81/S82 do not show a discrete, stable eclipse shape or spacing. Many nominal cores are well sampled, so missing data are not needed to explain the pattern. Same-photon corrected flux changes the oscillation amplitude, leaving its source classification uncertain.

## Timing, physics and source

A pulsation or other modulation is a better light-curve description than repeated eclipses at Gaia SB1 P48.0345 d; no measured eclipse clock exists.

## Limits and next check

The variable-star mechanism and source attribution are not fixed by these light curves. This refutes the selected eclipse interpretation only.

Use independent extraction and frequency analysis if the non-eclipse variability is to be classified.

## Reproduction

`lead_context.py` verifies source-packet, bulk-result and FITS SHA-256 values, then plots raw SAP for all 8 cached sectors. `lead-context.json` and `lead-local-series.json` retain numeric time/flux, actual quality-zero coverage and gaps. `lead-flag-diagnostics.json` records core endpoints for 27 selected dip windows. `lead-alternate.png/json` compare reductions of the same photons. `lead-gaia-geometry.json` records source-specific orbital elements where used. `lead-neighbors.json` records MAST TIC cone data for Q061/Q068; `lead-timing.json` and `lead-extended-timing.json` contain measured eclipse centers. `lead-halfphase.json` records revised-clock shorter-alias checks; `lead-sector-availability.json` documents the Q062 availability discrepancy. The independent helper audit supplies pixel and WCS evidence. Screening centers are predictions, not measured eclipse times.
