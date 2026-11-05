# Q038 — TIC 351554371

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

S94 3874.807 sits at a gap endpoint with only 28% nominal core coverage and the same asymmetric common feature as Q032/Q035/Q037/Q039. S94 3867.605 is a long monotonic segment decline rather than a closed trough. S103 4159.656 begins after a large baseline step, and 4166.538 is the start of a rising segment after a gap; neither reproduces an eclipse profile. S13 shows other shallow variability, but no secure repeated dip kind.

The four flags do not yield event-derived orbital timing for Gaia SB1 P40.662 d.

## Scope and uncertainty

The selected eclipse interpretation is refuted; unrelated low-level astrophysical variability is unresolved. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 5 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 4 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Use an independent continuous eclipse profile before assigning a binary period.
