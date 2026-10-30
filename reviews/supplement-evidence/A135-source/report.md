# TIC 182517223 (TYC 9347-571-1 = Flo 460): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.74, P 2.20762 d, 8.6 ppt, 56 events, dphi +0.001, diffimg 3.23″.

## Verdict: CONFIRMED (grazing F + early-M EB with a spotted, likely synchronised primary; the Gaia SB1 itself)

**Deciding numbers**
- **Period and conjunction:** P = 2.2076198 ± 0.0000003 d from 51 primaries, against Gaia 2.2076462 ± 0.000023 (−1.15σ). Mid-eclipse is +0.0004 phase from Gaia conjunction A (0.02σ; σ = 0.037 d with corr(ω, t_p) = 0.9999). Conjunction B excluded at more than 27σ.
- **Secondary eclipse:** 1.18 ± 0.08 ppt (14.6σ) at phase 0.49942 ± 0.00044, from fold fits on locally normalised windows.
  - T14 ratio 1.01 ± 0.05. Control windows at phases 0.25 and 0.75: −27 ± 58 and −106 ± 55 ppm (null).
  - e cos ω = −0.0009 ± 0.0007 and e sin ω = +0.005 ± 0.027. Gaia: e = 0.014 ± 0.009, ω = 29 ± 45° (e cos ω +0.012), consistent at ~1.4σ.
- **Localisation:** own PSF-fit difference images.
  - Primary (s27, s67, s68, s94): free-fit offsets 0.9–2.1″, mean (+0.1, +0.7)″. Every capable neighbour fits worse by Δχ² > 2400 in every sector: G 11.70 at 35.9″ (needs 1.9%), G 12.79 at 44.4″ (6.1%), G 15.26 at 48.8″ (35%).
  - Secondary (5 sectors): mean (−0.2 ± 0.7, +1.0 ± 0.8)″, χ² 10.6 for 10 dof against zero offset; the target is the best fixed position in 5 of 5 sectors.
  - The batch "deficit−light 10.6″" is just the light centroid being pulled by the G 11.70 star.

**Archives (queried 2026-10-18)**
- cats.py r = 60″: no VSX, ASAS-SN, Prša, IJspeert or Kostov rows. SIMBAD: Flo 460 [SB*] only.
- VizieR battery: no WDS, SB9, Gaia vari_*, RAVE or GALAH entries. ExoFOP: no TOI or CTOI. Web search: nothing.
- **SPOC s56–s69 DV (TESS-SPOC dvt file):** TCE_1: P 2.2076405, 10.16 ppt, SNR 87, impact 0.99. TCE_2: phase 0.4995, 1.41 ppt, SNR 13. **The pipeline saw both eclipses but no TOI or CTOI was ever made — disclose this in the paper.**

**Eclipses and ephemeris** (QLP SAP, QUALITY==0)
- **Primary:** T0 = BTJD 3115.008748 ± 0.000100; O−C rms 4.0 min (median error 0.9 min, χ²/dof 57.8/49; s28 noisy at rms 5 ppt). Folded depth 9.68 ± 0.08 ppt, T14 1.376 ± 0.009 h, T12 0.53 h.
- Odd/even: 9.49 ± 0.11 vs 9.57 ± 0.11 ppt. Per-sector depths 8.0–10.4 ppt.
- **Systematics:** no QUALITY bit-32 in any event core; background changes negligible in s67–s95; nearest listed systematic (s094 3875) is 1.6 d from any event.
- **Light curve:** ~1% spot modulation near P_orb, removed by a local quadratic per event.
- **Blind census:** with a 0.3-day high-pass, no other dips > 3 ppt (earlier 1-day-median census hits were spot residuals at mask edges).

**Independence**
- TESS-SPOC PDCSAP primary: s1 9.35 ± 0.22, s27 9.95 ± 0.14, s67 10.00 ± 0.11, s68 9.89 ± 0.11 ppt (CROWDSAP 0.86–0.89), timing within ≤ 1.6 min. Secondary: 1.23–1.55 ppt in all four sectors.
- TARS s94: primary 9.44 ± 0.14, secondary 1.54 ± 0.16 ppt. TGLC s1 consistent but noisy (9.2 ± 6 ppt).

**Physics**
- f(m) = 0.0599 M☉. With M1 = 1.21 (TIC; R1 1.33, Teff 6235), m2(i = 90°) = 0.58 M☉ and a = 8.66 R☉.
- Central T14 would be 3.8 h; the observed 1.38 h needs i ≈ 78°.
- A limb-darkened grazing model (R2 0.61) gives 9.2 ppt at T14 1.46 h, against 9.7 ppt and 1.38 h observed.
- Depth ratio 0.122 implies T2 ≈ 3650 K (0.8 µm blackbody) — a little cooler than a 0.6 M☉ dwarf (~3900 K) but within this crude model.
- Companion is in front at the primary eclipse (conj A).

**Changes to the paper row**
- Keep the row. P = **2.2076198(3)**.
- Depth ~9.7 ppt (QLP fold) or 9.9–10.0 ppt (TESS-SPOC PDCSAP); the row's 8.6 is the box value.
- Add the secondary: 1.2 ppt at phase 0.4994.
- Note the SPOC TCE_1/TCE_2 prior detection.

**Next eclipses (BTJD)**
- Primary (±0.3 min): 4251.9329, 4254.1406, 4256.3482, 4258.5558.
- Secondary (±2 min): 4253.0355, 4255.2431, 4257.4507, 4259.6583.

**What would settle it further:** a high-resolution spectrum to detect the M-dwarf lines and measure v sin i, testing the synchronised-rotation reading of the spot modulation.
