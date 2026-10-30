# TIC 234880209 (HD 259137, G2V, Tmag 10.14): per-object vet

**Verdict: CONFIRMED.** HD 259137 is an eclipsing binary: a G dwarf eclipsed every 4.270292 d by a ≈0.11 Msun M dwarf.

**Prior-art caveat:** the transit signal is already published as a *planet* candidate. It appears in the DTARPS-S Galactic-plane list (Melton+ 2024, AJ 167, 203, table4): P 4.27030, depth 0.0188, Rp 13.4 Re, T0 1470.880, ProbRF 0.75, no TOI. What is new is the classification: the Gaia SB1 orbit shows the companion is a star.

Wave 4, 2026-10-20/21. Resumed from a killed session; its receipts (gaia.json, cats-out.txt, exofop.json) checked out against fresh runs. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## 1. Archives
- `cats.py --r 60`: VSX none, ASAS-SN none, SIMBAD HD 259137 [SB*].
- Gaia DR3 NSS SB1: P 4.270326 ± 0.00049, e 0.113 ± 0.053, ω 86.5 ± 24°, K1 13.25 ± 0.81 km/s. vari_summary and vari_eclipsing_binary are empty. RUWE 1.19.
- VizieR cones found no entry in: SB9, WDS, GCVS, Prša+2022, IJspeert+2024, Gaia vEB, Kostov table2, Gaia-ASAS-SN, LAMOST.
- SIMBAD lists G2V, SB*, 7 references, including DTARPS II, which led to the table4 match above.
- ExoFOP: no TOI or CTOI. A web search found no papers about the star.
- MARVELS (Grieves+ 2018, J/MNRAS/481/3244): G2V dwarf, M 0.96, R 0.88, [Fe/H] −0.31 (implied density 1.41 solar; the eclipse duration gives 1.05, between MARVELS and TIC — fits b ≈ 0.75; m2 ≈ 0.106 M☉ with M1 = 0.96, barely moved). Not in DIAmante (Montalto+ 2020), matching the DIAmante=false flag in its DTARPS row. Gaia DR3 multiplicity (J/A+A/674/A34): the same SB1, no variability class.

## 2. Eclipse measurements (QLP SAP, QUALITY==0, no trimming)
Outputs: vet-out.txt, events.png, fold_oc.png.
- 15 primaries in s006, s033 and s087, each with S/N 31–85.
- Shape: **depth 18.76 ± 0.07 ppt, T14 2.22 h, T12 0.55 h, flat bottom 1.11 h**. A V shape is rejected (Δχ² +623).
- Depth by sector: 18.19 / 19.62 / 18.56 ppt. The same pattern shows up in other pipelines (SPOC PDCSAP 17.87 / 18.42, TARS 18.28 / 18.53 / 17.86), so it comes from the apertures, not the star.
- Odd 18.80 ± 0.11 vs even 18.72 ± 0.10 ppt.
- No momentum-dump (bit 32) cadences in any window and no event near a listed sector-wide systematic time.
- Centroid shifts: dX +0.3 ± 0.9 mpix, dY −0.5 ± 0.2 mpix.
- Control phases: all below 0.17 ppt except phase 0.5.
- Blind dip census: the 6 dips off the ephemeris are all ≤ 1.5 ppt. None reaches 9.4 ppt (half the eclipse depth).

## 3. Ephemeris and Gaia
- **P = 4.270292 ± 0.000001 d, T0 = 2508.56208 ± 0.00018 BTJD**, O−C rms 1.0 min over 6 years.
- Gaia P differs by **−0.07σ**.
- The eclipse sits at Gaia conjunction A (companion in front) to within +0.18σ / +0.07σ / +0.00σ in the three sectors.
- Gaia predicts the other conjunction at phase 0.503 ± 0.031; Gaia e cos ω = 0.005 ± 0.049, e sin ω = 0.103 ± 0.049.
- Secondary eclipse (sec2.py): a tentative 0.5–0.9 ppt dip appears near phase 0.49–0.51, but it is **not robust**:
  - its phase moves from 0.4925 to 0.5075 depending on the detrending mask;
  - it is absent in s087 (−0.03 ± 0.14 ppt);
  - individual events scatter from −0.6 to +3.4 ppt.
- So no secondary is claimed and no e cos ω / e sin ω is derived from the light curve. If the dip is real, |e cos ω| ≲ 0.02, which agrees with Gaia.

## 4. Independence
- Other pipelines see the same eclipse at the same times: TESS-SPOC PDCSAP 17.87 (s6) and 18.42 (s33), SPOC SAP 17.47 / 18.20, TARS 18.28 / 18.53 / 17.86.
- TGLC s6 aperture flux gives 26.0 ppt; its PSF flux is all NaN.
- Difference image from the TESS-SPOC s033 pixel file (5 events): the strongest loss is on the target pixel (S/N 41.8). In the single-star fit, the target wins with χ² 1173 against 9476 for the next star (G 11.65 at 65.8″); the target's implied dip is 16.3 ppt.
- Neighbours: G 11.65 at 65.8″ would need a 50 ppt dip and is rejected by the difference image. G 16.2 at 85″ and G 16.8 at 87″ would need more than 100%. TIC contamination ratio is 0.014.

## 5. Physics (TIC M1 1.04, R1 1.055)
- Mass function f(m) = 0.00101 Msun, so **m2(i = 90°) = 0.110 Msun** (0.099–0.120). a = 11.6 Rsun.
- k = 0.137, so R2 ≈ 0.145 Rsun.
- From the duration: b ≈ 0.75, a/R1 ≈ 11.25 (11.0 expected from TIC values), stellar density 1.05 solar (0.89 from TIC), i ≈ 86°.
- Expected occultation 0.8–1.2 ppt for a 2900–3100 K companion. Ellipsoidal and beaming signals are ≤ 0.16 ppt.
- The 3 ppt cos 2φ term appears only in s033, in every pipeline, so it is probably spot modulation on the G dwarf.
- Everything fits one geometry.

## 6. Verdict and predictions
**CONFIRMED.** G2V + ≈0.11 Msun M-dwarf eclipsing SB1. The deciding numbers:
- P agrees with Gaia to −0.07σ, and the eclipse sits within 0.2σ of Gaia conjunction A in all 3 sectors.
- 15/15 events give a constant 18.8 ppt depth in QLP, SPOC and TARS.
- The difference image is on target (Δχ² ≈ 8300).
- m2 = 0.11 Msun and R2 ≈ 0.145 Rsun are consistent.

It is prior art as a DTARPS planet candidate and should be reported as a stellar companion.

Next eclipses (BTJD):
- Primary (±0.7 min): 4336.2471, 4340.5173, 4344.7876, 4349.0579
- Secondary (tentative, phase 0.50 ± 0.01, ±1 h): 4338.382, 4342.653, 4346.923, 4351.193

What would settle it further: the occultation in future 200-s sectors, or RVs to pin down e.
