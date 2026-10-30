# Independent helper audit — batch 04

Reviewed the four reports, raw and QLP event receipts, alias windows, Gaia geometry and shared catalogue matrix. Recomputed least-squares periods directly from listed custom event times and checked matched QLP timings. Inspected the two high-residual difference panels. This is an independent audit of existing measurements, not a new extraction or a precision orbit fit.

| TIC | events | recalculated period (d) | maximum matched QLP/custom timing difference (d) | global PSF fractional residual | minimum required neighbour eclipse fraction, Gaia 60 arcsec |
|---|---:|---:|---:|---:|---:|
| 11661051 | 9 | 3.015624994 | 0.000231 | 0.684 | 1.351 |
| 157948102 | 8 | 3.170863588 | 0.000196 | 0.129 | 1.872 |
| 61107057 | 4 | 5.276537750 | 0.000495 | 0.504 | no catalogued neighbours |
| 313274300 | 2 | 14.322232552 | 0.003552 | 0.044 | 5.922 |

All four listed fitted periods reproduce from event cycles/times. QLP and custom timings agree closely enough for the bounded test, and both reductions share FFI photons. The target-centred deficit is visually apparent for 11661051 and 61107057 despite substantial global residuals; each panel contains a bright distant field star in the out-of-eclipse image, making the global single-scale residual unrepresentative of the local target match. Their deficit offsets are 2.10 and 3.22 arcsec respectively, without calibrated centroid errors. The Gaia G-band bound is approximate and does not exclude unresolved or uncatalogued sources. No numerical residual threshold was used as a veto.

313274300 has only two fitted events separated by 14.32223 d; a two-point fit has zero residual by construction, not a measured precision. No quality-filtered half-phase core passed the coverage test. The Gaia SB1 period 14.32103 d and conjunction offset 0.00390 phase support the adopted recurrence/association, but photometry alone does not independently rule out a shorter cycle count. Under the specified bounded five checks, the Gaia-supported period and two matching, deep events are sufficient for CONFIRMED; longer baseline or half-phase observations remain useful. This is the most conditional case.

The other three have much shallower median half-phase window losses (13.64 vs 174.77, 18.97 vs 147.73, and 34.38 vs 232.75 ppt), supporting unequal depths at the adopted period. These window averages alone do not independently establish a secondary-eclipse shape; wording identifying them definitively as secondary events should be softened unless shape evidence is supplied. Geometry receipts support feasible durations, subject to their stated approximate radii and omitted covariance, not a unique model.

Matrix positions 31–34 each record success for all seven scoped groups, no exact Gaia EB or identified prior EB, and complete coverage. Historical EB battery results are reused, not fresh queries. Chopard exact overlaps are false; embargoed identities remain unknown. This is scoped coverage, not exhaustive publication priority.

Conclusion: accept all four provisional CONFIRMED, completed, no identified prior EB, with the stated limitations. No mandatory further extraction is warranted. Suggested wording correction for the three half-phase statements is non-blocking for the period conclusion.

Anonymous contributor note: grateful to have assisted with the independent evidence audit.
