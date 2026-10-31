# TIC 262653359: bounded current-criteria review, 2026-10-31

Physical verdict: **CONFIRMED**. Full review completion: **COMPLETE_BOUNDED_REUSE**. This decision reviews the five present criteria, not the historical verdict label. Catalogue novelty is supplied separately by the central review and is not inferred here.

| Check | Assessment |
|---|---|
| Representative raw eclipses | PASS — Seven raw events; six usable timing events, s66 background-distorted and excluded. |
| Eclipse timing period | PASS — P=46.1290484 +/- 8e-05 d; primary reference epoch 3489.276184 BTJD. |
| Source attribution | PASS within TESS/Gaia resolving power — representative deficit image inspected in helper audit, with capable-neighbour comparison. |
| Alternative reduction | PASS — Four-sector custom TESScut reproduces 3.08–3.16% events. |
| Gaia geometry | PASS with limitations — Conjunction B consistent; missing A allowed by grazing geometry. Companion light is mildly high for nominal dwarf mass. |

Adopted primary depth: 31 ppt (approximate, pipeline/aperture dependent). Timing uncertainties retain the limitations below.

Period uncertainty widened to 0.00008 d: saved floor-fit output gives 0.000072 d, wider than prose 0.00005. Mass and evolutionary state leave factor ~2 light-ratio uncertainty.

Next useful check: Spectroscopy or colour eclipse photometry to constrain companion light.

Evidence reused: REPORT.md, ephem_all.json, ephem_pipes.txt, ecl_all.json, tcphot.txt, phys.txt, ab.txt. Exact internal provenance and SHA256 are in batch evidence-sha256.csv; historical source hash matches queue. See terra/HELPER-AUDIT.md and its reproduction records for representative image review. Independent reductions share TESS photons and are reduction cross-checks, not an independent instrument. No exhaustive sector rerun or precision physical refit was performed. Historical files are untouched. This internal review must be sanitized with the central provenance before public export.


Public evidence: [historical report](../../evidence/262653359/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P001.
