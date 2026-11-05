# T019  -  TIC 220343379

**Verdict:** REFUTED; bounded review COMPLETE. **Catalogue novelty:** UNKNOWN (shared catalogue review has four unavailable VizieR gates; see `../../shared-catalogues/REPORT.md`). The selection stratum is cross_method_dip; queue rank is not physical evidence.

## Deciding evidence

S13/S94/S101 QLP flags lie on broad slopes or gap-associated changes. S103 QLP shows a ~14 ppt trough near 4165.0 BTJD, but the target-centered 5x5 TESSCut raw pixels decline gradually into the screen time, rise into a local bright cusp, then jump downward after a gap and resume a decline; the selected core is 3.37 ppt brighter than the separated baselines (108 core, 302/259 baseline quality-zero samples). The difference pattern is a position/level change, not a centered flux deficit. New S105 pixels cover 4205.818-4233.006 BTJD; around the conditional +1 Gaia center 4205.974 the flux smoothly declines from above the later baseline, with no 14 ppt repeat, though the sector edge leaves ingress untested. These are positive contrary shapes for the selected eclipse flags.

Raw SAP quality-zero local plots are `lead-raw-*.png`; the independent full-data diagnostic is `lead-fold.png`. `lead-numeric.json` records all screened flags and file/cadence hashes, `lead-timing.json` records curated same-kind clocks, `lead-coverage.json` records tested actual windows where applicable, and `lead-geometry.json` records the approximate Gaia conjunction comparison. Source-packet and shared-catalogue receipts are outside this batch folder; `../helper-audit.md` and helper artifacts document alternative reduction and source attribution where material. A corrected QLP flux and a custom TESSCut aperture share the same TESS photons.

## Limits and next check

New S105 starts 0.16 d before the conditional Gaia repeat, so it does not test a full ingress; the S103 alternate-pixel morphology is the decisive contrary evidence.

Do not use the flagged troughs as eclipse times; obtain an independent repeat only if later photometry reveals a clean dip.
