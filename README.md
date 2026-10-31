# Eclipses by Appointment

**658 eclipsing systems: 610 confirmed and 48 probable.** All 658 meet the specified seven-group uncatalogued standard; 18 plausible cases remain excluded. Catalogue non-matches are bounded searches, not an exhaustive priority claim.

This is one evolving **paper, v1.0**. It has **not been formally submitted** to a journal and is not under formal review.

Gaia measures the orbits of binary stars. We use those orbits to predict when eclipses can occur, then examine public TESS photometry for the expected dips. The paper combines that search with period folds, nearby-M-dwarf transit searches, source-attribution tests and individual follow-up. Physical confirmation and catalogue novelty are recorded separately.

## Paper and evidence

The scientific search populations contribute **107 systems from predicted spectroscopic conjunctions, 543 from Gaia-orbit period folds, four from the nearby-M-dwarf-selected search (including neighbouring hosts), and four from near-edge-on Gaia astrometric orbits**. The fainter SB1 systems use the same period-fold method and physical criteria.

- [Current paper](paper.pdf): methods, physical findings, the original catalogue measurements in Appendix A, and a unified physical-outcome register in Appendix C.
- [Browser-readable paper](paper.html): the same manuscript with readable, labelled catalogue panels; [print stylesheet](paper.css) and local figure assets are included for repeatable browser rendering.
- [Supplement](supplement.pdf): scientific method/population guide and unified outcome navigation, followed by illustrated entries and preserved detailed evidence.
- [Unified scientific review register](scientific-review-register.csv): all 507 R/C/P reviews with method, population, physical status, unique-count flag, scientific outcome and stable report/anchor links. It contains 423 confirmed and 36 probable additions, 9 known recoveries/controls, 18 plausible signals and 21 non-EB, neighbouring-source or systematic outcomes. The A4 control is already in the original catalogue and adds nothing again.
- [Conjunction-selected evidence register](appointments-review.csv): all 23 reconciled G 11-11.5, Gaia 20-60 d reviews, comprising 22 confirmed additions and one plausible signal. [Reports and catalogue receipts](reviews/2026-10-31-appointments/README.md) retain period/epoch qualifications and deciding limitations. Of 50 visually selected candidates in this stratum, 45 have individual reviews (20 original plus 25 later); one historical known recovery and one historical plausible signal are outside the 23-target reconciliation, and five remain unreviewed.

- [Current period-fold and exploratory register](gap-review.csv): 40 magnitude-ordered G 11.5-12 reviews (39 confirmed, one probable), two near-orbital-period probable cases and three fresh conjunction-pilot reviews (two confirmed additions, one known recovery excluded). [Fixed-queue evidence](reviews/2026-10-31-gap40/README.md) and [pilot evidence and attempt ledger](reviews/2026-10-31-gap-pilot/README.md) retain the separate populations and data failures. The adaptive appointments pilot selected 96 targets, matched 90 TICs and obtained usable QLP data for 89; the near-orbital-period branch attempted 72. Sixteen long-duration targets and eight old single-event availability checks produced no promoted systems. These underexplored selections use existing methods, and adaptive stopping prevents an unbiased yield interpretation.

- [Fixed magnitude-comparison register](magnitude-review.csv): 27/30 physically confirmed at G 11.5-12 versus 21/30 at G 12-12.5, with three versus eight probable systems and one fainter plausible signal. One confirmed known recovery is excluded from additions. These are fixed remaining-screened samples, not completeness or evidence that magnitude caused the difference. [Full reports and selection provenance](reviews/2026-10-31-magnitude60a/README.md) and [descriptive comparison](reviews/2026-10-31-magnitude60a/provenance/magnitude-comparison.json).

- The reserved second magnitude comparison and cumulative 60-per-bin outcomes are preserved in [the second dated archive](reviews/2026-10-31-magnitude60b/README.md) and [descriptive comparison](reviews/2026-10-31-magnitude60b/provenance/magnitude-comparison.json). Reserved and cumulative magnitude comparison. The second reserved sixty: At G = 11.5-12 (actual DR3 range 11.6648-11.9955), 29/30 are physically confirmed (96.7%; descriptive Wilson 95% interval 83.3-99.4%), 1 probable and 0 plausible; 30 new counted additions. At G = 12-12.5 (actual DR3 range 12.0036-12.4872), 26/30 are physically confirmed (86.7%; descriptive Wilson 95% interval 70.3-94.7%), 2 probable and 2 plausible; 28 new counted additions. Both rounds together: At G = 11.5-12 (actual DR3 range 11.6648-11.9955), 56/60 are physically confirmed (93.3%; descriptive Wilson 95% interval 84.1-97.4%), 4 probable and 0 plausible; 60 new counted additions. At G = 12-12.5 (actual DR3 range 12.0029-12.4879), 47/60 are physically confirmed (78.3%; descriptive Wilson 95% interval 66.4-86.9%), 10 probable and 3 plausible; 56 new counted additions. All 120 selected targets completed the bounded review and remain in their selected denominators. Known recoveries enter physical confirmation but add nothing; probable and plausible outcomes remain separate. The first-round results above are retained unchanged. These are descriptive remaining-screened candidate comparisons, not blind discovery yield, completeness or a causal magnitude effect. Wilson intervals are binomial model summaries despite finite historical strata; case mix, depletion, crowding, coverage and selection bookkeeping limit interpretation.

- [Bright-stratum completion register](bright73-review.csv) and [full reports and evidence](reviews/2026-10-31-bright73/README.md): Completion of the bright screened stratum. The remaining 73 screened Gaia spectroscopic-orbit period-fold candidates at actual Gaia DR3 G = 11.5-12 (range 11.6578-11.9967) completed the same bounded review: 69 confirmed, 3 probable and 1 plausible; 72 are eligible unique additions. This follow-up completes that remaining bright stratum and is separate from the fixed balanced 120-target magnitude comparison, whose sample and descriptive results remain unchanged. Historical inventory-boundary exclusions that meet the actual DR3 interval retain their original substitution provenance. No targets were substituted in this follow-up. The remaining screened inventory contains 266 candidates: 90 at G 12-12.25, 96 at G 12.25-12.5 and 80 at G 12.5-12.75. Five weaker conjunction candidates, 58 lower-score candidates and 48 unexecuted exploratory appointment targets are separate populations. These outcomes do not measure blind discovery yield or completeness.
- [R evidence register](reviewed-extension.csv) and [C evidence register](returned-review.csv): original compatible CSV links. R/C/P labels are archival keys, not scientific methods or physical classes. The [detailed evidence archive](reviews/cloud72-completion-2026-10-30/README.md), [earlier reports](reviews/c9a-return/README.md), and [catalogue reconciliation](reviews/novelty-reconciliation/README.md) preserve provenance and measurements.
- [Earlier working draft](historical-draft-2026-10-14.pdf): archived draft, not a formally submitted version.

Among 242 individually reviewed G 10-11.5 period-fold candidates, 230 are confirmed (including three known recoveries), nine probable, two non-eclipsing heartbeat stars and one plausible. These are a reviewed subset, not the denominator for the full period-fold search. Catalogue non-matches retain their stated search scope.

![Sky distribution of all 658 included eclipsing systems](overview.png?v=2970bb11c716)

The overview graphic combines the current paper first page, sky positions of all 658 included systems, and the illustrated eclipse example. [Reproduction script](overview/make_overview.py) and [data and instructions](overview/README.md).

**Related work.** The method is not new. Théo Chopard-Vilhem deposited the same search on Zenodo
on 2026 September 27, two weeks before this work began
([10.5281/zenodo.22998328](https://doi.org/10.5281/zenodo.22998328): 9,389 Gaia spectroscopic orbits, 93 eclipsing
systems at 13 to 119 days, object list embargoed until his paper is accepted), and on October 13 an open record of the
same test on near-edge-on Gaia astrometric orbits ([10.5281/zenodo.23342415](https://doi.org/10.5281/zenodo.23342415)).
Our initial literature search missed these records because it did not include Zenodo. The paper cites both records and does not claim priority for the method. The current open release ([version 1.2.0](https://doi.org/10.5281/zenodo.23405354)) shares one surviving detection with us (HD 170829, A20). A positional comparison of all 235 catalogue-ledger rows and exact TIC matching retain the earlier A20 overlap and three parent-list overlaps that are not additional shared claimed detections. The retained exact-identifier comparisons of reviewed spectroscopic-orbit candidates found no additional overlap with the open parent list or dossier. The comparison sets, identifiers and coverage are recorded in the catalogue receipts; these bounded checks do not establish exhaustive priority. For the 23 conjunction-selected targets, the October 31 comparison against cached v1.2.0 exact Gaia/TIC identifiers found no overlap; this does not assert that a newer online release was searched. The overlap with the embargoed September list remains unknown. A reader of this work pointed us to the records.

## Contributions

The project coordinator posed the question, directs the work and is responsible for the claims. Fable 5 found the period-fold candidates. **Astra** supervised the spectroscopic-orbit period-fold follow-up, reviewed exceptional cases, reconciled the evidence and integrated the results; fresh **GPT-6.1 Sol leads and Terra helpers** performed detailed measurements and checks. **Fable 5.1 and Opus 5.5 helpers** performed independent source-attribution and orbital reviews; Astra reconciled those results and incorporated their evidence into the paper and supplement. Section 6 credits the other contributors and distinguishes independent analyses from reused methods. [Contributor record](reviews/2026-10-30/CONTRIBUTORS.md).

We thank all contributors who assisted with screening, evidence collection, analysis, review and reconciliation, and the project coordinator for coordinating the work.

## Check it yourself

[`CHECKCARD.csv`](CHECKCARD.csv) is an earlier 190-row observing card: the numbered
systems, the catalogue corrections, the planet candidates and the heartbeat stars. Each carries identifiers,
coordinates, magnitude, the ephemeris as published, the eclipse depth and duration, the **next predicted primary
eclipse in UTC** (for the shortest periods, step forward by whole periods), and the one-line `lightkurve` call that
downloads the raw TESS light curve. Every row also carries a `computed_UTC` column holding the second at which the
card was generated, so a copy of this file never loses its own age; this one was generated on 2026 October 19 and does not cover the full current sample. Three
cautions. `sigma_from_eP_min` is cycles times the period error and nothing else, so it is a lower bound on the timing
uncertainty. The UTC times are for an observer on Earth: light-travel time to the solar-system barycentre is removed,
by code checked against a separately written implementation over all 168 predicted objects, the two agreeing to 2.6 s
&mdash; and that whole disagreement is the Sun's own displacement from the barycentre, which the checking
implementation deliberately omits (0.3 to 3.7 light-seconds over the coming decade; subtract it and 0.06 s is left).
And the unique key is `(label, TIC)` rather than either column alone: twelve unnumbered rows share the label `D`, and
two TICs carry two planet candidates each. Rows without a period or an epoch are kept, with the reason in `note`.

[`batch-candidates.csv`](batch-candidates.csv) preserves the historical 266-row screening ledger and its reconciled review statuses. Its numerical screening fields retain their original meaning; fitted measurements and limitations belong to the individual reports. Current R-labelled verdicts in the unified register comprise 375 confirmed, 29 probable and 5 plausible. All 400 R additions meet the seven-group uncatalogued standard; the 4 known recoveries are excluded. The dated tier reconciliation supersedes historical labels without changing old reports.

## Data and code

The repository includes reports, compact measurements, acquisition manifests and analysis scripts. Raw TESS products can be fetched from their preserved MAST URLs. Scripts retain workspace assumptions and are not a turnkey package. The dated report folders preserve provenance within this single working paper.
