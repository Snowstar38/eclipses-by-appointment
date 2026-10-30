# TIC 306477840 (TYC 5361-543-1, Gaia DR3 2994311049695999616): per-object vet

Opus 5.5 subagent, wave 3, 2026-10-19. Resumed a dead session's folder. Every number below comes from a file in this folder.
The dead session left `vet-out.txt`, `bkgreg-out.txt`, `cats-out.txt`, `morecats-out.txt` and `mastlc-out.txt`. This session added
`indep-out.txt`, `tglc-out.txt`, `diff2-out.txt`, `sec-out.txt`, `hbtest-out.txt` (+ `hbtest_306477840.png`), `physics-out.txt`
and `conjepoch-out.txt`. Downloads are in `C:\Home\sky\data\qlp-sb-p20-60\pervet306477840\`.

## Verdict: CONFIRMED (eclipsing SB1; primary eclipse at Gaia conjunction A; no secondary, as the geometry predicts)

The deciding numbers:
- **Heartbeat test (mandatory: conjunction A sits at ν ≈ −11°, near periastron).** Both models share the same const + 3-harmonic base,
  fitted to 1000 bins (7.9 min); the trapezoid gives χ² 1189.
  - A Kumar heartbeat with Gaia's e = 0.129 and ω = 101° fixed (periastron phase and i free) is worse by **Δχ² = +5905**.
  - With e free within 3σ of Gaia (0.02–0.24) and ω free: **+5150**.
  - Even with e free to 0.9 (best e 0.76, 18σ from the RV e): +227.
  - The event is **flat-bottomed**: T14 3.72–3.75 h, T12/T14 0.35, flat 1.1 h. A Gaia-geometry heartbeat is a ~1-day-wide hump or dip.
- **Timing locked to the RV orbit.** At the Gaia epoch the TESS primary is **+0.28 h (+0.18σ) from conjunction A** (387.4849 ± 0.0661;
  MC with corr_vec, ω–Tp corr 0.9946). At the TESS sectors the offset is +1.9 to +5.1 h (+0.6σ). TESS P 5.520586(3) vs Gaia 5.520242(657): +0.5σ.
- **On target.** The free-position difference image puts the source **0.7″ (s6) and 0.9″ (s33)** from the target. Pinning it on the 20″
  G 15.52 neighbour is worse by Δχ² +1230 / +1810. The batch diffimg (s87) gives 1.63″, peak_on_target.
- **Repeats in other pipelines.** SPOC PDCSAP 10.06 ± 0.15 (s6) and 10.60 ± 0.15 (s33); SPOC SAP 9.64 / 10.04; TGLC s6 aperture 11.4 ± 0.2,
  psf 7.9–13.7 per event; QLP SAP 10.15 ± 0.10 ppt.
- **No prior art.** No VSX, ASAS-SN, SB9 or WDS entry; nothing in J/AJ/160/111, Gaia vari_*, or Prša/IJspeert/Kostov; ExoFOP has no TOI or CTOI;
  no SPOC DV/TCE among its TESS-SPOC products; SIMBAD lists SB* only; a web search on the TYC and TIC names found nothing.

## 1. Archives
`cats.py --r 60`: VSX none, ASAS-SN none, SIMBAD TYC 5361-543-1 [SB*]. `morecats.py`: SB9, WDS, J/AJ/160/111 none; ExoFOP empty.
Gaia TAP (`gaia.json`): SB1 P 5.520242(657), e 0.129(35), ω 100.8(18.9)°, Tp −1.3835(2837), K1 21.99(1.24) km/s, 22 RV epochs,
significance 17.8, RUWE 1.39, no vari rows. TIC: Teff 6484 K, logg 3.89, R 2.17 R☉, M 1.32 M☉, contratio 0.033.

## 2. Eclipse measurements (QLP SAP, QUALITY==0, untrimmed; `vet-out.txt`)
Global trapezoid: depth 10.26 ppt, T14 3.72 h, T12 1.30 h, flat 1.12 h. A V shape is rejected (T12/T14 = 0.5 is worse by Δχ² +103).
There are 13 primaries across s6/s33/s87, all with S/N 18–37 and depths 9.3–11.0 ppt.
- Depth constancy is χ² 22.1/12, driven by a sector offset: s6 9.65 ± 0.17, s33 10.75 ± 0.19, s87 10.14 ± 0.17. SPOC shows the same sign
  (s6 10.06, s33 10.60), so this is per-sector aperture dilution, not astrophysics.
- Odd and even depths are 10.11 ± 0.15 and 10.18 ± 0.14.
- Background regression implies ≤ 0.05 ppt. Centroid shifts in eclipse are −0.6 / −0.7 mpix (a 20″ source would give ~10 mpix).
- Two events need comment:
  - E400 (3677.77): 25 flagged cadences and a background excursion (+100 ppt of target), yet its depth (9.68) is normal.
  - E402 (3688.81): coincides with the listed s087 systematic at 3688.8, and its depth is normal (10.16).
  Every other event is clean. Two windows contain a bit-32 cadence.
- Control phases have no S/N > 3. Blind census: 14 dips at S/N ≥ 4; 13 are the eclipses, and the one other (1.7 ppt) is under half the eclipse depth.

## 3. Ephemeris, secondary, e cos ω / e sin ω
Primary: **P = 5.520586 ± 0.000003 d, T0 = 2474.27805 ± 0.00051 BTJD** (n 13, χ²/dof 25.1/11, errors scaled × 1.51, O−C rms 2.6 min).
**No secondary.**
- Gaia predicts Δφ(B−A) = 0.486 ± 0.026.
- The best peak anywhere in 0.40–0.60 is S/N 2.1, below the controls (`sec-out.txt`). At phase 0.500: +0.06 ± 0.09 ppt.
- The 3σ limit is ≲ 0.3 ppt over the Gaia window.
So e cos ω and e sin ω cannot be measured photometrically. Gaia's e sin ω = +0.120 ± 0.035 is what makes the secondary miss (§5).

## 4. Independence
- Other pipelines: TESS-SPOC PDCSAP/SAP (s6, s33) and TGLC (s6), all showing the eclipse at the QLP ephemeris.
- Difference images: two TPF sectors (`diff2-out.txt`); the pinned-PSF `tpfdiff.py` also prefers the target (χ² 1210 vs 6031 / 1130 vs 3746).
- Neighbours (G < 17 within 90″) and the dip each would need:
  - 15.52 at 20″ → 0.44, and excluded by the difference image.
  - 13.96 at 84″ → 103 ppt.
  - All others need ≥ 0.6 and lie ≥ 32″ away.

## 5. Physics
- Mass function: f(M) = 0.00593 M☉. For M1 = 1.32, m2(i ≈ 86°) ≈ 0.24 M☉, so the companion is an M dwarf (R2 ≈ 0.25 R☉, k ≈ 0.115, T2 ≈ 3300 K).
  a ≈ 15.2 R☉, a/R1 ≈ 7.0.
- Conjunction A (primary behind) is where the dip is, so this is the companion transiting the F star.
- At conjunction A the separation is r = a(1−e²)/(1+e sin ω) ≈ 0.87a. Central duration ≈ 5.9 h, so the observed 3.72 h gives **b ≈ 0.87**.
  That predicts T23/T14 ≈ 0.26 (observed flat/T14 = 0.30) and a depth of ≈ k² × LD ≈ 11 ppt (observed 10.2–10.8 after dilution).
  One geometry fits depth, duration and shape.
- **Secondary.** At conjunction B, b_B = b_A (1+e sin ω)/(1−e sin ω) ≈ 0.87 × 1.27 ≈ 1.10, against 1+k = 1.115. The occultation is at most
  a sliver, and even a full occultation of a 3300 K dwarf behind a 6484 K star would be only k²J ≈ 0.8 ppt. The null is the expected outcome.

## Row fixes for the paper table
| field | ledger | fix |
|---|---|---|
| P (d) | 5.52057 | **5.520586 ± 0.000003** |
| T0 (BTJD) | — | **2474.27805 ± 0.00051** |
| depth (ppt) | 9.4 | **10.15 ± 0.10** (QLP SAP trapezoid; per-sector 9.65–10.75; SPOC PDCSAP 10.06–10.60) |
| T14 (h) | — | **3.72** (flat-bottomed, T12 1.30 h) |
| n events | 13 | 13 (unchanged) |
| dphi | +0.014 | +0.014 to +0.039 across the sectors (+0.6σ); **+0.002 (+0.18σ) at the Gaia epoch** |
| secondary | — | none; < ~0.3 ppt (3σ), geometrically expected to miss (b_B ≈ 1.10) |
| heartbeat | — | rejected, Δχ² +5150 (Gaia-consistent e) |

## Next predicted eclipses (BTJD)
- Primary: **4400.9626, 4406.4832, 4412.0037** (± 2 min).
- Secondary (Gaia Δφ 0.486 ± 0.026; expected undetectable or a sliver): **4403.6456, 4409.1662, 4414.6867** (± 3.5 h).

## What would settle it further
- It is already settled as an eclipse.
- RV-quality e and ω (or a detected sliver secondary) would pin b_B and the companion temperature.
- A spectrum would refine M1, which fixes m2.
