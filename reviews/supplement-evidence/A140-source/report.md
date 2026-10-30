# TIC 430987029 (TYC 2741-1694-1, Gaia DR3 1905357825924892928): per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19. This finishes a vet whose first session died before the light-curve pass; everything below is backed by files in this folder. Batch row (c4b promotee): G 11.46, P 9.92091 d, 10.0 ppt, 5 events, dphi +0.012.

**VERDICT: CONFIRMED.** A flat-bottomed 8.6-ppt transit on target, at Gaia's period and Gaia conj A, on a pulsating F star.
**Caveat:** the eclipse duration is in 3.6σ tension with Gaia's e sin ω. The orbit is probably closer to circular than Gaia's weak e = 0.30.

**Star and orbit**
- G 11.46, Tmag 11.16. TIC (spectroscopic): Teff 7001 K, R 1.88 ± 0.09, M 1.54, d 594 pc. RUWE 1.06; ipd_frac_multi_peak 1.
- Gaia NSS SB1 (TAP, with corr_vec): P 9.921763 ± 0.004026 d, e 0.302 ± 0.105, ω 80.3 ± 19.0°, K1 13.4 ± 1.6 km/s, significance 8.2 (weak).
- f(M) 0.0021 Msun → m2(i=90°) 0.185 Msun.

**1. Archives** (`cats-out.txt`, `morecats-out.txt`, `gaiatap-out.txt`)
- `cats.py --r 60`: VSX and ASAS-SN none. SIMBAD: [SB*] only. EB tables none (also batch `c4-ebcats-out.txt`).
- SB9, WDS and J/AJ/160/111: none.
- Gaia vari tables: empty.
- ExoFOP: no TOI or CTOI.
- Web search on the TYC, TIC and Gaia ids (this session): nothing.
- Not previously catalogued.

**2. Eclipses** (`vet-out.txt`, `puls-out.txt`, `pipes-out.txt`, `pipes.png`, `census2-out.txt`)
- **Pulsating base:** the base pulsates at 2.03–2.06 c/d (~11.7 h; 3.1 ppt in s016, 1.1 ppt in s083), plus 2.81 c/d. That is ≈20.2× the orbital frequency, so it nearly survives a fold.
  - These were prewhitened before measuring; out-of-eclipse rms dropped from 2.7 to 1.6 ppt (s016) and from 2.3 to 2.1 ppt (s083).
- **Events:** 5 primaries, all QUALITY==0: s016 1747.445 and 1757.359 (30-min), and s083 3562.943, 3572.862, 3582.781 (200 s).
- **Shape:** T14 6.96 h, T12 ≈ 0.7 h, flat bottom 5.6 h. V-shaped fits are worse by Δχ² +385.
- **Depth (prewhitened):** s016 8.81 ± 0.31, s083 8.35 ± 0.13 (8.12/7.39/9.48; χ² 41.7/2 from residual pulsation, so realistic error ~0.5 ppt). Overall ≈ **8.6 ppt**.
  - The batch's 10.0 and the raw s016 10–15 ppt were inflated by the pulsation.
- **Odd/even:** 8.20 vs 8.21.
- **Systematics:**
  - In-minus-out background is negative (−0.4 to −22 ppt of target, the wrong sign for a fake). A fake would need +42 e-/s.
  - Centroids dX −0.6 ± 0.2, dY +0.5 ± 0.2 mpix.
  - One bit-32 cadence near s016 1757.3 is excluded by Q0. No event near a listed sector-wide systematic.
- **Blind census, prewhitened:** all 5 eclipses are the top 5 peaks (S/N 18–42). No off-ephemeris dip ≥ half depth; the largest is 3.9 ppt, a pulsation residual.
  - Raw census had 11 such dips, all s016 pulsation.
- **Secondary:**
  - At Gaia conj B (phase 0.529 ± 0.066): −0.27 ± 0.14 ppt (white). The scan's S/N spread is 4.7×, so the realistic error is ±0.6 ppt. Not detected; the expected M-dwarf occultation is ≲0.5 ppt.
  - A scan feature at phase 0.675 (1.6 ppt, 4 of 5 windows positive, χ² 23/4) is ~2.9σ in red-noise units and is the scan maximum over ~900 trials. Not claimed.
  - It would also need L2 ~1.6 ppt, roughly 3× what a 0.19 Msun companion gives.

**3. Ephemeris, jackknife, Gaia** (`puls-out.txt`, `jack-out.txt`)
- **Prewhitened:** P = 9.920766 ± 0.000016 d, T0 = 3364.52570 ± 0.0009 BTJD. χ² 4.7/3; O−C +5.3, −4.1, +2.4, −0.1, −1.8 min.
  - Raw: P 9.920841 ± 0.000082 with χ² 50/3, from pulsation-driven timing.
- **vs Gaia:** −0.23σ. The eclipses sit at Gaia conj A, −0.029 phase (−0.24σ), and 0.44 phase (3.1σ) from conj B.
  - The batch dphi was −0.012 (`c4-marg-vetsum-out.txt`); the **ledger's +0.012 has the wrong sign.**
- **Jackknife (raw):** P 9.920794–9.921042, conj A −0.028 to −0.030 phase, depth 8.27–9.21 ppt. **No event owns the verdict.**
- **e cos ω:** one eclipse kind, so not measurable.
- **e sin ω:** see Physics.

**4. Independence**
- **TESS-SPOC s16 (the only other pipeline):** PDC 13.97 and 9.23 ppt on the two s016 events (raw, pulsation-inflated, as QLP's raw 14.9/11.0).
- **Difference images:**
  - TESS-SPOC s16 TPF: Gaussian-PSF fit favours the target (χ² 13,745 vs ≥ 89,317 for any neighbour). The PRF-free centroid offset is 0.12 px (2.6"), and core-pixel depths are 11–13 ppt.
  - Batch diffimg s83 (3 events): deficit 1.16" from target, peak on the target pixel; depth ap1 8.36 > ap3 7.64 > ap5 7.26 ppt, i.e. it concentrates on the target.
  - TESScut s83 (`cutcheck-out.txt`): the target's 3×3 dims 6.8 ppt at eclipse vs |≤1.25| at 19 control phases. The G 11.67 star 146" away shows +3.1, inside its own ±2.8 control scatter.
- **Neighbours** (depth each would need, `diffimg/430987029/diff_s83.json`):
  - G 16.50 @ 11.6": 105% (impossible).
  - G 15.52 @ 30.5": 43%; G 15.00 @ 41.3": 27%; G 16.13 @ 50.3": 75%. All three sit 1.5–2.4 px off and are excluded by the difference images.

**5. Physics** (`phys2-out.txt`, `phys_ecc` runs)
- **Orbit and companion:** a = 23.3 Rsun. k ≈ 0.092, so R2 ≈ 0.19–0.20 Rsun, consistent with m2 = 0.185 Msun. The companion transits the F primary at conj A.
- **Duration tension:** Gaia puts conj A at ν ≈ 10° (near periastron), where the central T14 would be only 5.0 h (R1 1.88), shorter than the observed 6.96 h.
  - Solving the transit shape gives b ≈ 0.42 and a/R1 = 11.0 (circular), i.e. R1 = 2.12 Rsun.
  - With Gaia's e and ω the implied R1 is 2.85 (2.56–3.21) vs TIC 1.88 ± 0.09; 0.1% of Gaia draws land within 3σ.
  - Matching the TIC radius needs e sin ω ≈ −0.12 ± 0.04, against Gaia's +0.28 ± 0.10: **3.6σ** (4.8σ if T12 = 1 h).
- **Reading:** Gaia's e (a 2.9σ e from a significance-8 solution) and/or ω are overestimated. A near-circular orbit fits the transit with R1 ≈ 2.0–2.1 (NSS parallax gives R1 ≈ 1.97).
- **Why the attribution stands:** P agrees to 0.0009 d and the eclipse sits at conj A to 0.24σ, which ties it to the Gaia companion. A conj-B attribution would fix the duration but is 3.1σ off in timing.
- **Heartbeat check** (conj A near periastron at Gaia's e) (`heartbeat-out.txt`, `heartbeat-clean-out.txt`): the trapezoid wins by Δχ² +200 (raw) / +265 (prewhitened) at e free (best e 0.73), and by +729 / +916 at e ≤ 0.62. A heartbeat cannot make a 5.6 h flat bottom with 0.7 h ingress. **Not a heartbeat.**

**6. Verdict, row fixes, predictions**
- **CONFIRMED.** Deciding numbers:
  1. Five flat-bottomed transits, the top 5 census peaks after prewhitening, with no other dip ≥ half depth.
  2. On target in three independent image tests: TESS-SPOC s16 TPF, batch s83 diffimg, TESScut s83 controls.
  3. P −0.23σ from Gaia, eclipse at conj A −0.24σ, jackknife stable.
  4. Heartbeat rejected (Δχ² ≥ 200).
- **Caveats for the table:** only two sectors; a second pipeline exists only for s016; the Gaia e/ω duration tension.
- **Paper-table row fixes:**
  - Depth 10.0 → **8.6 ppt** (pulsation-cleaned; s083 8.35 ± 0.5).
  - P → **9.920766 ± 0.000016**.
  - dphi sign → **−0.012** (−0.029 at the s083 epoch).
  - Note: pulsating (γ Dor-like 2.05 c/d) F primary; transit of a ~0.19 Msun M dwarf; Gaia e sin ω disfavoured by the transit duration (3.6σ).
- **Next primaries** (±5 min including pulsation jitter): BTJD **4406.2061, 4416.1269, 4426.0477**.
- **Conj B** (no eclipse expected; occultation ≲0.5 ppt):
  - On Gaia's e and ω: primary + 0.529 P ± 0.65 d → BTJD **4411.45, 4421.38, 4431.30**.
  - If the orbit is near-circular, as the duration suggests: **4411.17, 4421.09, 4431.01**.
- **To settle further:** an RV orbit with more epochs (to fix e and ω), and 2-min or 200-s data in a new sector for limb-darkened b and k plus a deeper conj-B limit.
