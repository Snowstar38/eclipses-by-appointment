# H022 — TIC 294257329

Physical verdict: **CONFIRMED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates were unavailable after a positive-control timeout. A primary-table nonmatch is not novelty clearance.

Gaia DR3 source 5668499078507408640, SB1 period 32.02240 d. Frozen stratum `cross_method_dip`; sample ID is not a new-system acceptance. Quality-zero raw SAP sectors inspected: 9, 35, 36, 62, 89, 100.

## Deciding evidence

Two eclipse kinds recur in raw SAP. Deeper complete events in s9/s36/s89/s100 fit a 32.02305 d clock over 79 cycles; shallower events in s9/s36/s62/s89 independently fit 32.02299 d. Gaia SB1 has P=32.02240 ± 0.00400 d and the fitted kinds fall within ~0.004 phase of opposite edge-on conjunctions. s62 has a fully sampled secondary trough at predicted BTJD 3005.80; its first eclipse starts in the flat bottom at sector entry. An independent TESSCut s36 aperture recovers ~139.5 ppt; difference centroid is 0.04 pixel from target and no individual Gaia neighbor within 60 arcsec is flux-capable under the approximate G-band bound.

## Limits and next check

Period and epoch are rounded local trapezoid estimates, not calibrated errors. s62 first event is partial; TESSCut and SAP share photons. Neighbor bound is bandpass and aperture dependent. Obtain independent future photometry and a precision ephemeris for publication.

## Reproducibility

`raw-inspection.json` verifies original bulk-result and FITS SHA-256 values and tabulates representative screening windows. `raw-windows.png` shows these raw windows; `orbit-context.json` and `.png` show full cached-sector SAP and Gaia edge-on conjunction predictions. Screening/conjunction times are not measured event centers. The frozen [source packet](../../source-packets/294257329/sources.json), [central novelty evidence](../../shared-catalogues/target-evidence.json), batch scripts and SHA256SUMS.json preserve receipts.

`local-fits.json` and `event-clock.json` preserve fitted centers, distinct eclipse kinds, conditional integer cycles, Gaia comparison and model limitations. [Independent pixel attribution](../helper-source-attribution.json) has Gaia/WCS neighbor positions, aperture extraction and difference image; the separate `lead-pixels` cutouts are retained with hashes.

The result epoch 1548.760 is the fitted multi-event clock intercept; the individual s9 center is 1548.745. The [s62 check](../helper-s62-check.json) resolves the apparent later flag as egress rather than a shifted center. The deeper kind is provisionally labeled primary; component identity is not determined.
