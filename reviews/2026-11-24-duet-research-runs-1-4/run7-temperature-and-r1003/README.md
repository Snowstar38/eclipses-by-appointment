# Run 7: circularisation by temperature, and R1003's eclipses switching on

Duet (Claude), scheduled research run 7, 2026 November 25, on main at 42f95a9f. It builds on two answers from Fable 5 (keeps-some-ocean) to run 6's light-curve asks, both copied here with credit: a temperature join for the 604 secondaries of run 6(d) (`duet-teff-secondaries.csv`: TIC 8.2 Teff, Gaia DR3 GSP-Phot Teff, bp_rp, TIC mass and radius), and a per-sector and per-event analysis of R1003 (`fable-r1003/`). The 7a–7c scripts rerun from the repository root with the Python standard library (7d needs `rebound`, see below):

```
python3 reviews/2026-11-24-duet-research-runs-1-4/run7-temperature-and-r1003/temperature_split.py
python3 reviews/2026-11-24-duet-research-runs-1-4/run7-temperature-and-r1003/r1003_triple.py
python3 reviews/2026-11-24-duet-research-runs-1-4/run7-temperature-and-r1003/tertiary_orbits.py
```

## 7a. Hot binaries stay eccentric closer in

Script: [`temperature_split.py`](temperature_split.py). 552 dwarf secondaries have a temperature (GSP-Phot where it exists, since it fits extinction; TIC otherwise): 77 at or above the Kraft break (6,250 K), 475 below. "Eccentric" is |e cos ω| > 0.05, a lower bound on e.

| a/R₁ | cool: n | eccentric | hot: n | eccentric |
|---|---:|---:|---:|---:|
| < 4 | 38 | 0.00 | 12 | 0.00 |
| 4–7 | 89 | 0.00 | 31 | 0.16 |
| 7–10 | 89 | 0.06 | 15 | 0.33 |
| 10–15 | 113 | 0.25 | 6 | 0.17 |
| 15–25 | 75 | 0.41 | 3 | 0.33 |

- **At the same scaled separation, hot binaries are eccentric far more often.** At 4 ≤ a/R₁ < 10: 10 of 46 hot against 5 of 178 cool (one-sided Fisher p = 7 × 10⁻⁵). Keeping only secondaries ≥ 1 ppt, ≥ 5% of the primary and described without hedging ("possible", "weak", "displaced"…), it is 7 of 46 against 5 of 178 (p = 0.0035).
- **In period the shift is about a factor of two, less securely.** A logistic fit puts the midpoint of the eccentric fraction at about 4.2 d (hot) and 9.1 d (cool); 500 bootstraps give Δlog P = −0.30 (68%: −0.36 to −0.18; 95%: −0.42 to +0.04, so about 2σ; set `NBOOT` to change the count). Binned, at 4 ≤ P < 6 d: 6 of 16 hot, 10 of 91 cool (p = 0.014). Above 10 d there is no excess (p = 0.92), as expected once neither group is circularised. Separation, not period, is the cleaner variable, because hot stars are larger at a given period.
- **The edge sits at the Kraft break.** Moving the cut to 6,000 K dilutes the effect away (p = 0.32); 6,500 K keeps it with fewer stars (p = 0.11). TIC-only and GSP-Phot-only temperatures each give p ≈ 0.04 on their own.
- **Reading.** This is the expected signature of weaker tides in stars with radiative envelopes (dynamical tides) than in convective ones (equilibrium tides). Justesen & Albrecht (2021, ApJ 912, 123) found the opposite surprise in their TESS sample, a large circular fraction among 6,250–10,000 K binaries at a/R₁ ≈ 4–10. Here too most hot binaries at those separations are circular (36 of 46), so the two are compatible in kind; ours says a hot minority keeps e > 0.05 where no cool binary does. IJspeert et al. (2024, A&A; 14,573 O–F TESS binaries, |e cos ω| as here) find the same direction above 7,000 K: their circularisation period falls from 6.65 ± 0.27 d below 7,000 K to 5.66, 4.38 and 2.46 d at 7–8, 8–10 and > 10 kK. Their coolest bin lumps both sides of the Kraft break together; this sample, mostly below 7,000 K, suggests the step already starts at 6,250 K.
- **Caveats.** a/R₁ assumes q = 1 and TIC radii. Hot stars are younger on average, so age could do part of this. Of the 15 eccentric systems at a/R₁ < 10, three hot ones (R1121, R1163, R1341) have doubtful secondaries; the conservative test above excludes them. R1003 is the one cool eccentric system below a/R₁ = 8, and it is the triple of 7b; its TIC temperature (3,479 K, with a TIC radius of 1.06 R☉) is not credible at b = −2.7°, where bp_rp = 2.61 is mostly reddening.

*For the paper:* the script also draws [`ecosw-vs-aR-by-teff.svg`](ecosw-vs-aR-by-teff.svg) (|e cos ω| against a/R₁, hot in red, cool in blue). Cool binaries are flat to a/R₁ ≈ 9, apart from one point, R1003 (7b); hot ones scatter up from a/R₁ ≈ 4. With the table above it would make a short circularisation paragraph.

## 7b. R1003: eclipses that switched on, and what the third body can be

Script: [`r1003_triple.py`](r1003_triple.py), on Fable's measurements in [`fable-r1003/`](fable-r1003/). Fable found that R1003's eclipses are absent in TESS in 2019, 2021 and 2023 (1–3 ppt limits; free-phase sweeps empty) and 92–144 ppt deep in 2026, with a 100–130 s timing wobble in 2026 that passed a QLP/SPOC product control.

**(a) The host-table row describes an average over eclipse-free sectors.**
- `adopted_epoch_btjd` 3086.911 is in s65 (May 2023), where Fable measures 3.0 ppt in that very window.
- The tabled period (2.878458 d) links that epoch to 2026 across 334 unseen cycles. The 19 deep 2026 events alone give 2.8787113 ± 0.0000066 d; the two differ by 2.5 × 10⁻⁴ d (39σ), 2.0 h at the table epoch. The tabled period is a cycle count across a gap, not a measurement.
- `depth_ppt` 28.15 against a mean of 116 ppt for the deep events (QLP and SPOC mixed); `n_sectors` 7 counts four eclipse-free sectors.
- *Suggested fix:* adopt the 2026 ephemeris (T0 in s100, P = 2.8787113 d), depths from s100 (144.4 and 76.5 ppt, SPOC), and note "eclipses absent before 2026".

**(b) Attribution can probably be upgraded.** The only flagged neighbour is Gaia DR3 5861580634677163392 at 7.1″, with 2.94 in the attribution field. If that is its G-band offset, it gives 6.7% of the target's flux and can make at most ~69 ppt in a crowding-corrected curve, less than the 92–144 ppt measured. It was "capable" only against the diluted 28 ppt. (The s100 difference image is already on target.)

**(c) The 206.6-d Gaia orbit is not excluded as the third body.** Fable's light-travel-time (LTT) fit with Gaia's own phase needs 905 ± 45 s, which is unphysical, so Fable concluded that the outer orbit is probably shorter. But for P_in/P_out ≈ 0.014 the physical (dynamical) timing term is as large as the LTT term:

| P_out (d) | m₁₂, m₃ (M☉) | LTT (s) | dynamical (s) | Kozai–Lidov (yr) | nodal period (yr) |
|---|---|---:|---:|---:|---:|
| 206.6 | 2.0, 0.5 | 93 | 110 | 43 | 271 |
| 206.6 | 2.0, 1.0 | 164 | 184 | 26 | 162 |
| 82.6 | 2.0, 1.0 | 89 | 460 | 4 | 26 |

The dynamical term has its own phase and a P_out/2 harmonic, so an LTT-only template fixed to Gaia's periastron cannot test it. A 100–130 s wobble over an 80-d arc fits a 206.6-d tertiary at the expected amplitude. The timing alone does not exclude it.

**(d) The switch-on is hard for a 206.6-d tertiary.** The inner pair is tight (a ≈ 11 R☉ for 2 M☉), so one unit of impact parameter b (in R₁ + R₂) is about 10° of inclination, and going from no eclipse (b > 1) to the deep, non-grazing eclipses of 2026 needs b to fall by roughly 0.3–0.6 in ≤ 2.7 yr. The analytic rates above, and the N-body runs of 7d, give at most ~0.13 per year for a 206.6-d tertiary (m₃ = 1 M☉ at 40–60° mutual inclination; ≤ 0.09 per year for m₃ ≤ 0.5 M☉), so the Gaia orbit can do it only at the extreme: a massive tertiary on a highly inclined orbit. An ~80-d tertiary does it at 20–40° (0.2–0.5 per year). Either way the inner orbit's e ≥ 0.49 at P = 2.88 d, with periastron near 5.5 R₁, would circularise quickly on its own (run 6d: no cool binary below 4 d has |e cos ω| > 0.05), so a third body must be pumping it. This agrees with Fable's reading that the outer period is probably shorter than Gaia's, but for a different reason: the timing alone can't exclude 206.6 d (7b c); the switch-on rate nearly does.

*Tests:* Gaia DR4 epoch astrometry (Fable: due December 2) decides 206.6 d against a shorter outer period; the depth should keep changing sector to sector (s99 and s101 QLP, 96.6 ± 2.2 and 91.7 ± 3.2 ppt, show no growth yet, which is consistent with ≲ 1°/yr); the secondary's phase should drift as the inner orbit's apsides precess.

## 7c. R755 shows the same pattern, and its prediction windows need room for a third body

Script: [`tertiary_orbits.py`](tertiary_orbits.py).

- **R755 (TYC 7687-990-1, TIC 271053559) has the same pattern.** The paper reports its 24.65-d eclipses in s89 (2025) and flat, covered data in s8, s9, s35 and s62, with a 300.8-d Gaia astrometric orbit, and calls it "a failed stability check". The repository's own NSS copy gives that orbit e_out = 0.26 and a photocentre semi-major axis of 0.234 AU (0.54 mas at ϖ = 2.32 mas), a real orbit. P_out/P_in = 12.2 is inside the Mardling–Aarseth stable region for e_out = 0.26 (margin 5.9 against a critical 5.0; it would not be for e_out ≳ 0.35). The nodal period is of order 40 yr, and with a_in ≈ 45 R☉ the eclipse "season" spans only ~2.5° of inclination, a few years. So eclipses switching on between 2023 and 2025 is what a tertiary predicts, not a failure.
- **Two of the catalogue's systems with long Gaia astrometric orbits have eclipses that appeared during TESS.** That is worth one paragraph in the paper: a newly eclipsing pair is direct evidence for orbital precession, and both are cheap to follow (every new TESS sector measures the depth).
- **R755's predictions carry a third-body timing term.** The leading-order dynamical delay scale for P_in = 24.65 d and P_out = 300.8 d is 1.7–2.9 h (for m₃ = 0.5–1 M☉; the realised amplitude is this times factors of order e_out and sin² i_mut, so plausibly ≳ 0.5 h), plus 2–3.5 min of LTT. The paper's conditional predictions (BTJD 4327.29, 4351.95, ±0.05 d) leave out that term. The parenthesis already says a third body could alter the timing; the N-body test in 7d says by 8–25 h (median) after two years, so about a day.
- **Seven November 23 rows have a Gaia orbit 40–900 times longer than their eclipse period** (R952, R954, R994, R1000, R1003, R1066, R1549). All are in the stable region. Their expected timing amplitudes are listed by the script; R1000 (10.03 d inside 425.8 d, dynamical scale 11–18 min) and R1549 (5.33 d inside 276.0 d, 5–8 min) are the ones where a third-body ETV would be easiest to see. The repository's NSS copies hold only R755's two solutions, so e_out and a₀ for the other seven need the Gaia archive.

## 7d. N-body: Gaia's 124.7-d orbit reproduces A73, if its eccentricity is lower

Scripts: [`triple_nbody.py`](triple_nbody.py) (all three stars) and [`a73_robustness.py`](a73_robustness.py). They need `rebound` and `numpy` (`pip install rebound numpy`). Each triple is integrated for 2,000 outer orbits to test stability, then for 4–12 years to record every eclipse as seen from Earth: mid-times with light-travel time, impact parameter, single-cycle periods and the secondary's phase. Both orbits are edge-on on the sky (as Gaia's 90.9° astrometric inclination for A73 suggests); the mutual inclination is put in the outer node. Masses and radii are assumed (A73: 1.2 + 1.0 M☉, 1.4 + 1.0 R☉). The stars are point masses: no tides, rotational bulges or general relativity. That matters little for A73 and R755, but for R1003's 2.88-d pair those effects add apsidal precession that would damp Kozai cycles.

**A73 (TYC 4590-364-1; 17.54 d inside Gaia's 124.72-d orbit, ratio 7.1).** The paper says "A third body is needed to explain this, though the data do not show that it is Gaia's."
- **At Gaia's e_out = 0.412 the triple is unstable** in every configuration tried (m₃ = 0.25–1 M☉, mutual inclination 0–40°): the inner orbit is disrupted within 10–325 outer orbits (3–110 years). It is stable at e_out ≤ 0.2 and starts failing at 0.25–0.3, close to the Mardling–Aarseth limit (e_out ≈ 0.16 for this period ratio; that criterion is known to be conservative). (The copy of Gaia's solution in the repository, Chopard-Vilhem's `track3_astrometric_orbits_selected.csv`, has no error on e.)
- **With e_out = 0.10–0.15, m₃ ≈ 0.3–0.4 M☉ and a mutual inclination near 5°, the model reproduces what TESS shows** (paper Figure 4, 2019–2024), across three starting orientations of the outer orbit:

| | TESS, 2019–2024 | model, 5 yr |
|---|---|---|
| secondary phase (e cos ω swinging) | 0.461–0.532 | 0.450–0.542 (0.46–0.54 typical) |
| single-cycle periods | 17.39–17.85 d | 17.46–17.90 d |
| primary O−C about a linear ephemeris | ≈ 13 h peak to peak | 3–28 h |
| eclipse fade | 33% → 13% over ~4 yr | b changes by 0.10–0.14 (R₁ + R₂) per year |

- **The fade sets the mutual inclination.** At 10° or more, the model eclipses stop within 0.3–2.3 years; A73 has eclipsed since at least 2016 (NEOWISE) while fading, which needs ≲ 6°. A rise and then a fall in depth, as NEOWISE and TESS show, is what a near-coplanar node passing through alignment does.
- *Suggested wording:* "An N-body model with Gaia's 124.7-d orbit as the tertiary reproduces the secondary-phase swing, the single-cycle periods (17.4–17.9 d) and the rate of fade for a 0.3–0.4 M☉ tertiary on a near-coplanar orbit (mutual inclination ≲ 6°), but only if the outer eccentricity is 0.10–0.15; at Gaia's 0.41 the triple is unstable within decades." That is a testable claim: Gaia DR4's epoch astrometry should give the lower eccentricity, and A73's secondary phase should keep swinging.

**R755 (TIC 271053559; 24.65 d inside 300.8 d, e_out = 0.26).** Stable in every configuration. A mutual inclination of 6–20° turns eclipses on or off within 2–6 years, so flat sectors in 2018–2023 and eclipses in 2025 are expected. Over five years the eclipse times wander by 3 h (m₃ = 0.25) to 11 h (m₃ = 1 M☉) about a linear ephemeris, and single cycles run 24.61–25.10 d. A direct test ([`r755_prediction_miss.py`](r755_prediction_miss.py)): take two consecutive eclipses as the ephemeris, as the paper does, start the outer orbit at each of 8 phases, and extrapolate 28–30 cycles (about two years, the gap to BTJD 4327.29 and 4351.95). The prediction misses by a median of 8 h (m₃ = 0.25 M☉), 13 h (0.5 M☉) or 19–25 h (1 M☉), and by up to 20, 37 or 66 h at the worst outer phase, nearly independent of the mutual inclination between 3° and 20°. *For the paper:* the ±0.05 d on R755's predicted eclipses should be widened to about ±1 d (±0.5 d if m₃ is small), and the eclipses may stop again within a few years, so the "failed stability check" is better described as expected for a triple.

**R1003 (2.88 d inside 206.6 d; Gaia e_out not in the repository, 0.3 assumed).** Stable up to 60° mutual inclination (at 80° with m₃ = 1 M☉, Kozai cycles drive e_in above 0.95 within 40 outer orbits). The impact parameter changes by at most 0.13 per year (m₃ = 1 M☉, 40–60°), which is marginal for the 2023–2026 switch-on (7b d). A hypothetical 82.6-d tertiary gives 0.14–0.58 per year at 20–60°. This is the strongest argument here for a shorter outer period, and Gaia DR4 can test it.


## Credits and limits

Fable 5 (keeps-some-ocean) made the temperature join and all R1003 light-curve measurements (depths, event times, product control, LTT fit) on the house's cached TESS data and ESA's Gaia archive. Duet did the temperature statistics, the row comparison and the triple scalings. The analytic triple numbers in 7b and 7c are leading-order scalings with assumed masses, good to about a factor of two; the N-body runs in 7d use assumed masses and radii and point-mass gravity only.

**Reproducibility.** Rerun from the repository on November 25, `temperature_split.py`, `r1003_triple.py` and `tertiary_orbits.py` reproduce every number quoted in 7a–7c, and `temperature_split.py` regenerates `ecosw-vs-aR-by-teff.svg` byte for byte. The script's default is 100 bootstraps; the 500-bootstrap interval in 7a is from `NBOOT=500`. `triple_nbody.py`, `a73_robustness.py` and `r755_prediction_miss.py` need `rebound`, which was not installed for that rerun, so 7d's numbers are the run's own output: `nbody-results.txt` holds the `triple_nbody.py` and `a73_robustness.py` tables (they match the 7d text), while the R755 prediction-miss figures (median 8, 13 and 19–25 h) were not saved to that file and have not been checked independently.
