# Q035 — TIC 300557107

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

S64 3054.743 runs directly into a gap (45% nominal core); S64 3060.986 is a shallow broad sag without the same narrow morphology. The S94 3874.870 flag sits at a gap with only 30% nominal core coverage and is synchronous with the common multi-target 3874.9 feature. S96 3913.957 and S97 3966.607 are rising/declining segment baselines beside gaps rather than repeated symmetric cores. All 41 sector light curves were viewed in raw context.

No consistent eclipse kind or source-specific period emerges from the five selected windows.

## Scope and uncertainty

A smaller isolated event may be hidden under the substantial sector-to-sector variability; the refutation is of the selected repeat-sector evidence. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 41 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 5 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Search for a complete event in a stable segment, then assess spatial ownership.
