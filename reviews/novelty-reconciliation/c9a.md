# C9a novelty reconciliation - 2026-10-30

Ten count-addition C rows: **0 established uncatalogued, 0 established known, 10 unresolved** under the original core-catalogue definition. Physical confirmation is separate; these are incomplete catalogue checks, not rejected eclipses.

Definition: `short/sec_methods.html`, Section 2.7 Status words: VSX, SIMBAD primary classifications, Gaia DR3 EB, Prsa2022, IJspeert2024, vetted Kostov2025 tables, ASAS-SN. No exhaustive literature, SB9 or WDS gate was added. An SB* classification, a non-eclipsing VSX type, or Kostov unvetted table 2 alone does not remove an object.

## Other researcher systems

The returned reports checked IJspeert2021 (`J/A+A/652/A120`), which does not substitute for IJspeert2024 (`J/A+A/691/A242/obaf-eb1`). They do not establish coverage of the vetted Kostov2025 tables 3/4. Thus the answer to whether these ten have been fully crosschecked against those systems is: **not yet established by the retained evidence**. Table 2 is the unvetted machine-learning list and is not a novelty veto. No verified table2 target flags were established in this reconciliation.

## Evidence matrix

N = reported no target EB; R = prior non-eclipsing type permitted; U = unresolved; S = SB* only. I24 and K34 refer to the required 2024 IJspeert and vetted Kostov tables.

| Row | TIC | VSX | SIMBAD | Gaia EB | Prsa22 | I24 | K34 | ASAS-SN | Status |
|---|---:|---|---|---|---|---|---|---|---|
| C02 | 468181994 | N | S | N | N | U | U | N | unresolved |
| C03 | 470235665 | N | S | N | N | U | U | N | unresolved |
| C04 | 379251709 | N | S | N | N | U | U | N | unresolved |
| C06 | 331293467 | N | S | U (predecessor) | N | U | U | U | unresolved |
| C07 | 283532878 | N; neighbour EB | S | N; neighbour EB | N | U | U | U | unresolved |
| C08 | 407877153 | N | S | N | N | U | U | U | unresolved |
| C09 | 15855794 | N | S | N | N | U | U | U | unresolved |
| C10 | 92881948 | R ROT | S | N | N | U | U | U | unresolved |
| C11 | 468827621 | N | S | N | N | U | U | N | unresolved |
| C12 | 416285595 | N | S | N | N | U | U | N | unresolved |

## Retained evidence and gaps

**C02 / TIC 468181994 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks. 
Report: `reviews/c9a-return/reports/vet01.md`. Source evidence: `evidence/80e6ff13be-s2_archives.out`, `evidence/a9b8b3a181-s2b_archives.out`.

**C03 / TIC 470235665 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks. 
Report: `reviews/c9a-return/reports/vet02.md`. Source evidence: `evidence/ac40b45105-s1_archives.out`, `evidence/532cf6f01b-s1c_archives.out`.

**C04 / TIC 379251709 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks. 
Report: `reviews/c9a-return/reports/vet02.md`. Source evidence: `evidence/ac40b45105-s1_archives.out`, `evidence/532cf6f01b-s1c_archives.out`.

**C06 / TIC 331293467 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks ASAS-SN explicit successful check not established Gaia EB query validation remains weak; reuse predecessor only with this limitation. 
Report: `reviews/c9a-return/reports/vet03.md`. Source evidence: `evidence/4588eb4bba-s2_archives.out`, `evidence/8745386760-REPORT.md`.

**C07 / TIC 283532878 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks ASAS-SN explicit successful check not established. Nearby Gaia DR3 2202301140233408128, P=1.79747 d, excluded as source in returned physical review; not target prior EB.
Report: `reviews/c9a-return/reports/vet04.md`. Source evidence: `evidence/01a402aece-s12d_recheck.out`, `evidence/7d2464ecb0-s12b_archives.out`, `evidence/f28435a7fe-s12e_neighbour_eb.out`.

**C08 / TIC 407877153 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks ASAS-SN explicit successful check not established. 
Report: `reviews/c9a-return/reports/vet04.md`. Source evidence: `evidence/01a402aece-s12d_recheck.out`, `evidence/7d2464ecb0-s12b_archives.out`, `evidence/f28435a7fe-s12e_neighbour_eb.out`.

**C09 / TIC 15855794 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks ASAS-SN explicit successful check not established. 
Report: `reviews/c9a-return/reports/vet05.md`. Source evidence: `evidence/5adf6d943a-s10b_archives_redo.out`, `evidence/957d742820-s10c_vizier_check.out`, `evidence/c294cf22c0-s10d_controls_gaiavar.out`.

**C10 / TIC 92881948 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks ASAS-SN explicit successful check not established. Gaia SOLAR_LIKE classifier is likewise not a prior EB classification.
Report: `reviews/c9a-return/reports/vet05.md`. Source evidence: `evidence/5adf6d943a-s10b_archives_redo.out`, `evidence/957d742820-s10c_vizier_check.out`, `evidence/c294cf22c0-s10d_controls_gaiavar.out`.

**C11 / TIC 468827621 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks. 
Report: `reviews/c9a-return/reports/vet06.md`. Source evidence: `evidence/215f005025-s1_archives.out`, `evidence/8b69c3c2a1-s1b_archives.out`.

**C12 / TIC 416285595 ? unresolved.** IJspeert2024 table (not 2021) requires successful validated target check Kostov2025 vetted tables 3 and 4 require successful validated target checks. 
Report: `reviews/c9a-return/reports/vet06.md`. Source evidence: `evidence/215f005025-s1_archives.out`, `evidence/8b69c3c2a1-s1b_archives.out`.

## Query and reuse accounting

Reused successful positive controls and the repaired vet04 `s12d_recheck.out`; its initial all-empty run and failed all-catalogue checks were rejected. Vet05 repairs/controls supersede initial cones. An Algol VSX control does not by itself prove every sparse catalogue query works; corresponding table controls remain relevant. Vet03 Gaia failure is retained explicitly. Incorrect `I/357/varisum` empty responses are not accepted as Gaia variability negatives.

Missing-core target checks were attempted against IDIA, following failed CDS/IDIA discovery probes. The JSON retains all 35 target requests and bounded responses/errors. HTTP200 with metadata alone lacks the required positive control and is not promoted to absence. The attempted ASAS-SN `II/366/catalog` source was invalid and all five errors remain unresolved; the earlier successful `II/366` queries for the other rows remain usable. No endless retries. Earlier c3?c8 exact-TIC vetted-table caches supplied no matching rows for these ten.

No eclipses rerun, images generated, manuscript edited or commits created. Only this Markdown and its JSON evidence companion were written.

The returned physical reviews are valuable and the repaired checks were preserved. Completing the few missing catalogue tables can resolve novelty without repeating the eclipse work.

## One bounded bulk improvement pass

Requested complete tables without cone filters, unlimited rows, and TIC/RA/Dec columns: `J/A+A/691/A242/obaf-eb1`, `J/ApJS/279/50/table3`, `J/ApJS/279/50/table4`. All three IDIA downloads read timed out (8-second connect / 25-second read timeout). Five parallel requests using the correct exact ASAS-SN source `II/366` also read timed out. Manifests: `c9a-evidence/manifest.json`, `c9a-evidence/asas-manifest.json`. No successful full tables or hashes could be obtained. A complete downloaded table with actual rows would validate the service/table without requiring per-target controls; none was obtained. All ten statuses remain unresolved. No further retries.
