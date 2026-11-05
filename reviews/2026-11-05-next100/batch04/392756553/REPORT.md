# Q032 — TIC 392756553

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

S94 selected windows at 3869.644 and 3874.878 land exactly at actual data-gap boundaries; the former has a -7.42 ppt median step across its nearest gap, and the latter covers only 38% of its nominal core. S104 4197.371 likewise has only 44% nominal core coverage and an abrupt gap-associated recovery. S102 4144.319 is a shallow ripple/step on a changing baseline. The S94 3874.9 trough occurs at nearly the same time and shape in Q035/Q037/Q038/Q039 on multiple CCDs, so the selected repeat-sector pattern is common instrumental structure.

No stable same-kind eclipse train or source-specific Gaia conjunction timing can be measured from these flagged windows.

## Scope and uncertainty

Refutes the selected eclipse interpretation, not the possibility of a separate binary signal elsewhere in the target light curve. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 8 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 4 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Require a fully observed isolated trough in another sector before reopening an eclipse claim.
