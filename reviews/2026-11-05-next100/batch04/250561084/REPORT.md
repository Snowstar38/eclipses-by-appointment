# Q036 — TIC 250561084

**Physical verdict:** REFUTED. **Novelty:** UNKNOWN. **Completion:** COMPLETE.

## Evidence

Four sharp ~10 ppt raw SAP dips occur in S18 at BTJD 1792.5226, 1798.6643, 1804.8080, and 1810.9590, each with ingress and egress visible in SAP and KSPSAP. S85 adds three similarly deep events at 3618.0014, 3624.1476, and 3630.2890; the middle one was not retained by the screening flags and was recovered in raw context. The long separation is conditional on 297, 298, and 299 cycles at ~6.1464 d, with later S85 residuals -0.0002 and -0.0052 d. Adjacent integer aliases shift the four S18 events relative to the narrow profiles. Covered P/3 predictions in S18/S85 are generally flat, while P/2 windows can have shallow structure but not matching ~10 ppt same-kind dips.

The photometric period is grossly inconsistent with Gaia SB1 P20.14331 d; the observed S18 center is ~0.18 Gaia orbital phase from either edge-on conjunction. Fresh S18 and S85 TESSCut WCS cutouts identify Gaia DR3 358527789513614336 (G15.339, 28.90 arcsec north) as the favored dimming source. After corner-sky subtraction and per-pixel local sideband detrending, both difference maps peak at the neighbor WCS pixel (5,7). Positive deficit centroids are 0.29/0.10 pixel from the neighbor and 1.12/1.31 pixels from the queued target. Disjoint target-side and neighbor-side x4..6 stripes lose 8.43 versus 37.69 e/s in S18 and 4.00 versus 39.99 e/s in S85, despite the target-side baseline being brighter. The G flux ratio 0.0281 makes the blended loss feasible for a deep neighbor eclipse. This refutes attribution of the selected eclipse train to the queued target, while preserving a real neighboring EB lead.

## Scope and uncertainty

The ~6.1464 d period and ~10 ppt depth describe the off-target lead and are omitted from the queued target RESULTS fields. Target and neighbor are separated by ~1.4 TESS pixels; PRF overlap and similar S18/S85 WCS orientation limit precision localization, but both corrected maps and disjoint aperture strips favor the neighbor. One S85 event lies close to a gap, and local Gaussian timing is diagnostic; no precision period uncertainty is supplied. This does not exclude unrelated binarity of TIC 250561084. The catalogue gate for this exact queue failed; cached primary nonmatch does not establish novelty. The representative raw SAP context plots all 2 cached sectors. `lead-context.json` records source SHA-256, actual quality-zero positive-flux cadence coverage, gaps and all selected flags. `lead-local-series.json` preserves the numerical flagged-window time series. `lead-flag-diagnostics.json` records actual core endpoints and gaps for all 6 selected dip windows. Screening centers are predictions; fitted centers, where used, are separate diagnostic measurements. The independent `../helper-audit.md` and helper numeric receipts provide separate source and coverage checks.

## Reproduction and next check

Run `python lead_context.py`, `python lead_flag_diagnostics.py`, and for Q031/Q036 `python lead_timing.py` and `python lead_alias_geometry.py` from this batch directory. All scripts assert the sealed source-packet and used FITS hashes. The alternative KSPSAP flux shares the same observing photons and is displayed in `lead-dip-zooms.png` where present. For Q036, `../OFF-TARGET-LEADS.json` records the separate neighbor identification.

Review Gaia DR3 358527789513614336 as a separate eclipsing object and obtain a resolved next event.
