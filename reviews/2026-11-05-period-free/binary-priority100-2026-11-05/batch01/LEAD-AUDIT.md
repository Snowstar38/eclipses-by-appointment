# Batch01 lead audit

The ten fixed queue identities T001–T010 were reviewed. Each has `lead-numeric.json`, `lead-timing.json`, raw SAP plots, and a readable `REPORT.md`; `RESULTS.csv` carries the bounded physical result. Every cached FITS used by `lead_measure.py` was checked against its bulk receipt SHA-256 before extraction. Source packets separately bind the bulk result, fold result and FITS receipts to the fixed queue. The shared novelty status is UNKNOWN for all ten because four VizieR catalogue gates did not return a valid positive control; no physical verdict is counted as a new system here.

`lead_measure.py` plots every retained period-free dip in quality-zero raw SAP and records actual sector endpoints, cadence and internal gaps. Its local trapezoid centers are exploratory. Singular covariance, source gaps and broad baseline trends were not promoted to precise timings. `lead_timing.py` explicitly curates eclipse kinds and finite centers, and keeps integer-cycle assumptions visible. Its errors are half-cadence or scatter allowances, not calibrated instrumental or model systematics. The Gaia orbit check uses source-specific correlated NSS covariance and measured centers where available; it is linearized and descriptive.

| Sample | Physical result | Deciding evidence |
|---|---|---|
| T001 | PROBABLE | Strong two-kind repeat at 28.0358 d; a capable Gaia source only 2.71 arcsec away remains unresolved. |
| T002 | PROBABLE | New S105/S108 pixel events resolve 29 cycles at 24.620831 d and exclude 28/30 plus P/2; Gaia conjunction timing remains 2.8–3.1 linear sigma discrepant. |
| T003 | CONFIRMED | Deep and shallow kinds independently give 48.5277 and 48.5272 d; pixel reduction and Gaia geometry support selected source. |
| T004 | CONFIRMED | Deep 28-cycle and shallow 27-cycle spans agree near 38.1157 d; sector-102 core gap is retained as timing limitation. |
| T005 | CONFIRMED | Adjacent and later-sector raw eclipses of two kinds; target-centered pixel loss despite QLP correction suppressing the long event. |
| T006 | CONFIRMED | Two raw dips 43.062 d apart and actual covered nulls at shorter aliases; target-centered pixel deficit and Gaia geometry. |
| T007 | PLAUSIBLE | Broad S7/S34/S61/S88 depressions include partial occasions, but 18/19/20 cycle aliases and eclipse morphology remain insecure; S109 edge trend is inconclusive. |
| T008 | PLAUSIBLE | One broad S62 event with a 1.6-d center gap; alternate cutout is detector-edge invalid, S109 flat only in a bounded interval. |
| T009 | CONFIRMED | Two recurring kinds near 42.569 d; target-centered pixel deficit and Gaia conjunction agreement. |
| T010 | REFUTED | QLP 31.19-ppt rectangle absent in simultaneous target-centered, flux-bearing TESSCut 3x3 (−1.10-ppt loss). Its QLP origin is unassigned. |

T002 was initially two-event ambiguous, then newer S105 and S108 data resolved the integer count. S107 has near-zero target-aperture flux and was excluded from null tests. The four-full-center photometric period is 24.620831 d; the partial event at the start of S108 is supporting evidence only. Its 0.000050-d allowance covers cross-pipeline timing beyond the formal regression scatter. The unresolved Gaia timing is why it is probable. T003 P/2 at BTJD 3977.696 has 138/138 expected core samples and 0.16-ppt loss; T004 P/2 at 3089.062 has 123/147 core samples and −0.05-ppt loss. Both are gross-deep sensitive against >100-ppt events. T004's result-row 0.0005-d period allowance is deliberately wider than the 0.000058-d two-center formal allowance because the S102 core is gapped. T007's broad-event 38.88-d alignment remains a recurrence guide, not a precision period. T008 and T010 have no measured repeat clock. T001 source ambiguity is physical attribution, not catalogue novelty. An alternative extraction of the same TESS photons checks processing and pixel location; it is never an additional occasion. The S109 cutout for T010 contains near-zero target flux and is not used as a null.

The helper's independent checks, pixel figures, source hashes, actual alias coverage and Gaia covariance are in `helper-audit.md` and the linked `helper-*.json`/`helper-*.py` artifacts. The lead reviewed the contradictory T008/T010 cutouts and T007 invalid center before setting verdicts. No paper, prior review or shared scientific register was changed by this batch.
