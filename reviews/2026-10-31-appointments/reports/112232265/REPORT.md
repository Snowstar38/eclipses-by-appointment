# TIC 112232265: bounded current-criteria review, 2026-10-31

Physical verdict: **CONFIRMED**. Full review completion: **COMPLETE_BOUNDED_REUSE**. This decision reviews the five present criteria, not the historical verdict label. Catalogue novelty is supplied separately by the central review and is not inferred here.

| Check | Assessment |
|---|---|
| Representative raw eclipses | PASS — Six TESScut events span epochs -52 to +47; two forward-predicted events recovered within a minute. |
| Eclipse timing period | PASS — P=28.40515 +/- 3e-05 d; primary reference epoch 2978.3647 BTJD. |
| Source attribution | PASS within TESS/Gaia resolving power — representative deficit image inspected in helper audit, with capable-neighbour comparison. |
| Alternative reduction | PASS — SPOC, eleanor and TGLC recover eclipses; independent custom aperture reduces neighbour pulsation. |
| Gaia geometry | PASS with limitations — B conjunction, grazing duration and absent A fit Gaia geometry; companion light is tight but viable. |

Adopted primary depth: 33 ppt (approximate, pipeline/aperture dependent). Timing uncertainties retain the limitations below.

Intrinsic depth approximately 30–36 ppt; custom 3x3 is diluted (~19 ppt), QLP background affects depth. RUWE 3.51 allows third-body uncertainty. T16 parse with zero cadences is not evidence.

Next useful check: Spectroscopy and source-resolved eclipse depths to constrain companion.

Evidence reused: REPORT.md, step3.txt, pipe2.txt, mypix.py, myphys.py. Exact internal provenance and SHA256 are in batch evidence-sha256.csv; historical source hash matches queue. See terra/HELPER-AUDIT.md and its reproduction records for representative image review. Independent reductions share TESS photons and are reduction cross-checks, not an independent instrument. No exhaustive sector rerun or precision physical refit was performed. Historical files are untouched. This internal review must be sanitized with the central provenance before public export.


Public evidence: [historical report](../../evidence/112232265/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P008.
