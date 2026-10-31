# TIC 325399242: bounded current-criteria review, 2026-10-31

Physical verdict: **CONFIRMED**. Full review completion: **COMPLETE_BOUNDED_REUSE**. This decision reviews the five present criteria, not the historical verdict label. Catalogue novelty is supplied separately by the central review and is not inferred here.

| Check | Assessment |
|---|---|
| Representative raw eclipses | PASS — Repeated primary and secondary raw events; five complete primary timing events are directly preserved in corrected ephemeris artifact. |
| Eclipse timing period | PASS — P=28.03808637 +/- 0.00021722 d; primary reference epoch 2830.458306 BTJD. |
| Source attribution | PASS within TESS/Gaia resolving power — representative deficit image inspected in helper audit, with capable-neighbour comparison. |
| Alternative reduction | PASS — TARS recovers both eclipse kinds. |
| Gaia geometry | PASS with limitations — Giant plus M dwarf geometry is viable; e cos omega differs by about 2 sigma. |

Adopted primary depth: 5 ppt (approximate, pipeline/aperture dependent). Timing uncertainties retain the limitations below.

Historical prose claims seven-event P=28.038374 +/-0.000191, but saved ephem_A and Afix each have five rows. Adopt corrected five-event artifact. Capable 13.2 arcsec neighbour is disfavoured at roughly 3–4 sigma per sector with systematic floor, not mathematically impossible.

Next useful check: Additional orientation/source-resolved imaging would strengthen close-neighbour rejection.

Evidence reused: REPORT.md, ephem_Afix.json, ephem_A.json, ephem_Bfix.json, ecl_Afix.json, tars.txt, physics.txt, ebfit_u60.json. Exact internal provenance and SHA256 are in batch evidence-sha256.csv; historical source hash matches queue. See terra/HELPER-AUDIT.md and its reproduction records for representative image review. Independent reductions share TESS photons and are reduction cross-checks, not an independent instrument. No exhaustive sector rerun or precision physical refit was performed. Historical files are untouched. This internal review must be sanitized with the central provenance before public export.


Public evidence: [historical report](../../evidence/325399242/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P003.
