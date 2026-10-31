# TIC 4808224: bounded current-criteria review, 2026-10-31

Physical verdict: **CONFIRMED**. Full review completion: **COMPLETE_BOUNDED_REUSE**. This decision reviews the five present criteria, not the historical verdict label. Catalogue novelty is supplied separately by the central review and is not inferred here.

| Check | Assessment |
|---|---|
| Representative raw eclipses | PASS — Five primary events give unique cycle count, supported by adjacent-cycle s8/s9; secondary repeats near phase 0.608. |
| Eclipse timing period | PASS — P=25.08348476 +/- 5.7e-05 d; primary reference epoch 1526.830229 BTJD. |
| Source attribution | PASS within TESS/Gaia resolving power — representative deficit image inspected in helper audit, with capable-neighbour comparison. |
| Alternative reduction | PASS — SPOC/TGLC primary and secondary reproduced from cached FITS in bounded helper check. |
| Gaia geometry | PASS with limitations — Gaia P differs by 2.33 sigma and secondary phase by ~1.6 sigma; physically viable M-dwarf companion remains. |

Adopted primary depth: 51 ppt (approximate, pipeline/aperture dependent). Timing uncertainties retain the limitations below.

Single-sector s89 pixel test; pulsation affects secondary depth/timing. Discard s35 secondary fit: all input points flagged and optimiser wandered. Approximate physics.py formula has pi/4 error; exact Kepler-grid result is used.

Next useful check: Another orientation pixel test or improved RV orbit would reduce association uncertainty.

Evidence reused: REPORT.md, ephem.json, ecl.json, secfit.json, conj.json, physics.py. Exact internal provenance and SHA256 are in batch evidence-sha256.csv; historical source hash matches queue. See terra/HELPER-AUDIT.md and its reproduction records for representative image review. Independent reductions share TESS photons and are reduction cross-checks, not an independent instrument. No exhaustive sector rerun or precision physical refit was performed. Historical files are untouched. This internal review must be sanitized with the central provenance before public export.


Public evidence: [historical report](../../evidence/4808224/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P006.
