# TIC 329314665 (TYC 9000-1011-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.45, P 3.77334 d, 8.3 ppt, 34 events, dphi +0.012, diffimg offset 7.53″ (the outlier).

## Verdict: CONFIRMED (grazing F + K-dwarf EB, the Gaia SB1 itself; the 7.53″ batch offset is a centroiding artefact in a crowded field)

**Deciding numbers**
- **Period and conjunction:** P = 3.7733403 ± 0.0000019 d from 33 primaries, against Gaia 3.773505 ± 0.000119 (−1.4σ). Mid-eclipse is −0.012 phase from Gaia conjunction A (companion in front), −0.3σ using the full covariance (corr(ω, t_p) = 0.9998, σ = 0.14 d). Conjunction B is excluded at 13σ.
- **Secondary eclipse:** phase 0.50016 ± 0.00024, depth 3.34 ± 0.14 ppt (SNR 25), present in all 7 sectors.
  - e cos ω = +0.0003 ± 0.0004; T14 ratio 0.99 ± 0.03 → e sin ω = −0.003 ± 0.017.
  - Gaia has e = 0.014 ± 0.030 (e cos ω +0.009, e sin ω −0.011) — consistent.
- **Localisation:** own PSF-fit difference images in 7 sectors (s11, s38, s64, s65, s99, s100, s101; several camera/CCD orientations).
  - The primary deficit lies 1.2–6.8″ from the target (median ~2.6″, about 0.12 px).
  - A fixed-position fit at the target is the best fixed position in 6 of 7 sectors for the primary and 7 of 7 for the secondary.
  - The only cheap host is the red G 14.19 (RP 12.94) star at 11.2″ W, which would need a 5.6% dip; it fits worse than the target by Δχ² +292 to +1659 in every sector.

**Archives (queried 2026-10-18)**
- cats.py r = 60″: no VSX, ASAS-SN, Prša, IJspeert or Kostov t2/t3/t4 rows. SIMBAD: TYC 9000-1011-1 [SB*] only.
- VizieR battery: nothing in WDS, SB9, Gaia DR3 vari_* (classifier, EB, summary), RAVE or GALAH. Gaia phot_variable_flag NOT_AVAILABLE.
- ExoFOP: no TOI, no CTOI, no notes. Web search on the TYC/TIC names: nothing.
- MAST: no SPOC or TESS-SPOC light curve or DV exists, so no SPOC TCE. Prior art: none.

**Eclipses and ephemeris** (QLP SAP, QUALITY==0, no trimming; events_329314665_pfix/sfix.txt)
- **Primary:** T0 = BTJD 3773.739862 ± 0.000333; O−C rms 3.2 min against a 2.4-min median error (χ²/dof 56.7/31; errors scaled). Folded depth 8.64 ± 0.12 ppt in s99–101 and 9.39 ± 0.14 ppt over all sectors. T14 = 2.30 h, T12 = 0.87 h: near-V, grazing.
- **Per-sector depths:** 7.95–10.6 ppt, varying with QLP aperture dilution (TIC contratio 0.61). Odd/even: 8.60 ± 0.16 vs 8.71 ± 0.15 ppt.
- **Secondary:** P = 3.7733276 ± 0.0000043 from 20 events, 2.7σ from the primary P (secondary timings noisier; not considered significant).
- **Systematics:** background change through events negligible; centroid shifts ≤ 0.004 px; no event core contains a QUALITY bit-32 dump. The one event near a listed systematic (s65 3090.76, 1 d from 3089.8) agrees with the rest.
- **Blind dip census:** nothing else deeper than 3 ppt at SNR > 5 once the eclipses are masked.

**Independence**
- TGLC s11: aperture 9.48 ± 0.26 ppt; PSF 6.49 ± 0.23 ppt. eleanor-lite s11: 10.69 ± 0.39 ppt. TARS s38/64/65: 8.56, 8.24, 7.83 ppt. Timing agrees with QLP to ≤ 4 min, and every pipeline shows the secondary (2.7–3.6 ppt).
- **Caveat on TGLC:** the TGLC files of the neighbours at 11.2″, 15.1″ and 23.0″ show the same dip with the same absolute flux loss (~37–56 e/s, equal to the target's) — the target's deficit leaking into overlapping 3×3 apertures and broad PSF fits 0.5–1.1 px away. TGLC confirms the signal but cannot localise it; localisation rests on the multi-sector PSF-fit difference images (loc_prim*, loc_sec*).
- **Neighbour table** (neighbours_out.txt, G < 17.5 within 120″, b = −3°): many stars could host 9 ppt by flux alone. Within 10″ only G 16.72 at 4.3″ comes close (needs 70% in RP, 116% in G); the difference-image fits disfavour it at Δχ² +119 to +635 in 5 of 7 sectors.
- **Why the batch 7.53″ is an artefact:** the batch number is a clipped-positive 5×5 centroid, pulled by noise in a field where the light centroid itself sits ~12″ off the target.

**Physics**
- f(m) = 0.0909 M☉. With M1 = 1.28 (TIC; R1 2.02, Teff 6400), m2(i = 90°) = 0.71 M☉ and a = 12.8 R☉.
- Central T14 would be 6.2 h; the observed 2.3 h needs a projected separation of 0.93 (R1 + R2), i ≈ 78.5°, so m2 ≈ 0.73 M☉.
- Depth ratio 0.386 implies T2 ≈ 4830 K, a K2–3 dwarf of ~0.75 M☉ — matching the mass function independently.
- A limb-darkened grazing model (R1 2.02, R2 0.74) gives 9.5 ppt at T14 2.6 h, consistent with 8.6–10.7 ppt and 2.3 h (a trapezoid underestimates T14 for a V shape).
- The deeper eclipse is at conj A, so the K dwarf is in front at primary eclipse.

**Changes to the paper row**
- Keep the row. P = **3.7733403(19)**.
- Replace the 7.53″ diffimg offset with "on target: PSF-fit deficit 1–7″, median 2.6″, 7 sectors; 11″ neighbour excluded, Δχ² ≥ 292".
- Add the secondary: 3.3 ppt at phase 0.5002.
- Undiluted depth 8–11 ppt by pipeline (contratio 0.61); quote ~9 ppt.

**Next eclipses (BTJD)**
- Primary (±0.6 min): 4252.9541, 4256.7274, 4260.5008, 4264.2741.
- Secondary (±3 min): 4254.8414, 4258.6147, 4262.3880, 4266.1614.

**What would settle it further:** a spectrum showing the K-dwarf lines (SB2), or a seeing-limited ground-based light curve, which resolves 11″ easily.
