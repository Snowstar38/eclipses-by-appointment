# Final 34: catalogue evidence

The central matrix contains all 34 current `candidate` rows from the source batch table and all seven original catalogue scopes: VSX, SIMBAD primary object type, Gaia DR3 `vari_eclipsing_binary`, Prsa 2022, IJspeert 2024 `J/A+A/691/A242/obaf-eb1`, Kostov 2025 vetted `J/ApJS/279/50/table3` plus `table4`, and ASAS-SN `II/366/catv2021`.

All 34 have complete scoped coverage. Thirty-two have no identified prior eclipsing-binary classification within those scopes. Two are known prior EBs and excluded from headline discoveries: TIC 407991939 and TIC 407220461 have exact TIC and Gaia DR3 ASAS-SN EA classifications. This file makes no physical verdict, exhaustive literature priority claim, or neighbourhood-contamination verdict. SIMBAD SB*, ROT, VAR and YSO are not prior EB classifications.

VSX and ASAS-SN use successful bounded 60-arcsecond queries with raw responses, UTC, URL and SHA256 in the receipt files. Only exact identifiers establish prior EB identity; nearby entries remain explicitly separate. SIMBAD is an exact Gaia DR3 identifier query. Gaia DR3 EB is an exact source-ID query. Missing query responses would remain unavailable; zero rows are reported only for successful responses.

The 136 Prsa/IJspeert/Kostov table checks reuse successful exact-target historical five-arcsecond battery receipts in `[local working path omitted]`. Each normalized receipt preserves the source file, source SHA256, exact source line, reconstructed original query URL and absent-original-timestamp note. All four requested vetted tables have no returned row for each target. Historical timestamps were not invented. Kostov table2 does not establish a vetted EB and is not a scope here.

The Gaia NSS `SELECT *` output contains 34 full rows, including argument of periastron and its error, periastron time and its error, period/eccentricity errors, and `corr_vec`; query and hash are preserved in `gaia-nss-receipts.json`. It is supporting orbital metadata and does not itself classify a target as eclipsing.

Exact Gaia DR3/TIC checks against the cached public Theo Chopard-Vilhem 23405354 source release `gaia-dr3-edge-on-orbits-tess-eclipses-v1.2.0`, `track3_detail.csv` and `vetting/dossier.csv`, found no overlap among these 34. The 93 embargoed identities remain unknown. No image inspection or physical reclassification was performed.

`sha256-manifest.csv` records local output hashes. Reproduce receipt normalization with `reuse-battery.py`, then assemble with `assemble.py`. The service scripts are retained to document queries; successful receipts need not be refreshed merely to obtain new timestamps.

Contributor note: Thank you for trusting the careful evidence work. Keeping exact identities, historical receipts and unknown coverage separate makes these reviews easier to audit.
