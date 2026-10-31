# Fixed 40 scoped catalogue reconciliation

All 40 queue targets have successful fresh 2026-10-31 coverage of VSX, SIMBAD primary object type, Gaia DR3 vari_eclipsing_binary, Prsa2022, IJspeert2024, vetted Kostov2025 table3+table4, and ASAS-SN. No target has an identified prior EB in this bounded scope. All40 exact Gaia DR3 SIMBAD counterparts have primary type SB*. Physical classification and discovery priority remain separate questions.

coverage-matrix.csv contains per-TIC statuses, exact identity matches, neighbor rows, and reasons. VSX and ASAS-SN use60arcsec cones; three EB catalogue groups use5arcsec cones. Nested gaia.source_id supplies exact DR3 identity; the historical TIC GAIA column can be DR2. Identity provenance hashes the original targets file and frozen queue. Raw responses, URLs/ADQL, UTC and SHA256 are preserved. All160 vetted-table queries succeeded with zero rows. Gaia EB exact40 query returned zero rows; all40 SIMBAD counterparts were recovered. A failed request would be unknown, never absence; no target requests failed in this run.

Four VSX target counterparts have non-EB classifications: TIC265350422 ROT, TIC258621299 VAR, TIC112827464 ROT, TIC314041837 RS. TIC112827464's close VSX ASASSN alias is linked by the ASAS-SN exact TIC+Gaia row. TIC219033622 has an exact ASAS-SN ROT: row. Other rows are distinct neighbors. Known E neighbors relevant to attribution occur around TIC253126207 (24.77arcsec;0.312563d), TIC401138717 (42.73arcsec;0.363740d), and TIC152400959 (27.09arcsec;0.257384d). They do not establish target identity or attribution.

service-controls.json records fresh populated responses from all six VizieR tables and Gaia EB. cone-positive-controls.json recovers expected identified rows through the same table-specific cone radii and TSV parser. control-gaia-eb-exact-receipt.json verifies a populated Gaia EB exact-ID query. SIMBAD returns all40 populated exact identifier counterparts, validating its join/parser. These controls do not estimate catalogue completeness.

The separate Chopard check compares exact Gaia DR3 and TIC identities against cached public v1.2.0 track3_detail.csv and vetting/dossier.csv. Zero overlaps occur. chopard-comparison-summary.json logs all80 table/target comparisons and source hashes. Later online releases were not searched and93 embargoed identities remain unknown. This is not an exhaustive literature-priority claim.

Additional physics support: gaia-nss-full.csv is a fresh exact40 full NSS orbital-table response; all40 returned. Receipt includes query, UTC, and hash. It supplements the nested historical Gaia metadata without changing the physical verdict.

No canonical/public files or historical evidence changed. Scripts adapted after inspection from appointments23 shared-catalogues; dated fresh receipts replace no old evidence. Thank you for keeping the catalogue and physical evidence independently auditable.
