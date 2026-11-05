# Q040 — TIC 233301662

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

Across ten sectors the raw light curve has smooth high-amplitude waves and long monotonic slopes; the five retained dip flags at 2431.832, 3325.324, 3352.302, 3380.106, and 3564.256 sample those slopes or discontinuities. S74/S75/S76 centers are about 27–28 d apart, but their local traces are still declining at the flagged time, without an isolated core and egress. Numerous bright flags mark the same oscillatory wave and segment jumps.

The selected windows do not demonstrate detached eclipses or a measured eclipse period. S41 SAP slope is largely suppressed by KSPSAP, so the broad modulation cannot be positively classified as astrophysical from these reductions alone.

## Scope and uncertainty

The mechanism of the smooth SAP modulation is unresolved; broad eclipses beneath it are not mathematically excluded. This verdict refutes the selected repeat-dip evidence only. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 10 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 5 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Check independent reductions and pixels for the broad modulation; revisit residuals if an isolated eclipse appears.
