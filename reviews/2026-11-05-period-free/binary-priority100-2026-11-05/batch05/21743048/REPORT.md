# T043 / TIC 21743048: PLAUSIBLE

Gaia DR3 1338435641930684672; queue stratum cross_method_dip; Gaia selection P=55.596013550568685 d. This is sample position T043, not a physical rank.

## Bounded physical finding

S78 selected 0.96-d window includes an abrupt raw-flux level drop and recovery with unequal pre/post baselines; an eclipse versus extraction/sector-level change cannot be decided from this event. The fold-screen 55.5943-d prediction in S25 has 21 core/23 side quality-zero cadences and -0.7 ppt deficit, but that predicted phase differs from the S78 period-free flag and is not a recurrence null for it. A new TESSCut S78 attempt has target x=5.76 close to near-zero edge columns x>=7; the integer-centered 3x3 mask includes x=7 and drifts by >10%, so it cannot reliably localize or veto the QLP event.

The source packet SHA-256 is `f304ac50b212752a9e604f7b2db5691df47604aa63de8b1bb8d80e4716ad70e5`. `lead-numeric.json` records SHA-256 of each used QLP FITS, raw quality-zero sector endpoints, cadence, largest internal gaps and representative screen-seed fits. The detector times and fold predictions are not assumed to be measured eclipse centers. `lead-fold-windows.json` records actual cadence coverage at the independently selected fold-screen period. The raw and pixel figures show deciding context. Source packet and FITS hashes were verified before measurement.

## Limits and next check

Only one insecure event at the selected phase, no measured clock, and an edge cutout with severe baseline drift. The S25 fold null constrains the fold-screen signal only.

Next: Obtain a stable pixel extraction and another observing occasion at an event-derived prediction.

Physical review completion: COMPLETE (bounded review of the selected claim). Catalogue novelty: UNKNOWN; shared seven-group work left VSX, ASAS-SN and Kostov 2025 tables 3/4 unqueried after failed positive controls. No new-system count follows from this physical verdict.

Supporting local artifacts: `lead-numeric.json`, `lead-fold-windows.json`, `lead-raw-01.png`, `lead-fold-stack.png`, `lead-s78-check.json`, `lead-s78-check.png`. Shared catalogue receipts: `../../shared-catalogues/TARGET-STATUS.csv` and `../../shared-catalogues/gaia-neighbors.json`. Helper independent findings: `../helper-audit.md`.
