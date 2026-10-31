# TIC 23999420: bounded current-criteria review, 2026-10-31

Physical verdict: **CONFIRMED**. Full review completion: **COMPLETE_BOUNDED_REUSE**. This decision reviews the five present criteria, not the historical verdict label. Catalogue novelty is supplied separately by the central review and is not inferred here.

| Check | Assessment |
|---|---|
| Representative raw eclipses | PASS — Two complete primaries 33 cycles apart plus five repeating secondaries independently test period. |
| Eclipse timing period | PASS — P=22.127652 +/- 4.4e-05 d; primary reference epoch 2349.7517 BTJD. |
| Source attribution | PASS within TESS/Gaia resolving power — representative deficit image inspected in helper audit, with capable-neighbour comparison. |
| Alternative reduction | PASS — TARS and eleanor recover secondary; TARS also recovers primaries. |
| Gaia geometry | PASS with limitations — Both phases, durations and mass function fit evolved primary plus ~0.28 solar-mass M dwarf. |

Adopted primary depth: 22 ppt (approximate, pipeline/aperture dependent). Timing uncertainties retain the limitations below.

Adopt primary timing uncertainty 0.000044 d rather than joint model formal 0.000015 d. Secondary 9.7-sigma pixel regression is historical numerical evidence; representative image has no colour scale.

Next useful check: Recover missing/flagged s91 primary only if additional refinement needed.

Evidence reused: REPORT.md, ecl.json, ecl_allq.json, ebfit3_q0_L0.json, ephem.py, conj.json. Exact internal provenance and SHA256 are in batch evidence-sha256.csv; historical source hash matches queue. See terra/HELPER-AUDIT.md and its reproduction records for representative image review. Independent reductions share TESS photons and are reduction cross-checks, not an independent instrument. No exhaustive sector rerun or precision physical refit was performed. Historical files are untouched. This internal review must be sanitized with the central provenance before public export.


Public evidence: [historical report](../../evidence/23999420/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P007.
