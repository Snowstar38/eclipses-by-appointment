# TIC 4965877 (TYC 7166-2609-1, Gaia DR3 5436996115010241664): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.45, P 10.22082 d, 6.0 ppt, 8 events, dphi +0.011.

**VERDICT: CONFIRMED.** A grazing eclipse at Gaia conj B, 21° from periastron. Conj A, near apastron, misses.

**Star and orbit**
- G 11.45, Tmag 11.07. TIC (spectroscopic): Teff 6120 K, R 1.98, M 1.16, d 468 pc. RUWE 1.11.
- Gaia NSS SB1: P 10.220388 ± 0.000711 d, e 0.189 ± 0.009, ω 290.7 ± 3.4°, K1 50.30 ± 0.44 km/s, significance 115.
- f(M) = 0.128 Msun; m2(i=90°) = 0.78 Msun (a K-dwarf companion, about 8% of the light).

**1. Archives**
- `cats.py`: VSX and ASAS-SN none. SIMBAD: [SB*] only. Prša, IJspeert and Kostov: none.
- No SB9 or WDS entry. Gaia vari tables empty. ExoFOP: no TOI or CTOI.
- Web search on the TYC, TIC and Gaia ids: nothing. Not previously catalogued as an eclipsing binary.

**2. Eclipses**
- **Primaries:** 11 clean (s008, s009×2, s035×2, s062×3, s089×2, s099), each S/N 9.6–22.7.
  - Weighted depth 6.79 ± 0.14 ppt. Depth constancy χ² 27/10: s008 and s099 ~5.8–5.9, s062 7.7 — QLP aperture/dilution differences, since SPOC agrees within the same range.
  - Odd 6.54 ± 0.21 vs even 6.95 ± 0.18.
  - Global trapezoid: T14 2.58 h, T12 1.03 h, near-V (flat-bottomed T12/T14 = 0.1 worse by Δχ² = +245).
- **Systematics:** no bit-32 cadences in any event window, no event near a listed systematic time; background regression bounds a fake dip at ≤ 0.27 ppt; centroids dX +0.21 ± 0.17, dY +0.42 ± 0.21 mpix; per-epoch plots (`look_pri.png`) show flat background (s062 E11's ramp comes after the dip).
- **Controls:** all phases within ±0.4 ppt, nothing above S/N 3.
- **Census:** all 11 eclipses are S/N ≥ 4 peaks; four off-ephemeris peaks, all 1–1.7 ppt — no other dip of half the eclipse depth or more.
- **Secondary:** none. At conj A (phase ~0.443 ± 0.04): 0.22 ± 0.31 ppt. Full-phase scan max is S/N 3.5 at phase 0.66 (0.45 ppt), not significant.

**3. Ephemeris and Gaia**
- P = 10.220874 ± 0.000008 d, T0 = 2901.40080 ± 0.00075 BTJD. χ² 23.7/9 (errors scaled ×1.62). O−C rms 4.1 min.
- vs Gaia P: +0.00049 d = +0.68σ.
- Jackknife: P shifts ≤ 6 ppm-d; every dropped event's O−C within 2.4σ; depth stays 6.69–7.05 ppt.
- Gaia conjunctions: eclipses on **conj B**, +2.5 h (s008) to +5.4 h (s099), +0.86 to +1.15σ; the growth over time reflects the small period difference. Conj A is 0.44 in phase away (17–48σ). Gaia's phase(B) − phase(A) = 0.543 ± 0.007.
- One eclipse kind only: no photometric e cos ω / e sin ω. Gaia: e cos ω +0.067 ± 0.011, e sin ω −0.177 ± 0.010.

**4. Independence**
- **TESS-SPOC PDCSAP:** s8 6.67 ± 0.33, s9 7.46 ± 0.32, s35 7.35 ± 0.24 ppt.
- **TGLC PSF photometry:** s8 5.88 ± 0.34, s9 6.77 ± 0.46 ppt (deblends neighbours; still sees the dip).
- **SPOC TPF difference image, s35:** target favoured, χ² 1.7e4 vs ≥ 5.0e5 for any neighbour; implied dip 7.66 ppt. The G 12.94 at 50" would need 9 ppt of its own and fits 32× worse. s9 single-event image: peak loss on the central pixel. Batch diffimg (s062): 1.54" offset, peak on target.
- **Neighbours** (dip each would need): G 12.94 @ 50" → 24 ppt; G 12.10 @ 89" → 11 ppt; G 15.30 @ 19" → 218 ppt.

**5. Physics**
- a = 24.7 Rsun. Separation 0.820a at conj B (ν = 339°), 1.171a at conj A (ν = 159°).
- Central eclipse at B would last 7.3 h; observed 2.58 h means b = 0.94, i ≈ 82.6° — a graze.
- Conj A misses by 0.94 Rsun.
- An occultation of the companion. Predicted uniform-disc depth 3.7–5.7 ppt (M1 1.16–1.32, R1 ±10%) vs 6.8 observed — factor ~1.3, within the uncertainty of the companion's radius and light ratio.
- **Heartbeat check** (conj B near periastron): with e = 0.19 any tidal pulse would be broad (~a day) and well under 1 ppt; the observed event is a 2.6 h V shape reproduced by SPOC and TGLC — not a heartbeat.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers: (1) three pipelines agree — QLP 6.8, SPOC 6.7–7.5, TGLC 5.9–6.8 ppt; (2) P +0.68σ from Gaia with eclipses on conj B at ~1σ; (3) jackknife stable to 6 ppm-d and the difference image on target.
- **Paper row:** n_events should be 11, not 8. Nothing else to strike.
- **Next primaries** (±2 min): BTJD 4403.869, 4414.090, 4424.311.
- **Conj A** (no eclipse expected; ±0.25 d): 4408.40, 4418.62, 4428.84.
- **To settle further:** an RV epoch near conj B, or 2-min SPOC data for a proper impact-parameter fit.
