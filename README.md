# Eclipses by Appointment

**339 eclipsing systems identified in public TESS and Gaia data: 327 confirmed and 12 probable.** Ten further cases remain plausible and are excluded from that total. The original catalogue checks support an uncatalogued subset of **329 systems**; catalogue coverage remains unresolved for **10 physically confirmed systems**. Uncatalogued is a scoped catalogue result, not a claim of discovery priority.

This is one evolving **working draft, v1.0**. It has **not been formally submitted** to a journal and is not under formal review.

Gaia measures the orbits of binary stars. We use those orbits to predict when eclipses can occur, then examine public TESS photometry for the expected dips. The paper combines that search with period folds, nearby-M-dwarf transit searches, source-attribution tests and individual follow-up. Physical confirmation and catalogue novelty are recorded separately.

## Paper and evidence

- [Current paper](paper.pdf): the unified working manuscript, including the catalogue-screened systems in Appendix A and physical-review evidence in Appendix C.
- [Supplement](supplement.pdf): catalogue entries, light curves and individual review evidence, including the 140 R-labelled reviews and the returned Fable reports.
- [Review register](reviewed-extension.csv) and [original 70 individual reports](reviews/2026-10-30/README.md) plus [70 further reports](reviews/2026-10-30-next70/README.md): 131 physical confirmations (one known recovery excluded from additions) and nine plausible cases, with novelty limitations and next tests. The CSV filename is retained for link compatibility.
- [Returned review register](returned-review.csv) and [Fable review reports and evidence](reviews/c9a-return/README.md): 12 returned confirmations, including ten additions, one existing A4 control and one known catalogue recovery. Seven further candidates await individual vetting.
- [Historical catalogue reconciliation and Chopard-Vilhem cross-match](reviews/novelty-reconciliation/README.md), supplemented by the [current catalogue checks and recovered coverage](reviews/2026-10-30-next70/shared-catalogues/README.md): the earlier audit accepted 48 R-labelled confirmations; recovered ASAS-SN checks now clear the remaining 16, and 66 further additions bring the scoped catalogue-screened total to 329. Ten returned confirmations retain catalogue gaps. The earlier 74 confirmations and all 70 newly reviewed targets were checked against the open release with no additional overlap; these comparison sets include the known recovery and plausible cases and are not a count of unique additions. His separate 93-system release remains embargoed.
- [Earlier working draft](historical-draft-2026-10-14.pdf): an archived draft, not a formally submitted version.

Of the 266 candidates from the G 10-11.5 batch fold, 208 have individual reviews: **197 physical confirmations (including one known recovery), two heartbeat stars and nine plausible cases**. Another **34 await individual review**; the other rows record known signals, catalogue corrections and holds. The earlier 16 R-labelled ASAS-SN gaps are resolved by retained recovery queries; all 130 R-labelled additions meet the scoped seven-group catalogue standard. Ten returned confirmations retain required catalogue gaps. Failed repeat requests are not negative matches.

![Sky distribution of the original 199 A-labelled systems](overview.png)

The overview graphic shows the original 199 A-labelled systems, not all 339 systems or the full 329-system catalogue-screened subset.

**Related work.** The method is not new. Théo Chopard-Vilhem deposited the same search on Zenodo
on 2026 September 27, two weeks before this work began
([10.5281/zenodo.22998328](https://doi.org/10.5281/zenodo.22998328): 9,389 Gaia spectroscopic orbits, 93 eclipsing
systems at 13 to 119 days, object list embargoed until his paper is accepted), and on October 13 an open record of the
same test on near-edge-on Gaia astrometric orbits ([10.5281/zenodo.23342415](https://doi.org/10.5281/zenodo.23342415)).
Our initial literature search missed these records because it did not include Zenodo. The paper cites both records and does not claim priority for the method. The current open release ([version 1.2.0](https://doi.org/10.5281/zenodo.23405354)) shares one surviving detection with us (HD 170829, A20). A positional comparison of all 235 catalogue-ledger rows and exact TIC matching retain the earlier A20 overlap and three parent-list overlaps that are not additional shared claimed detections. The earlier 74 confirmations and all 70 newly reviewed targets have no identified overlap with its parent list or dossier in the retained identifier checks. These are comparison sets rather than headline additions: the new 70 include 67 confirmations (one a known recovery) and three plausible cases. The overlap with the embargoed September list remains unknown. A reader of this work pointed us to the records.

## Contributions

The project coordinator posed the question, directs the work and is responsible for the claims. Fable 5 found the batch candidates. **Astra** supervised the 140-object follow-up, reviewed exceptional cases, reconciled the evidence and integrated the results; fresh **GPT-6.1 Sol leads and Terra helpers** performed detailed measurements and checks. **Fable 5.1 and Opus 5.5 helpers** performed the returned c9a reviews; Astra reconciled those results and incorporated their evidence into the paper and supplement. Section 6 credits the other contributors and distinguishes independent analyses from reused methods. [Contributor record](reviews/2026-10-30/CONTRIBUTORS.md).

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

[`batch-candidates.csv`](batch-candidates.csv) preserves all 266 screening rows and their current review statuses. Its numerical screening fields retain their original meaning; fitted measurements and limitations belong to the individual reports. All 64 R-labelled confirmations count toward the physical sample; 48 meet the original uncatalogued definition and 16 await valid ASAS-SN coverage. Six R-labelled plausible cases remain unresolved after targeted tests.

## Data and code

The repository includes reports, compact measurements, acquisition manifests and analysis scripts. Raw TESS products can be fetched from their preserved MAST URLs. Scripts retain workspace assumptions and are not a turnkey package. The dated report folders preserve provenance within this single working paper.
