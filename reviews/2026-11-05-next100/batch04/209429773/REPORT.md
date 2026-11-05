# Q031 — TIC 209429773

**Physical verdict:** CONFIRMED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

Three same-kind raw SAP dips at BTJD 2123.0984 (S30), 2165.6410 (S31), and 3952.2486 (S97) support a conditional 43-cycle period of 42.5384 d. The middle event misses that prediction by only +0.0042 d, whereas the adjacent 42/44 long-baseline aliases miss it by -1.009/+0.971 d. S31 also has a distinct shallower event near 2146.48, which is treated as another eclipse kind rather than a half-cycle constraint. The S97 main event retains a full measured core and baseline; S31 main event is close to a gap, so its Gaussian timing is diagnostic. A covered S97 P/2 prediction at 3973.518 has -0.15 ppt local depth with 138 of 138 expected core cadences, versus ~5.6 ppt in the observed S97 event; covered P/3 and P/4 predictions are also flat.

Gaia SB1 P42.54056 d agrees with the conditional eclipse clock. Source-specific edge-on A conjunction is BTJD 2123.1794, 0.0810 d after the measured S30 center (phase -0.0019). Fresh 11x11 TESSCut target-centered extractions retain 5.26, 4.28, and 6.17 ppt losses in S30/S31/S97, with difference centroids 0.26, 0.14, and 0.11 pixel from target WCS. The nearest other Gaia source in 120 arcsec is G16.67 at 31.6 arcsec, with nominal G flux ratio only ~0.0006 to this G8.61 target; this favors target ownership.

## Scope and uncertainty

Same-photon KSPSAP and TESSCut extractions are alternate reductions, not new observing occasions. The S31 ingress is near a 0.153-day gap and local Gaussian centers depend on baseline and morphology; the catalogue period column is rounded to 42.54 d and no precision period error is justified. Gaia G flux contrast is bandpass dependent, while the WCS evidence supplies the stronger source-location check. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 4 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 4 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Obtain a later clean target-centered main eclipse to refine the timing and check for an unresolved close companion.
