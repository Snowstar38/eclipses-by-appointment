# T011  -  TIC 355493553

**Verdict:** REFUTED; bounded review COMPLETE. **Catalogue novelty:** UNKNOWN (shared catalogue review has four unavailable VizieR gates; see `../../shared-catalogues/REPORT.md`). The selection stratum is cross_method_dip; queue rank is not physical evidence.

## Deciding evidence

The screened S96 raw QLP SAP appears about 6% low immediately after a 1.3 d gap and rises over 0.7 d, but a target-centered 5x5 extraction from the same S96 TESSCut raw pixels is 54.7 ppt brighter than pre/post baselines during 3921.796-3921.946 BTJD (65 core, 432/432 baseline quality-zero samples). Its pixel light curve is a positive recovery, contradicting an astrophysical eclipse deficit in the target pixels. Conditional Gaia-period windows S102 +4 and S104 +5 are fully covered at +/-0.6 d with 519/514 samples and essentially zero deficit. New S105 raw pixels cover 4206.21-4233.00 BTJD, showing no comparable dip; the next conditional Gaia center lies outside coverage. The candidate eclipse flag is a gap/processing artifact; this does not deny the Gaia binary.

Raw SAP quality-zero local plots are `lead-raw-*.png`; the independent full-data diagnostic is `lead-fold.png`. `lead-numeric.json` records all screened flags and file/cadence hashes, `lead-timing.json` records curated same-kind clocks, `lead-coverage.json` records tested actual windows where applicable, and `lead-geometry.json` records the approximate Gaia conjunction comparison. Source-packet and shared-catalogue receipts are outside this batch folder; `../helper-audit.md` and helper artifacts document alternative reduction and source attribution where material. A corrected QLP flux and a custom TESSCut aperture share the same TESS photons.

## Limits and next check

The S96 QLP dip resumes after a 1.3 d gap, but target-centered S96 TESSCut raw pixels show an opposite-sign brightening/recovery. S105 does not cover the next +6 Gaia-cycle center at 4234.5 BTJD; its strong bright spike at 4219 is not an eclipse.

No eclipse follow-up from the S96 flag; independently investigate the QLP/raw-pixel discrepancy if this star is otherwise of interest.
