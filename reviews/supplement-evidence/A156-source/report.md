# TIC 159836610

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent). Batch row: G 11.14, P 5.70229 d, 93.0 ppt, 14 events, dphi +0.010, diffimg offset 2.36" (peak not on target, s28).

**Verdict: CONFIRMED.** The eclipsing binary is the target, on Gaia's orbit.

TYC 7485-869-1 = Gaia DR3 6584193527718873856. G 11.14, RVS template Teff 6750 K, Gaia FLAME R 2.12 / M 1.35, parallax distance about 450 pc. Gaia RUWE is 7.0.
Gaia NSS SB1: P 5.702265 ± 0.000573 d, e 0.107 ± 0.047, ω 63.5 ± 16.0°, K1 37.56 ± 1.19 km/s.

**What decides it:**
- **Timing matches Gaia.** The period agrees to 0.05σ. Every sector's primary falls +0.2 to +0.6σ from Gaia's conjunction A.
- **The secondary matches Gaia's orbit.** It is at phase 0.5128 ± 0.0001; Gaia predicts 0.5265 ± 0.0204 (0.7σ). It is 7.9 ppt deep, in 15 of 15 covered epochs, at S/N 31–51 each.
- **The difference images put the dip on the target** in all four sectors, 0.0–1.1″ off. Δχ² against the only plausible neighbour is 1,323–174,363 (6.6–21σ after scaling). The undiluted depth stays at 85–90 ppt for every aperture size.
- **No Gaia neighbour can host it.** The brightest within 60″ (G 15.09 at 25.7″) would need 350% of its own flux.
- **The physics closes.** An F star with a 0.47 Msun M dwarf: k ≈ 0.29, Teff2 ≈ 3600 K, and the durations ordered as e sin ω > 0 requires.

**1. Archives and web**
- `cats.py --r 60`: VSX, ASAS-SN and every EB catalogue have nothing. SIMBAD lists it as [SB*] (RAVE DR4/5/6, APASS, Gaia DR3 multiplicity).
- ExoFOP: no TOI or CTOI. SB9, WDS, GCVS and Gaia vari tables: nothing within 60″. A web search turned up nothing.
- Not a catalogued eclipsing binary.

**2. Eclipses**
Method: SAP_FLUX with QUALITY == 0, no trimming. The primary is 90.1 ppt deep (QLP), T14 4.74 h, ingress 1.18 h, flat bottom 2.37 h. A flat bottom is strongly preferred over a V shape (Δχ² +16,000 for ingress/T14 = 0.5).

| sector | E | tc (BTJD) | depth (ppt) |
|---|---|---|---|
| s1 | 0, 1, 2 | 1330.1813, 1335.8831, 1341.5854 | 91.5, 90.3, 90.7 |
| s28 | 129–132 | 2065.7772, 2071.4790, 2077.1818, 2082.8836 | 94.8, 99.2, 94.9, 94.2 |
| s68 | 320, 321, 323, 324 | 3154.9146, 3160.6169, 3172.0215, 3177.7243 | 95.3, 94.3, 94.4, 94.8 |
| s95 | 448, 449, 451 | 3884.8082, 3890.5105, 3901.9151 | 83.1, 82.6, 82.3 |

- Each primary has S/N 93–355. Timing errors are about 0.4 min.
- Depth differences are between sectors (s95 is the lowest), which is dilution. Within a sector, odd and even events agree to ≤ 0.7%.
- E = 3 (1347.29) is missing from QLP's good-quality data but appears in ELEANOR-lite.
- Background shows nothing at the eclipse times; the per-event background column has broken units. Centroid shifts are about 2 mpix. Two windows contain a bit-32 cadence; no event lies near a listed systematic.
- Six control phases are zero. The seventh, phase 0.5, contains the secondary.
- The blind census finds only the primaries and secondaries, plus dips ≤ 3 ppt.
- Secondary: phase 0.5128, T14 5.28 h, ingress/T14 0.25, depth 7.905 ± 0.055 ppt (S/N 144). Per event it ranges 7.3–8.5 ppt. Across 149 control phases the S/N rms is 1.57, with a maximum of 2.83.

**3. Ephemeris and orbit shape**
- P = 5.7022928 ± 0.0000004 d. T0 = 1330.18107 BTJD at E = 0, or 2618.89923 ± 0.00007 at E = 226. χ²/dof 11.2/12, O−C rms 0.3 min.
- Against Gaia's conjunction A: the eclipse is +0.009 to +0.0125 phase **late**. The table's +0.010 has the right sign.
- e cos ω = +0.020 (range +0.016 to +0.020), against Gaia's +0.042 ± 0.032.
- The duration ratio (secondary/primary) is 1.114 ± 0.029, giving e sin ω ≈ +0.054 ± 0.013 against Gaia's +0.092 ± 0.043. That puts e ≈ 0.06, against Gaia's 0.107 ± 0.047 (about 1σ).

**4. Independence, attribution, dilution**
- **Other pipelines** see the primary:

  | pipeline | depth (ppt) |
  |---|---|
  | TESS-SPOC s68 PDCSAP (crowding-corrected) | 89.6–90.1 |
  | TESS-SPOC s68 SAP | 86.2–86.9 |
  | ELEANOR-lite s1 | 87–89 |
  | T16 s1 | 88–94 |
  | TASOC raw s1 | 85–86 |
  | TGLC s1 | 104–106 |

  TASOC's corrected flux is broken, and TGLC's flux zero point looks high. The secondary appears in all of them at 7.2–10.3 ppt.
- **Difference images:**

  | sector | source | offset from target | Δχ² vs G 15.09 at 25.7″ | other measure |
  |---|---|---|---|---|
  | s1 | TESScut | 1.0″ | 1,323 | — |
  | s28 | TESScut | 1.1″ | 9,074 | — |
  | s68 | SPOC target-pixel file | 0.0″ ± 0.6″ | 174,363 | 47σ (jackknife) |
  | s95 | TESScut | 0.0″ | 83,114 | 50σ (jackknife) |

  The undiluted depth is aperture-invariant: 85–89 ppt (TESScut) and 89.3–90.3 ppt (target-pixel file) for radii 0.8–4 px.
- **Why the batch flagged it.** The WCS puts the target at y = 7.43, but the light centroid is at y = 7.52, so the target is effectively on the row 7/8 boundary (peak pixel [7,8] against target pixel [7,7]). The batch's 2.36″ deficit-to-target offset is the WCS zero point: the light centroid is offset by the same amount, and there is no bright neighbour to pull it.
- **Dilution.** Adopted undiluted primary 90 ± 2 ppt (QLP ranges 82.6–95 by sector); secondary 7.9 ppt.
- **Caveat: Gaia RUWE is 7.0** (astrometric excess noise 1.24 mas, significance 1969). ipd_frac_multi_peak is 1% and the harmonic amplitude 0.016, so Gaia does not see a resolved double. The 5.7-day orbit moves the photocentre only about 44 μas, so a further, longer-period companion is likely. Its light would mean the true depth is somewhat larger. It does not move the attribution: the period, phases and e cos ω all tie the eclipse to the Gaia SB1.

**5. Physics**
- f(M) = 0.0308 Msun. With M1 = 1.35, m2(i = 90°) = 0.466 Msun (0.435–0.497) and a = 16.4 Rsun.
- Conjunction A is at r/a = 0.902 (faster), conjunction B at r/a = 1.093 (slower). So the primary eclipse should be the shorter one, and it is: 4.74 h against 5.28 h.
- k = 0.28–0.30, so R2 ≈ 0.50–0.54 Rsun at R1 = 1.8 (a main-sequence 0.47 Msun dwarf is about 0.47 Rsun).
- The flat bottom needs b ≈ 0.3–0.4, which favours R1 ≈ 1.6–1.8. At R1 = 1.8 the predicted secondary duration is 5.20 h against 5.28 h measured. FLAME's 2.12 assumes no extra light, and the RUWE suggests there is some.
- The surface-brightness ratio is 0.097, which fits Teff2 ≈ 3600–3650 K.
- The s68 phase curve shows terms of the expected size (0.3–0.6 ppt). But the second-harmonic sign is wrong for pure ellipsoidal variation, and one sector cannot separate spots or systematics, so I did not use it.

**Next predicted eclipses (BTJD)**

| E | primary (±0.2 min) | secondary (±0.8 min) |
|---|---|---|
| 539 | 4403.7169 | 4406.6410 |
| 540 | 4409.4192 | 4412.3433 |
| 541 | 4415.1215 | 4418.0456 |
| 542 | 4420.8238 | 4423.7479 |

**What would settle it further:**
- RVs at quadrature to check K1 against the eclipse epoch.
- High-resolution imaging or speckle to find the companion behind the RUWE of 7, and fix the third light and the true depth.
- A near-IR spectrum to see the M dwarf, which would give a double-lined solution with masses and radii.

**Row fixes for the paper table**
- P = 5.7022928 ± 0.0000004 d (table: 5.70229). T0 = 1330.18107 BTJD (E = 0).
- Depths:
  - Primary: 90.1 ppt QLP trapezoid (sector range 82.6–95.0), 90 ± 2 ppt undiluted. The table's 93.0 is the sapdepth median.
  - Secondary: 7.9 ppt at phase 0.5128 (new).
- Durations: primary 4.74 h (ingress 1.18 h, flat 2.37 h); secondary 5.28 h.
- Events: 14 primaries in QLP (plus 1347.29 in the other pipelines) and 15 secondaries.
- Conjunction offset: +0.009 to +0.0125 phase (eclipse late, +0.2 to +0.6σ). The table's +0.010 is fine.
- Orbit from eclipses: e cos ω = +0.020, e sin ω ≈ +0.05.
- Difference-image flag: a pixel-boundary and WCS zero-point artefact. The dip is on the target in 4 of 4 sectors (including the s68 target-pixel file, 47σ by jackknife), and no neighbour can host it.
- Note: Gaia RUWE 7 suggests a third body.
- Status: candidate → **confirmed**.
