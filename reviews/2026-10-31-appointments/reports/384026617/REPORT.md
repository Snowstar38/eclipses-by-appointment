# TIC 384026617: bounded current-criteria review, 2026-10-31

Physical verdict: **CONFIRMED**. Full review completion: **COMPLETE_BOUNDED_REUSE**. This decision reviews the five present criteria, not the historical verdict label. Catalogue novelty is supplied separately by the central review and is not inferred here.

| Check | Assessment |
|---|---|
| Representative raw eclipses | PASS — Nine primary and eight secondary events reported; saved primary/secondary timing artifacts give concordant periods. |
| Eclipse timing period | PASS — P=30.05386902 +/- 5.444e-05 d; primary reference epoch 2903.27302 BTJD. |
| Source attribution | PASS within TESS/Gaia resolving power — representative deficit image inspected in helper audit, with capable-neighbour comparison. |
| Alternative reduction | PASS — TGLC suppresses neighbour pulsation while preserving eclipses; SPOC also recovers primary. |
| Gaia geometry | PASS with limitations — Both eclipse geometries support the Gaia binary with moderate joint e-vector tension (~2.1 sigma). |

Adopted primary depth: 47.2 ppt (approximate, pipeline/aperture dependent). Timing uncertainties retain the limitations below.

Historical 0.6 arcsec WDS pair is doubtful but unresolved by TESS; attribution is to the Gaia source footprint. Gaia statistics alone do not prove pair spurious.

Next useful check: High angular resolution imaging to check historical WDS component.

Evidence reused: REPORT.md, eclfixA_ephem.json, eclfixA_allq_ephem.json, eclfixS_ephem.json, secondpipe2.txt, physics.txt. Exact internal provenance and SHA256 are in batch evidence-sha256.csv; historical source hash matches queue. See terra/HELPER-AUDIT.md and its reproduction records for representative image review. Independent reductions share TESS photons and are reduction cross-checks, not an independent instrument. No exhaustive sector rerun or precision physical refit was performed. Historical files are untouched. This internal review must be sanitized with the central provenance before public export.


Public evidence: [historical report](../../evidence/384026617/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P004.
