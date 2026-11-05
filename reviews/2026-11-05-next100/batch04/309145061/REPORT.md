# Q034 — TIC 309145061

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

The S9 1557.346 window begins at a segment gap and has 50% nominal core coverage; the raw series rises monotonically from the segment start. S10 1571.492 is a smooth decline flattening into a new level, while the alternate KSPSAP reduction is nearly flat. These are not two repeated eclipse profiles. Other sectors show large raw brightening spikes and boundary behavior, confirming this target has reduction/systematics complications.

The 14.146 d separation of two flagged windows is not a measured eclipse period or a secure half-cycle of Gaia SB1 P27.309 d.

## Scope and uncertainty

The diagnostics refute these selected windows as an eclipse train; they do not rule out a separate weak binary signal. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 23 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 2 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Review a fully covered event away from segment boundaries with target-centered pixels.
