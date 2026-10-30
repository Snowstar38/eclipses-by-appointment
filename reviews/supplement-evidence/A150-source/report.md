# TIC 7795044 (CD-35 10394, TYC 7335-183-1, Gaia DR3 6013256545738149888): per-object vet
Opus 5.5 subagent for Fable 5, wave 3b, 2026-10-19. Batch row: G 10.17, P 9.43204 d, 13.9 ppt, 7 events, dphi +0.001.

**VERDICT: CONFIRMED.** A grazing transit of a subgiant by a ~0.9 Msun companion at Gaia conjunction A, which lies 18° of true anomaly past periastron. That is the heartbeat blind spot, and the test is decisive: a heartbeat model loses to the trapezoid by Δχ² ≥ 10,569. A weak (~1–2 ppt) broad tidal dip at periastron is also present on top of the eclipse. Conj B misses, as the geometry predicts.

**Star and orbit**
- G 10.18, Tmag 9.55. TIC: Teff 5531 K, R 4.0, lumclass GIANT, d 343 pc, E(B−V) 0.23. Gaia GSP-Phot: 6610 K, logg 3.61 — a subgiant. RUWE 0.91.
- Gaia NSS SB1 (full row with corr_vec): P 9.432060 ± 0.000360 d, e 0.187 ± 0.007, ω 71.6 ± 2.8°, K1 53.03 ± 0.56 km/s, significance 95.
- f(M) = 0.138 Msun. m2(i=90°) = 0.87–0.97 Msun for M1 1.3–1.6; a = 24–26 Rsun.

**1. Archives**
- `cats.py --r 60`: VSX and ASAS-SN none. SIMBAD: CD-35 10394 [SB*] only. Prša, IJspeert and Kostov t2/t3/t4: none.
- SB9 and WDS none. Gaia vari tables empty. ExoFOP: no TOI or CTOI, no imaging or spectroscopy.
- Batch ebcats: none. Web search on CD-35 10394, TYC 7335-183-1 and TIC 7795044: nothing. Not previously catalogued as an eclipsing binary.

**2. Eclipses** (QLP SAP, QUALITY==0; s038 10-min, s065 and s103 200-s)
- **Primaries:** 7 in QLP Q0 data (s038 ×2, s065 ×3, s103 ×2), each S/N 78–114.
  - Trapezoid: 14.4–15.0 ppt, T14 4.5–4.6 h, T12/T14 0.4 (V-ish). A flat bottom (T12/T14 0.1) is worse by Δχ² 7754.
  - A third s103 event (BTJD 4166.35) is missing from QLP Q0 but present in TESScut, so **8 eclipses** in all.
- **Depth "variation" is a QLP artefact.** QLP gives s038 15.15, s065 15.41, s103 12.65 ppt (χ² 584/6). My own aperture photometry on TESScut cutouts (r = 1–3.5 px) gives s065 15.0–15.3 and s103 14.8–14.95 ppt, with all three s103 events at 14.5–15.1. The depth is constant at ~15.0 ppt.
- **Systematics:**
  - Two windows contain a bit-32 cadence (s038; depths unchanged). None near a listed systematic time.
  - Background regression implies ≤ 0.07 ppt. Centroids dX +0.33 ± 0.11, dY +0.06 ± 0.05 mpix.
- **Controls:** all phases within ±0.12 ppt.
- **Census:** 8 dips at S/N ≥ 4 — 7 are the eclipses. The other is 0.9 ppt (S/N 5.9, s103 4169.90, phase 0.376). None off-ephemeris at ≥ 50% of the eclipse depth.
- **Heartbeat test** (`hb.py`, ±0.75 d windows, a 4-d detrend that preserves broad shapes):
  - Trapezoid: χ² 2990, depth 15.0 ppt, T14 4.62 h.
  - Kumar heartbeat with Gaia's e and ω fixed: χ² 27,957 (Δχ² +24,967).
  - Fully free heartbeat (e 0.05–0.7, ω, periastron time, i): best χ² 13,558 (Δχ² +10,569). It cannot make a 4.6-h V; see `heartbeat_test.png`.
  - Trapezoid plus Gaia-geometry tide: Δχ² −734 vs trapezoid alone, tide coefficient S 1.7 ppt, eclipse depth 14.2 ppt. So a weak broad (~1 day) periastron tidal dip of about 1 ppt sits under the eclipse. It is real at Δχ² 734, though partly degenerate with the detrending.
- **Secondary at Gaia conj B** (phase 0.538 ± 0.006): 0.007 ± 0.060 ppt (T14 ×1.4), 3σ < 0.19 ppt, over 5 covered conj-B passes. The window maximum, 0.32 ppt at phase 0.556 (S/N 6.3), and the vet.py scan peaks at 0.45/0.25 (S/N 8–10) are red-noise-level features at the scan's 99th percentile. Not claimed.

**3. Ephemeris and Gaia**
- P = 9.4320556 ± 0.0000068 d, T0 = 3194.85288 ± 0.00053 BTJD. χ² 141/5 (errors scaled ×5.3). O−C rms 2.0 min.
- vs Gaia P: −0.000004 d = −0.01σ.
- Gaia conjunctions (MC with corr_vec): the eclipse sits on **conj A** at +0.13/+0.12/+0.10 h (s038/s065/s103) = +0.07/+0.05/+0.03σ, +0.0005 in phase. Conj B is 0.46 phase away (28–47σ).
- One eclipse kind only, so no photometric e cos ω / e sin ω. Gaia: e cos ω +0.059 ± 0.010, e sin ω +0.177 ± 0.007; conj-B phase offset 0.538 ± 0.006, where the data show nothing.

**4. Independence**
- **TESS-SPOC s65:** PDCSAP 15.14 ± 0.08, SAP 14.56 ± 0.08 ppt.
- **TARS:** s38 14.04 ± 0.16, s65 15.46 ± 0.12. My own TESScut photometry: s65 15.0, s103 14.85.
- **SPOC TPF difference image, s65:** peak loss on pixel (5,5), S/N 201. Loss-weighted centroid (4.73, 4.84) vs target (4.69, 4.82). Target fit χ² 18,236 vs ≥ 85,422 for every neighbour. Batch diffimg s65: peak on target, 1.17″.
- **Neighbours** (dip each would need for 15 ppt): G 13.97 @ 40″ → ~490 ppt; G 15.50 @ 55″ → ~1.9e3; G 15.77 @ 40″ → ~2.5e3; fainter ones impossible. Dilution is excluded.

**5. Physics**
- For M1 1.3–1.6 and R1 3.4–4.0: conj A at ν 18.4°, separation 0.82a; conj B at ν 198°, separation 1.17a.
- Central T14 at A 10–12 h vs 4.6 h observed: chord fraction 0.37–0.44, b ≈ 0.90–0.93 (R1+R2), i ≈ 77–79°.
- At conj B the projected separation exceeds R1+R2 by 1.25–1.6 Rsun, so **conj B misses**, consistent with the < 0.19 ppt limit.
- At A the companion (~0.9 Msun, about 4–7% of the TESS light) transits the primary. An occultation could not give 15 ppt.
- Uniform-disc graze depth from the straight-chord inversion is 6–12 ppt vs 15 observed — within the crudeness of that inversion; a slightly larger companion or smaller b closes the gap.
- The tidal term at periastron (~1 ppt) is the expected order for R1/r_peri ≈ 0.17–0.2 and q ≈ 0.6.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers:
  1. A 4.6-h V-shaped 15.0 ppt eclipse beats any heartbeat model by Δχ² ≥ 10,569.
  2. P matches Gaia to −0.01σ and the eclipse is on conj A at +0.07σ.
  3. QLP, SPOC, TARS and my TESScut photometry agree at 14–15.5 ppt, and the SPOC difference image is on target (neighbours ≥ 4.7× worse in χ²).
- **Paper row fixes:**
  - Depth 15.0 ppt, not 13.9; QLP s103's 12.6 is a QLP aperture/background artefact.
  - n_events 8 (QLP Q0 has 7; the third s103 event is in TESScut).
  - P 9.4320556(68).
  - dphi +0.0005.
  - Note a weak periastron tidal (heartbeat) component of ~1 ppt under the eclipse — an EB row with a heartbeat note, not a heartbeat row.
  - TIC "GIANT, R 4.0, 5531 K" vs Gaia 6610 K / logg 3.6: call it a subgiant.
- **Next primaries** (±2 min): BTJD 4402.1560, 4411.5880, 4421.0201.
- **Conj B** (no eclipse expected; Gaia ±~0.15 d): BTJD 4407.23, 4416.66, 4426.10.
- **To settle further:** a joint eclipse + tide model on the 200-s data to pin b and k and the tidal amplitude, and a spectrum to check for an SB2 signature of the ~0.9 Msun companion.
