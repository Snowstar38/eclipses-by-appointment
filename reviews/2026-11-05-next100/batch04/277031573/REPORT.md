# Q039 — TIC 277031573

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

S94 3874.893 is at a gap (29% nominal core), coincident with the S94 feature in several other targets. S101 4119.117 is a small sag touching a segment break, and S102 4145.375 terminates at a gap with only 29% nominal core. The latter two do not repeat the S94 asymmetry or supply same-kind eclipse centers.

No measured eclipse clock supports associating the selected windows with Gaia SB1 P27.688 d.

## Scope and uncertainty

A separate weak eclipse is not disproved; the selected detector windows are inadequate. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 9 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 3 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Obtain complete ingress/core/egress away from the observed gaps.
