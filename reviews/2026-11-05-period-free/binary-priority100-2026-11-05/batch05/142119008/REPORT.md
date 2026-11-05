# T048 / TIC 142119008: REFUTED

Gaia DR3 558116779478994304; queue stratum cross_method_dip; Gaia selection P=37.31191652466777 d. This is sample position T048, not a physical rank.

## Bounded physical finding

The S26 QLP flag comprises two isolated ~9.6-ppt low cadences with intervening baseline cadences, not a contiguous ingress/egress. A simultaneous flux-bearing target-centered TESSCut 3x3 aperture (10.4k electrons/s side baseline) has no matching dips and rises across the selected core; QLP raw core median deficit is 4.50 ppt while TESSCut raw core is a 9.88-ppt brightening. Six actually covered fold-screen windows are mostly flat. This positively refutes the selected target eclipse interpretation.

The source packet SHA-256 is `e60a97765424b94e1346a56b356d7ffbf257bce22ec51cbabb4ef378d016c124`. `lead-numeric.json` records SHA-256 of each used QLP FITS, raw quality-zero sector endpoints, cadence, largest internal gaps and representative screen-seed fits. The detector times and fold predictions are not assumed to be measured eclipse centers. `lead-fold-windows.json` records actual cadence coverage at the independently selected fold-screen period. The raw and pixel figures show deciding context. Source packet and FITS hashes were verified before measurement.

## Limits and next check

TESSCut outer-pixel background has 15.5% zero pixels, so its background-subtracted curve is invalid and excluded; the raw 3x3 comparison is used. A different unobserved orbit is not excluded.

Next: Revisit only if an independent observing occasion supplies a coherent dip.

Physical review completion: COMPLETE (bounded review of the selected claim). Catalogue novelty: UNKNOWN; shared seven-group work left VSX, ASAS-SN and Kostov 2025 tables 3/4 unqueried after failed positive controls. No new-system count follows from this physical verdict.

Supporting local artifacts: `lead-numeric.json`, `lead-fold-windows.json`, `lead-raw-01.png`, `lead-fold-stack.png`, `lead-cutout.json`, `lead-cutout.png`, `lead-qlp-cutout-compare.png`. Shared catalogue receipts: `../../shared-catalogues/TARGET-STATUS.csv` and `../../shared-catalogues/gaia-neighbors.json`. Helper independent findings: `../helper-audit.md`.
