# TIC 39013890: bounded current-criteria review, 2026-10-31

Physical verdict: **CONFIRMED**. Full review completion: **COMPLETE_BOUNDED_REUSE**. This decision reviews the five present criteria, not the historical verdict label. Catalogue novelty is supplied separately by the central review and is not inferred here.

| Check | Assessment |
|---|---|
| Representative raw eclipses | PASS — Three primaries and four secondaries repeat, including flagged QLP primary recovered in other reductions. |
| Eclipse timing period | PASS — P=20.92352919 +/- 3e-06 d; primary reference epoch 1859.073426 BTJD. |
| Source attribution | PASS within TESS/Gaia resolving power — representative deficit image inspected in helper audit, with capable-neighbour comparison. |
| Alternative reduction | PASS — TESS-SPOC and TARS recover both eclipse kinds. |
| Gaia geometry | PASS with limitations — Both conjunctions and secondary phase fit Gaia; a G+M geometry fits durations and light ratio. |

Adopted primary depth: 157 ppt (approximate, pipeline/aperture dependent). Timing uncertainties retain the limitations below.

Unresolved third light remains possible (ipd multi-peak 69%; RUWE 1.55), affecting derived radii and geometry precision.

Next useful check: Resolve close companion or constrain third light spectroscopically.

Evidence reused: REPORT.md, ephem2.json, evt.json, secondpipe.txt, secondpipe_tars.txt, phys.txt. Exact internal provenance and SHA256 are in batch evidence-sha256.csv; historical source hash matches queue. See terra/HELPER-AUDIT.md and its reproduction records for representative image review. Independent reductions share TESS photons and are reduction cross-checks, not an independent instrument. No exhaustive sector rerun or precision physical refit was performed. Historical files are untouched. This internal review must be sanitized with the central provenance before public export.


Public evidence: [historical report](../../evidence/39013890/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P002.
