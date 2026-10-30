# TIC 116246364 (TYC 3093-1294-1, Gaia DR3 1344576143791084416): per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19. A first subagent died after running vet.py; this one resumed from its files on disk. Batch row: G 11.39, P 14.74818 d, 10.4 ppt, 9 events, dphi +0.004.

**VERDICT: CONFIRMED.** The companion grazes across the primary at Gaia's conjunction A, which is 13° before periastron. A heartbeat is ruled out by Δχ² = 5391. Conjunction B misses on geometry, and no secondary is seen there.

**Star and orbit**
- G 11.38, Tmag 10.92. TIC: Teff 5559 K, R 1.96 ± 0.11, M 0.98, d 388 pc. Gaia GSP-Phot gives logg 4.08 (TIC 3.85). RUWE 1.15.
- Gaia NSS SB1 (full archive row with corr_vec, `gaia.json`): P 14.748178 ± 0.002110 d, e 0.250 ± 0.023, ω 103.0 ± 3.5°, Tp 2.151 ± 0.125 (BTJD 391.151), K1 27.63 ± 0.50 km/s, significance 54.9.

**1. Archives**
- `cats.py` (`cats-out.txt`): VSX, ASAS-SN, Prša, IJspeert and Kostov all none. SIMBAD lists TYC 3093-1294-1 as [SB*] only.
- `morecats-out.txt`: no SB9, WDS or J/AJ/160/111 entry. ExoFOP: no TOI or CTOI, no imaging, no spectroscopy.
- Gaia vari_summary and vari_eclipsing_binary are empty.
- Web search on the TYC, TIC and Gaia ids: nothing.
- Not previously catalogued as an eclipsing binary.

**2. Eclipses** (raw QLP SAP, QUALITY == 0, no trimming; `vet-out.txt`, `events.png`, `fold_oc.png`)
- **Primaries:** 12 measured, each S/N 15–33: s025 ×1, s026 ×2, s040 ×2, s052 ×2, s053 ×2, s079 ×1, s080 ×2.
  - Weighted depth 11.39 ± 0.12 ppt. Constancy χ² 12.8/11. Per sector 11.08–12.10 ppt.
  - Odd 11.34 ± 0.18 vs even 11.44 ± 0.17.
- **Shape:** global trapezoid T14 3.12 h, T12 1.25 h (T12/T14 0.4), flat 0.62 h. Fully V (T12/T14 0.5) is worse by Δχ² +34; flat-bottomed (0.1) is worse by +779.
- **Systematics:**
  - No bit-32 cadence in any event window, and no event within 0.5 d of a listed sector-wide systematic.
  - Background regression (`bkgreg-out.txt`): the largest fake dip background could produce is 0.42 ppt (s052); every other sector ≤ 0.11 ppt.
  - QLP centroids in eclipse: dX −0.66 ± 0.36, dY −0.62 ± 0.37 mpix.
- **Controls:** seven control phases all within ±0.25 ppt, none above S/N 3.
- **Blind census:** 28 dips at S/N ≥ 4. 13 are on the primary ephemeris. The 15 off-ephemeris dips are all ≤ 4.7 ppt, so there is no other dip of half the eclipse depth or more.
- **Secondary** (own fixed-shape test `sec2.py`; `sec2-out-0.463-*.txt`):
  - At Gaia's conj B phase, 0.4634 ± 0.0109: depth −0.03 ± 0.10 ppt with a 3.1 h template, +0.05 ± 0.09 ppt with 5.1 h (the expected B/A duration ratio is 1.65).
  - Best value anywhere in ±0.04 of that phase is S/N 2.1. A same-width scan reaches that S/N at 81–90% of control centres.
  - **No secondary.** 3σ limit ≈ 0.3 ppt.
  - `sec.py` crashed (singular matrix). Its earlier S/N 3.7 "secondary" at phase 0.42 is not significant against its own control rms of 2.6.

**3. Ephemeris and Gaia**
- P = 14.748239 ± 0.000011 d, T0 = 2765.23338 ± 0.00040 BTJD (E = 52). χ² 17.0/10 (errors scaled ×1.31). O−C rms 1.7 min.
- vs Gaia P: +0.000061 d = +0.03σ.
- Gaia conjunctions (Monte Carlo of 20k draws with the full covariance): the eclipses sit on **conj A**, 1.53–1.66 h early. That is −0.0045 in phase, or −0.14 to −0.29σ.
  - Conj B is predicted at phase 0.4634 ± 0.0109 from A, and the eclipse is 15–27σ away from it.
  - True anomaly at the eclipse is 343.9° (Gaia mean elements) against 347.0° expected for conj A.
- Only one eclipse kind, so no photometric e cos ω or e sin ω. Gaia: e cos ω −0.056 ± 0.017, e sin ω +0.243 ± 0.022.

**4. Independence**
- **TESS-SPOC PDCSAP**, all seven sectors (`indep-out.txt`): 11.50, 11.62, 11.25, 11.54, 10.93, 11.07, 11.78 ppt (±0.2–0.37). SPOC-SAP gives 10.60–11.36 ppt.
- **TASOC s026 FLUX_RAW** (`tasoc-out.txt`): 10.88 ± 0.48 and 10.18 ± 0.64 ppt.
- **TESS-SPOC TPF difference images**, s40/s53/s80 (`tpfdiff-out.txt`): the target is the best single-star fit, with χ² 1.7–2.4× lower than any neighbour. Implied own dip 8.9–9.7 ppt.
- **Own centroid-shift test** (`censhift.py`, all seven TPFs, `censhift-out.txt`):
  - Measured in-eclipse shifts are all ≤ 1.5 mpix (typical ±0.2–0.8).
  - Each neighbour would produce 20–50 mpix and is excluded at χ² 840–50,000 per sector.
  - The target hypothesis gives χ² 0.9–66. The residual comes from a 0.1–0.3 px WCS/aperture offset of c0, not from a neighbour.
- **Batch diffimg** (s40): peak on target, offset 3.0".
- **Neighbours** (fractional dip each would need = 11.4 ppt × 10^(0.4 Δm)):
  - G 14.78 @ 88": 260 ppt
  - G 14.81 @ 89": 265 ppt
  - G 16.23 @ 48": 990 ppt
  - G 16.36 @ 44": > 100% (impossible)
  - All excluded by the centroids anyway.

**5. Physics** (`phys-out.txt`, `transfit-out.txt`, `hbtest-out.txt`)
- f(M) = 0.0293 Msun. With M1 0.98, m2(i = 90°) = 0.378 Msun (an M dwarf, TESS-band light ratio about 0.5%). a = 28.0 Rsun.
- Separation at conj A (ν 347°) is 0.753a (central T14 would be 7.4 h). At conj B (ν 167°) it is 1.240a.
- The observed 3.12 h chord implies i ≈ 84.1°. At B the projected separation is 3.55 Rsun against R1 + R2 = 2.38 Rsun, so **B misses by 1.2 Rsun**. That matches the absent secondary.
- **Limb-darkened eclipse fit** of the stacked short-cadence primaries, with v_t fixed at 15.34 Rsun/d:
  - R1 = 1.50–1.75 Rsun (1σ). The TIC R1 of 1.96 is disfavoured by Δχ² +62.
  - The k–b graze is degenerate: R2 0.18–0.67 Rsun at b 0.90–1.24. That range includes the R2 ≈ 0.38 an 0.38 Msun dwarf would have.
  - The smaller R1 agrees with Gaia GSP-Phot logg 4.08, which gives R ≈ 1.5 Rsun at 0.98 Msun. The tension is with the TIC luminosity radius. It is worth a footnote, not a strike.
- **Heartbeat check** (conj A is 13° before periastron and e = 0.25, so this is required; `hbtest.py`, `hbtest.png`):
  - Kumar et al. tidal model with free e (±3σ), t_peri (±0.6 d), i and φ against the trapezoid, same per-event quadratic baselines, 13 windows of ±1.2 d.
  - Best heartbeat: χ² 6734. Trapezoid: χ² 1343. **Δχ² = +5391 for the trapezoid.**
  - Heartbeat plus trapezoid gives depth 11.17 ppt and improves χ² by only 3.4.
  - Physical tide scale is (m2/M1)(R1/r_p)³ = 0.31 ppt, spread over the ~54 h periastron passage. The observed event is 11.4 ppt in 3.1 h.
  - **Not a heartbeat.**
- **Which star is in front:** conj A, so the M dwarf grazes across the G subgiant. The companion's occultation at B does not happen.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers:
  1. P +0.03σ from Gaia, with the eclipse on Gaia conj A at −0.14 to −0.29σ.
  2. Heartbeat excluded by Δχ² 5391.
  3. Three pipelines agree: QLP 11.4, TESS-SPOC PDCSAP 10.9–11.8, TASOC 10.2–10.9 ppt. The centroids exclude every neighbour at χ² ≥ 840.
- **Paper row fixes:**
  - n_events 9 → **12**. QLP s025/s026 add three; the batch sapdepth only used s040 onward.
  - depth 10.4 → **11.4 ppt** (trapezoid).
  - P → **14.748239(11) d**.
  - dphi sign is **−0.0045** (eclipse earlier than conj A), not +0.004.
  - Primary-only system; no secondary (< 0.3 ppt, 3σ), as the geometry predicts.
- **Next primaries** (±2 min): BTJD **4402.288, 4417.036, 4431.784**.
- **Conj B** (no eclipse expected; ±0.16 d): BTJD 4409.12, 4423.87, 4438.62.
- **To settle further:** a spectroscopic radius or logg for the primary (TIC 1.96 vs eclipse 1.5–1.75 Rsun), and an RV epoch at conj A.
