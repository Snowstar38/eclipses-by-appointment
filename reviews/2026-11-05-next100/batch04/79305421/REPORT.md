# Q037 — TIC 79305421

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

S94 3874.939 is exactly at a data-gap boundary with only 26% nominal core coverage; its asymmetric decline/recovery matches the simultaneous S94 feature in several other targets. S104 4185.390 is a segment onset step, followed by a slow trend rather than an eclipse-shaped return. The two flagged windows therefore do not establish recurrence.

No measured same-kind period or Gaia conjunction association follows from the flagged structures.

## Scope and uncertainty

An unflagged independent eclipse elsewhere is not excluded. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 6 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 2 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Require an isolated two-sided event with a valid target-centered extraction.
