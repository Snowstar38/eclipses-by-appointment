# Batch05 lead audit (T041-T050)

All ten fixed identities in `queue.csv` have one `RESULTS.csv` row, one readable per-TIC `REPORT.md`, a raw-SAP numeric artifact, representative raw plots, actual quality-zero sector endpoints/internal gaps and fold-window coverage. `source-verification.json` rechecks ten packet identities, their bulk and fold hashes, and 91 cached FITS SHA-256 receipts. Catalogue novelty is UNKNOWN for every row: four scoped VizieR gates remained unavailable after failed positive controls in the shared catalogue work. No row is counted as a new system here.

| Sample | Bounded physical verdict | Deciding evidence |
|---|---|---|
| T041 | REFUTED | The selected 29.366-d fold is almost exactly 162 cycles of a coherent 0.18128-d smooth oscillation; 30 covered fold windows stack to a sinusoid rather than isolated eclipses. |
| T042 | PROBABLE | Four raw dips at cycles 0, 30, 51, 52 yield 47.387088 d; half-phase nulls are actually covered; target-vicinity independent pixel deficit and Gaia geometry support it, but close capable neighbors remain unresolved. |
| T043 | PLAUSIBLE | S78 has a raw level drop/recovery with unequal baselines; fold-screen S25 null is a different phase. S78 edge cutout drifts strongly and cannot decide source or artifact. |
| T044 | REFUTED | S6 69-ppt QLP flag localizes to the wing of Gaia G=7.06 field star near cutout pixel (9.55,5.79), away from the target at (5.44,5.05). Positive/negative pixel lobes may be pointing/background redistribution; no astrophysical neighbor eclipse is claimed. |
| T045 | PLAUSIBLE | Most flags are broad trends/gaps; the separate S67 trough appears in both QLP and cutout but sits within a smooth trough-to-rise shape and has no repeated clock. |
| T046 | REFUTED | Selected core is above its local side baseline on a monotonic rise/gap rather than a dip. |
| T047 | REFUTED | Retained trough is part of adjacent smooth oscillations; helper short-timescale periodogram is about 1.3315 d, not a measured eclipse clock. |
| T048 | REFUTED | Two separated single-cadence QLP drops have no simultaneous target-centered raw cutout counterpart. The cutout 3x3 has 10.4k e/s side flux and brightens across the selected core. Outer-background curve is excluded because 15.5% of its pixels are zero. |
| T049 | REFUTED | S61 and S88 show broad, smoothly curved raw waves crossing the selected windows, with no isolated event. New S108/S109 cutouts show strong continuous background/aperture variation and are not sensitive nulls. |
| T050 | PLAUSIBLE | S27 broad decline/deepening is cut by a 1.181-d gap; the Gaia-period continuation falls inside a 3.109-d S92 quality-zero gap, so no sensitive repeat check is available. |

T042 clock: S13/S66/S100/S102 fitted centers are 1678.65847/3100.27375/4095.40239/4142.78887 BTJD. The four-center weighted formal period error is 0.000130 d with half-cadence floors. `RESULTS.csv` reports a separate conservative 0.0005-d allowance for shape and pipeline effects, not a calibrated precision. S93 and S101 half-phase windows span about +/-0.078 d with 69 and 58 core cadences and raw deficits 0.12 and -0.01 ppt. The unflagged S66 and S102 events resolve the same-kind cycle count. The helper's S66 TESSCut reduction uses the same photons, and the nearest Gaia conjunction is 1.84 linear sigma away using the published covariance. Capable G=14.43/G=16.19 blends keep source attribution open.

The selected detector flags are the object of each REFUTED judgment. None says the Gaia SB1 has no orbit or excludes unrelated weaker eclipses. PLAUSIBLE rows are completed bounded reviews with an insecure physical interpretation; their unresolved material checks are stated in their reports and next-check columns. `helper-audit.md` documents the independent T041/T042 and remaining morphology audit. All new cutouts carry URL and SHA-256 receipts. T043 edge-cutout columns are near-zero (not literal zero), and its 3x3 includes an edge column with severe baseline drift. T044 target aperture is contaminated by the nearby very bright star and is not used as a stand-alone null. T048's raw 3x3 is used without the invalid background correction.

No paper, old review, shared register, other batch or external publication was changed. Root scientific acceptance remains required.
