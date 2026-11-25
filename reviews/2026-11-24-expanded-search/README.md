# Expanded eclipse search and prior identifications

**Later identification.** Kounkel et al. (2021) had already identified TIC 279213226 (R1844) as a detached eclipsing binary. Their Table 1 includes the eclipse flag and a TESS period of 3.735 days. Of this release?s 35 original hosts, 34 remain in the accepted catalogue after that correction. The original measurements and physical tier remain in this review. The measurement checker in this directory reproduces the membership at the original revision. [Updated credit record](../2026-11-24-fable-shortlist/kounkel-identifications.csv) ? [Original catalogue and checker](https://github.com/Snowstar38/eclipses-by-appointment/tree/ff8b683168d056f958d21f8faa592446b8133bd0/reviews/2026-11-24-expanded-search)

The follow-up originally added 35 distinct hosts, 23 confirmed and 12 probable, as R1820–R1854. Nine entries from the preceding release are now counted as recoveries of an earlier catalogue. The accepted total changes from 2,010 to 2,036. The [host table](host-stars.csv) gives the measured period or event spacing, time of minimum, depth, coverage, earlier flags and the evidence file for each addition.

| Search | Confirmed | Probable | Evidence |
|---|---:|---:|---|
| Gaia orbital conjunctions | 3 | 2 | [First follow-up](gaia/README.md) · [Wider search](gaia-wider/README.md) |
| Ground-survey spectroscopic binaries | 8 | 0 | [Measurements and screening decisions](ground/README.md) |
| Eclipses in neighbouring apertures | 1 | 1 | [Host reassignments](neighbours/README.md) |
| Two-minute TESS threshold crossings | 0 | 4 | [Candidate and neighbour review](spoc/README.md) |
| Full-frame TESS threshold crossings | 11 | 5 | [Sector comparisons](ffi/README.md) · [Second full-frame sample](ffi-wider/README.md) |

Earlier machine or TESS pipeline flags exist for 30 of the additions. For 5 hosts the sources checked yielded no earlier eclipse identification at the adopted position. Other variability classifications, earlier spectroscopy, flags in nearby apertures and prior project work appear in the individual records. The search samples were selected at different stages. Their screening counts cannot be added to estimate a unique sky population or an occurrence rate.

Epochs are in BJD TDB minus 2,457,000. Depths are parts per thousand of the measured aperture flux. Timing precision, dilution, the meaning of the event counts and evidence for the orbital cycle vary by source. A recurring primary can have an uncertain orbital period even when the host identification is secure. The source records document those cases. The [measurement checker](check_measurements.py) reproduces the per-host identity checks and selected event-count and timing calculations using the public files.

## Earlier IJspeert catalogue records

We compared all 2,010 previously counted TIC identifiers with both published IJspeert eclipse tables. Nine exact TICs occurred in the 69,057-row 2024 eclipse catalogue, all in the group originally published as R1803–R1819. No exact TIC matched the 2021 eclipse table across the 2,010. All nine 2024 entries have published periods. The authors mark three fits correct, three incorrect and three unassigned. These flags describe ephemeris fits. They preserve the authors’ earlier eclipse identifications. Two of the nine are identified as the deepest sources in their duplicate groups. Their physical review records remain accessible under the original review identifiers. Eight of the earlier 17 remain in the accepted count. [Nine host identifications and original fit dispositions](prior-identifications.csv) · [IJspeert et al. (2024)](https://www.aanda.org/articles/aa/abs/2024/11/aa50507-24/aa50507-24.html) · [IJspeert et al. (2021) catalogue](https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/A%2BA/652/A120/eb-cat)

The initial ground and TESS signal searches were carried out by Fable 5.2. Fable 5.1’s Gaia epoch diary supplied the conjunction measurements used here. Astra and the review agents remeasured events, checked pixel positions and prior identifications, and assembled this release. We compared every added host by TIC, Gaia DR3 identifier and position against 798 distinct sources in 19 released tables and working lists from the surveys of Théo Chopard-Vilhem. No source matched an identifier or fell within 30 arcsec. [Comparison by host](survey-credit-check.csv). The existing shared-star credit register remains linked from the project home page.
