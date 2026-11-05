# Frozen 100-target review: final physical outcomes

All 100 selected targets received completed bounded reviews and explicit root acceptance. Outcomes: 4 confirmed, 5 probable, 13 plausible, 69 refuted, 4 non eclipse variable, 5 unresolved. These are physical review outcomes; none is added to the prior 913 new-system claims because catalogue novelty is unresolved.

| Sample group | Reviewed | Confirmed | Probable | Plausible | Refuted selected signal | Non-eclipse variable | Unresolved |
|---|---:|---:|---:|---:|---:|---:|---:|
| Both searches: dip leads | 30 | 3 | 3 | 6 | 18 | 0 | 0 |
| Other multi-sector dips | 20 | 1 | 2 | 2 | 15 | 0 | 0 |
| Other single-sector dips | 20 | 0 | 0 | 2 | 18 | 0 | 0 |
| Period-fold only | 10 | 0 | 0 | 1 | 9 | 0 | 0 |
| Brightening leads | 10 | 0 | 0 | 0 | 1 | 4 | 5 |
| Near-threshold period folds | 10 | 0 | 0 | 2 | 8 | 0 | 0 |

## Confirmed and probable signals

These physical tiers do not certify catalogue novelty. Periods retain the precision and limitations of their linked reports.

| Sample | TIC | Physical tier | Period (days) | Evidence |
|---|---:|---|---:|---|
| H002 | 352438536 | Confirmed | 59.03 | [Report](batch01/352438536/REPORT.md) |
| H012 | 54494046 | Probable | 58.93 | [Report](batch02/54494046/REPORT.md) |
| H016 | 467963921 | Probable | 49.7160 | [Report](batch02/467963921/REPORT.md) |
| H022 | 294257329 | Confirmed | 32.023 | [Report](batch03/294257329/REPORT.md) |
| H023 | 224631871 | Probable | 44.872 | [Report](batch03/224631871/REPORT.md) |
| H027 | 113645244 | Confirmed | 41.94565 | [Report](batch03/113645244/REPORT.md) |
| H032 | 372989764 | Probable | 28.24465 | [Report](batch04/372989764/REPORT.md) |
| H042 | 313617927 | Confirmed | 38.5 | [Report](batch05/313617927/REPORT.md) |
| H046 | 246124257 | Probable | 3.419619 | [Report](batch05/246124257/REPORT.md) |

The sample oversamples some groups. Report each group separately; the mixed total is not a survey-wide confirmation rate, calibrated detection efficiency, or occurrence estimate. The denominator is the frozen selection, with no replacements. Nonflags and catalogue-known objects were not sampled.

## Selection and evidence

From 2,904 queued detector leads without exact cached primary-table or known-note identity matches, select the lowest SHA256(seed|stratum|TIC) values within six disjoint groups. Seed and allocation were fixed before sample review in queue-seal.json; the selection was committed at df21bd48c. The parent overlaps historical searches and is not new sky coverage.

The parent harvest scanned 6,186 cached targets period-free; a 1,924-target subset also received period-fold screening. Initial source packets verified 705 cached FITS against frozen hashes and TIC headers. Later targeted coverage queries and cutouts have separate receipts and do not change the selected denominator. Each ten-target batch has fresh Sol/Terra work, deciding raw-event evidence, limits, source hashes, and a root acceptance record. Root adjudications explicitly identify any final work completed after a helper finished.

Confirmed requires recurring raw eclipses with a supported clock, target attribution, an alternative reduction, and compatible orbital geometry. Probable retains real repeat evidence with an unresolved check; plausible retains insecure or insufficient event/period evidence. Refuted refers to the selected signal interpretation, not a proof that the star cannot be binary. For brightening leads, alternate variability outcomes are recorded separately rather than promoted into eclipse claims.

## Catalogue status

All 100 remain novelty UNKNOWN. Complete cached Prsa and IJspeert exact-identity and five-arcsecond checks, bounded historical comparisons, and successful Gaia/SIMBAD queries found no prior eclipse association in those scopes. VSX, ASAS-SN, and the two vetted Kostov tables were unqueried after the known-source VizieR positive control timed out. Missing checks are not negative matches. The previous 913 accepted claims (807 confirmed,106 probable), physical ledger959, and public paper remain unchanged.

## What to pursue next

The clearest review priority is the remaining cross-method and multi-sector dip leads. This sample returned confirmed or probable signals in 6/30 and 3/20 respectively. These modest samples guide effort; they do not establish the exact yield of the remaining pool. Single-sector and fold-only detections retain some plausible cases but did not supply confirmed recurrence in this sample.

H046 (TIC 246124257) is especially interesting: a measured 3.419619 d train of deep events differs sharply from its Gaia SB2 period of 42.409012 d. The relation between the signals is unresolved; a hierarchical system is a hypothesis, not a demonstrated result. H032 (TIC 372989764) supplies a real repeating signal missed by the period-fold flag, with source blending still unresolved. These are useful cases for source separation and for understanding search complementarity.

Before adding any confirmed or probable sample signals to the novel-system ledger, complete the unavailable catalogue checks and resolve duplicate associations. Source separation and orbital-geometry checks remain the specific next steps for probable cases. Preserve the full frozen sample, including negative and unresolved outcomes, for any later detector comparison.

## Files

- accepted-results.csv: exact root-accepted rows and report paths.
- accepted-summary.json: row-derived group counts.
- queue.csv / queue-seal.json: frozen100 and selection provenance.
- batch01 through batch10: evidence, reports, audits, and acceptance locks.
- shared-catalogues/: scoped evidence and unavailable gates.
- review-yield.png: physical outcome counts within groups.

