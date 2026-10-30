# TIC 93103821 (BD-17 691, TYC 5873-244-1, Gaia DR3 5102568177264285824): per-object vet
Opus 5.5 subagent for Fable 5, wave 3b, 2026-10-19. Batch row: G 11.03, P 1.63502 d, 13.5 ppt, 13 events, dphi +0.022.

**VERDICT: CONFIRMED.** A grazing, near-circular F + K-dwarf eclipsing binary. Both eclipses are present: the primary eclipse (15.5 ppt) falls at Gaia conjunction A, and the secondary (5.8 ppt) falls at phase 0.50000 ± 0.00025.

**Star and orbit**
- G 11.03, Tmag 10.60. TIC: Teff 6247 K, R 1.29, M 1.21, d 250 pc. Gaia GSP-Phot: 6056 K, logg 4.21. RUWE 1.12.
- Gaia NSS SB1 (full row with corr_vec from the archive): P 1.6350635 ± 0.0000198 d, e 0.015 ± 0.019, ω 180 ± 49°, K1 88.28 ± 1.74 km/s, significance 50.6.
- f(M) = 0.1165 Msun. m2(i=90°) = 0.71–0.77 Msun for M1 1.05–1.21; a = 7.1–7.3 Rsun.

**1. Archives**
- `cats.py --r 60`: VSX and ASAS-SN none. SIMBAD: BD-17 691 [SB*] only. Prša, IJspeert and Kostov t2/t3/t4: none.
- SB9 and WDS none (VizieR). Gaia vari_summary and vari_eclipsing_binary empty. ExoFOP: no TOI or CTOI, no imaging or spectroscopy.
- Batch ebcats: none. Web search on BD-17 691, TYC 5873-244-1 and TIC 93103821: nothing. Not previously catalogued as an eclipsing binary.

**2. Eclipses** (QLP SAP, QUALITY==0, no trimming; s004 has 30-min cadence, s031 10-min)
- **Primaries:** 24 measured — 10 in s004 and 14 in s031; the row says 13. Every one has S/N 10–48.
  - Per-sector depths: s004 13.7 ± 0.13, s031 15.35 ± 0.11 ppt.
  - Supersampled trapezoid: s031 15.55 ppt, T14 1.44 h, T12/T14 0.4 (V-ish, so a graze). s004 still gives 13.85 even with 30-min smearing modelled. The s004/s031 difference is therefore aperture dilution between sectors; SPOC shows a smaller version of it (14.6 vs 15.3).
  - Odd 14.48 ± 0.11 vs even 14.90 ± 0.12 — this reflects the sector mix, not an odd/even effect.
- **Secondary:** 20 events, all S/N > 3; phase-0.5 control gives 4.98 ± 0.08 ppt. Supersampled fit: 5.77 ppt, T14 1.39 h, at phase 0.50000 ± 0.00025. Depth ratio sec/pri 0.37.
- **Systematics:**
  - No event within 0.5 d of a listed sector-wide systematic time. Three primary windows contain a bit-32 cadence; their depths match the rest.
  - In-out SAP_BKG change is −1.3 ppt-equivalent (the wrong sign to fake a dip). Background regression implies ≤ 0.007 ppt.
  - Centroids dX −0.04 ± 0.12, dY −0.10 ± 0.12 mpix.
- **Controls:** phases 0.125/0.25/0.375/0.625/0.75/0.875 all within ±0.22 ppt.
- **Census:** 45 dips at S/N ≥ 4 — 22 on the primary, 20 on the secondary, and 3 others of 0.9–7.3 ppt at single epochs. No off-ephemeris dip at or above half the primary depth except one 7.3 ppt S/N 4.2 blip (s031 2163.52, phase 0.185), a single cadence group.
- **Out of eclipse** (both eclipses masked): ellipsoidal cos2φ −1.8 to −2.2 ppt (minima at conjunctions, the correct sign); reflection-like cos φ −1.1 / −3.2 ppt (brighter at the secondary); sin terms disagree between sectors (30-min s004 systematics).

**3. Ephemeris and Gaia**
- P = 1.6350307 ± 0.0000004 d, T0 = 1868.90788 ± 0.00009 BTJD. χ² 62/22 (errors scaled ×1.68). O−C rms 0.6 min.
- vs Gaia P: −0.000033 d = −1.66σ.
- Gaia conjunctions (MC 20k draws with corr_vec): the primary sits on **conj A** at −0.88 h (s004, −3.0σ) and −1.18 h (s031, −2.6σ), i.e. −0.023/−0.030 in phase. Conj B is 0.49 phase away (31–45σ).
  - The ~3σ timing offset is the only tension. With e consistent with zero, Gaia's ω (±49°) and t_peri are nearly degenerate, so the propagated conjunction error (0.29–0.46 h) is probably underestimated. It is not a sign of misattribution: the secondary sits exactly at 0.5, and the deeper eclipse is the F star eclipsed, as conj A requires.
- Photometric e cos ω = (π/2)(φ_sec − 0.5) = +0.0000 ± 0.0004 vs Gaia −0.0136 ± 0.014 (1.0σ). e sin ω ≈ (T2 − T1)/(T2 + T1) = −0.009 ± 0.018 vs Gaia 0.000 ± 0.017. Circular, consistent with Gaia.
- Batch dphi sign: the eclipse precedes Gaia conj A, so dphi = **−0.022** (c4-vetsum has −0.022; the ledger's +0.022 is the wrong sign).

**4. Independence**
- **TESS-SPOC PDCSAP:** s4 14.58 ± 0.11, s31 15.29 ± 0.09 ppt. SPOC-SAP: 14.52 and 15.20.
- **TARS:** s4 14.45, s31 15.42. **TGLC s4:** PSF 12.48 ± 0.28, aperture 16.83 ± 0.19. Every pipeline sees it.
- **SPOC TPF difference image, s31 (14 events):** peak loss on pixel (4,5), S/N 48. Loss-weighted centroid (5.18, 4.64) vs target (5.02, 4.52). Single-star fit on the target implies a 12.4 ppt own dip.
- Batch diffimg s31: deficit-light 0.22″, peak on target.
- **Neighbours:** none in Gaia DR3 brighter than G 17 within 90″. The brightest within 60″ is G 19.0 at 21.9″, which would need a 15.5 × 10^(0.4 × 7.97) ≈ 24,000 ppt dip — impossible. Dilution is excluded.

**5. Physics**
- With M1 1.05–1.21 and R1 1.15–1.29: central T14 3.3–3.5 h vs 1.42 h observed. Chord fraction 0.40–0.43, b ≈ 0.91 (R1+R2), i ≈ 75–76°.
- e ≈ 0, so both conjunctions graze identically. The companion (K dwarf, R ~0.75–0.8) transits the F star at A (primary eclipse) and is occulted at B.
- Uniform-disc predictions: transit 15–19 ppt (limb darkening lowers a graze) vs 15.5 observed; occultation 7.3–8.5 vs 5.8 observed.
- The depth ratio 0.37 implies a TESS-band surface-brightness ratio for T2 ≈ 4700 K, which matches a 0.71–0.77 Msun K dwarf.
- Ellipsoidal predicted 2.9–4.4 ppt (R1 1.05–1.29) vs 1.8–2.2 observed. That is a factor ≤ 2 and favours the smaller Gaia-like R1.
- One consistent geometry. **Heartbeat check:** e = 0.015 ± 0.019, so there is no periastron tide to mimic; the events are 1.4-h eclipses at both conjunctions.

**6. Verdict and predictions**
- **CONFIRMED.** Deciding numbers:
  1. Both eclipses are present — 24 primaries at 15.5 ppt and 20 secondaries at 5.8 ppt — with the secondary at phase 0.50000 ± 0.00025, matching Gaia's e ≈ 0.
  2. P is −1.7σ from Gaia and the primary sits on conj A.
  3. QLP, SPOC, TARS and TGLC agree, the SPOC difference image peaks on target, and there is no neighbour brighter than G 17 within 90″.
- **Paper row fixes:**
  - n_events 24 primaries (+ 20 secondaries), not 13.
  - Depth 15.5 ppt (10-min s031; 13.7–13.9 in 30-min s004 QLP), not 13.5.
  - Add a secondary of 5.8 ppt at φ 0.5000.
  - P 1.6350307(4).
  - dphi −0.022 (sign).
- **Next primaries** (±1 min): BTJD 4401.5705, 4403.2055, 4404.8405.
- **Next secondaries** (±1 min): BTJD 4402.3880, 4404.0230, 4405.6580.
- **To settle further:** a light-curve model with limb darkening (b, k, surface-brightness ratio) on 2-min or 200-s data, and an SB2 spectrum to see the K dwarf and resolve the ~1 h Gaia conjunction offset.
