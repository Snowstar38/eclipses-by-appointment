# Q017 — TIC 288055150

**Physical verdict: REFUTED.** Bounded review of the selected eclipse claim; full review completion: COMPLETE. **Novelty: UNKNOWN.** The exact-queue shared catalogue leaves VSX, ASAS-SN, and Kostov table 3/4 gates unavailable; prior nonmatches cannot establish novelty.

## Evidence

S54 raw SAP declines from about 1.6 times its sector median toward zero on both spacecraft observing orbits, with ripples through the flagged windows. S55 repeats a rising ramp followed by a sharp reset. S14/S41/S81 do not show matching clean losses. These are large extraction or detector baseline pathologies, not normalizable isolated eclipse profiles.

Positive orbit-repeating pathological flux behavior refutes the selected eclipse windows.

## Limits and next check

No physically meaningful depth or eclipse epoch can be extracted from these segments; this does not exclude a different binary signal.

Check a stable independent photometric reduction before considering any eclipse timing.

## Reproducibility

`lead-inventory.json` records the actual quality-zero, finite positive SAP ranges, >0.2-day gaps, retained windows, source paths and SHA256 hashes. `lead-raw-overview.png` shows every cached sector. `lead-review.json` records this bounded interpretation and packet hash. The batch scripts reproduce raw overviews and the Q011/Q015 deciding checks. The independent `helper-audit.md` checks the pathological S54/S55 raw context.
