# Proposed additions from pipeline detections and ground-survey binaries

**Snapshot of 23 November 2026. This is a proposal under review. These systems are not part of the 1,138-host catalogue, and the paper's counts are unchanged.**

**654 systems** are proposed after a per-object review of 1,081 stars: **470** meet the confirmed criteria below and **184** are probable. The catalogue and literature checks found no earlier eclipse candidate for **86**. The other **568** validate earlier machine-selected candidates (the unvetted machine-learning list of Kostov et al. 2025 and/or the Gaia DR3 variability classifier). The two groups are counted separately throughout.

| Earlier eclipse evidence | Confirmed | Probable | Total |
|---|---:|---:|---:|
| No earlier candidate in the sources checked | 39 | 47 | 86 |
| Prior machine-selected candidate | 431 | 137 | 568 |
| Total | 470 | 184 | 654 |

- [Proposed systems](proposed-systems.csv): identifiers, coordinates, adopted period and reference epoch (BTJD = BJD_TDB − 2,457,000), depth, attribution, ground-survey detections and the reason for the tier. Read Gaia identifiers as text.
- [Counts](counts.json).

## Where the stars came from

| Search | Proposed |
|---|---:|
| Spectroscopic binaries from ground-based surveys (LAMOST, APOGEE, GALAH, RAVE, Gaia-ESO) | 177 |
| SPOC two-minute pipeline detections not promoted to objects of interest | 192 |
| TESS-SPOC full-frame pipeline detections not promoted to objects of interest | 285 |

The first two searches read the TESS pipelines' own threshold-crossing events: periodic signals the pipeline detected and that were never promoted or vetted. The third looks for eclipses in stars that ground-based spectroscopic surveys list as binaries. Every proposed star lies outside the 1,138 published hosts by TIC and by position (5″).

## Criteria

- **Confirmed**: a repeating discrete eclipse re-measured over all available sectors (capped at eight well-spread sectors for stars with more) in photometry independent of the detecting pipeline; a period from the eclipses themselves; difference images in at least two sectors favouring the target over every Gaia DR3 source within 60″ bright enough to supply the depth; and a second look, either a ground-survey detection at the predicted phase (ASAS-SN, ZTF, Gaia epoch photometry) or two independent TESS reductions.
- **Probable**: a real repeating eclipse with one named limitation, given in the `reason` column.
- Smooth, contact-like and ellipsoidal variables are excluded. Two equal minima per orbit at periods under 0.5 d are never above candidate.

## Limitations

- **The confirmed count is an upper bound.** 244 of the 470 confirmed systems have a ground-survey detection. The others rest on two TESS reductions, and for many of them a ZTF query failed or was still pending at the time of this snapshot. A ground-survey non-detection would move a system to probable.
- **No visual inspection.** Every decision in this snapshot was made from measured quantities. The November 22 review assessed each star visually; that step has not been done here.
- **Literature depth.** Checks cover the catalogues used for the November 22 review, SIMBAD object types and paper titles, Gaia DR3 non-single-star orbits, K2 eclipsing-binary catalogues by position, and the SuperWASP false-positive catalogue of Schanche et al. 2019 (MNRAS 488, 4905), which alone removed 36 stars that the other checks had passed. Abstracts were read where available. No full paper texts were read.
- **Periods.** 81 confirmed systems list an alternative period at a factor of two (`period_alternative_days`).
- **Attribution.** TESS pixels are 21″. "On target" excludes capable neighbours beyond about 10″; closer companions cannot be excluded.
- Part of the ground-survey binary list (437 of 923 candidates reviewed) was still being processed at the time of this snapshot.
- No historical search establishes absolute priority.

Prepared by Fable 5.2 with three Opus 5.5 review agents.
