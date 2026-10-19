# Eclipses by Appointment

![105 eclipsing star pairs across the sky](overview.png)

**105 pairs of stars that eclipse each other, which no catalogue had recorded, found in public data from NASA's TESS
satellite and ESA's Gaia mission.**

Some stars come in pairs that orbit each other. When the orbit is seen nearly edge-on, each star passes in front of
the other once per orbit, and from Earth the pair's light dips on a regular schedule. Gaia measured the orbits of
hundreds of thousands of such pairs from the tiny shifts in the colour of their light as the stars swing towards and
away from us. This work used those orbits to predict *when* an
eclipse should happen, looked in TESS's brightness measurements at exactly those times, and found eclipses that
nobody had catalogued.

## The paper

- [`paper.pdf`](paper.pdf): the paper, shortened version, last updated 2026 October 17 (19 pages; the catalogue of all 105
  systems with their ephemerides and next eclipses is its Appendix A)
- [`supplement.pdf`](supplement.pdf): one entry per system, with its light curve (153 pages)
- [`paper-as-submitted.pdf`](paper-as-submitted.pdf): the 57-page version sent to the journal on October 14 (with the deposit link removed)

*Eclipses by Appointment: 104 Uncatalogued Eclipsing Systems, Catalogue Corrections and a Measured Null Planet Search
from Public TESS and Gaia DR3 Data.* Submitted to the Journal of the AAVSO on 2026 October 14; under review; not yet
refereed. The first outside reader said, rightly, that 57 pages was not a reviewable paper and that it read like a
working notebook. The shortened version above is the same results written as a journal paper: about 5,000 words of
text, the systems in one table, a literature review, and the per-object detail left to the supplement. It also carries
results found after submission: ASAS-SN photometry from 2014 to 2018 shows the eclipses of 20 of the 55 systems it
could test, at the predicted times, with the depths matching the predictions in the 11 examined; ASAS-3 photometry
from 2000 to 2009 shows them for 10 of 34; and one more system (A108) is seen on the Harvard plates. One sentence of
the submitted version is corrected: on the plates A63 is consistent with its TESS eclipse depth, not absent, once the
eclipse shape is used.

**Prior work (added 2026 October 15).** The method is not new. Théo Chopard-Vilhem deposited the same search on Zenodo
on 2026 September 27, two weeks before this work began
([10.5281/zenodo.22998328](https://doi.org/10.5281/zenodo.22998328): 9,389 Gaia spectroscopic orbits, 93 eclipsing
systems at 13 to 119 days, object list embargoed until his paper is accepted), and on October 13 an open record of the
same test on near-edge-on Gaia astrometric orbits ([10.5281/zenodo.23342415](https://doi.org/10.5281/zenodo.23342415)).
Both versions of our paper say we were not aware of a previous search of this kind; that was true when written and is
now false, because our literature search did not include Zenodo. The current `paper.pdf` cites both records and drops the
claim. Matched by Gaia source identifier, the open October record shares one detection with us (HD 170829, our A20) and
lists three more of our objects among its unclaimed candidates. The overlap with the embargoed September list is not yet
known. A reader of this work pointed us to the records.

In short: 105 eclipsing systems (94 confirmed, 11 probable) that are in no vetted variable-star or eclipsing-binary
catalogue; twelve Gaia orbit solutions the eclipses contradict; six new heartbeat stars; eleven corrections to existing
catalogue entries; old Harvard photographic plates (1890-1990) that show the eclipses of 17 systems at the predicted
times; a transit search of about 3,100 nearby red dwarfs that found no new planet, with the reason measured; and the
predicted time of the next eclipse for every system, so that anyone with a telescope can check them.

## How it was done

The searches, measurements, checks and writing were carried out by AI agents (Claude models from Anthropic and GPT
models from OpenAI) running on one home computer, with a human author who posed the question, directed the work and is
responsible for what is claimed. Every candidate from the main searches was re-analysed independently with separately written code before
being counted. Section 6 of the paper sets out who did what.

## Check it yourself

[`CHECKCARD.csv`](CHECKCARD.csv) is one row per catalogued object (141 rows: the 105 systems, the heartbeat stars,
the corrections and the rest), with identifiers, coordinates, magnitude, the ephemeris as published, the eclipse
depth and duration, the **next predicted primary eclipse in UTC** (computed 2026 October 19 01:20 UT; for the shortest periods, step
forward by whole periods), and the one-line `lightkurve` call that downloads the raw TESS light curve. Two cautions:
`sigma_from_eP_min` is cycles times the period error and nothing else, so it is a lower bound on the timing
uncertainty; and the UTC times are for an observer on Earth (light-travel time to the barycentre removed). Rows without
a period or an epoch are kept, with the reason in `note`.

[`batch-candidates.csv`](batch-candidates.csv) (added 2026 October 17) is one row per candidate from the period folds of Gaia orbits shorter than 20 d at G 10-11.5: 266 rows that passed the same tests run in bulk (conjunction attribution on Gaia's orbit, per-sector depth consistency, difference imaging), with the status each row holds after an adversarial review that queried ExoFOP, VSX and SIMBAD and re-folded 60 at random from fresh TESS data. 242 are `candidate`; the rest are TESS Objects of Interest already called false positives or eclipsing binaries, known signals that Gaia's orbit newly attributes to a stellar companion, VSX variables whose period or type the eclipses correct, or one hold. None is counted among the 104, because none has had the per-object re-analysis the paper requires; they are published so that anyone can check them.

## Data and code

Everything behind the paper (code, per-system analysis reports, ephemerides, figures and tables) is in a public data
deposit, available from the author.
