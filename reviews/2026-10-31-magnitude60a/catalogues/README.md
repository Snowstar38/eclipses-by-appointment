# Corrected fixed60 scoped catalogue reconciliation

Fresh 2026-10-31 coverage of all60 corrected queue targets: VSX, SIMBAD primary object type, Gaia DR3 eclipsing binaries, Prsa2022, IJspeert2024, vetted Kostov2025 tables3+4, and ASAS-SN. Full Gaia NSS SELECT * returns all60 exact nested DR3 source IDs. The TIC historical GAIA field is DR2 and is never used as the DR3 join. Identity provenance hashes queue and metadata.

coverage-compact.csv is the small index; coverage-matrix.csv retains exact matches, close identity-review rows, distinct neighbours, and reasons. VSX/ASAS-SN use60arcsec cones; historical EB tables use5arcsec cones. Failed requests remain unavailable, never absent. Successful scope checks do not establish catalogue completeness, physical confirmation, or exhaustive literature priority.

TIC377389892 has VSX EA counterpart ASASSN-V J104558.09+574951.0 at0.02arcsec, period1.147d. It is treated conservatively as known prior EB on explicit close positional association; this is not an exact-ID alias join. A follow-up SIMBAD query returns the Gaia counterpart SB* but does not return that ASASSN alias. Other close VSX aliases are ROT. Distinct E neighbours include TIC314047448 at41.34arcsec (2.15175d) and TIC419573851 at29.55arcsec (0.58703d); neither establishes target identity or pixel attribution.

Fresh populated table controls plus same-radius cone positive controls and populated Gaia exact-ID EB control validate services and parsing. SIMBAD recovers all60 exact Gaia identifiers. Raw responses, queries, UTC and hashes are preserved in receipts. The Chopard comparison covers only cached public v1.2.0 track3_detail and dossier with source hashes: no exact overlaps. Later releases were not searched; embargo93 identities remain unknown.

The corrected queue excludes229308711 and451086560 and adds180871891 and448485777 solely for actual G boundaries. Initial result files are retained under excluded-boundary-history and are not active coverage. Raw cone files for excluded targets may remain as history. Active scope is defined by targets-selected.json and the corrected parent queue.

Thank you to the project coordinator and reviewers for keeping catalogue identity and physical evidence auditable. No canonical or public files changed.
