> Historical report: superseded by the current reconciliation at ../../../reports/49416839/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 49416839 (UCAC4 424-055126): adversarial check

Gaia DR3 SB1, P 21.43249 ± 0.00834 d, e 0.3558 ± 0.0184, ω 314.38 ± 4.34°, K1 33.36 ± 0.69 km/s, significance 48. G 11.47, BP−RP 0.82, parallax 2.24 mas, RUWE 0.89; TIC R 2.01 R☉. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 5, 19:22–19:29). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, every step in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED, and there are two eclipse kinds, not one

The classifier saw two eclipses at conjunction B. I found three B eclipses and also three shallow eclipses at conjunction A. The s036 background spike is a single bad cadence and does not affect the eclipse. A neighbour that Kostov table 2 flags is ruled out as the source at the pixel level.

## 1. Archives (what was queried, what came back)
- **Gaia DR3** (`gaia_q.py`, `arch2.py`):
  - Target: G 11.47, BP−RP 0.82, parallax 2.24 mas, RUWE 0.89.
  - NSS SB1 orbit: P 21.43249 ± 0.00834 d, e 0.3558 ± 0.0184, ω 314.38 ± 4.34°, T_peri −8.118 ± 0.166 (BTJD 380.882), K1 33.36 ± 0.69 km/s, significance 48. RV amplitude (robust) 67 km/s over 16 transits.
  - vari_summary and vari_eclipsing_binary: 0 rows.
- **Neighbours within 90″:** G 13.20 at 28.8″ (TIC 49416838), G 12.98 at 61.8″, G 12.78 at 65.8″, G 15.84 at 68.4″. All others are fainter than G 16.5.
- **VizieR TAP:** VSX, SB9 and WDS returned 0 rows.
- **VizieR asu-tsv 60″ cones** (`viz.py`): 0 rows from VSX, Prša+2022, IJspeert+2024, Kostov t3, Kostov t4, ASAS-SN II/366, SB9, WDS, ATLAS, Gaia vclassre and ASAS ACVS.
  - **Kostov t2 flags the neighbour TIC 49416838** (Tmag 12.62, 28.8″). That is an unvetted ML list, and the flag is almost certainly our eclipse blended into the neighbour's light curve; see section 4.
  - The "Mowlavi" query returned 326 rows from the synthetic-photometry table. That is not prior art.
- **cats.py:** no VSX or ASAS-SN entry. SIMBAD lists the star only as [SB*].
- **ExoFOP:** HTTP 503 (one try, plus curl). CTOIs were not checked.
- **NASA Exoplanet Archive TOI table:** no TOI.
- **Web search** on the UCAC4, TIC and Gaia DR3 ids: nothing about this star.
- **Light curves on MAST:**
  - QLP: s9, s36, s46, s72.
  - TESS-SPOC: s9, s36, s46, s72.
  - TARS: s9, s36, s46, s72.
  - TGLC, eleanor-lite and T16: s9 only.
  - No SPOC 2-min data.

## 2. Every eclipse measured
Fits are trapezoids on raw SAP or FLUX (`ecl.py`, `afit.py`).

**B eclipses (ν = 270° − ω; the primary passes in front of the companion):**

| Event | Sector | Pipeline | Mid-time (BTJD) | Depth | T14 | T12 | Flat |
|---|---|---|---|---|---|---|---|
| B1 | s9 | TESS-SPOC, all cadences | 1558.2868 ± 2.4 min | 1.15% | 5.81 h | 2.2 h | 1.4 h |
| B2 | s36 | QLP | 2286.8527 ± 2.2 min | 1.33% | 6.05 h | 2.4 h | 1.3 h |
| B3 | s72 | QLP | 3272.5624 ± 1.9 min | 1.35% | 5.79 h | 1.9 h | 1.9 h |

- **B1 (s9):** every QLP cadence in it is flagged 4096 (scattered light), but it is unflagged in TESS-SPOC, TARS and eleanor. Depths by pipeline: QLP 1.22%, TARS 1.19%, eleanor 1.00%. Mid-times agree within 10 min.
- **B2 (s36):** TESS-SPOC 1.12% and TARS 1.43%, mid-times within 1 min. The "background spike" is one cadence at 2286.8219 (QUALITY 4096, flux 0.473, SAP_BKG 1172 against about 250). The dip itself is about 35 unflagged cadences with flat background, so the spike is irrelevant.
- **B3 (s72):** TESS-SPOC 1.18% and TARS 1.15%. The event is complete before the data gap.
- **Background and centroids:** background in-minus-out is within 1 sd in its own units for every event, and centroid shifts are 0.01 px or less.
- **Common mode:** at the three B times, other stars on the same camera/CCD show at most 0.04%, 0.03% and 0.17%. These are not systematics.

**A eclipses (ν = 90° − ω; the companion passes in front), newly found:**

| Event | Sector | Mid-time (BTJD) | Depth | T14 | Shape and notes |
|---|---|---|---|---|---|
| A1 | s9 | 1564.955 ± 6 min | 0.32–0.48% | 3.8–4.3 h | V-shaped; seen in QLP, TESS-SPOC and TARS |
| A2 | s46 | 2572.082 ± 12 min | 0.21–0.28% | 2.9–4.7 h | Seen in TESS-SPOC and TARS, and visible by eye in QLP. The QLP fit diverged and was not used. |
| A3 | s72 | 3279.25 ± 40 min | 0.20–0.28% | — | Just before a gap, so egress is lost. Weakest of the three. |

- All three fall at the same phase, 0.3104–0.3139 after B.
- Other stars on the same camera/CCD show at most 0.08%, 0.18% and 0.08% at these times, so A3 is not the pre-gap common mode.

**Blind census** (`windows.py`, QLP q0 and all cadences, TESS-SPOC, TARS):
- Nothing deeper than max(0.3%, 5 sd) apart from these events and the sector-start or post-gap ramps.
- At the P/2 alias times (1547.57, 2297.57, 2554.71, 2576.14, 3283.28) the light curve is flat to 0.3% or better, so the period is not P/2.
- The s46 B (2565.42) falls in the orbit gap.
- The s36 A (2294.11) falls in the gap or the flagged ramp after it.

## 3. Ephemeris and the Gaia comparison
Scripts: `ephem.py`, `conjmc.py` (this star's own corr_vec), `physics.py`.
- **B ephemeris:** T0 = 1558.28495 ± 3.9 min, P = 21.428467 ± 0.000048 d over cycles 0, 34 and 80. O−C is +2.6, −0.2 and +0.1 min; χ² 0.08 for 1 degree of freedom.
- **Against Gaia's period** (21.43249 ± 0.00834): −0.48σ.
- **Against Gaia's predicted B conjunctions:** −0.30σ, −0.37σ and −0.41σ.
- **A ephemeris:** P 21.42833 ± 0.00018 d, which agrees with B.
- **Phase separation:** A falls at phase 0.3113 after B, so the B−A separation is 0.6887. Gaia predicts 0.6614 ± 0.0121, a difference of +2.3σ.
- **e cos ω:** at Gaia's e, the observed separation needs ω = 326.0° (Gaia 314.4 ± 4.3°). That gives e cos ω = 0.295 against Gaia's 0.248 ± 0.020, and e sin ω ≈ −0.20.
- **e sin ω from the duration ratio:** not derived from trapezoids, because A is grazing. The limb-darkened two-sphere grid in section 5 handles it instead.
- **Net:** this is mild (about 2.3σ) tension in the phase separation; there is none in the period or the conjunction times.

## 4. Independence tests
- **Second pipelines:**
  - B is seen in TESS-SPOC, TARS and eleanor (s9), TESS-SPOC and TARS (s36), and TESS-SPOC and TARS (s72).
  - A is seen in TESS-SPOC and TARS in all three sectors.
- **Pixel regression** on TESScut 11×11 cutouts with a trapezoid template, run for B in s9, s36 and s72 (`pixreg.py`):

  | Sector | Target pixel depth | Neighbour TIC 49416838 pixel depth | Largest residual outside the 3×3 |
  |---|---|---|---|
  | s9 | 1.22 ± 0.05% | 0.65% | 5.9σ |
  | s36 | 1.27 ± 0.05% | 0.66% | 6.8σ |
  | s72 | 1.16 ± 0.06% | 0.56% | 7.5σ |

  - The deficit centroid is 3.4–4.2″ from the target, and closer to the target than the out-of-eclipse light centroid is.
  - The largest values inside the 3×3 are 19.6–27.4σ, so the outside values are the target's PSF wing.
- **Neighbour-dilution table** (depth the neighbour itself would need to dip):

  | Neighbour | Needed for B | Needed for A | Comment |
  |---|---|---|---|
  | G 13.20 at 28.8″ (TIC 49416838) | 6.1% | 1.6% | Its pixel shows only about half the target's fractional depth, so it is not the source |
  | G 12.98 at 61.8″ | 5.0% | — | Pixel shows 0.1% |
  | G 12.78 at 65.8″ | 4.2% | — | Pixel shows 0.1% |
  | G 15.84 at 68.4″ | 70% | — | Impossible |

  The source is the target.

## 5. Physics
- **Mass and orbit:** mass function f(M) = 0.0673 M☉. For M1 = 1.0–1.2, m2(i = 90°) = 0.54–0.60 M☉ (a K7–M0 dwarf) and a = 37.5–39.5 R☉.
- **Separations:** about 26.6 R☉ at B and 44.8 R☉ at A, so impact parameters at A are 1.68 times those at B.
- **Central durations** (R1 2.01 + R2 0.58): 8.3 h at B and 13.9 h at A. Both observed durations are shorter, as non-central chords should be.
- **Two-sphere grid** (quadratic limb darkening on the primary, uniform companion, ω from the observed separation; `physics.py`):
  - Best fit: i ≈ 87.0°, k ≈ 0.23–0.33, R1 ≈ 1.7–1.9 R☉ (TIC gives 2.01).
  - Impact parameters: b_A ≈ 1.1–1.3, so the A transit of the primary is grazing; b_B ≈ 0.75–0.85, so the B occultation of the companion is near-full.
  - Companion light in the TESS band: 1.3–1.6%. A rough blackbody estimate for a 4000 K, 0.58 R☉ companion next to a 5900 K, 2 R☉ primary gives about 1.9%.
  - The grid reproduces A depth 0.32–0.38%, T14_A 3.6–4.0 h and T14_B 5.7–6.0 h, with χ² below 1 on the three numbers it was fitted to.
- **Which star is in front:** at B the primary passes in front of the companion (deep, flat-ish, at the close conjunction). At A the companion grazes the primary (shallow and V-shaped, at the far conjunction).
- **Consistency:** depths, durations and shapes fit one geometry and fit the light an SB1 companion of the Gaia mass would give.

## 6. Verdict: CONFIRMED
Deciding numbers:
- Three B eclipses in 3 to 5 pipelines, on target at the pixel level, with O−C under 3 min.
- Period within 0.5σ of Gaia, and every B within 0.41σ of Gaia's predicted conjunction (MC with this star's own corr_vec).
- Three independent A eclipses at a constant phase.
- One physical geometry fits both eclipse kinds.

Caveats:
- The B−A separation is 2.3σ from Gaia's e cos ω.
- A3 sits at a gap edge.
- CTOIs are unchecked because ExoFOP was down.

**Next predicted eclipses (BTJD):**

| Cycle | B | A |
|---|---|---|
| E130 | 4343.9856 ± 5.6 min | 4350.656 ± ~8 min |
| E131 | 4365.4141 ± 5.7 min | 4372.085 ± ~8 min |
| E132 | 4386.8425 ± 5.7 min | 4393.513 ± ~8 min |
| E133 | 4408.2710 ± 5.8 min | 4414.942 ± ~8 min |

**What would settle it further:**
- A full A eclipse in a future sector, or a joint limb-darkened fit of A and B with e and ω free, to resolve the 2.3σ phase-separation tension.
- An RV measurement or spectrum to detect the K/M companion.
- A CTOI check once ExoFOP is back.
