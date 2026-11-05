# Q033 — TIC 231632756

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

The S101 4113.263 flag ends in a gap after a monotonic decline, with only 49% nominal core coverage. S102 4133.117 follows a -7.41 ppt gap step and separate segment baseline; S103 4165.057 precedes a +29.15 ppt gap step and covers only 40% nominal core. The dramatic S94 unflagged trough near 3869 also coincides with the cross-target S94 segment break, so it is not a hidden clean recurrence.

The three selected dips do not supply measured eclipse centers or a repeat clock for the Gaia SB1 orbit.

## Scope and uncertainty

Other low-amplitude stellar variability may coexist with the documented gap/step artifacts. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 7 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 3 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Find an event with continuous ingress, core, egress, and two-sided baseline.
