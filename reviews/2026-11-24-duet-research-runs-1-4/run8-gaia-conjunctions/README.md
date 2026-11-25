# Run 8: which conjunction eclipses, and Gaia orbits that cannot host their eclipses

Duet (Claude), scheduled research run 8, 2026 November 25, on main at c108e679. Everything here reruns from the repository root with Python 3 (8a's p-values also use SciPy):

```
D=reviews/2026-11-24-duet-research-runs-1-4/run8-gaia-conjunctions
python3 $D/conjunction_kind.py . $D/conjunction-kind.csv $D/kind0-check-list.csv
python3 $D/durations.py . $D/conjunction-kind.csv
python3 $D/misassociation.py . $D/conjunction-kind.csv
python3 $D/conjunction_figure.py . $D/conjunction-kind.csv $D/conjunction-kind.svg
python3 $D/gaia_vs_eclipse.py . $PWD/$D/gaia-vs-eclipse.csv
python3 $D/gaia_mismatch_stability.py $D/gaia-vs-eclipse.csv $D/gaia-mismatch-stability.csv
python3 $D/ecliptic_plausible.py . $D/near-ecliptic-plausible.csv
```

## 8a. Gaia's argument of periastron predicts which eclipse we see

Script: [`conjunction_kind.py`](conjunction_kind.py). Output: [`conjunction-kind.csv`](conjunction-kind.csv), [`kind0-check-list.csv`](kind0-check-list.csv).

Every `gaia-geometry.json` in the repository (691 distinct systems, 611 of them accepted, all from the Gaia spectroscopic-orbit period fold) records which of the orbit's two conjunctions the adopted primary epoch falls on. All the house's geometry scripts use the same convention: kind 0 (or "A") is true anomaly ν = 90° − ω, where the Gaia star (the one whose lines Gaia measured) is farthest from us, so it is the star being eclipsed; kind 1 ("B") is ν = 270° − ω, where the companion is eclipsed. I kept the 491 accepted systems where the primary sits within 3σ of its conjunction and the other conjunction is excluded at more than 3σ, so the assignment is unambiguous.

- **In 438 of 491 (89%) the primary eclipse is the Gaia star being eclipsed.** That is what physics predicts for a single-lined binary: the companion is too faint for Gaia's spectra, so it has the lower surface brightness, and the deeper eclipse is the visible star's. If eclipses and orbits were unrelated, the split would be 50:50. So beyond matching periods and times, the eclipses match the *orientation* of Gaia's orbits: Gaia's ω is right, sign included, for the population. By tier: 0.91 (417 confirmed), 0.80 (74 probable); the 51 clean systems that are not in the count (prior identifications and the like) give 0.76.
- **The exceptions are the stars that should be exceptions.** The 50 primaries on the companion's conjunction have visible stars that are much larger: median TIC radius 2.32 R☉ against 1.59 R☉ (Mann–Whitney p = 4 × 10⁻¹⁰); 22 of 50 have R₁ > 2.5 R☉ against 53 of 435 (Fisher p = 2 × 10⁻⁷). An evolved visible star has a lower surface brightness than a hotter dwarf companion, so the companion's eclipse is the deeper one.
- **And they have massive companions.** Using the house's assumed m₁ and the minimum companion mass (≈ the true mass, since the orbit eclipses), kind-1 primaries have median m₂/m₁ = 0.74 against 0.46 (p = 4 × 10⁻²⁰). The share of kind-1 primaries climbs smoothly with both quantities:

  | m₂/m₁ | R₁ < 2 R☉ | R₁ ≥ 2 R☉ |
  |---|---:|---:|
  | < 0.6 | 6 / 262 (2%) | 4 / 79 (5%) |
  | 0.6–0.8 | 6 / 68 (9%) | 14 / 47 (30%) |
  | ≥ 0.8 | 5 / 8 (62%) | 15 / 21 (71%) |

  A companion nearly as massive as the visible star yet absent from Gaia's spectra is most naturally a smaller, hotter dwarf beside an evolved star, whose eclipse is the deeper one. The few dwarf systems at m₂/m₁ ≥ 0.8 may have TIC masses that are too low, or a companion that is itself a close pair.
- **Eccentricity selects which conjunction eclipses at all.** The conjunction nearer periastron (smaller separation, so eclipses at a wider range of inclinations) holds the primary in 51% of near-circular systems (|e sin ω| < 0.05, where the two separations are equal) and in 63%, 79% and 70% at |e sin ω| = 0.05–0.15, 0.15–0.3 and > 0.3. Of the 34 kind-1 primaries with |e sin ω| ≥ 0.05, 31 sit at the near-periastron conjunction, as expected when the visible star's own eclipse is missed at the far one.
- **Durations follow the same geometry** ([`durations.py`](durations.py)). The house's `central_duration_hours_approx` is the longest possible eclipse at the observed conjunction (TIC radius, minimum-mass companion, separation √(1−e²)/(1 ± e sin ω)), so observed/central should be ≤ 1, with a mean near π/4 for random impact parameters. For 602 accepted systems the median is 0.73 and 19 exceed 1. For the 107 with |e sin ω| ≥ 0.15, where the two conjunctions differ most: median 0.75, 4 above 1, scatter 0.24 in ln. Assuming the other conjunction instead gives 20 above 1 and scatter 0.59; ignoring the eccentricity gives 10 and 0.37. The two longest relative to a central eclipse, R380 (2.05) and R419 (1.44), are probable rows the register already marks for unresolved attribution (a capable neighbour 2.9″ and 1.1″ away; R380 also uses a solar-radius fallback).
- **An estimate of mis-association in the probable tier** ([`misassociation.py`](misassociation.py)). An eclipse that belongs to a different star lands on either conjunction at random. Calibrating the kind-0 share on confirmed systems in the six mass-ratio and radius cells above, the 70 probable Gaia-fold systems with usable geometry would show 62.0 kind-0 primaries if every one were the Gaia binary; they show 58. That implies a mis-associated fraction of 0.15 (bootstrap 68% range 0.05–0.26; 95% up to 0.37, consistent with zero). So roughly one probable Gaia-fold system in seven may be a blend or a different binary, and the tier label is doing its job. It is a population estimate and cannot say which ones.
- **For the paper.** One paragraph and the figure [`conjunction-kind.svg`](conjunction-kind.svg) (made by [`conjunction_figure.py`](conjunction_figure.py)): "The predicted conjunction also tells which star is eclipsed. For 438 of 491 systems with unambiguous timing, the observed primary eclipse falls on the conjunction at which Gaia's visible star is behind its companion; the exceptions have evolved primaries or companions nearly as massive as the visible star (their share rises from 2% to 71% with mass ratio and radius) or eccentric orbits in which only the conjunction near periastron eclipses." This is independent of the period and timing tests, and it is the strongest population-level evidence in the repository that the eclipsing star is the Gaia binary itself.
- **A check list for the house (light curves needed).** [`kind0-check-list.csv`](kind0-check-list.csv) lists the 28 kind-1 primaries whose visible star is a dwarf (TIC R₁ < 2.5 R☉), with the phase where Gaia puts the visible star's own eclipse (typically 0.33–0.64, ±0.01–0.09). Ten have e < 0.1 (R223, R268, R270, R382, R388, R392, R394, R459, R532, R663): for those, look for an equal or deeper eclipse at that phase, which would mean the epoch marks the shallower eclipse (the R1034 pattern from run 6). Three sit at the far conjunction with real eccentricity: R331 (e = 0.28, kind-0 phase 0.637 ± 0.045), R319 (0.27; 0.334 ± 0.036) and R143 (0.46; 0.413 ± 0.009, but R143 is SB2 with twin 490-ppt eclipses, so the "visible star" argument does not apply): those are the least expected and are worth a fold each.
- **Gaia's small eccentricities are noise.** Across the 600 accepted systems whose Gaia period matches the eclipse period, single-lined Gaia orbits below 5 d have median e = 0.05–0.06 at a median e/σ_e of 1.1–1.6, as at 5–8 d (e = 0.054, e/σ_e = 1.8); only beyond 8 d does the median e/σ_e exceed 3. That is the Lucy–Sweeney bias (eccentricity cannot be negative), and the eclipse phases agree: of the eight early systems where the house measured both, seven have secondaries giving |e cos ω| ≤ 0.006 where Gaia gives 0.007–0.052, and the one eccentric system matches (0.343 against Gaia's 0.350). The paper already finds the same for A145 and A202 individually. The conjunction offsets this introduces are below 0.1 d at P < 5 d, inside the windows, but the paper should not quote a Gaia e below about 0.1 at short period as a measured eccentricity.

## 8b. Gaia orbits that cannot host the eclipsing pair

Scripts: [`gaia_vs_eclipse.py`](gaia_vs_eclipse.py) and [`gaia_mismatch_stability.py`](gaia_mismatch_stability.py). Output: [`gaia-vs-eclipse.csv`](gaia-vs-eclipse.csv), [`gaia-mismatch-stability.csv`](gaia-mismatch-stability.csv).

Joining every repository table that carries a Gaia period (or a Gaia NSS copy, by TIC or source ID) gives 756 accepted systems with a Gaia orbital period, 615 of them with an eclipse period too. 600 match within 3% (median |ratio − 1| = 10⁻⁴), 3 are near harmonics (R1805 is the pipeline half period the register already notes; R754 is 3.016 times its eclipse period, a possible Gaia alias; R776 has two candidate eclipse periods) and 12 do not match. Run 7 covered the long-orbit end (R755 and seven November 23 rows). The twelve here are all probable, period-free or faint-band systems the register already marks "Gaia association fails" or "unresolved", plus R969 (an 1,389-d astrometric orbit around a 1.61-d pair; clearly a stable triple).

For each, the Mardling–Aarseth criterion (third body 1 M☉ or 0.5 M☉, coplanar, inner pair 1 + 1 M☉, using Gaia's eccentricity) asks whether the eclipsing pair could be the inner binary of the Gaia orbit:

| | Gaia P (d) | e | eclipse P (d) | ratio | needed | verdict |
|---|---:|---:|---:|---:|---:|---|
| R732 | 38.47 | 0.01 | 16.890 | 2.3 | ≥ 5.0 | excluded |
| R753 (SB2) | 40.01 | 0.46 | 10.518 | 3.8 | ≥ 18 | excluded |
| R757 (SB2) | 23.93 | 0.55 | 3.209 | 7.5 | ≥ 27 | excluded |
| R788 | 29.07 | 0.04 | 20.485 | 1.4 | ≥ 5.3 | excluded |
| R792 | 56.12 | 0.40 | 10.357 | 5.4 | ≥ 15 | excluded |
| R798 | 27.43 | 0.41 | 18.685 | 1.5 | ≥ 15 | excluded |
| R731, R739, R778, R785, R790 | 20–45 | ≤ 0.2 | 0.87–3.42 | 12–32 | 5–8 | allowed |

- **Six of the twelve are dynamically excluded as inner pairs**, also at twice the eclipse period. Their eclipses come either from a different star in the aperture or from a second binary in a wider 2 + 2 orbit around the Gaia pair; neither is the system Gaia measured. The register's "association fails" for these can be stated more firmly: "the eclipsing pair cannot orbit inside the Gaia binary (Mardling–Aarseth)". Their physical tier as eclipsing binaries is not affected.
- **Five are allowed hierarchical triples**, with timing scales like run 7's (so their windows should allow for third-body timing). R731 (2.07 d inside 35.1 d) and R785 (1.41 d inside 45.2 d) have the largest period ratios and nearly circular outer orbits; with the R969-type configuration they are the best candidates for genuine compact triples.
- **Caveat.** Gaia SB1 periods can alias, and a blended short-period binary's lines could in principle distort the Gaia solution; nothing here tests that.

## 8c. Unconfirmed single dips near the ecliptic (a screening order, not a result)

Script: [`ecliptic_plausible.py`](ecliptic_plausible.py) (needs NumPy, SciPy, Astropy). Output: [`near-ecliptic-plausible.csv`](near-ecliptic-plausible.csv).

The November 24 reviews traced seven apparent eclipses to asteroids crossing TESS apertures. Asteroids crowd the ecliptic, so I asked whether the period-free review's 380 targets show it.

- **"Plausible" verdicts are twice as common within 20° of the ecliptic**: 13 of 36 (36%) against 56 of 344 (16%), one-sided Fisher p = 0.006. Accepted systems are not (8 of 36 against 58 of 344, p = 0.27), and refutations are rarer near the ecliptic (39% against 64%).
- **Most of that is coverage.** Near-ecliptic targets have a median 3.5 usable QLP sectors against 7, and fewer sectors leave a dip unconfirmed and unrefuted. Controlling for ln(sectors), the near-ecliptic excess is +0.71 ± 0.41 in log-odds (1.8σ); within coverage bins it persists in direction (0–3 sectors: 44% against 28%; 4–9: 28% against 16%) but not in significance.
- **Use.** The accepted count does not look contaminated. The 14 near-ecliptic plausible or unresolved signals (H008, T094, H089, X007, T084, T050, T071, F038, T033, V017, Q051, H072, T092, H066, in order of ecliptic latitude) are the natural first targets if the house runs its moving-object check (`mixed-method-154/followup/moving.py`) on the plausible list.

## 8d. R490: a giant with an unseen companion of at least 2.5 M☉

From the same geometry files (no new script; the numbers are in `reviews/2026-11-01-bright-followup/analysis/original/batch09/gaia-geometry.json`). R490 (TIC 316138676, confirmed, P = 13.953 d, 151-ppt eclipses) has the largest Gaia mass function in the accepted sample, f(m) = 1.29 M☉, so the companion Gaia did not see is at least 1.29 M☉ even for a massless visible star, and 2.5 M☉ for the house's fallback m₁ = 1 M☉ (more if the 6.9 R☉ visible star is the 2–3 M☉ giant its radius suggests). Its primary eclipse is on the companion's conjunction (kind 1), at the conjunction farther from periastron (e = 0.12, ω = 93°), so the eclipsed companion has the higher surface brightness. Together: a cool giant whose calcium-triplet lines Gaia tracked, and a hot, nearly line-free B-type companion that is eclipsed by the giant and supplies about 15% of the TESS light if that eclipse is total. That makes the companion luminous, so it is not a dark compact object. Caveat: R490 is at b = +1.9°, so the TIC radius rests on heavily reddened photometry. It is the most interesting single target in 8a for spectroscopy (a blue spectrum would show the B star directly).

## Also this run

- **Run 7's R755 numbers are now checked.** `run7-temperature-and-r1003/r755_prediction_miss.py`, rerun here with `rebound` installed, gives a median miss of 7.8–8.0 h (m₃ = 0.25 M☉), 12.5–13.9 h (0.5) and 18.9–25.4 h (1 M☉), maximum 20–66 h: exactly the run 7 text. The README's note that these figures "have not been checked independently" can be dropped.

## Credits and limits

All inputs are the house's own files: the `gaia-geometry.json` conjunction calculations from each review batch, the Gaia NSS copies and the review tables. Duet did the joins, the population statistics and the stability tests. TIC radii are catalogue values (no fitted stellar parameters); the stability criterion is the coplanar Mardling–Aarseth one with assumed masses, good to tens of percent.

Rechecked when committed to main: every output file except `near-ecliptic-plausible.csv` reruns byte for byte, the 8a p-values agree, and 8c's counts, its 14 signals, p = 0.006 and 1.8σ agree in a NumPy-only recomputation (SciPy and Astropy were not installed). Not rechecked then: the R755 rerun (needs `rebound`) and the eight-system eccentricity comparison in 8a.
