# TIC 1695417 (BD-13 3646, TYC 5542-763-1, Gaia DR3 3524875747112977920): per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19. This finishes a vet whose first session died after the vet.py pass; everything below is backed by files in this folder. Batch row: G 10.07, P 17.79741 d, 9.5 ppt, 3 events, dphi +0.017.

**VERDICT: CONFIRMED.** The companion transits the primary at Gaia conj A. It is a ~0.14 Msun M dwarf, and the geometry checks out against Gaia's e and ω. There are five events, not three, and none of them carries the result.

**Star and orbit**
- G 10.08, Tmag 9.64. TIC: Teff 5889 K, R 1.60 ± 0.08, M 1.07, d 193 pc. RUWE 1.14.
- Gaia NSS SB1 (TAP, with corr_vec): P 17.792314 ± 0.007005 d, e 0.143 ± 0.026, ω 66.8 ± 11.7°, K1 9.89 ± 0.25 km/s, significance 40.
- f(M) 0.0017 Msun → m2(i=90°) 0.136 Msun.

**1. Archives** (`cats-out.txt`, `morecats-out.txt`, `gaiatap-out.txt`, all on disk)
- `cats.py --r 60`: VSX and ASAS-SN none. SIMBAD: BD-13 3646 [SB*] only. Prša, IJspeert and Kostov t2/t3/t4: none.
- SB9, WDS and J/AJ/160/111: none.
- Gaia vari_summary and vari_eclipsing_binary: empty.
- ExoFOP: no TOI or CTOI, no imaging, no spectroscopy, no companions.
- Web search on the BD, TYC and TIC names (redone this session): nothing.
- Not previously catalogued as an eclipsing binary.

**2. Eclipses** (`vet-out.txt`, `pipes-out.txt`, `pipes.png`, `look.png`)
- **Events:** the three QUALITY==0 events in QLP SAP are s037 2326.384, s046 2557.758 and s046 2575.555, at 9.37–9.78 ppt and S/N 61–88. Two more events sit in cadences QLP flags:
  - **s010 1578.8705**, seen in SPOC 2-min PDC (8.83 ± 0.13 ppt, ±0.7 min), TESS-SPOC (8.62), TARS (7.91), TGLC aperture (8.58) and ELEANOR-lite (8.66). QLP's own s010 flux there is flagged and unusable.
  - **s037 2308.586**, in the sector-start ramp: QLP flagged 9.36 ± 0.15, TESS-SPOC PDC 9.27 ± 0.13, TARS 10.48.
  - The s091 primary (3785.8) falls in the mid-sector gap.
- **Shape:** T14 4.44 h, T12 1.11 h (T12/T14 0.25), flat for 2.2 h. V-shaped (Δχ² +342) and boxier (+563) fits are both worse.
- **Depth:** weighted 9.34 ± 0.06 ppt over the five events. QLP gives 9.4–9.8 and SPOC/TESS-SPOC PDC 8.6–9.7.
- **Odd/even:** 9.54 ± 0.08 vs 9.47 ± 0.16.
- **Systematics:**
  - No bit-32 cadences in any window, and no event within 0.5 d of a listed sector-wide systematic.
  - In-minus-out background is −1.2 ppt of the target — the wrong sign for a background fake, which would need +199 e-/s.
  - Centroids dX −0.30 ± 0.10, dY +0.37 ± 0.50 mpix.
- **Controls:** all 7 phases within ±0.07 ppt, none at S/N > 3.
- **Blind census:** every eclipse is a census peak, and no off-ephemeris dip is ≥ half the depth (largest 1.27 ppt).
- **Secondary:**
  - The phase-0.185 scan peak (0.74 ppt, S/N 11.5) comes from one s091 window at 3789.11, at a gap edge. The other three windows give 0.00 ± 0.08 (`xcheck-0185.txt`), so it is a systematic.
  - At Gaia conj B (phase 0.5348): −0.22 ± 0.05 ppt, systematics-dominated (χ² 27.7/3). SPOC 2-min gives +0.16 ± 0.13. No occultation.

**3. Ephemeris, jackknife, Gaia** (`jack-out.txt`)
- **All 5 events:** P = 17.797939 ± 0.000010 d, T0 = 2326.38398 ± 0.0002 BTJD. χ² 0.4/3; O−C within ±0.5 min.
- **vs Gaia:** P is +0.0056 d = +0.80σ from Gaia. The eclipses sit +0.028 phase (+0.67σ) from Gaia's predicted conj A, and 0.494 phase (11.5σ) from conj B.
- **Jackknife (drop each of 5):** P stays within 17.797933–17.797942, depth 9.22–9.49 ppt, conj A +0.026 to +0.030 phase (all within 0.68σ).
  - **No single event decides the verdict.**
- **Ledger's 3 events only:** P 17.797933 ± 0.000030. Dropping s037 E(2326) leaves the s046 pair one cycle apart, and P loosens to 17.79746 ± 0.00081, still +0.73σ from Gaia.
  - So among the original three, the s037 event set the period's precision. The two recovered events remove that dependence.
- **e cos ω:** only one eclipse kind, so not measurable.
- **e sin ω:** the duration gives the speed factor at the conjunction. With R1 = TIC that requires e sin ω ≈ +0.15 ± 0.06, against Gaia's +0.130 ± 0.031 (−0.3σ) (`phys2-out.txt`).

**4. Independence**
- **Five pipelines see the dip:** SPOC 2-min, TESS-SPOC (s10/s37/s46), TARS (s10/37/46), TGLC and ELEANOR-lite (`pipes-out.txt`).
- **Difference images, PRF-free** (`tpfdiff2-out.txt`):
  - s37: difference and out-of-eclipse centroids agree to 1.3"; per-pixel depth 5.9–10.7 ppt across the 9 brightest pixels.
  - s46: 0.8"; per-pixel depth 7.7–9.9 ppt, uniform, which is what you see when the target is the source.
  - s10 (one event): centroids agree to 0.8–2.0". The core pixel is anomalously shallow (2.3 ppt vs 9–15 around it) in both the SPOC 2-min and the FFI TPF. That looks like image motion during the flagged s10 stretch, not an offset source.
  - The Gaussian-PSF fit (`tpfdiff.py`) is unstable with 1–2 events and is not used.
  - Batch diffimg s46: peak on target, deficit−light 0.65".
- **Neighbours** (dip each would need): G 15.14 @ 48" → ~99%; G 16.49 @ 35" → 340%, both impossible; G 13.63 @ 80" → 25%, but excluded by the difference images. Nothing brighter than G 15 within 60".

**5. Physics** (`phys_ecc` runs, `phys2-out.txt`)
- **Orbit:** a = 30.5 Rsun. Conj A is at ν = 23° (r = 0.866a). Central T14 there would be 6.9 h; the observed 4.44 h gives b ≈ 0.76–0.83 and i ≈ 87.1°.
- **Radius test:** solving the transit shape (Seager & Mallén-Ornelas) and applying Gaia's e and ω gives R1 = 1.59 (1.54–1.64) Rsun against TIC 1.60 ± 0.08. 99.9% of the Gaia draws land within 2σ.
- **Companion:** k ≈ 0.10, so R2 ≈ 0.15–0.17 Rsun, which matches m2 = 0.136 Msun.
- **Which star is in front:** the companion transits the primary at conj A. The uniform-disc prediction is 10.8 ppt; limb darkening at b ~0.8 brings it near the observed 9.3.
- **Conj B:** the projected separation is ≈ R1+R2 (graze or miss). A full M-dwarf occultation would only be ≲0.5 ppt anyway, so the nondetection is expected.
- **Heartbeat check** (conj A is 23° from periastron) (`heartbeat-out.txt`, `heartbeat.png`): a Kumar-family pulse loses to the trapezoid by Δχ² +700 even at e free (best e 0.87, which Gaia excludes), and by +18,065 at e ≤ 0.22. With e = 0.14 a tidal pulse would be days wide; the event is a 4.4 h flat-bottomed transit. **Not a heartbeat.**

**6. Verdict, row fixes, predictions**
- **CONFIRMED.** Deciding numbers:
  1. Five events in five pipelines, and the jackknife moves P by ≤ 9e-6 d with conj A held at +0.67σ.
  2. P +0.80σ from Gaia; the eclipse sits on Gaia conj A.
  3. The photometric R1 with Gaia's e and ω is 1.59 vs TIC 1.60.
  4. Difference images on target; heartbeat rejected (Δχ² ≥ 700).
- **Paper-table row fixes:**
  - n_events 3 → **5** (2 in QLP-flagged data, recovered with SPOC/TESS-SPOC).
  - P → **17.797939 ± 0.000010**.
  - Depth 9.5 → **9.3 ppt**: QLP 9.4–9.8; PDC 8.6–9.7.
  - dphi: +0.017 at the batch epoch, +0.028 at T0 2326 (sign confirmed +).
  - Note: transit of an M dwarf (~0.14 Msun, ~0.16 Rsun) at conj A.
- **Next primaries** (±2 min): BTJD **4408.7428, 4426.5407, 4444.3387**.
- **Conj B** (no eclipse expected, at most a sub-ppt graze; primary + 0.5348 P ± 0.26 d): BTJD **4418.26, 4436.06, 4453.86**.
- **To settle further:** RVs would pin m2 and i, and a high-cadence transit would give limb-darkened k and b. It already reads as a good low-mass-EB benchmark.
