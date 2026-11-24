# Audit of the November 23 additions against their own rules

An independent read of the 756 systems added on November 23 (R946–R1701), checking each row of [`host-stars.csv`](../2026-11-23-pipeline-and-survey-review/host-stars.csv) against the criteria in that review's [methods](../2026-11-23-pipeline-and-survey-review/methods.md), and the whole 1,894-system catalogue for duplicates. This audit changes no tier and no row. It lists rows for the reviewers to decide.

**Outcome.** The review's stated totals all reproduce, the registers agree with each other, and the catalogue has no duplicates. Five confirmed rows do not meet the confirmed rule as written or carry a reviewer's own unresolved concern, one probable row breaks the short-period rule and one more may, and about thirty rows have data-column errors or gaps. Nothing here suggests a systematic problem with the November 23 review.

## What reproduces

- 506 confirmed and 250 probable; 104 with no earlier candidate and 652 prior machine candidates, by search, as in the summary and `current-accounting.json`.
- 316 confirmed systems with a ground-survey detection and 83 with a listed factor-of-two alternative.
- Visual review: 624 first readings in agreement and 132 adjudicated; 72 additions that the numeric shape test did not accept; 28 refit periods, 8 of them doubled.
- Every host row is marked as added in `reviewed-stars.csv` under the same TIC, and every "added" outcome there has a host row.
- No TIC or Gaia DR3 identifier appears twice among the 1,894 accepted systems, and no two accepted systems lie within 5 arcmin of each other, so no blended signal is counted twice.
- Every period and epoch is positive and inside the TESS range, and every eclipse lasts under a fifth of its orbit.

## What needs a decision

All rows are listed with the finding and a suggested action in [`flags.csv`](flags.csv).

**Confirmed rows that the rule or the reviewer's own note does not support (5).**

- **R1431:** the difference images favour the target in one sector; the confirmed rule asks for two. The row's own limitation says attribution is limited.
- **R1053:** labelled on target in three sectors, but the free-fit centroid lies 28–33 arcsec from the target in all three, more than one TESS pixel, with no capable Gaia neighbour within 90 arcsec.
- **R1501:** two of its three on-target sectors have free-fit offsets of 140–152 arcsec, leaving one sector within a pixel.
- **R1337:** the visual reviewer records eclipses absent in s7, s34 and s88, with depth varying 2–6% between sectors, and asks for a human look. s88 is one of its on-target sectors.
- **R1093:** the period was refit from 14.24 d to 6.1666 d, which is not a harmonic, and the eclipses run about an hour late against the adopted ephemeris. The depth, event count and period columns still describe the old period.

**The short-period rule (2).** The methods say two equal minima per orbit at periods under 0.5 d are never above candidate. **R1008** is probable at 0.387 d with two equal minima in its own visual note, so on the stated rule it would leave the count. **R988** is probable at 0.263 d: the numeric test calls its alternate dips unequal, but the visual note calls them equal. R1355 (confirmed, 0.477 d) passes: its near-equal pair appears only in the 0.954 d fold, above the limit.

**Data columns (about 30 rows).** R1617 has a negative depth (−116.9 ppt). R1683 lists one primary eclipse where the visual note counts four. Three rows have a secondary phase that disagrees with their own period test. Six rows put the deeper eclipse at the secondary. Nineteen rows (nine confirmed) leave the factor-of-two period choice open in their own text but list no alternative period, so the 83 in the methods would be about 92 if those choices are really open. Six refit rows still describe the earlier period in `period_resolution`.

**Questions of judgement.**

- Six confirmed rows (R966, R967, R968, R970, R971, R1263) have a Gaia DR3 orbit whose period differs from the eclipse period. The confirmed rule does not say whether that caps the tier.
- Twenty-three confirmed rows have an on-target sector whose free-fit offset is about 7 arcsec or more, up to 68.6 arcsec in one sector of R1274. Each still meets the rule with two sectors within a pixel, but the methods could say how the label relates to the offset.

## What this audit could not do

The light curves were not re-measured, and no external catalogue was queried: MAST, VizieR, SIMBAD, ExoFOP and the Gaia archive were not reachable from the environment the audit ran in. Every finding here comes from the repository's own tables. Twelve of the 1,140 diagnostic sheets are published; publishing at least the 132 adjudicated ones would let a reader check the visual decisions that changed a tier.

## Reproduce

From the repository root, with Python 3 and no extra packages:

```sh
python3 reviews/2026-11-24-audit-of-nov23-additions/rule_checks.py audit-output.json
```

The script prints the checks and writes every flag to the JSON file named on the command line. Its keyword screen (`X2`) is a reading aid: most matches are words such as "sharp contacts", and the 72 visual acceptances it surfaces are disclosed in the methods. `flags.csv` is the curated result after reading each flagged row.

Audit by Duet (Claude), 2026 November 24.
