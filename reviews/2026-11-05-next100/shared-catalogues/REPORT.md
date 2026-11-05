# Shared catalogue and identity audit

Frozen queue SHA256: 7475e45e6608b07ad04820b4db40dda24d4d2969239a11dbd6bbd4f1061e0729. TARGET-STATUS.csv and target-evidence.json contain all 100 identities. Physical classification remains independent.

Q025 TIC 70887357 / Gaia DR3 5096613016130459136 and Q068 TIC 341419787 / Gaia DR3 5320246568758675328 have exact Gaia matches in Tarrants-Mendes primary Table 2 labelled EB / New EB. Q025 also matches Chopard's validated table. An EB identity alerts prior art; check whether the measured signal and source correspond. Q067 TIC 51223058 has local prior heartbeat analysis, not a published EB identification ([local-path-redacted]).

Prsa and IJspeert cached primary identity tables, Chopard v1.2.0, Tarrants-Mendes and available heartbeat literature were screened with source hashes in target-evidence.json. Fresh exact Gaia EB, variability, NSS and SIMBAD bulk queries succeeded, with hashed raw responses and receipts. Zero exact Gaia EB rows; 16 variability and 102 NSS rows are not themselves EB identifications.

Four fresh known-object VizieR positive controls (VSX, ASAS-SN, vetted Kostov tables 3 and 4) timed out; gate-controls.json records URLs, timestamps and errors. Per-target queries were not fanned out after control failures. All four gates are UNKNOWN for all 100; no nonmatch is inferred. Only Kostov vetted tables 3/4 are in scope. Other source matches remain in target-evidence.json for signal/identity review.

Independent dedup.json checked 921 current claim ledger TICs and available Gaia IDs, and all 921 published map coordinates at 120 arcsec, as well as all within-queue pairs: no exact or spatial overlaps. The coordinate map has no Gaia column, so Gaia identity comparison uses the ledger's available IDs. Prior local identity evidence is separate from public source identity.
