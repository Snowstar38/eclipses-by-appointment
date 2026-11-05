# Catalogue recovery handoff

Completed isolated recovery on actual tool clock 2026-11-05 00:45 UTC onward (workspace campaign label remains November 4). No accepted-batches, progress, original evidence or public files changed. `audit.py` verifies all 101 original files against `original-manifest.json`; all 21 original successful receipt JSONs and their raw hashes remain byte-identical. `current-failure-archive/` preserves current failures, receipts and logs before retry. Original historical failure archive is also copied within batch02.

Harvard VizieR recovered the known Kostov table4 control TIC10507 while IDIA, CDS and NAOJ timed out at eight seconds. The isolated batch02 retry used Harvard first and recovered all 13 target cones plus all six controls. All six controls recovered their expected identifiers: VSX Gaia DR3 4685168858707787776; ASAS-SN TIC441157335; Prsa TIC185259483; IJspeert TIC80452824; Kostov table3 TIC8636; table4 TIC10507. Fresh controls are now successful; original failed controls are retained as failures in the archive.

## Results requiring root adjudication

| Queue | TIC / Gaia DR3 | Catalogue disposition |
|---|---|---|
| batch02 | 24668377 / 2902439805151595008 | Exact prior IJspeert EB, both IDs; 0.018 arcsec. Recovery. |
| batch02 | 150465032 / 5587540216297835136 | No identified prior EB in searched scope. |
| batch02 | 331650047 / 550563615634343424 | No identified prior EB; exact VSX ROT retained as other-variable counterpart. |
| batch02 | 384744604 / 5776280282072990208 | No identified prior EB in searched scope. |
| batch02 | 109560492 / 5613374508997583232 | No identified prior EB in searched scope. |
| batch03 | 167197264 / 1868634515521921152 | No identified prior EB; exact VSX Gaia name, Type RS, at 0.06 arcsec is another-variable counterpart. |
| batch03 | 155346713 / 5694314546391164032 | Exact prior IJspeert EB, both IDs; 0.149 arcsec. Recovery regardless physical assessment. |
| C57 | 402940895 / 5816361019962769664 | No identified prior EB. VSX ASASSN-V J163852.99-635901.5 at 0.01 arcsec, ROT, 69.89 d; positional counterpart rather than literal TIC/Gaia match. SIMBAD SB*. |

All eight targets have complete executed scope and no under-five-arcsec EB identity alerts. C57's generic matrix `exact_other_variable_counterparts=[]` reflects literal identifier matching only: its close ROT counterpart is explicitly retained here and in raw VSX rows, and agrees with the historical coverage row. No physical verdict or new-system count is assigned by this catalogue task.

## Exact query scope and limits

Six VizieR tables: B/vsx/vsx and II/366/catv2021 at 60 arcsec; J/ApJS/258/16/tess-ebs, J/A+A/691/A242/obaf-eb1, J/ApJS/279/50/table3 and table4 at 5 arcsec. All columns, radial distance, maximum 100 rows (parser rejects >=100); raw replies and per-cone URLs, coordinates, UTC dates and SHA256s retained. Batch02 successful original receipts reused; its missing receipts recovered from equivalent Harvard cones. Batch03/C57 newly queried Harvard directly. Exact Gaia source-ID IN queries for DR3 vari_eclipsing_binary, vari_summary and nss_two_body_orbit use Heidelberg TAP; exact Gaia DR3 identifier SIMBAD query uses Harvard SIMBAD TAP. No bulk astronomy downloads.

All targets also have cached primary-source comparisons against Callahan2025 full 112-row ANC/SBTABLE.full.tex (TIC identity, eclipse flag), eight other cached heartbeat paper sources (exact numeric TIC token), public Chopard v1.2.0 track3_detail/dossier (Gaia and TIC), and Tarrants-Mendes cached same-parent cross-match plus primary HTML Gaia-string check. No target overlap in these comparisons. C57 was freshly included in these checks. Source paths, hashes and boundaries are in each heartbeat-overlaps.json, chopard-overlaps.json and tarrants-mendes-overlaps.json. Chopard embargoed identities/later releases, OGLE/KIC-only aliases and unsearched literature remain unexamined; this is scoped catalogue clearance, not universal proof of novelty.

## Reproducibility

`audit.json` stores exact target coordinates/identities, queue and matrix hashes and dispositions; `SHA256SUMS.json` hashes every evidence file. `audit.py` reparses all successful cone raws and verifies receipt/raw hash, table, coordinates, radius, maximum rows, locked queue and Gaia NSS identity coverage. Batch02 verify_controls.py additionally passes all six fresh controls and all 34 target/bulk receipts. Receipt counts: batch02 34, batch03 16, C57 10. Zero missing target checks or controls remain within this scope.

Locked queue hashes: batch02 `292eec2c110bdaf42f16a1c797dbb6e9e7e4e31179fc7be2839f9040d93c5c17`; batch03 `5c224f6294cb2dcb0ae0906f64305a91b74ed61c5a6d3488168b5922db8a6a97`; C57 `ee5bbdb8dd99bedeba0a6e3ae7e68053bb0d6483e804d6bf3fd4871598e2140c`.

Root must explicitly adjudicate revised novelty/addition identities; successful retries do not update accepted lists automatically. TIC155346713's physical plausibility is unchanged by its prior catalogue identification. Historical failed queries never serve as nonmatches.
