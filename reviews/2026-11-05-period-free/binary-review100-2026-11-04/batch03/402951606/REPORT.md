# H028 — TIC 402951606

Physical verdict: **REFUTED**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates were unavailable after a positive-control timeout. A primary-table nonmatch is not novelty clearance.

Gaia DR3 source 2300554981056288128, SB1 period 30.66971 d. Frozen stratum `cross_method_dip`; sample ID is not a new-system acceptance. Quality-zero raw SAP sectors inspected: 18, 19, 20, 25, 26, 40, 52, 53, 58, 59, 60, 73, 78, 79, 85, 86.

## Deciding evidence

The only retained s59 dip at BTJD 2924.73 starts exactly at the post-gap low-flux recovery and relaxes monotonically over ~1 d; it has no ingress. Full 16-sector raw SAP context contains gap recoveries and low-amplitude baseline evolution, not a matching isolated eclipse.

## Limits and next check

Refutes this selected event as an eclipse; does not prove no other eclipse exists. Current sector inventory also lists s47, absent from cached QLP files, but cannot rescue the positive gap-recovery feature. Inspect a stable future conjunction if a separate signal is found.

## Reproducibility

`raw-inspection.json` verifies original bulk-result and FITS SHA-256 values and tabulates representative screening windows. `raw-windows.png` shows these raw windows; `orbit-context.json` and `.png` show full cached-sector SAP and Gaia edge-on conjunction predictions. Screening/conjunction times are not measured event centers. The frozen [source packet](../../source-packets/402951606/sources.json), [central novelty evidence](../../shared-catalogues/target-evidence.json), batch scripts and SHA256SUMS.json preserve receipts.

`sector-availability.raw` and `../sector-availability.json` record the current TESSCut sector inventory and response hash.
