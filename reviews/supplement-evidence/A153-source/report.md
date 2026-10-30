# TIC 375435321

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent). Batch row: G 11.27, P 18.21422 d, 22.5 ppt, 7 events, dphi +0.030, diffimg offset 2.73" (peak not on target, s90).

**Verdict: CONFIRMED.** The eclipsing binary is the target, on Gaia's orbit.

TYC 8187-1030-1 = Gaia DR3 5407588611377633792. G 11.27, Teff 6306 K, R 1.89 Rsun, d 445 pc. The field is crowded: TIC contamination ratio 0.42, 88 Gaia sources within 60″.
Gaia NSS SB1: P 18.22161 ± 0.00749 d, e 0.368 ± 0.031, ω 213.4 ± 7.6°, K1 15.75 km/s.

**Three things decide it:**
1. **The secondary is where Gaia's orbit puts it.** It sits at phase 0.3034 ± 0.0001; Gaia predicts 0.3052 ± 0.0210 (0.1σ). It is 1.32 ± 0.09 ppt deep (S/N 15) and shows in each of the 8 covered epochs (S/N 4.4–8.1). Four other pipelines recover it too. At Gaia's e sin ω, the eclipse timing gives e = 0.367 and ω = 213.0°, against Gaia's 0.368 and 213.4°.
2. **The difference images put the dip on the target** in 6 of 6 clean sector images. The fitted deficit is 1.5–2.3″ from the target. Δχ² against the best neighbour is 268–826, which is 5.6–8.2σ per sector after scaling.
3. **The physics closes.** The mass function implies a 0.24 Msun M dwarf at i ≈ 88.5°.
   - The 23 ppt undiluted, U-shaped transit gives R2 ≈ 0.27–0.29 Rsun.
   - The 1.35 ppt flat occultation implies T2 ≈ 3300 K.
   - One inclination fits both durations: 9.42 h at the wide conjunction, and 6.62 h predicted against 6.96 ± 0.30 h measured at the close one.

**1. Archives and web**
- `cats.py --r 60`: no VSX entry at the target. Within 60″ there are two Gaia-classifier-only VSX objects: one ROT (G 12.9) at 51″ and one DSCT|GDOR (G 15.1) at 58″. ASAS-SN, Prša, IJspeert and Kostov t2/t3/t4: nothing. SIMBAD lists it as [SB*], with Gaia DR3 multiplicity as its only reference.
- ExoFOP: no TOI or CTOI, no spectra or imaging. SB9, WDS, GCVS and Gaia vari_eclipsing_binary: nothing within 60″. A web search turned up nothing.
- Neither the target nor any neighbour is a catalogued eclipsing binary.

**2. Eclipses**
Method: SAP_FLUX with QUALITY == 0, no trimming. The primary shape is 21.5 ppt deep (QLP, diluted), T14 9.42 h, ingress 1.88 h, flat bottom 5.65 h. The batch's "6.3 h" was the box width, not the eclipse.

| E | sector | tc (BTJD) | depth (ppt, QLP) | S/N |
|---|---|---|---|---|
| 0 | s9 | 1550.0973 | 21.8 | 82 |
| 1 | s9 | 1568.3120 | 21.6 | 38 (new; not in sapdepth) |
| 2 | s10 | 1586.5267 | 22.3 | 65 |
| 41 | s36 | 2296.8713 | 23.5 | 88 |
| 81 | s63 | 3025.4276 | 23.3 | 113 |
| 121 | s90 | 3753.9934 | 22.0 | 99 |
| 122 | s90 | 3772.2061 | 22.4 | 105 |
| 138 | s99 | 4063.6317 | 18.5 | 144 |

- The depth spread between sectors is aperture dilution. s99 also has a pre-eclipse baseline sag that pulls its depth down.
- No event lies near a listed sector-wide systematic. QLP centroid shifts are ≤ 7 mpix.
- Seven off-eclipse control phases are all consistent with zero.
- The off-ephemeris dips in the blind census are gap-edge or momentum-dump artefacts.
- Secondaries (QLP):

  | sector | tc (BTJD) | depth (ppt) | S/N |
  |---|---|---|---|
  | s10 | 1573.837 | 1.20 | 4.7 |
  | s10 | 1592.051 | 0.91 | 4.4 |
  | s36 | 2284.184 | 1.25 | 4.6 |
  | s36 | 2302.398 | 1.26 | 5.5 |
  | s63 | 3030.958 | 1.48 | 6.7 |
  | s90 | 3759.519 | 1.66 | 6.5 |
  | s99 | 4050.943 | 1.02 | 6.5 |
  | s99 | 4069.157 | 1.22 | 8.1 |

  The depths are constant (χ² 8.3/7). Across 390 control phases the S/N rms is 1.92, with a maximum of 7.4.

**3. Ephemeris and orbit shape**
- P = 18.214018 ± 0.000011 d. T0 = 1550.0968 BTJD at E = 0, or 3498.99671 ± 0.00056 at E = 107. O−C rms is 2.7 min.
- Against Gaia's P: −1.01σ.
- Against Gaia's conjunctions: the primary is −0.028 phase (−1.05σ) from conjunction A, and the secondary about −0.030 from B. Both shift by the same amount, so this is Gaia's period/periastron-time error, not a misattribution.
- e cos ω = −0.308 (at e sin ω = −0.20), against Gaia's −0.304 ± 0.035. The duration ratio gives e sin ω ≈ −0.15 ± 0.02 in the equal-chord approximation, against Gaia's −0.20 ± 0.045.

**4. Independence, attribution, dilution**
- **Other pipelines** see the primary:

  | pipeline | depth (ppt) |
  |---|---|
  | TGLC s9, PSF photometry | 20.9 ± 0.4 |
  | TGLC s9, decontaminated aperture | 23.5 ± 0.3 |
  | ELEANOR-lite | 17.3–17.6 |
  | T16 | 19.3–20.8 |
  | TARS (5 sectors) | 17.1–20.0 |

  They recover the secondary too: TGLC 1.37, ELEANOR 0.90, T16 1.20, TARS 1.21–1.66 ppt.
- **Difference images** (TESScut, Gaussian scene model at Gaia positions):

  | sector (event) | offset from target | Δχ² vs best neighbour | scaled σ |
  |---|---|---|---|
  | s9 | 1.5″ | 308 (G 14.23 at 6.3″) | 5.6 |
  | s10 | 2.3″ | 268 (G 14.23 at 6.3″) | 7.1 |
  | s36 | 2.3″ | 361 (G 15.05 at 7.2″) | 5.8 |
  | s63 | 1.5″ | 626 (G 15.05 at 7.2″) | 7.6 |
  | s90 (3772.21) | 1.5″ | 579 (G 15.05 at 7.2″) | 6.9 |
  | s99 | 2.3″ | 826 (G 15.05 at 7.2″) | 8.2 |

- **One event excluded.** On its own, the s90 event at 3753.99 localises 11″ off. Its ingress falls in a momentum-dump gap (3753.66–3753.90, QUALITY 32/40), so its before and during images straddle a pointing reset.
- **Why the batch flagged it.** The batch used only event 3772.22 and measured 2.73″ (0.13 px), which is consistent with the target. The "peak not on target" flag came from the target sitting at x = 7.49 px, on a pixel boundary (peak pixel [8,7] against target pixel [7,7]).
- **Neighbours as hosts:**

  | Gaia DR3 | G | separation | fractional dip it would need |
  |---|---|---|---|
  | 5407588508298418560 | 14.23 | 6.3″ | 290–320 ppt |
  | 5407588611377633920 | 15.05 | 7.2″ | 640–720 ppt |
  | 5407588611377634048 | 13.44 | 12.0″ | 110–155 ppt |

  The position fits disfavour all three, and none is a catalogued eclipser.
- **Dilution.** Small apertures on the TESScut images give 21.5–23.4 ppt undiluted; TGLC's decontaminated aperture gives 23.5. Adopted: 23 ± 1 ppt primary, about 1.35 ppt secondary.

**5. Physics**
- f(M) = 0.00593 Msun. With M1 = 1.30, m2 = 0.242 Msun (0.224–0.259 for M1 1.15–1.45) and a = 33.7 Rsun.
- At conjunction A the Gaia star is behind. The deep eclipse is the M dwarf crossing the F star at r/a = 1.084; the shallow one is the M dwarf being hidden at r/a = 0.719.
- i = 88.55° gives impact parameters 0.49 and 0.32. R1 ≈ 2.0 Rsun matches both durations exactly.
- The occultation-to-transit surface-brightness ratio is 0.065, which fits T2 ≈ 3300 K.
- Ellipsoidal (~33 ppm) and beaming (~210 ppm) signals are too small to see.

**Next predicted eclipses (BTJD)**

| E | primary | secondary |
|---|---|---|
| 157 | 4409.6976 (±1 min) | 4415.2237 (±3 min) |
| 158 | 4427.9116 | 4433.4378 |
| 159 | 4446.1256 | 4451.6518 |
| 160 | 4464.3397 | 4469.8658 |

**What would settle it further:** two RV epochs to tie Gaia's orbit to the eclipse epoch, and a near-IR spectrum to look for the M dwarf. A seeing-limited ground light curve of one primary would separate the 6.3″ and 12″ neighbours; a 23 ppt dip is easy from the ground.

**Row fixes for the paper table**
- P = 18.214018 ± 0.000011 d (table: 18.21422). T0 = 1550.0968 BTJD (E = 0).
- Depths:
  - Primary: 21.5 ppt QLP (sector range 18.5–23.5), 23 ± 1 ppt undiluted.
  - Secondary: 1.32 ± 0.09 ppt at phase 0.3034 (new).
- Durations: primary 9.42 h (ingress 1.88 h, flat 5.65 h); secondary 6.96 h. The table's 6.3 h was the box.
- Events: 8 primaries (table says 7) and 8 secondaries.
- Conjunction offset: **−0.028 phase (eclipse early)**. The table's +0.030 is a sign slip.
- Orbit from eclipses: e ≈ 0.367, ω ≈ 213°, e cos ω = −0.308.
- Difference-image flag: a pixel-boundary artefact plus neighbours pulling the light centroid. The dip is on the target in 6 of 6 clean images (5.6–8.2σ); s90 event 3753.99 is excluded for the momentum dump.
- Status: candidate → **confirmed**.
