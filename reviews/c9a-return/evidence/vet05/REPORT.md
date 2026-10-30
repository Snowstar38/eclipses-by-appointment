# vet05: adversarial check of TIC 15855794 (UCAC4 564-009141) and TIC 92881948 (WISE J053256.98-225927.8)

Opus 5.5 subagent, 2026-10-30, for Fable 5.1. This run resumed from a predecessor that was killed by a container restart; that run had finished s1–s9 and part of s10. This run added s10b/c/d (archives), s11 (own TESScut photometry, difference images, dilution), s12 (master event table, ephemerides), s13 (Gaia geometry MC) and s14 (physics). The coordinator cut the budget, so the report is short. Scripts and outputs are in this folder. Downloads are in the scratchpad `data/vet05/<tic>/`; all TESScut cubes have been deleted. Depths are in ppt, times in BTJD = BJD_TDB − 2457000. "C" = own TESScut photometry with a 3×3 aperture, "Q" = QLP SAP, "S" = TESS-SPOC SAP (QUALITY==0 throughout).

**TIC 15855794: CONFIRMED.** (1) Repeating events: I measured 12 primaries and 11 secondaries one by one from raw flux. (2) Period: the eclipse period is 5.8911458 ± 0.0000038 d, +0.54σ from Gaia. (3) Pixels: in s44, s70 and s71 the difference-image deficit lies 0.4–0.9″ from the target, and every neighbour is excluded. (4) Pipelines: Q, S and C agree on depth to within 4%. (5) Geometry: the primary falls at Gaia conjunction A (+0.03 ± 0.08 d at the Gaia epoch; conjunction B is excluded at ~40σ), and the secondary phase of 0.50182 matches Gaia's prediction of 0.502 ± 0.021. Corrections to the screen: the primary is 35.3 ppt after dilution correction, not "probably larger", and it lasts 3.25 h. The secondary is 5.0–5.4 ppt.

**TIC 92881948: CONFIRMED.** (1) Repeating events: 24 primaries and 22 secondaries measured one by one. (2) Period: 8.8049754 ± 0.0000013 d, +0.43σ from Gaia. (3) Pixels: in all 7 sectors the deficit lies 0.3–1.6″ from the target, and the depth scales with the target's flux fraction in the aperture. (4) Pipelines: Q, S and C agree once dilution is accounted for. (5) Geometry: the primary falls at conjunction A (+0.06 ± 0.09 d; B is excluded at ~44σ). The secondary phase is 0.48334 ± 0.00008, so e cos ω = −0.026, which is 1.0σ from Gaia's prediction of 0.502 ± 0.018. Corrections to the screen: the primary depth is 16.4 ppt (Q) / 18.3 ppt (C) / 19.0 ppt dilution-corrected, not ~11 ppt. It lasts 1.69 h, not the 1.2 h that BLS gave. The secondary is 5.0–5.3 ppt at phase 0.4833.

Not tested for either star: the common-mode test (brief item 8, outside the five protocol checks) and next-eclipse UTC predictions (budget).

## 1. Archives and web (s10, s10b, s10c, s10d)
- **15855794:** no rows within 60″ in VSX, Prsa+2022 (J/ApJS/258/16), IJspeert+2021, Gaia DR3 vari_eclipsing_binary / I/358/veb, or SB9. It is not in Gaia vari_summary. SIMBAD: SB*, 1 bibcode (2023A&A...674A..34G). ExoFOP: TOIs 0, CTOIs 0.
- **92881948:** VSX has one entry at 1.35″: "Gaia DR3 2964506347485091072", type **ROT**, G 12.76–12.80. Nothing in Prsa, IJspeert, Gaia-EB or SB9. Gaia vari_summary: in_vari_eclipsing_binary = 0; the classifier's best class is SOLAR_LIKE (0.63). SIMBAD: SB*, 1 bibcode. ExoFOP: TOIs 0, CTOIs 0.
- **Neither star is a catalogued eclipsing binary.**
- **Positive controls:** each catalogue cone found a known row (Prsa, I/358/veb, IJspeert and SB9 via control rows; VSX via the 92881948 row itself).
- **Brief error:** the brief lists "I/357/varisum", but Gaia DR3 variability is I/358 (I/357 is the NSS part), so Gaia variability was queried through TAP.

## 2. Independence, systematics, pixels (s11_*.out, s12_compile.out, s14_physics.out)
- **Depths, 15855794 (all events):**
  - Primary: Q 35.84 ± 0.27 (n=11), S 34.56 ± 0.32 (n=4), C 34.90 ± 0.23 (n=12), C dilution-corrected 35.34 ± 0.23.
  - Secondary: Q 5.00 ± 0.30, S 4.91 ± 0.43, C 5.36 ± 0.24.
  - The C primary χ² of 34/11 comes from E124 (27.6 ppt, at the end of the s70 orbit, a cadence QLP flags).
- **Depths, 92881948:**
  - Primary: Q 16.43 ± 0.24, S 18.20 ± 0.24, C 18.33 ± 0.18, C r2.5 15.90 ± 0.23. Divided by the modelled target fraction, 3×3 gives 18.99 ± 0.19 and r2.5 gives 19.17 ± 0.28: they agree.
  - QLP is shallower because its larger aperture takes in a G 13.67 star (60″) and a G 14.56 star (53″). TESS-SPOC CROWDSAP is 0.90–0.94.
  - Secondary: Q 5.02 ± 0.21, S 5.33 ± 0.24, C 5.08 ± 0.18.
- **Difference images** (median of the eclipse core minus median of the flanks, per sector; pixel-integrated Gaussian fit; errors from 200 fake-event stacks):
  - 15855794, primary: offsets from the target 0.4″ (s44, 1.1σ), 0.5″ (s70 without E124, 0.8σ; the run including E124 is distorted by that event) and 0.9″ (s71, 2.1σ). Every neighbour is >45″ from the centroid at >100σ. Secondary: 1.2–3.5″, ≤1.0σ.
  - 92881948, primary: offsets 1.3″ (s5), 1.6″ (s6), 1.4″ (s32), 0.9″ (s98), 0.3″ (s107), 1.5″ (s108), 0.9″ (s109), all ≤2.8σ, with errors of 0.02–0.06 px. The nearest neighbour is at 29″. In every sector the pixel with the deepest fractional dip is the target pixel or one next to it.
- **Dilution arithmetic** (Gaussian PSF, and a PSF 1.5× broader):
  - 15855794: in the 3×3 aperture the brightest neighbour (G 16.03, 45″) contributes ≤1.9% of the flux. It would need an intrinsic depth of ≥180% to make the primary: excluded. All other neighbours contribute ≤0.6%: excluded.
  - 92881948: in 3×3, G 13.67 (60″) contributes 0.11–1.44% and would need ≥127%: excluded. G 14.56 contributes ≤3.95% and would need ≥46%; it is not excluded by arithmetic alone, but it is excluded by the centroid (53″ away) and because the depth grows in the smaller aperture. G 16.46 (29″) contributes ≤2.4% and would need ≥75%; it is excluded by the centroid.

## 3. TIC 15855794 (joint shape fit, s6: P 35.25 ± 0.31 ppt, T14 3.255 ± 0.025 h, T23 0.70 ± 0.03 h; S 4.89 ± 0.38 ppt, T14 3.14 ± 0.19 h)

There is no 2-min SPOC data. The s43 TESScut cut-out is empty (RAW_CNTS = −1, s11_15855794_s43_check.out).

| Event | Mid BTJD | Depth ppt (S / Q / C) | pipelines |
|---|---|---|---|
| S E−1 | 2500.18 | lost (gap/flags) | – |
| P E0 | 2503.12275 ± 0.00077 | 34.25 / 34.40 / 34.20 | S Q C |
| S E0 | 2506.0791 ± 0.0049 | 5.10 / 4.79 / 4.99 | S Q C |
| P E1 | 2509.01328 ± 0.00066 | 34.46 / 35.24 / 36.59 | S Q C |
| S E1 | 2511.97 | lost (gap) | – |
| P E2 | 2514.90506 ± 0.00059 | 34.45 / 36.19 / 34.79 | S Q C |
| S E2 | 2517.8619 ± 0.0062 | 4.54 / 5.00 / 4.47 | S Q C |
| P E3 | 2520.79709 ± 0.00074 | 35.07 / 36.27 / 35.79 | S Q C |
| S E3 | 2523.7436 ± 0.0048 | 4.99 / 5.99 / 5.26 | S Q C |
| P E120 | 3210.06068 ± 0.00106 | – / 37.03 / 35.22 | Q C |
| S E120 | 3213.0275 ± 0.0078 | – / 4.10 / 5.43 | Q C |
| P E121 | 3215.95111 ± 0.00085 | – / 36.48 / 35.55 | Q C |
| S E121 | 3218.9089 ± 0.0063 | – / 4.91 / 5.50 | Q C |
| P E122 | 3221.84 | lost (flags, all pipelines) | – |
| S E122 | 3224.8002 ± 0.0061 | – / 5.38 / 5.60 | Q C |
| P E123 | 3227.73365 ± 0.00081 | – / 37.28 / 34.94 | Q C |
| S E123 | 3230.6864 ± 0.0057 | – / 5.35 / 5.74 | Q C |
| P E124 | 3233.6255 ± 0.0019 | – / flagged / 27.64 (end of orbit, suspect) | C |
| S E124 | 3236.5893 ± 0.0065 | – / 4.79 / 5.79 | Q C |
| P E125 | 3239.51638 ± 0.00085 | – / 36.17 / 35.01 | Q C |
| S E125 | 3242.4652 ± 0.0066 | – / 4.37 / 5.01 | Q C |
| P E126 | 3245.40761 ± 0.00090 | – / 35.35 / 34.55 | Q C |
| S E126 | 3248.36 | lost (flags) | – |
| P E127 | 3251.29757 ± 0.00090 | – / 34.85 / 33.77 | Q C |
| S E127 | 3254.2567 ± 0.0054 | – / 5.55 / 5.62 | Q C |
| P E128 | 3257.18858 ± 0.00085 | – / 35.70 / 35.34 | Q C |
| P E264 | 4058.39 | lost (gap; segment "s1751") | – |
| S E264 | 4061.3461 ± 0.0060 | – / – / 4.92 | C |

- **Period** (s12): primaries only, P = 5.8911449 ± 0.0000038 (χ² 4.8/10). Secondaries only, P = 5.8911779 ± 0.0000229. TESScut alone, P = 5.8911437 ± 0.0000042. All are +0.53 to +0.56σ from Gaia's 5.890538 ± 0.001133.
- **Odd/even primaries:** Δ = +0.6σ (S), +0.7σ (Q), +1.8σ (C). There is no hint of 2P.
- **Primary O−C** scatter is ≤1.2 min.

## 4. TIC 92881948 (s6: P 16.63 ± 0.45 ppt [Q/S fast cadence], T14 1.692 ± 0.030 h, T23 0.20 ± 0.05 h (V-shaped); S 5.00 ± 0.35 ppt, T14 1.76 ± 0.12 h)

| Event | Mid BTJD | Depth ppt (S / Q / C) | pipelines |
|---|---|---|---|
| S E−1 | 1440.6495 ± 0.0027 | 6.09 / 5.99 / 4.97 | S Q C |
| P E0 | 1445.2014 ± 0.0011 | 16.40 / 16.19 / 18.08 | S Q C |
| S E0 | 1449.4544 ± 0.0028 | 4.41 / 4.01 / 5.19 | S Q C |
| P E1 | 1454.0066 ± 0.0010 | 17.78 / 16.75 / 18.38 | S Q C |
| S E1 | 1458.2549 ± 0.0035 | 5.06 / 5.73 / 6.65 | S Q C |
| P E2 | 1462.8129 ± 0.0010 | 18.96 / 16.96 / 18.83 | S Q C |
| P E3 | 1471.6159 ± 0.0006 | 19.98 / flagged / 19.95 | S C |
| S E3 | 1475.8763 ± 0.0021 | 6.41 / 4.72 / 5.95 | S Q C |
| P E4 | 1480.4223 ± 0.0006 | 18.24 / 17.06 / 17.14 | S Q C |
| S E4 | 1484.6802 ± 0.0035 | 4.51 / 3.93 / 3.63 | S Q C |
| P E5 | 1489.2272 ± 0.0011 | 17.53 / 15.78 / 18.18 | S Q C |
| P E83 | 2176.0155 ± 0.0007 | 17.85 / 17.50 / 18.44 | S Q C |
| S E83 | 2180.2716 ± 0.0022 | 5.09 / 4.98 / 5.29 | S Q C |
| P E84 | 2184.8210 ± 0.0007 | 17.48 / 14.82 (partial) / 18.06 | S Q C |
| S E84 | 2189.0738 ± 0.0033 | 4.85 / 4.97 / 5.33 | S Q C |
| P E85 | 2193.6244 ± 0.0008 | 18.44 / 17.15 (partial) / 17.92 | S Q C |
| S E85 | 2197.8764 ± 0.0020 | 5.93 / 5.49 / 5.81 | S Q C |
| P E289 | 3989.8400 ± 0.0014 | – / flagged / 17.88 | C |
| S E289 | 3994.0970 ± 0.0035 | – / flagged / 4.38 | C |
| P E290 | 3998.6438 ± 0.0007 | – / 15.62 / 17.53 | Q C |
| S E290 | 4002.90 | lost (gap) | – |
| P E291 | 4007.4468 ± 0.0012 | – / flagged / 19.97 | C |
| S E291 | 4011.7102 ± 0.0022 | – / 4.56 / 5.24 | Q C |
| P E292 | 4016.2547 ± 0.0007 | – / 16.51 / 18.36 | Q C |
| S E292 | 4020.5174 ± 0.0073 | – / flagged / 3.79 | C |
| P E293 | 4025.0597 ± 0.0008 | – / 16.72 / 18.94 | Q C |
| S E293 | 4029.3183 ± 0.0022 | – / 5.16 / 5.29 | Q C |
| P E294 | 4033.8637 ± 0.0015 | – / flagged / 21.07 | C |
| S E294 | 4038.1176 ± 0.0031 | – / flagged / 5.58 | C |
| P E295 | 4042.6692 ± 0.0007 | – / 15.56 / 17.12 | Q C |
| P E320 / E321 / E322 / E323 (s107) | 4262.7954 ± 0.0013 / 4271.5989 ± 0.0008 / 4280.4041 ± 0.0008 / 4289.2104 ± 0.0008 | C: 19.30 / 18.47 / 18.99 / 17.11 | C |
| S E320 / E321 / E322 (s107), E323 (s108) | 4267.0482 ± 0.0031 / 4275.8536 ± 0.0029 / 4284.6636 ± 0.0036 / 4293.4656 ± 0.0032 | C: 4.83 / 4.72 / 3.76 / 4.79 | C |
| P E324 (s108) | 4298.01 | partial (no pre-ingress baseline) | – |
| S E324 / E325 (s108), E326 (s109) | 4302.2707 ± 0.0029 / 4311.0736 ± 0.0024 / 4319.8790 ± 0.0039 | C: 4.47 / 5.87 / 6.60 | C |
| P E325 / E326 (s108) | 4306.8209 ± 0.0011 / 4315.6232 ± 0.0008 | C: 17.93 / 18.20 | C |
| P E327 / E328 (s109) | 4324.4292 ± 0.0009 / 4333.2316 ± 0.0021 | C: 18.87 / 18.88 | C |
| S E327 / E328 (s109) | 4328.6871 ± 0.0024 / 4337.4867 ± 0.0031 | C: 5.75 / 5.60 | C |

- **Sectors without other pipelines:** sectors 107–109 exist only in TESScut (no QLP or SPOC light curves). There is no 2-min SPOC data.
- **Period:** primaries only, P = 8.8049749 ± 0.0000013 (χ² 26.8/22). Secondaries only, P = 8.8049820 ± 0.0000049. TESScut alone, P = 8.8049753 ± 0.0000014. All are +0.43σ from Gaia's 8.804360 ± 0.001441.
- **Odd/even primaries:** +1.6σ (S), +0.2σ (Q), +0.7σ (C).
- **Secondaries** are not at phase 0.5 and differ from the primaries in depth, so this is not an equal-pair P/2 system.

## Geometry vs Gaia (s13_geometry.out; 20000 draws, NSS correlation matrix)
- **How the test works:** with ω and T_peri correlated at +0.9996, conjunction times are well defined. Without the correlations the prediction is uninformative (σ ≈ 2 d). The order of the first four corr_vec parameters is uncertain, so all 24 orders were run; they give the same answer.
- **15855794:**
  - Observed primary minus conjunction A, at the Gaia epoch: +0.030 d (robust σ 0.080; over the 24 orders +0.23 to +0.46σ). Minus conjunction B: −2.93 d (−39σ).
  - Carried forward with Gaia's P: +0.65σ.
  - Secondary phase: predicted 0.5019 ± 0.0209, observed 0.50182 ± 0.00030; e cos ω = +0.0029 ± 0.0005, against Gaia's +0.003 ± 0.033.
- **92881948:**
  - Primary minus conjunction A: +0.060 d (σ 0.086; +0.35 to +0.69σ). Minus conjunction B: −43σ.
  - Forward with Gaia's P: +0.52σ.
  - Secondary phase: predicted 0.5016 ± 0.0181, observed 0.48334, a 1.0σ difference (32% of draws lie as far from 0.5). e cos ω = −0.0262, against Gaia's +0.003 ± 0.028.
- **Which conjunction:** in both stars the primary is conjunction A, the companion passing in front of the RV star.
- **Physics (s14, uniform discs):**
  - 15855794: f(m) = 0.0437 M☉, so m2 ≥ 0.49 M☉ (M dwarf, about 3630 K). The observed T14 needs b ≈ 1.07 (grazing). Predicted depths are 32.2 / 4.2 ppt; observed 35.3 / 5.4 ppt. The depth ratio implies a companion at 3760 K.
  - 92881948: f(m) = 0.0144 M☉, so m2 ≥ 0.22 M☉. Grazing, b ≈ 1.22. Predicted 14.6 / 4.0 ppt; observed 19.0 / 5.3 ppt. The depth ratio of 0.277 matches the Planck ratio (0.275) for a 3180 K companion.
  - Both are physically sane.

## Ephemerides and next eclipses (s12_compile.out)
- **15855794:** T_ref = BTJD 2886.04720 ± 0.00024 (BJD_TDB 2459886.04720), P = 5.8911458 ± 0.0000038 d. Secondary at +2.95631 ± 0.00179 d.
- **92881948:** T_ref = BTJD 3047.70744 ± 0.00019 (BJD_TDB 2460047.70744), P = 8.8049754 ± 0.0000013 d. Secondary at +4.25578 ± 0.00070 d.
- **Next three eclipses in UTC:** not computed (budget cut). Use T_ref + nP. Those times are BJD_TDB, so no barycentric correction has been applied for an observer.

## Caveats
- **Common mode:** not tested with other stars. Partial substitutes: the residual sky and the neighbour pixels show no dip at the target's fractional depth, and the depth scales with the target fraction.
- **TESScut times:** taken from the FFI time stamps; the barycentric correction is for the FFI, not the target (errors under a minute).
- **15855794 E124:** shallow (27.6 ppt), at the end of an orbit, and flagged by QLP. Its primary-stack difference image was redone without it (s11_15855794_s70_exclE124).
- **PSF model:** a Gaussian with a 1.5× variant, not the TESS PRF. Neighbour exclusions rely on the 3×3 arithmetic plus the centroids.

## Files
`s1`–`s9` (predecessor run); `s10b_archives_redo`, `s10c_vizier_check`, `s10d_controls_gaiavar` (.py/.out); `s11_tesscut.py` with `s11_<tic>_s<sec>.{out,json}`, `_lc.npz`, `_diff.npz`, `s11b_redownload_s70`, `s11_15855794_s43_check.out`; `s12_compile.{py,out,json}`; `s13_geometry.{py,out,json}`; `s14_physics.{py,out,json}`; plus `common.py` and `fitlib.py`.
