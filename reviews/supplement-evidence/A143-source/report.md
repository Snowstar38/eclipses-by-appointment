# TIC 192973862 (CD-24 8975, TYC 6623-355-1, Gaia DR3 5472790166292593664): per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19. This finishes the run a first session started; anything that session only stated in prose was redone. Batch row: G 10.80, P 19.21187 d, 10.6 ppt, 8 events, dphi +0.015.

**VERDICT: CONFIRMED.** There is one eclipse per orbit, at Gaia conjunction B, 13 h after periastron. It is a total-ish occultation of the M-dwarf companion by the G dwarf. Three things back it:
- A tidal (heartbeat) model loses to a trapezoid by Δχ² 15,029.
- TESS-SPOC, TGLC and TARS all show the eclipse.
- The SPOC difference image puts it on the target.

Conjunction A is empty (0.00 ± 0.07 ppt), which is what the orbit geometry predicts.

**Star and orbit**
- G 10.80, Tmag 10.33, d 164 pc. TIC: Teff 5646 K, R 1.05 Rsun, M 1.00 Msun, a dwarf. RUWE 1.33.
- Gaia NSS SB1, full row with corr_vec: P 19.20495 ± 0.00489 d, e 0.3448 ± 0.0102, ω 247.48 ± 2.94°, K1 28.27 ± 0.32 km/s, significance 87.
- f(M) = 0.0372 Msun. With M1 = 1.0, m2(i = 90°) = 0.42 Msun, an M dwarf (R2 ~0.46 Rsun, Teff ~3600 K). a = 34.0 Rsun.

**1. Archives**
- `cats.py --r 60`: VSX none, ASAS-SN none. SIMBAD has CD-24 8975 as [SB*] only. Prša, IJspeert and Kostov: none. Batch ebcats: none.
- SB9, WDS and J/AJ/160/111: none. Gaia vari_summary and vari_eclipsing_binary: empty.
- ExoFOP: no TOI or CTOI, no imaging, spectroscopy or companions.
- Web search on CD-24 8975, TYC 6623-355-1 and TIC 192973862: nothing. **Not previously catalogued as an eclipsing binary.**

**2. Eclipses** (QLP SAP, QUALITY = 0, no trimming; `vet.py`, `sec.py`, `bkgreg.py`, `hbtest.py`)
- **Events:** 9, not 8 (s009, s035 ×2, s036, s062 ×2, s089, s099 ×2), each with S/N 13.6–64.
- **Shape:** global trapezoid depth 10.98 ppt, T14 3.48 h, T12 1.39 h, flat bottom 0.7 h. A V shape is worse by Δχ² 2780.
- **Depths:** weighted 10.93 ± 0.08 ppt. Depth constancy χ² 169/8, mostly from s099 (9.6–10.1 ppt, on a steep background) against 11.5–12.0 elsewhere. Odd 11.06 ± 0.10, even 10.72 ± 0.12.
- **Systematics:**
  - Background regression fakes ≤ 0.09 ppt, against a 5.8–7.2 ppt dip in the same windows.
  - Centroid shifts are −1.1 ± 0.6 and +1.9 ± 0.4 mpix.
  - 2 events have a bit-32 cadence in the window; none is near a listed systematic time.
- **Controls:** all 7 control phases within ±0.2 ppt.
- **Census:** all 9 eclipses are S/N ≥ 4 peaks of the census. There are no off-ephemeris dips ≥ 5.5 ppt. The −10 ppt feature at phase −0.17 in the raw fold is an s099 orbit-start ramp (`offeph.png`).
- **Heartbeat test** (conj B is 22.5° of true anomaly after periastron; `hbtest.png`):
  - Trapezoid: χ² 183 over 160 bins.
  - Kumar+95 tide + heating + beaming, with Gaia e, ω (±2σ), periastron phase and i free: χ² 15,212.
  - Tide plus trapezoid: χ² 161, with the trapezoid at 11.39 ppt.
  - The expected tidal amplitude, (m2/M1)(R1/r_peri)³, is ~0.03 ppt. **Not a heartbeat.**
- **Secondary at conj A** (phase 0.5884, T14 6.7 h predicted from the velocity ratio):
  - 5 epochs give −0.16 ± 0.06 ppt.
  - The one outlier (s089, 3731.97, −0.96 ppt) sits on the listed 3732 systematic. Without it the result is 0.00 ± 0.07 ppt (3σ < 0.2 ppt).
  - `vet.py`'s scan best (phase 0.6575, 0.6 ppt, T14 ×2) is 7σ from Gaia's conj A and not confirmed by `sec.py`. **Do not report it.**

**3. Ephemeris and Gaia**
- P = 19.211924 ± 0.000008 d, T0 = 3144.30777 ± 0.00027 BTJD. χ² 19.8/7 (errors ×1.68), O−C rms 1.5 min.
- Jackknife: dropping any event or sector moves P by ≤ 7 ppm-d. Depth stays 10.78–11.26.
- vs Gaia P: +0.00698 d = +1.43σ.
- Every eclipse is at **conj B**: +7 to +29 h from prediction, +1.0 to +1.3σ. The lag grows with time because Gaia's P is 1.4σ short. Conj A is 0.41 phase away (9–24σ).
- One eclipse kind only, so no photometric e cos ω / e sin ω. Gaia gives e cos ω −0.132 ± 0.015 and e sin ω −0.318 ± 0.014.

**4. Independence** (`indep-out.txt`, `tpfdiff-s0062/0035-out.txt`)
- TESS-SPOC PDCSAP: s009 11.95 ± 0.27, s035 11.22 ± 0.15, s036 12.07 ± 0.19, s062 11.89 ± 0.14 ppt.
- TGLC PSF (deblended), s009: 11.82 ± 0.40 ppt.
- TARS s009–s089: 10.0–14.5 ppt.
- SPOC TPF difference images: the PSF fit puts the loss on the target in both sectors.
  - s062: target χ² 1.23e5 vs 4.88e5 for either neighbour; max-loss pixel S/N 578.
  - s035: target χ² 1.04e4 vs ≥ 2.9e4 for any neighbour.
  - Batch diffimg (s35): peak on target.
- **Neighbours** (dip each would need): G 11.76 @ 62.5″ → 26.5 ppt; G 15.55 @ 85.6″ → 868 ppt (impossible). Nothing else with G < 17 within 90″. The G 11.76 star is rejected by both difference images.

**5. Physics** (`phys-out.txt`)
- **Conjunctions:**
  - B: ν = 22.5°, r = 0.668a, central T14 4.66 h.
  - A: ν = 202.5°, r = 1.293a, central T14 9.0 h.
- **Inclination:** the observed 3.48 h gives a chord fraction of 0.75 → i = 87.5°.
- **Conj A:** the projected separation is 1.95 Rsun vs R1+R2 = 1.51 Rsun, so it misses by 0.43 Rsun. This holds for R1 ±10%, matching the empty conj A.
- **Which star is in front:** under the Gaia convention, B means the primary is in front, so the companion is occulted.
  - Predicted uniform-disc occultation depth: 13–17 ppt, against 10.93 observed. The crude Planck light ratio puts the companion at ~3% of the TESS light; consistent within the model's slack.
  - The other reading, a transit of the G star by an object this size, would be 40–95 ppt. **Ruled out.**
- Depth, duration, flat-ish bottom and the missing A eclipse all fit one geometry.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers:
  1. On Gaia conj B (+1.0 to +1.3σ), with P +1.4σ from Gaia.
  2. Heartbeat excluded, Δχ² 15,029.
  3. Independent SPOC, TGLC and TARS depths of 11–12 ppt.
  4. SPOC difference image on target in two sectors.
  5. Conj A < 0.2 ppt (3σ), as the geometry predicts.
- **Row fixes for the paper table:**
  - P 19.211924(8) d (CSV 19.21187).
  - Depth 10.9 ppt (trapezoid; CSV 10.6).
  - **9 events, not 8.**
  - Note that it is an occultation of the M-dwarf companion at conj B, near periastron, with i ≈ 87.5°.
  - Batch dphi +0.015 grows to +0.063 by s100 because of Gaia's P.
- **Next eclipses** (conj B, ±1 min): BTJD **4412.2948, 4431.5067, 4450.7186**.
- **Conj A** (no eclipse expected; ±~0.01 d from Gaia's e, ω): BTJD 4404.387, 4423.599, 4442.811.
- **Periastron:** ~0.56 d before each eclipse.
- **To settle further:** an RV epoch to tie the conjunction labels, or a high-precision eclipse to test for a total (flat) occultation.
