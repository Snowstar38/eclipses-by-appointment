# TIC 219543346 (TYC 1643-218-1, Gaia DR3 1829189638955084672): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.36, P 19.20532 d, 5.9 ppt, 7 events, dphi +0.005.

**VERDICT: CONFIRMED.** The single eclipse per orbit is at Gaia conj B. It is a grazing occultation of the companion by the subgiant primary; conj A misses as the geometry predicts.

**Star and orbit**
- G 11.36, Tmag 10.96. TIC: Teff 6324 K, R 3.49 Rsun (a subgiant), M 1.25, d 833 pc. RUWE 1.52.
- Gaia NSS SB1 (full row with corr_vec): P 19.20610 ± 0.00375 d, e 0.437 ± 0.018, ω 348.5 ± 5.1°, K1 54.2 ± 3.2 km/s, significance 17.
- f(M) = 0.231 Msun; m2(i=90°) = 1.08 Msun — a ~1.06 Rsun, ~6000 K dwarf carrying about 7% of the TESS light.

**1. Archives**
- `cats.py --r 60`: VSX has only two unrelated ROT stars (40", 42"). ASAS-SN: none. SIMBAD: [SB*] only. Prša, IJspeert and Kostov: none.
- No SB9 or WDS entry. Gaia `vari_summary` and `vari_eclipsing_binary` empty. ExoFOP: no TOI/CTOI, no imaging or spectroscopy.
- Web search on the TYC, TIC and Gaia ids: nothing. Not previously catalogued as an eclipsing binary.

**2. Eclipses** (QLP SAP, Q0, no trimming; `vet.py`, `sec.py`, `look2.py`)
- **Primaries:** 7 measured (s014, s041, s054, s055×2, s082×2), each S/N 12.7–21.7.
  - Weighted depth 6.94 ± 0.14 ppt. Depth constancy χ² 15.8/6 (range 6.4–7.8). Odd 7.07 ± 0.18 vs even 6.66 ± 0.25.
  - Global trapezoid: T14 4.56 h (1σ 4.50–4.62), T12 1.82 h, flat bottom 0.9 h. Close to V-shaped: the flat-bottomed T12/T14 = 0.1 is worse by Δχ² = +300.
- **Events seen but not counted:** s014 E-64 is fully flagged in QLP, though the dip is visible (TASOC has it). s081 E31 is fully flagged and sits on a huge background ramp, unusable.
- **Systematics:** background flat through every clean event; background regression bounds a fake dip at ≤ 0.43 ppt vs 3.6–4.9 ppt measured; centroids dX −0.37 ± 0.18, dY +0.32 ± 0.24 mpix; one bit-32 cadence in one window; nothing near a listed systematic time.
- **Controls:** all control phases within ±0.3 ppt of zero.
- **Census:** all 7 primaries are S/N ≥ 4 peaks; the off-ephemeris peaks (s054 2777.6, 2791.1; s081 3531.4, 3532.5) are background features (`census_offeph.png`).
- **Secondary:** `vet.py`'s phase-0.22 "secondary" (2.9 ppt, S/N 14.6) is the s081 orbit-end ramp plus flagged s014 data (`look_sec022.png`). With s081 excluded, the best dip in phase 0.206–0.266 is 0.02 ± 0.15 ppt (T14 scan 1–14 h; no epoch over S/N 2). 3σ upper limit ≈ 0.45 ppt at conj A. **Must not be reported as a secondary.**

**3. Ephemeris and Gaia**
- P = 19.205350 ± 0.000065 d, T0 = 2919.47988 ± 0.00199 BTJD. χ² 23.5/5 (errors scaled ×2.17). O−C rms 6.8 min.
- vs Gaia P: −0.20σ.
- Jackknife: P shifts ≤ 48 ppm-d (≤ 0.75σ); depth stays 6.77–7.09 ppt; leave-one-sector-out P runs 19.205302–19.205389. E39 (s041) is +18.5 ± 4.6 min off the rest; dropping it gives χ² 5.9/4 with P and depth unchanged — no single event owns the verdict.
- Gaia conjunctions (Monte Carlo with corr_vec): every eclipse on **conj B**, +0.6 to +2.4 h from prediction (+0.04 to +0.25σ). Conj A falls 0.236 ± 0.010 in phase after each eclipse, 7–14σ away, and empty.
- One eclipse kind only, so no photometric e cos ω / e sin ω. Gaia: e cos ω +0.426 ± 0.018, e sin ω −0.087 ± 0.038; the geometry is consistent.

**4. Independence**
- **TASOC s014 ensemble FLUX_CORR:** E-63 6.18 ± 0.42 ppt; E-64 6.78 ± 0.38 ppt (the event QLP flagged). TASOC FLUX_RAW too noisy (7.8 ppt point-to-point). MAST has no SPOC, TESS-SPOC, TGLC or ELEANOR products.
- **Difference image** (TESScut s082, 2 events): PSF fit prefers the target, χ² 4.7e4 vs ≥ 2.6e6 for any neighbour; implied dip 6.17 ppt. Batch diffimg (s055): 2.73" offset, peak on target.
- **Neighbours** (dip each would need): G 13.81 @ 55" → 56 ppt; G 14.58 @ 57" → 115 ppt; G 15.08 @ 46" → 180 ppt; G 11.48 @ 89" → 7.8 ppt — the only physical mimic, and the difference image rejects it (χ² 600× worse, implied dip wrong sign).

**5. Physics** (`phys_ecc.py`)
- a = 40.0 Rsun. Separation 0.745a at conj B (ν = 281°), 0.886a at conj A (ν = 101°): projected separation 1.19× larger at A.
- Central eclipse at B would last 13.8 h; observed 4.56 h means b = 0.94 (R1+R2), i ≈ 81.7° — grazing, matching the V shape.
- Conj A: projected separation 5.11 Rsun vs R1+R2 = 4.55 — a miss by 0.55 Rsun, robust to R1 ±10% and M1 1.25–1.45.
- Gaia convention: B = primary in front, so an occultation of the companion. Predicted uniform-disc depth 4.4–6.3 ppt vs 6.94 observed. Depth, duration, shape and the missing A eclipse fit one geometry.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers: (1) conj B timing within 0.04–0.25σ and P at −0.20σ from Gaia; (2) TASOC detects it independently at 6.2–6.8 ppt; (3) difference image on target; (4) < 0.45 ppt at conj A matches the predicted miss.
- **Paper row:** no change. Note it is an occultation of the companion, and drop the s081 "secondary".
- **Next primaries** (conj B, ±8 min): BTJD 4417.497, 4436.703, 4455.908.
- **Conj A** (no eclipse expected; ±0.19 d): 4422.03, 4441.24, 4460.44.
- **To settle further:** a clean sector covering both conjunctions, or an RV epoch near conj B.
