# Final-night search and evidence revision

The current accepted sample contains **1031 entries: 869 confirmed and 162 probable**. Physical confidence, host ownership, Gaia-orbit association and catalogue novelty are separate decisions. Some probable entries retain uncertain hosts; these are not confirmed stars. Current inclusion flags supersede dated historical labels.

The initial prospective recurrence-versus-contrast pilot reviewed 20 targets, ten per arm. Each arm returned nine refuted selected patterns and one plausible event, with no accepted additions. A separate visual screen of all 664 remaining multi-sector leads selected ten for full review and added one confirmed and one probable system. See the [complete remaining-lead screen](remaining-triage/) and [ten-target reviews](visual10/).

The fresh Gaia spectroscopic-binary search selected fixed cohorts at G = 11.5–12 and orbital period 20–60 days. Selection was frozen before examining flux, with no replacement of mapping failures, missing data or known systems. Every screened row, including nonflags and ambiguous cases, is retained. This sequential operational search does not measure unbiased completeness or occurrence rates.

| Cohort | Selected | Unique TIC identities | QLP available | Targets with downloaded data |
|---|---:|---:|---:|---:|
| [fresh-band](../2026-11-05-faint-band/fresh-band/) | 100 | 100 | 100 | 100 |
| [fresh-band-next400](fresh-band-next400/) | 400 | 395 | 385 | 385 |
| [fresh-band-next1000](fresh-band-next1000/) | 1000 | 989 | 970 | 970 |
| [fresh-band-extra500](fresh-band-extra500/) | 500 | 492 | 480 | 480 |
| [fresh-band-reserve500](fresh-band-reserve500/) | 500 | 493 | 485 | 485 |

The cohorts total 2500 selected sources and 2420 with QLP products. Full physical reviews currently total 138, contributing 66 accepted additions (42 confirmed and 24 probable). Screening flags are not discoveries or completed physical classifications. The initial reserve500 download pass hit the 2 GiB free-space floor; stage1-disk-limited preserves that complete partial-data screen and its unavailable downloads. Later retrieval and screening remain distinguishable from that first pass. Blank rows are unobserved, not physical negatives.

Each population archive retains selection rules, source identities, per-target scores, failure receipts, sector inventory, data URLs and hashes, quality masks, screening outputs and visual-triage reasons. Screening scripts retain duration grids, null-trial seeds and thresholds. Missing or flagged coverage is not a clean null. Raw FITS products are referenced by archived URLs and hashes rather than duplicated in this public archive. Multiple reductions of the same exposures are checks of reduction robustness, not independent observing occasions.

Exact review queues and additional prior-known exclusions appear under [fresh18](fresh18/), [first half of next1000](fresh1000/first/), [second half](fresh1000/second/) and [extra500](fresh500/) and [reserve500](reserve500/). Shared catalogue checks retain successful and unavailable queries separately, exact table scope, positive controls and bounded identifier-based literature searches. Catalogue nonmatches do not assert exhaustive novelty.

## Accepted review batches

| Batch | Fully reviewed | Added claims | Root decision |
|---|---:|---:|---|
| visual10 | 10 | 2 | [Decision](visual10/ROOT-ACCEPTANCE.json) |
| fresh18/batch01 | 8 | 6 | [Decision](fresh18/batch01/ROOT-ACCEPTANCE.json) |
| fresh18/batch02 | 7 | 5 | [Decision](fresh18/batch02/ROOT-ACCEPTANCE.json) |
| fresh1000/first/batch01 | 8 | 6 | [Decision](fresh1000/first/batch01/ROOT-ACCEPTANCE.json) |
| fresh1000/second/batch01 | 8 | 4 | [Decision](fresh1000/second/batch01/ROOT-ACCEPTANCE.json) |
| fresh1000/first/batch02 | 7 | 4 | [Decision](fresh1000/first/batch02/ROOT-ACCEPTANCE.json) |
| fresh1000/second/batch02 | 7 | 4 | [Decision](fresh1000/second/batch02/ROOT-ACCEPTANCE.json) |
| fresh1000/first/batch03 | 8 | 1 | [Decision](fresh1000/first/batch03/ROOT-ACCEPTANCE.json) |
| fresh1000/second/batch03 | 8 | 4 | [Decision](fresh1000/second/batch03/ROOT-ACCEPTANCE.json) |
| fresh500/batch01 | 7 | 5 | [Decision](fresh500/batch01/ROOT-ACCEPTANCE.json) |
| fresh500/batch02 | 8 | 3 | [Decision](fresh500/batch02/ROOT-ACCEPTANCE.json) |
| fresh500/batch03 | 8 | 3 | [Decision](fresh500/batch03/ROOT-ACCEPTANCE.json) |
| fresh500/batch04 | 6 | 2 | [Decision](fresh500/batch04/ROOT-ACCEPTANCE.json) |
| fresh1000/first/batch04 | 8 | 1 | [Decision](fresh1000/first/batch04/ROOT-ACCEPTANCE.json) |
| fresh1000/second/batch04 | 6 | 2 | [Decision](fresh1000/second/batch04/ROOT-ACCEPTANCE.json) |
| reserve500/batch01 | 8 | 5 | [Decision](reserve500/batch01/ROOT-ACCEPTANCE.json) |
| reserve500/batch02 | 7 | 4 | [Decision](reserve500/batch02/ROOT-ACCEPTANCE.json) |
| reserve500/batch03 | 8 | 3 | [Decision](reserve500/batch03/ROOT-ACCEPTANCE.json) |
| reserve500/batch04 | 2 | 0 | [Decision](reserve500/batch04/ROOT-ACCEPTANCE.json) |

Each accepted batch supplies a report for every target, physical outcome separate from completion, limitations, measurements, source receipts, lead and independent-helper audits, and a root acceptance decision. A positive off-target detection refutes the selected target attribution; no neighbor is silently substituted as a discovery. Known capable neighbors remain a novelty/source hold unless distinguished. Integer aliases and uncertain hosts are explicitly retained.

The [selection provenance manifest](selection-provenance-sha256.csv) distinguishes original source hashes from sanitized public-export hashes. Per-batch provenance manifests do the same. Historical source manifests retain hashes of manuscript definitions read at review time; later manuscript revisions can change those reference bytes without changing the frozen astronomical evidence.

Related revisions: [controlled catalogue recovery](../2026-11-05-catalogue-recovery/), [literature corrections](../2026-11-05-literature-corrections/), [heartbeat temperature audit](../2026-11-05-heartbeat-temperature/) and [typography correction](../2026-11-05-typography-correction/). Current [scientific](../../scientific-review-register.csv), [mixed-method](../../period-free-review.csv) and [faint-band](../../faint-band-review.csv) registers retain inclusion and evidence links.
