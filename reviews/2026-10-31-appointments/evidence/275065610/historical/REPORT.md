> Historical report: superseded by the current reconciliation at ../../../reports/275065610/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 275065610 (TYC 1561-794-1): adversarial check

Gaia DR3 SB1, P 28.05277 ± 0.00388 d, e 0.5113 ± 0.0079, ω 83.98 ± 1.36°, K1 39.92 ± 0.32 km/s, significance 126. G 11.33, parallax 1.317 mas (about 760 pc), RUWE 1.73. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 3, 18:50–19:07). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, step-by-step notes in `progress.md`; downloads in `[local path omitted] Everything the stopped earlier checker left was rerun.

## Verdict: CONFIRMED

The star is a detached, eccentric eclipsing binary that the eclipse catalogues I could query don't list. Its only listing is Kostov table 2, which is unvetted and doesn't count. There are four A eclipses of about 5.0–5.3%, and all four sit on the target's pixel. The B eclipse is missing because the geometry rules it out, not because TESS failed to cover it.

---

## 1. Archives

| Source | Script | Result |
|---|---|---|
| Gaia DR3 gaia_source | `gaia_q.py` | G 11.33, BP−RP 0.81, parallax 1.317 mas (about 760 pc), RUWE 1.73, non_single_star 2 |
| Gaia DR3 NSS orbit | `arch2.py` | SB1: P 28.05277 ± 0.00388 d, e 0.5113 ± 0.0079, ω 83.98 ± 1.36°, Tp 7.964 ± 0.074 (BTJD 396.96), K1 39.92 ± 0.32 km/s, γ 8.21 km/s, significance 126 |
| Gaia DR3 variability tables (vari_summary, vari_eclipsing_binary, classifier, rotation, LPV) | `arch2.py`, `arch3.py`, `arch4.py` | Target: none. Within 120″: no eclipsing binaries. Only two unrelated classifier entries (G 15.2 at 73″ SOLAR_LIKE; G 17.8 at 118″ RS) |
| VizieR TAP: VSX, SB9, WDS | `arch2.py` | 0 rows each |
| VizieR asu-tsv 60″ cones | `arch3.py` | Prša+2022, IJspeert+2024, Kostov t3/t4, ZTF (Chen+2020), ATLAS, ASAS-SN, WISE, VSX, SB9, WDS, ASAS ACVS, Justesen, KELT: 0 rows each |
| Kostov+2025 table 2 (unvetted) | `arch3.py`, `arch4.py` | Lists the target **and also the neighbour TIC 275065613** (45″, Tmag 11.38) |
| Mowlavi Gaia EB catalogue (`J/A+A/674/A16`) | `arch3.py` | Returned a dump of an unrelated table, so unusable. The direct Gaia vari_eclipsing_binary query above replaces it |
| `cats.py` | `cats.py` | VSX none, ASAS-SN none, Kostov t2 only, SIMBAD type SB* |
| SIMBAD | `arch3.py` | Names: TYC 1561-794-1, 2MASS J17533827+1848541. Types: *, NIR, SB*. Only reference is the Gaia DR3 NSS paper (2023A&A...674A..34G) |
| ZTF DR light curve (IRSA) | `arch3.py` | 0 rows (the star is too bright) |
| ExoFOP | `arch2.py` | **HTTP 503, tried once. CTOIs are unchecked** |
| NASA Exoplanet Archive TOI table | `arch4.py` | No TOI for TIC 275065610, TIC 275065613, or anything in the surrounding box |
| MAST CAOM 10″ | `archives.py` | QLP s26 (1800 s), s53 (600 s), s79 and s80 (200 s); TASOC s26. **No SPOC, TESS-SPOC or TGLC products** |
| Web search on all three names | — | No hits about this star |

**Neighbours within 60″:**

| Neighbour | Separation | Dip it would need (5.1% × 10^(0.4Δm)) |
|---|---|---|
| G 12.11 (TIC 275065613; BP−RP 1.49, parallax 0.24, non_single_star 0) | 45.2″ | about 8.4% (using ΔT = 0.49) |
| G 17.66 | 4.3″ | about 17× its own flux, so impossible |
| G 17.4–17.9 (several) | 44–58″ | impossible |

---

## 2. Eclipses measured

Method (`meas.py`, results in `meas.txt` and `overview.png`): a trapezoid times a quadratic baseline, fitted to raw SAP_FLUX within ±0.8 d of each eclipse. The t0 error comes from the profile χ² multiplied by a red-noise β.

| Sector | t0 (BTJD) | Depth | T14 | T12 | Flat bottom | Notes |
|---|---|---|---|---|---|---|
| s26 | 2023.8732 ± 0.0013 | 5.26% | 6.97 h | 2.69 h | 1.59 h | 10 of 14 in-eclipse cadences carry QLP flag 4096. Using only unflagged cadences: 2023.8760, 5.18% |
| s53 | 2753.1511 ± 0.0013 | 5.15% | 6.84 h | 2.63 h | 1.58 h | unflagged cadences |
| s79 | 3454.3817 ± 0.0014 | 5.12% | 6.82 h | 2.51 h | 1.80 h | all unflagged |
| s80 | 3482.4326 ± 0.0014 | 5.04% | 6.93 h | 2.62 h | 1.69 h | all unflagged |

- **Background (SAP_BKG):** the in-minus-out difference is within the out-of-eclipse scatter in every sector (s26 −239 vs 304; s53 −1613 vs 1975; s79 +321 vs 1228; s80 −4 vs 61, all e-/s).
- **QLP centroid:** SAP_X moves by −0.008 to −0.016 px during every eclipse. The pixel test below explains this: the light centroid is pulled toward the G 12.1 neighbour, so when the target dims the centroid moves toward that neighbour.
- **Blind dip census** (`census.py`, `census.txt`): boxes of 3, 7, 14 and 21 h over every sector, unflagged cadences only, keeping anything deeper than 4σ and 2000 ppm.
  - The four A eclipses are the only real hits.
  - s80 also shows dips at 3489–3493 and 3503–3506. They sit on SAP_BKG swells after the s80 scattered-light event (`s7980.png`), are not at the B phase, and are systematics.
  - The first census run had a sign bug in the depth; I fixed it and reran.
- **Second pipeline, TASOC s26 FLUX_RAW** (`tasoc.py`, `tasoc.txt`): t0 2023.8823 ± 0.0031, depth 4.29%, T14 6.97 h, T12 2.74 h. TASOC marks all 74 cadences in the window as good, although QLP flags them. The shallower depth and the 13-minute timing difference come from a different aperture, raw untrended flux and 1800 s cadence. The eclipse is independently present.

---

## 3. Ephemeris and comparison with Gaia

From `ephem.py` (`ephem.txt`), a linear fit to the A eclipses:

- **T0 = 2023.87270 ± 0.00181**
- **P = 28.04921 ± 0.00005 d**
- Epochs 0, 26, 51, 52; χ² 0.75 for 2 degrees of freedom.
- O−C: +0.8, −1.5, −0.8, +1.6 min.
- Mid-span epoch: T0 = 3089.74261 ± 0.00104.

I ruled out a period of P/2: there is unflagged flat data at 3468.4 in s79.

**Against Gaia:**
- Gaia's P is longer by 0.00356 d, which is −0.92σ.
- Gaia-predicted A conjunctions come from `conjmc.py` using this star's own 6×6 correlation vector, not one copied from another star. Observed minus predicted is −0.282, −0.376, −0.464 and −0.466 d, or −1.11, −1.07, −1.03 and −1.03σ. That is one correlated offset in Tp and ω, not four separate discrepancies.
- Gaia's B−A phase separation is 0.5396 ± 0.0089; its e cos ω is 0.054 ± 0.012 and e sin ω is 0.508 ± 0.008.
- With no B eclipse, there is no measured e cos ω or duration-ratio e sin ω to compare.

---

## 4. Independence tests

**Pixel test** (`tcut.py`, `pixreg.py`; output `pix.txt`, `pix_s26/53/79/80.png`). I fitted every pixel of 11×11 TESScut cutouts with a quadratic trend plus the eclipse template, over four sectors and three camera/CCD combinations:

| Sector | Depth on target pixel | Depth on the 45″ neighbour's pixel | Deficit centroid to target | Deficit centroid to light centroid |
|---|---|---|---|---|
| s53 | 4.98 ± 0.05% | 0.37 ± 0.05% | 6.6″ | 9.0″ |
| s79 | 4.94 ± 0.04% | 0.38 ± 0.04% | 4.9″ | 12.9″ |
| s80 | 4.87 ± 0.04% | 0.26 ± 0.06% | 2.8″ | 12.0″ |
| s26 | 4.96 ± 0.09% | 0.22 ± 0.10% | 2.5″ | 13.2″ |

- The fractional depth falls steadily from the target to the neighbour (for example in s80: 4.87 → 3.14 → 0.26 → 0.0%).
- If the neighbour were the source, its own pixel would show about 8%.
- **So the eclipse is on TIC 275065610.** The Kostov t2 flag on TIC 275065613 is most likely light bleeding from the target.

**Second pipeline:** TASOC s26, above. MAST has no SPOC or TGLC product for this star.

**B windows** (`census.py`, `bnull.json`). I placed them using the measured A ephemeris plus Gaia's phase separation, giving σ = 0.25 d, and scanned box centres over ±0.75 d (3σ):

| Sector | B time (BTJD) | Coverage | Largest box depth at 7 / 14 / 21 h |
|---|---|---|---|
| s79 | 3469.52 | 100% | 430 ± 163 / 628 ± 110 / 793 ± 93 ppm |
| s80 | 3497.57 | 100% | 352 ± 132 / 269 ± 94 / 335 ± 77 ppm |
| s26 | 2010.96 | 29–49% (sector start) | at most 650 ppm |
| s53 | 2768.29 | 55–73% (sector end) | at most 880 ppm |

That sets an upper limit on a B eclipse of about 0.1% in two fully covered windows.

---

## 5. Physics

From `physics.py` (`physics.txt`):

- **Mass function** f(M) = 0.1173 M☉. The minimum companion mass m2(i = 90°) is 0.77, 0.84 or 0.90 M☉ for M1 = 1.2, 1.4 or 1.6.
- **Orbit size:** a ≈ 49–53 R☉. The separation is about 24–26 R☉ at the A conjunction (near periastron) and about 73–79 R☉ at B (near apastron).
- **Which star is in front:** A is at true anomaly ν = 90° − ω, when the RV primary is farthest from us. So at A the companion passes in front of the primary. At B the primary would cover the companion.
- **Limb-darkened two-sphere fit** of all four A eclipses, with Gaia's e and ω held fixed, a dark companion, and quadratic limb darkening 0.32/0.27:
  - a/R1 = 15.86, k = R2/R1 = 0.250, impact parameter b_A = 0.82 R1, inclination 83.95°, χ² 1318 for 1389 points.
  - That implies R1 ≈ 3.1 R☉, close to the TIC's 3.42 and to my luminosity estimate of about 3.7 from the parallax. The primary is a subgiant, although the TIC labels it a dwarf.
  - R2 ≈ 0.78 R☉, which matches a main-sequence companion of about 0.8 M☉ and fits the mass function.
  - Depth, duration and the V/U shape are all consistent with one geometry. The companion's light (a few percent) is ignored in the fit, which would raise k slightly.
  - The first version of this fit had a self-normalising χ² bug; I fixed it and reran.
- **Why B is missing:** the impact parameter at B is larger by (1 + e sin ω)/(1 − e sin ω) ≈ 3.07, so b_B = 2.51 R1, far beyond the contact limit of 1 + k = 1.25. Fits with b_A ≤ 0.6 are excluded (Δχ² > 1200), and even b_A = 0.6 gives b_B = 1.84. A B eclipse would need e sin ω below about 0.21, against Gaia's 0.508 ± 0.008. **The geometry predicts the miss.** Had B occurred, it would have been at most the companion's light fraction, about 3%.

---

## 6. Verdict: CONFIRMED

**The deciding numbers:**
- Four A eclipses at 5.04–5.26% repeat on a linear ephemeris to within ±1.6 min.
- The period agrees with Gaia's to −0.9σ.
- The pixel-level depth is 4.9–5.0% on the target against at most 0.4% on the only neighbour bright enough to matter, in four sectors.
- TASOC independently shows the s26 eclipse.
- The eclipse shape with Gaia's e and ω gives R1 ≈ 3.1 R☉ and R2 ≈ 0.78 R☉, consistent with the mass function.
- B is absent because the geometry excludes it (b_B ≈ 2.5 R1), and the data agree (no B deeper than about 0.1% in two fully covered windows).
- The Gaia conjunction times run about 0.3–0.47 d early, a single correlated −1σ offset.

**Next predicted eclipse times (BTJD):**
- **A (eclipse):** 4351.957, 4380.006, 4408.055, 4436.105, 4464.154. Each ±0.003 d formal.
- **B conjunctions (no eclipse expected):** 4367.09, 4395.14, 4423.19, 4451.24, each ±0.25 d.

**What would settle it further:**
- A spectroscopic double-lined detection, or a high-resolution RV check of the companion's mass.
- One more A eclipse in a future sector, to tighten the period.
- Re-checking ExoFOP for CTOIs once it is back up.

**Services that couldn't be checked:** ExoFOP (503), so CTOIs are unchecked. The Mowlavi VizieR table returned garbage and was replaced by the direct Gaia query.
