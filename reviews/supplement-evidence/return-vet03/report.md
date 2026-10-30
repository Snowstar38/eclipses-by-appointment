# vet03: adversarial check of TIC 70665829 (UCAC4 537-050325) and TIC 331293467 (UCAC4 150-142995)

Opus 5.5 subagent, 2026-10-30, for Fable 5.1. This run resumed from a predecessor that was killed by a container restart. The predecessor wrote `s1`–`s7` and their outputs. Its pixel run for 331293467 stopped part-way through s100 (`s7_pixels_331293467.out`). I checked those outputs, re-ran the pixel analysis for 331293467 in all four sectors (`s7b`), and wrote `s9`–`s14` plus `s2c`, `s10a`, `s12b`. All scripts, `.out`/`.json` outputs and the `pix_*.png` plots are in this folder. Downloads are under `/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet03/<tic>/`; the TESScut cubes have been deleted. Notation: **A** = the companion passes in front of Gaia's RV star (true anomaly ν = 90° − ω). **B** = the RV star passes in front of the companion. Depths are in ppt of the raw (undetrended) flux unless marked "undiluted".

**TIC 70665829: CONFIRMED.** A K dwarf with an early-M companion, P = 3.4657654 d.
- **(1) Events, pass:** 24 primaries and 28 secondaries (SPOC), and 22 and 28 (QLP), measured one by one from SAP QUALITY==0 flux.
- **(2) Period, pass:** the eclipse period matches Gaia's at −0.43σ.
- **(3) Pixels, pass:** the difference images in s46, s48 and s72 (three cameras) sit 0.5–1.2″ from the target. The only neighbour (G 14.44 at 64″) would need an intrinsic depth above 1500%.
- **(4) Independence, pass:** QLP, TESS-SPOC, my TESScut aperture photometry and ZTF g/r all see both eclipses. Absolute depths differ by up to ~10% between apertures. The secondary/primary depth ratio is 0.216–0.233 in every pipeline, so the differences are dilution or background, not the signal.
- **(5) Geometry, pass:** the secondary falls at phase 0.46048, which is e cos ω = −0.0621. Gaia predicts 0.4547 +0.024/−0.024 if the deep eclipse is A (+0.24σ), and needs 3.6–5.6σ if it is B. The deep eclipse coincides with conjunction A (+0.4 ± 0.5 h when Gaia's orbit is conditioned on the TESS period). So the deep event is Gaia's RV star (the K dwarf) being eclipsed. ZTF colours agree: the deep eclipse is deeper in g, the shallow one deeper in r.
- **Screen:** correct on all points (deep ~300–330 ppt at phase 0, ~65–72 ppt secondary at 0.4605, flat baseline, P 3.4658 d).

**TIC 331293467: CONFIRMED.** An A/F star with a K-dwarf companion, P = 5.2568199 d. The light is heavily blended, so the undiluted depths are uncertain.
- **(1) Events, pass:** 21 primaries and 24 secondaries measured individually from QLP SAP QUALITY==0. Every secondary is above 3σ, and null phases 0.25/0.75 give −0.11 ± 0.16 and −0.09 ± 0.15 ppt.
- **(2) Period, pass:** +0.51σ from Gaia.
- **(3) Pixels and dilution, pass:** the diff-image source sits 0.3–3.6″ from the target in s38, s99, s100 and s101 (cameras 2, 4, 3, 2).
  - The G 17.07 star at 8″ needs 305–458%, the G 16.07 at 24″ needs 143–287%, and the G 16.14 at 14″ needs 91–115% (over 100% in s99). All are arithmetically excluded or effectively so.
  - The only neighbour that passes the arithmetic, G 13.78 at 30.5″ (needs 25–84%), is excluded by position. The fit is 10–19× worse at its position, and the measured offset points 0.00–0.11 of the way toward it.
  - ZTF has no data at Dec −60. No higher-resolution light curve was available.
- **(4) Independence, pass in dilution-free form:** no TESS-SPOC or SPOC light curve exists. My TESScut 3×3 photometry sees every eclipse with the same T14 (4.05–4.08 h against QLP 4.07 h) and a secondary/primary ratio of 0.168–0.202 against QLP 0.160–0.176. Raw depths differ by aperture (QLP 61–73, TESScut 47–56 ppt). The undiluted primary depth is model-dependent: 80–89 ppt from PSF amplitudes, 80–116 ppt from aperture shares.
- **(5) Geometry, pass:** the secondary is at phase 0.50013 ± 0.00023 (Gaia predicts 0.5015, so this cannot tell A from B). The deep eclipse sits on Gaia's conjunction A: +0.1 ± 1.0 h when conditioned on the TESS period, and +0.49σ on Gaia alone with correlations. B is excluded at 6.7σ (Gaia alone) or ≫10σ (conditioned). This test needs Gaia's ω–T_p correlation (0.9997); with independent errors it does not decide. Landing on the target's own spectroscopic conjunction is further evidence that the signal is on the target.
- **Screen:** the ~66 ppt and ~11 ppt figures are right for QLP SAP. The undiluted target depths are about 8–11% and 1.3–2%.

## 1. Archives and web
- **Catalogue cones (`s2_archives.py`, 60″, VizieR mirror):**
  - 70665829: nothing in VSX, Prsa+2022, IJspeert+2021, Gaia DR3 VEB, Gaia varisum or SB9.
  - 331293467: the same, except one VSX entry at 33.7″: Gaia DR3 5866907631080924672, type L, G 18.4–18.63. It is not our star and is fainter than the 90″ neighbour list (G < 18).
  - Neither star is a catalogued eclipsing binary within 60″ in these catalogues.
- **Sanity checks:** the VSX cone was checked on Algol (1 row at 0.11″, `s2_archives.out`). `s2c` showed the mirror serves Prsa (nearest EB 1621″ from 331293467) and IJspeert (nearest 2860″ from 70665829). The mirror then began timing out, so Gaia-VEB, varisum and SB9 were not sanity-checked (`s2c_catalogue_sanity.out`). The all-catalogue 5″ query (`s2b`) returned only I/ catalogues, even for Algol, so it is truncated and was not relied on.
- **SIMBAD (10″):**
  - 70665829 = UCAC4 537-050325, type SB*, 3 bibcodes (2023A&A...674A..34G, 2022AJ....163..152S, 2022ApJS..259...35A).
  - 331293467 = UCAC4 150-142995, type SB*, 1 bibcode (2023A&A...674A..34G).
- **ExoFOP:** no TOIs or CTOIs for either star (`s2b_allcat.out`).
- **Gaia NSS rows (`s10a_gaia_nss.csv`):** both are SB1 with flags 0. corr(ω, T_p) is 0.9984 for 70665829 and 0.9997 for 331293467.

## 2. Independence, systematics, pixels
- **Pipelines (`s1_download_lc.out`):**
  - 70665829: QLP s45, s46, s48, s72; TESS-SPOC s45, s46, s48, s72 and "s1751". MAST labels that last product sector 1751 (camera 1, BTJD 4055.76–4063.00, 1480/3131 good cadences); it is used as given. No 2-min SPOC.
  - 331293467: QLP only (s11, s38, s99–s102). No TESS-SPOC and no 2-min data.
- **Per-sector depths, primary / secondary in ppt (`s9_indep.out`):**

| TIC / sector | QLP SAP | TESS-SPOC SAP | TESScut 3×3 raw | TESScut / target share | PSF amp / target flux | d2/d1 (QLP, SPOC, TESScut) |
|---|---|---|---|---|---|---|
| 70665829 s45 | 325.3 / 72.3 | 300.3 / 67.3 | — | — | — | 0.222, 0.224, — |
| 70665829 s46 | 306.6 / 66.1 | 296.2 / 66.6 | 297.6 / 67.2 | 325.3 / 73.4 (0.915) | 287.5 / 65.8 | 0.216, 0.225, 0.226 |
| 70665829 s48 | 312.2 / 70.6 | 282.7 / 64.1 | 288.1 / 67.1 | 285.2 / 66.4 (1.010) | 264.6 / 60.4 | 0.226, 0.227, 0.233 |
| 70665829 s72 | 329.8 / 72.2 | 299.0 / 67.9 | 300.6 / 66.2 | 340.8 / 75.0 (0.882) | 290.9 / 64.1 | 0.219, 0.227, 0.220 |
| 331293467 s11 | 61.4 / 9.8 | — | — | — | — | 0.160 |
| 331293467 s38 | 64.7 / 10.6 | — | 46.7 / 9.4 | 80.5 / 16.3 (0.580) | 79.6 / 14.2 | 0.163, —, 0.202 |
| 331293467 s99 | 72.6 / 12.0 | — | 50.4 / 9.2 | 115.8 / 21.1 (0.435) | 89.3 / 14.6 | 0.165, —, 0.182 |
| 331293467 s100 | 70.1 / 11.7 | — | 51.3 / 8.6 | 99.2 / 16.6 (0.517) | 87.5 / 12.7 | 0.166, —, 0.168 |
| 331293467 s101 | 61.4 / 10.7 | — | 55.5 / 9.6 | 106.7 / 18.5 (0.520) | 81.5 / 12.1 | 0.174, —, 0.173 |
| 331293467 s102 | 70.5 / 12.4 | — | — | — | — | 0.176 |

  - For 70665829, QLP SAP is 4–10% deeper than TESS-SPOC SAP in every sector, but the d2/d1 ratios match. This is a multiplicative aperture or background-scale difference, not a different signal. TESS-SPOC CROWDSAP is 0.966 (s46) and 0.969 (s1751).
  - For 331293467, raw depths depend on the aperture (TIC contamination ratio 0.70), while d2/d1 and T14 agree.
- **ZTF (`s13_ztf.out`, 2″ cone):**
  - 70665829: 1789 rows from 2018 to 2025 (HJD−2457000 1202.8–3969.0), folded on the TESS ephemeris.
    - Primary core: zg 361 and 316 ppt, zr 325 and 315 ppt (4–8 points per field).
    - Secondary core: zg 26 and −9 ppt, zr 60 and 33 ppt.
    - So the eclipses are seen by an independent instrument, the ephemeris holds back to 2018, and the secondary is redder.
  - 331293467: 0 rows (Dec −60, outside ZTF).
- **Common mode:** I did not fetch other QLP stars. Both signals repeat at a fixed period across 3 cameras (70665829) and 3 cameras over 7 years (331293467), with secondaries at fixed phase, and the difference images show no off-target deficit. A sector-wide systematic cannot do that.
- **Blind dip census (`s3_events_*.out`, 5×MAD below a running median; `s11_census.out`):** every dip is a primary or secondary except:
  - TESS-SPOC s1751 at 4059.25–4059.7: a ramp from 0.935 to 0.98 right after a data gap (phase 0.77–0.90), background flat.
  - QLP s48 at 2621.1–2621.5: QLP background −110 to −210, many cadences flagged 2048/4096.
  - Both are systematics.
- **Pixels (`s7_pixels_70665829.out`, `s7b_pixels_331293467.out`):** median in-eclipse minus out-of-eclipse images from the TESScut 11×11 cubes, a PSF-fitted source position, and the dilution needed for every Gaia neighbour within 90″ with G < 18, in a 3×3 aperture (scene model with Gaussian PSF and TIC-style T from G and BP−RP).
  - **70665829, primary:** offset 1.0 ± 0.2″ (s46), 1.2 ± 0.6″ (s48), 0.5 ± 0.1″ (s72).
  - **70665829, secondary:** 2.3 ± 0.3″, 1.1 ± 0.8″, 1.8 ± 0.1″.
  - **70665829, neighbour:** the only one, G 14.44 at 64.3″, needs 7253–47260% (primary) and 1573–10587% (secondary), with a χ² ratio of 41–78. Excluded.
  - **331293467, primary offsets:** 0.3 ± 0.2″ (s38), 2.0 ± 0.2″ (s99), 1.2 ± 0.3″ (s100), 3.6 ± 0.5″ (s101). Bootstrap errors are surely underestimates of the systematics, but every offset is far smaller than any separation that matters.
  - **331293467, neighbour by neighbour:**
    - G 17.07 at 8.0″: needs 377/458/334/305%. χ² ratio 3.6–4.6. Offset projection onto it is 0.03/0.23/0.00/−0.18 of the way.
    - G 16.14 at 14.0″: needs 91/115/99/97%. χ² ratio 3.8–10.5. Projection −0.01/0.01/−0.08/0.24.
    - G 16.07 at 24.4″: needs 143–287%.
    - G 13.78 at 30.5″: needs 84/45/28/25%, so not excluded by arithmetic. χ² ratio 19.1/10.1/19.1/16.0 and projection 0.00/−0.00/0.04/−0.11, so excluded by position.
    - G 14.73 at 47.3″: needs 96–5754%, χ² ratio 10–20.
    - All other neighbours need more than 150%.
  - **331293467, secondary:** the fit gives 0.2 ± 0.7″, 1.9 ± 1.0″, 3.2 ± 0.6″, 3.2 ± 1.3″. The χ² cannot separate the target from the 8″ and 14″ stars here (ratio ~1.0–1.1), and a G 12.85 VARIABLE star at 89.4″ on the cutout edge fits the secondary diff image better (ratio 0.14–0.36). That star contributes 0.0000 of the aperture flux, so it is noise in a 4–5 event average, not a source. The secondary is tied to the target because it keeps a fixed phase (0.5002) and a fixed d2/d1 with the on-target primary.

## 3. TIC 70665829
**Measurements** (raw SAP QUALITY==0; trapezoid with quadratic baseline; `s3_events_70665829.out` lists every event). Sector summaries:

| Event | Mid BTJD (first … last) | Depth (SPOC / QLP / TESScut) | T14 / T23 | pipelines |
|---|---|---|---|---|
| Primary s45 ×6 | 2528.21356 … 2549.00771 | 300.3 / 325.3 / — | 2.83 / 0.53 h (all SPOC primaries; range 2.80–2.90) | SPOC, QLP |
| Primary s46 ×6 | 2555.93930 … 2576.73431 | 296.2 / 306.6 / 297.6 | " | SPOC, QLP, TESScut |
| Primary s48 ×6 | 2611.39079 … 2635.65071 (2614.85610 SPOC only) | 282.7 / 312.2 / 288.1 | " | SPOC, QLP, TESScut |
| Primary s72 ×5 | 3262.95482 … 3283.74972 | 299.0 / 329.8 / 300.6 | " | SPOC, QLP, TESScut |
| Primary s1751 ×1 | 4060.08215 ± 0.00010 | 299.86 | 2.84 / 0.53 h | SPOC |
| Secondary s45 ×7 | 2526.34374 … 2547.13826 | 67.3 / 72.3 / — | 2.77 / 0.54 h (all SPOC secondaries; range 2.57–2.88) | SPOC, QLP |
| Secondary s46 ×8 | 2554.07007 … 2578.32973 | 66.6 / 66.1 / 67.2 | " | SPOC, QLP, TESScut |
| Secondary s48 ×6 | 2612.98690 … 2633.78190 | 64.1 / 70.6 / 67.1 | " | SPOC, QLP, TESScut |
| Secondary s72 ×6 | 3264.54980 … 3285.34512 | 67.9 / 72.2 / 66.2 | " | SPOC, QLP, TESScut |
| Secondary s1751 ×1 | 4061.67233 (partial, egress lost) | 54.78 | — | SPOC |

- **Lost events:** in TESS-SPOC, s45/46/48/72 lose 1/2/5/4 events to gaps (`s11_census.out`). QLP flags more of s48: it has 1 full and 11 partial events there.
- **Period (`s12_ephem.out`, full-coverage events, joint fit):**
  - SPOC: T0 = 2791.61111 ± 0.00009 BTJD, P = 3.4657654 ± 0.0000007 d. QLP: 3.4657623 ± 0.0000006 d.
  - The 3σ difference comes from the single s1751 primary. Without it, SPOC primaries give 3.4657637 ± 0.0000012, and the s1751 eclipse arrives +2.30 min late (`s12b_no1751.out`).
  - Primary O−C has χ²_r of 24–30 against the formal errors: sector means range from −1.9 to +1.3 min (s48 is early in both pipelines while its secondaries are not). This was not pursued, but the realistic timing error is about ±2 min.
  - Gaia P = 3.4658878 ± 0.0002846, so (P − P_Gaia)/σ = −0.43 for both pipelines.
- **Odd/even (`s4_period_70665829.out`):** primary +0.62 ± 0.82 ppt (SPOC), −0.87 ± 1.24 (QLP). Secondary +0.17 ± 0.54, −1.06 ± 0.74. No difference.
- **Which eclipse is primary:** the primary (300 ppt) and secondary (67 ppt) differ by a factor of 4.5 and sit at an off-centre phase. So P is neither half nor double the true period, and the deeper event is unambiguous.

## 4. TIC 331293467
**Measurements** (QLP SAP QUALITY==0. Primaries have a free trapezoid fit (`s3_events_331293467.out`). Secondaries use the primary's shape with free t0 and depth (`s5_secondary_331293467.out`)):

| Event | Mid BTJD (first … last) | Depth QLP (TESScut raw) | T14 / T23 | pipelines |
|---|---|---|---|---|
| Primary s11 ×4 | 1601.23407 … 1622.26045 | 61.4 | 4.07 / 0.83 h (all primaries; range 3.93–4.23) | QLP |
| Primary s38 ×5 | 2337.18980 … 2358.21445 | 64.7 (46.7) | " | QLP, TESScut |
| Primary s99 ×2 | 4050.91270, 4066.68276 | 72.6 (50.4) | " | QLP, TESScut |
| Primary s100 ×3 | 4077.19684 … 4098.22307 | 70.1 (51.3) | " | QLP, TESScut |
| Primary s101 ×4 | 4103.47964 … 4124.50456 | 61.4 (55.5) | " | QLP, TESScut |
| Primary s102 ×3 | 4129.76349 … 4150.78766 (last one partial) | 70.5 | " | QLP |
| Secondary ×24 (3/4/4/5/4/4 per sector) | 1603.8613 … 4148.1608 | 11.42 ± 0.15 weighted mean (8.6–13.4 each) | primary shape (TESScut free fit 3.5–4.2 h) | QLP, TESScut |

- **Lost events:** 14 events fall in gaps across the six sectors (`s11_census.out`).
- **Period (`s12_ephem.out`, full-coverage, joint):** T0 = 3467.40446 ± 0.00029 BTJD, P = 5.2568199 ± 0.0000020 d.
  - All primaries: 5.2568187 ± 0.0000017. Secondaries only: 5.2568291 ± 0.0000074 (1.4σ).
  - Gaia P = 5.2565467 ± 0.0005365, so +0.51σ.
- **Odd/even, primary:** −1.19 ± 0.49 ppt (formal 2.4σ, 1.8% of the depth). It is driven by sectors with 1–2 events and a partial s102 event, and the sector-to-sector depth scatter (61–73 ppt) is much larger. At 2P both halves are the same eclipse type, and the 11 ppt secondary at phase 0.5002 rules out P/2. Not a sign of a wrong period.

## Geometry vs Gaia
All from `s10_geometry.out`: 20000 draws each with independent errors, with Gaia's correlation matrix, and with that matrix conditioned on the TESS period.

**70665829.** Gaia: e = 0.0769 ± 0.0397, ω = 175.4 ± 22.2°, T_p = 390.5724 ± 0.2071 BTJD.
- **Secondary phase:** measured shallow-after-deep phase is 0.46048 ± 0.00008. The implied e cos ω = −0.0621, the same exact or to first order.
- **Gaia prediction:** (t_B − t_A)/P = 0.4547 (+0.0239/−0.0238). That is below 0.5 in 100% of draws, with e cos ω = −0.0711 ± 0.0362.
  - Deep = A matches at +0.24σ. Deep = B would need 0.5395, at +3.55σ.
  - Conditioned on the TESS period: 0.4630 ± 0.0136, giving A −0.19σ and B +5.64σ.
- **Absolute timing (630 cycles from T_p):**
  - Independent errors: deep minus A = −0.0215 ± 0.0999 P (−0.22σ); minus B = −4.71σ.
  - Gaia correlated: deep minus A = −0.0204 ± 0.0585 P (−1.7 h, −0.35σ); minus B = −11.7σ.
  - Conditioned on the TESS period: deep minus A = +0.0051 ± 0.0064 P (+0.4 h, +0.80σ); minus B = −56σ.
- **Conclusion: deep eclipse = conjunction A.** Gaia's ω decides this through two independent routes (secondary phase and absolute timing).
- **Durations:** T14 is 2.77 h for the secondary and 2.83 h for the primary (SPOC). This is consistent with Gaia's small e sin ω = +0.0032 ± 0.0310.
- **Physics (`s14_physics.out`, M1 = 0.85 M☉):** f(m) = 0.0807 M☉, giving m2 ≈ 0.54 M☉ (≈3760 K, ≈0.52 R☉). a = 10.75 R☉ (a/R1 = 14.2). A central eclipse would last 3.15 h against 2.83 h observed, so b > 0. The expected d2/d1 ≈ J(800 nm) ≈ 0.28 against 0.22 observed.
- A cooler M-dwarf companion makes the K dwarf's eclipse the deep one, as the timing says. ZTF agrees: the deep eclipse is deepest in g, the shallow one deeper in r.

**331293467.** Gaia: e = 0.0215 ± 0.0250, ω = 287.0 ± 69.8°, T_p = 389.8053 ± 1.0004 BTJD.
- **Secondary phase:** 0.50013 ± 0.00023 (joint fit) and 0.5002 ± 0.0001 (`s5`). That gives e cos ω = +0.0003 to +0.0004 ± 0.0002, against Gaia's +0.0024 ± 0.0227. Consistent, but it cannot separate A from B.
- **Absolute timing (699 cycles from T_p):**
  - Independent errors: deep minus A = +0.14σ, minus B = −1.90σ. Not decisive.
  - Gaia correlated: deep minus A = +0.0321 ± 0.0649 P (+4.1 h, +0.49σ); minus B = −6.66σ.
  - Conditioned on the TESS period: deep minus A = +0.0009 ± 0.0077 P (+0.1 h, +0.12σ); minus B = +81σ. Conditioning shifts T_p by +0.29 d and ω by +20.7°, because corr(P, T_p) = 0.57.
- **Conclusion: deep eclipse = conjunction A,** the K dwarf in front of the A/F star. This rests on Gaia's corr(ω, T_p) = 0.9997, which is physically expected at e ≈ 0.
- **Physics (M1 = 1.69 M☉):** f(m) = 0.0630 M☉, giving m2 ≈ 0.71 M☉ (≈4580 K, ≈0.70 R☉, k ≈ 0.41). a = 17.04 R☉. A central eclipse would last 5.76 h against 4.07 h observed (b > 0). The expected d2/d1 ≈ 0.21 against 0.16 observed. The undiluted primary depth of 8–11% is below k² ≈ 0.17, as a partial or high-b transit should be.

## Ephemerides and next eclipses
From `s12_ephem.out`. Times are BJD_TDB / BTJD, converted to UTC calendar dates without the barycentric-to-Earth light-time correction (up to ±8.3 min).
- **TIC 70665829:** T0 = 2791.61111 ± 0.00009 BTJD (BJD_TDB 2459791.61111), P = 3.4657654 ± 0.0000007 d (SPOC). The secondary follows at +1.59591 ± 0.00029 d (phase 0.46048). Realistic timing error is ±2 min (see §3).
  - Next primaries: 4344.2740 (2026-10-30 18:33 UTC), 4347.7398 (2026-11-03 05:44), 4351.2055 (2026-11-06 16:54). The QLP ephemeris is 1–2 min earlier.
  - Next secondaries: 4345.8699 (2026-11-01 08:51), 4349.3357 (2026-11-04 20:02), 4352.8014 (2026-11-08 07:12).
- **TIC 331293467:** T0 = 3467.40446 ± 0.00029 BTJD (BJD_TDB 2460467.40446), P = 5.2568199 ± 0.0000020 d. The secondary follows at +2.62912 ± 0.00123 d (phase 0.50013).
  - Next primaries: 4345.2934 ± 0.0004 (2026-10-31 19:01 UTC), 4350.5502 (2026-11-06 01:11), 4355.8070 (2026-11-11 07:20).
  - Next secondaries: 4347.9225 (2026-11-03 10:07), 4353.1793 (2026-11-08 16:17), 4358.4361 (2026-11-13 22:26).

## Caveats
- **331293467 has a single pipeline (QLP) plus my own TESScut photometry.** Its undiluted depths rest on a Gaussian-PSF scene model: primary 80–116 ppt (79.6–89.3 ppt from PSF amplitude), secondary ~13–21 ppt. Only the fact that the signal is on the target, the timing and the ratios are robust.
- **Attribution for 331293467 is pixel-level, not resolved.** ZTF has no data at Dec −60. The G 13.78 star at 30.5″ is excluded only by position (and by the timing match to Gaia's conjunction), not by arithmetic. Bootstrap centroid errors (0.2–0.5″) understate the systematics, but the closest call is still 0.24 of the way toward any neighbour.
- **Gaia geometry for 331293467 is decisive only with the corr_vec decoding** (order P, Vcm, K, e, ω, T_p, column-major upper triangle; the 0.9997 ω–T_p term confirms it).
- **70665829 timing:** the O−C scatter between sectors (±1–2 min) and the late s1751 primary (+2.3 min) are unexplained. Candidates are timestamps in the unusual "sector 1751" product, or real timing variations. This does not affect the classification.
- **Archives:** the cones for Gaia-VEB, varisum and SB9 were not checked on a known object, because the mirror failed during `s2c`. Their empty results stand from `s2` only.
- **Common mode:** not done with other stars (see §2).

## Files
- **Light curves:** `lcio.py`, `s1_download_lc.py` / `.out`.
- **Archives:** `s2_archives.py` / `.out`, `s2b_allcat.py` / `.out`, `s2c_catalogue_sanity.py` / `.out`.
- **Events:** `s3_events.py`, `s3_events_70665829.out` / `.json`, `s3_events_331293467.out` / `.json`.
- **Periods:** `s4_period.py`, `s4_period_*.out`, `s4_ephem_*.json`; `s5_secondary_331.py`, `s5_secondary_331293467.out` / `.json`.
- **Pixels:** `s6_tesscut.py` / `.out`; `s7_pixels.py`, `s7_pixels_70665829.out`, `s7_pixels_331293467.out` (interrupted; superseded by s7b); `s7b_pixels.py`, `s7b_pixels_331293467.out`; `pix_70665829_s46/s48/s72.png`, `pix_331293467_s38/s99/s100/s101.png`; `tesscut_ap3x3_*.txt` (own photometry).
- **Independence:** `s9_indep.py` / `.out` / `.json`.
- **Geometry:** `s10a_gaia_query.py` / `.out`, `s10a_gaia_nss.csv`, `s10_geometry.py` / `.out` / `.json`.
- **Census:** `s11_census.py` / `.out`.
- **Ephemerides:** `s12_ephem.py` / `.out` / `.json`, `s12b_no1751.py` / `.out`.
- **ZTF:** `s13_ztf.py` / `.out` (raw CSVs in the scratchpad `ztf/` folder).
- **Physics:** `s14_physics.py` / `.out`.

TIC 70665829: CONFIRMED; P_ecl=3.4657654±0.0000007 d; depth1=283–330 ppt (pipeline-dependent; SPOC ~300); depth2=64–72 ppt at phase 0.46048; pixel: on target; pipelines: 4 (QLP, TESS-SPOC, TESScut, ZTF); Gaia geometry: pass (deep = conjunction A, Gaia RV star eclipsed)
TIC 331293467: CONFIRMED; P_ecl=5.2568199±0.0000020 d; depth1=61–73 ppt QLP raw (≈80–116 ppt undiluted); depth2=11.4 ppt QLP (≈13–21 ppt undiluted) at phase 0.50013; pixel: on target (30.5″ G13.78 excluded by position only); pipelines: 2 (QLP, TESScut); Gaia geometry: pass (deep = conjunction A; needs Gaia ω–T_p correlation)
