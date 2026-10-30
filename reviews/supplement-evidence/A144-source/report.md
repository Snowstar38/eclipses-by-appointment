# TIC 200398115 (TYC 3624-860-1, Gaia DR3 1986778586111123968): per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19. This finishes the run a first session started; anything that session only stated in prose was redone. Batch row (c4b promotee): G 11.09, P 7.30556 d, 11.0 ppt, 22 events, dphi +0.007.

**VERDICT: CONFIRMED, as an eclipsing heartbeat binary.** The out-of-eclipse light curve is a large heartbeat: ~18 ppt peak-to-peak, with the maximum at periastron, phase ~0.22–0.26. The eclipses sit on top of it:
- **Primary at Gaia conj A:** a full transit of the F subgiant by the M-dwarf companion, 12.0 ppt and 8.8 h. Tide alone cannot make it (Δχ² 11,000–12,750).
- **New secondary at conj B:** the companion's occultation, 2.1–2.2 ppt at phase 0.3625. It sits 0.26σ from Gaia's conjunction separation, and its depth matches the predicted 1.2–2.1 ppt.

Both eclipses are on the target, not on the brighter G 9.93 neighbour 38″ away.

**Star and orbit**
- G 11.09, Tmag 10.77, d 1034 pc. TIC: Teff 6726 K, R 4.26 Rsun, logg 3.3, L 33 Lsun, an evolved F star (TIC mass 1.43, likely 1.4–1.8). RUWE 0.94.
- Crowded field: TIC contratio 1.15, mainly from G 9.93 at 38.4″.
- Gaia NSS SB1, full row with corr_vec: P 7.305697 ± 0.001008 d, e 0.218 ± 0.045, ω 192.7 ± 13.4°, K1 31.96 ± 1.52 km/s, significance 21.
- f(M) = 0.0230 Msun. m2(i = 90°) = 0.43 Msun for M1 1.43, 0.50 for M1 1.8. a = 19.5–20.9 Rsun.

**1. Archives**
- `cats.py --r 60`:
  - VSX has one entry, Gaia DR3 1986778483031908992 [E], P 0.38264 d, at 27″. This is the G 15.91 VARIABLE neighbour, unrelated: 7.3056/0.38264 = 19.09 is not commensurate, and it would need an 881 ppt dip.
  - ASAS-SN none. SIMBAD has TYC 3624-860-1 as [SB*] only. Prša, IJspeert and Kostov: none.
  - c4 ebcats: none.
- SB9, WDS and J/AJ/160/111: none. Gaia vari tables empty for the target. ExoFOP: no TOI or CTOI.
- Web search on TYC 3624-860-1, TIC and Gaia ids: nothing. MAST has QLP only; no SPOC, TESS-SPOC, TGLC, TASOC or ELEANOR products.
- **Not previously catalogued** as an eclipsing binary or heartbeat star.

**2. Light curve** (QLP SAP, QUALITY = 0, no trimming; `vet.py`, `pcfit.py`, `persec.py`, `offeph.py`)
- **Phase curve** (`fold_oc.png`, `pcfit-k.png`): sharp dip at phase 0; brightening to +9 ppt at 0.22; broad tidal low at 0.30–0.38 ending in a sharp step at 0.38; plateau to phase 1.
- **Per-sector folds** (`persec.png`): the step at 0.38 repeats in **7/7 sectors**, including the 2019 30-min s016, at +3.9 to +5.5 ppt.
- **Primary, `vet.py` local-linear fits:** **23 events, not 22** (3 in s016, 4 in s056, 4 in s057, 3 in s076, 3 in s077, 2 in s083, 4 in s084), each with S/N 6.5–27.
  - Weighted depth 10.37 ± 0.10 ppt, T14 7.14 h, T12/T14 0.25, flat 3.6 h. A V shape is worse by Δχ² 497.
  - Depth constancy χ² 96/22; odd and even agree.
  - Background: median in-minus-out −0.07 ppt of target; a fake would need +77 e-/s.
  - Centroids +1.1 ± 0.5 and +0.5 ± 0.2 mpix.
  - Control phases are ±2 ppt because the heartbeat curve is not removed by 3 harmonics. That is expected, not a problem.
- **Heartbeat vs eclipse, global model** (`pcfit.py`, 1000 bins; Kumar+95 tide + r² heating + beaming; e, ω, periastron phase, i gridded; trapezoids at conj A and at a free conj-B centre):
  - Tide only: χ² 14,566 (Kumar basis) / 12,987 (extended r⁴, r⁵ basis).
  - Tide + eclipse A: 1813 / 1782. **The phase-0 dip is an eclipse**, Δχ² 12,752 / 11,205.
  - Eclipse A in that model: depth 12.05 ppt, T14 8.77 h, T12/T14 0.35.
  - Tide + A + B: 1528 / 1519, **Δχ² 286 / 263 for the conj-B eclipse**. B: centre phase 0.3625, depth 2.24 / 2.09 ppt, T14 ~10.5 h. Its ingress is hidden in the tidal decline; the egress is the sharp step.
  - Tidal-fit geometry: e 0.27–0.30, ω 207–212°, periastron at phase 0.25–0.26, vs Gaia 0.218 ± 0.045 and 192.7 ± 13.4° (≤ 1.8σ with a simplified model).
  - Tidal amplitude 3–6 ppt (Kumar S), against an expected (m2/M1)(R1/a)³ ≈ 3 ppt.
- **Census:**
  - The 5 deep off-ephemeris dips are artefacts or known features (`offeph.png`):
    - 3417.14 (s077 sector start, flagged ramp);
    - 2838.32 (s056 gap with a 40 mpix centroid jump);
    - 2860.72 (s057 gap edge);
    - 1744.40 (s016, wing of the primary);
    - 2836.41 (the conj-B feature).
  - The many 2–5 ppt census peaks are QLP point noise. QLP rms is 4.3 ppt per cadence here, against 1.8 ppt in my own TESScut photometry.
  - 1 event is near a listed systematic (3564.5, s083 E249), and its depth (11.3) is normal.
- **Bogus vet.py secondary:** the 6 ppt dip its scan found at phase 0.3375 is mostly tidal; the real occultation is 2.1 ppt at 0.3625. Do not report the scan value.

**3. Ephemeris and Gaia**
- P = 7.305664 ± 0.000049 d, T0 = 3170.06233 ± 0.00263 BTJD. χ² 261/21 (errors ×3.53), O−C rms 19.6 min.
- The large timing scatter comes from fitting local-linear baselines on a steep heartbeat curve. The heartbeat itself is not a timing signal.
- vs Gaia P: −0.03σ.
- Every primary is at **conj A**, +0.6 to +0.8 h from prediction (+0.05 to +0.16σ). Conj B is 5.6–11σ away from the primary.
- Secondary − primary = 0.3625 phase (±~0.005, two bases agree) vs Gaia 0.3658 (MC median 0.369 ± 0.027): 0.26σ.
- With Gaia's e sin ω (−0.046), this gives **e cos ω = −0.2175 ± 0.008**, against Gaia's −0.206 ± 0.042. The secondary's duration is too poorly defined (hidden ingress) for a photometric e sin ω.

**4. Independence** (TESScut s56 and s76; `tpfdiff-s56/s76-out.txt`, `ownphot-out.txt`)
- **Difference images, primary:** the PSF fit prefers the target.
  - s56: χ² 40.8 vs ≥ 512 for any star; G 9.93 gets 606.
  - s76: χ² 9.6 vs ≥ 145; G 9.93 gets 173.
  - Implied own dip on the target: 8.7–8.9 ppt.
  - Batch diffimg-c4b (s56): peak on target, 2.51″.
- **Own aperture photometry** (no other pipeline exists):
  - Target, 3 px: primary 8.97 ± 0.16 (s56) and 7.74 ± 0.23 (s76) ppt. Conj-B step +3.75 ± 0.27 and +3.08 ± 0.21 ppt.
  - G 9.93 neighbour, 2–4 px: primary 0.68 ± 0.10 and 0.13 ± 0.13 ppt (leakage). Step −0.07 and +0.25 ppt.
  - Larger target apertures get shallower (6.7 / 5.5 ppt), as expected when they pull in neighbour light.
  - **Both eclipses and the heartbeat live on the target.** QLP's 10–12 ppt is not badly diluted.
- **Neighbours** (dip each would need, for 10.4 ppt):
  - G 9.93 @ 38.4″ → 3.6 ppt: possible in principle, excluded by the images and apertures above.
  - G 13.82 @ 40″ → 129 ppt; G 14.15 @ 37″ → 174 ppt: excluded by the images.
  - G 15.22 @ 30″ → 467 ppt; G 15.91 @ 27″ → 881 ppt; fainter stars > 1000 ppt: all impossible.

**5. Physics** (`phys-out.txt`)
- **Conjunctions:**
  - A: ν = 257°, r = 1.00a, central T14 13.1–13.9 h.
  - B: ν = 77°, r = 0.91a, central T14 11.9–12.6 h.
- **Inclination:** T14(A) 8.77 h gives b = 0.74–0.78 (R1+R2), i ≈ 79–80°.
  - At A the companion sits fully on the disc: a full transit, matching the flat bottom.
  - At B the companion is totally occulted: projected separation 3.2–3.3 Rsun < R1−R2.
- **Predicted depths:**
  - Transit at A: 12.05 ppt (M1 1.43), 9.9–15.5 ppt across R1 ±10% and M1 1.43–1.8, against **12.0 observed**.
  - Occultation at B: 1.15 ppt (m2 0.43, Teff2 ~3600 K) to 2.14 ppt (m2 0.50, ~3900 K), against **2.1–2.2 observed**. That favours M1 ~1.6–1.8.
- Periastron falls 0.22–0.26 phase after the primary, where the heartbeat peaks.
- One geometry fits both eclipses, their phase separation and the tidal curve.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers:
  1. Primary at Gaia conj A (+0.05 to +0.16σ), P −0.03σ.
  2. Eclipse vs tide-only: Δχ² 11,000–12,750.
  3. Secondary at conj B: Δχ² 263–286, step in 7/7 sectors, phase separation 0.26σ from Gaia.
  4. Difference images and own photometry put both on the target.
  5. Depths match an M-dwarf transit and occultation.
- **Row fixes for the paper table:**
  - P 7.305664(49) d (CSV 7.30556).
  - **23 events, not 22.**
  - Primary depth 12.0 ppt on the tidal baseline (10.4 ppt local-linear; CSV 11.0). T14 8.8 h.
  - **Add a secondary:** 2.1 ppt at phase 0.3625, e cos ω −0.2175(80).
  - Flag it as an **eclipsing heartbeat star** (~18 ppt peak-to-peak tidal curve, periastron at phase ~0.25). The batch eye-read "messy osc + dip / sec at φ 0.35" was this.
  - The VSX EB at 27″ is an unrelated neighbour, not prior art.
- **Next primaries** (conj A, ±13 min): BTJD **4404.7195, 4412.0252, 4419.3309**.
- **Next secondaries** (conj B, ±~0.04 d): BTJD **4407.368, 4414.674, 4421.979**.
- **Heartbeat maxima** (periastron, ±~0.15 d): BTJD ~4406.6, 4413.9, 4421.2.
- **To settle further:** a physical light-curve model (e.g. PHOEBE with tides) to pin i, M1 and the secondary's ingress. Also a TESS-SPOC or TGLC product if one is ever released; QLP is noisy here.
