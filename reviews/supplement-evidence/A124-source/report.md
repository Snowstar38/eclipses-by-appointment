# TIC 310162414 (TYC 3371-625-1, Gaia DR3 261968648300074752): per-object vet
Opus 5.5-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.75, P 4.55127 d, 3.5 ppt, 26 events, dphi +0.001, diffimg 2.34″.

## Verdict: CONFIRMED (on-target grazing eclipses in a near-twin SB2)

**1. Archives** (`cats-out.txt`, `archives-out.txt`)
- cats.py --r 60:
  - VSX: only Gaia DR3 261968747082052224 [ROT], P 0.596 d, at 49″ (a different star).
  - ASAS-SN, Prša+2022, IJspeert+2024, Kostov t2/t3/t4: none.
  - SIMBAD: TYC 3371-625-1 [SB*].
- Gaia DR3 has no vari_summary or vari_eclipsing_binary row.
- nss_two_body_orbit SB2:
  - P 4.551136 ± 7.4e-5, e 0.0025 ± 0.0092, ω 35.9 ± 145.7 (undefined at e ≈ 0).
  - K1 87.77 ± 0.85, K2 90.51 ± 0.85, RUWE 1.79.
- SB9, WDS and VizieR Gaia veb within 60″: none. ExoFOP: no TOI or CTOI. Web search on the TYC/TIC/Gaia names: no hits.
- MAST has QLP s19/59/73/86, TESS-SPOC s19/59/73, TEQUILA s19.
- Not previously catalogued as eclipsing.

**2. Eclipses** (`vet1.py`, `vet1-out.txt`, `events_310162414.png`; QLP SAP, q==0, untrimmed)
- 31 QLP events fitted; TESS-SPOC adds the s19 odd eclipses QLP lacked core points for (1817.05, 1821.60, 1826.14, 1835.26, 1839.80).
- Shape: median T14 2.45 h, T23 0.55 h, V-ish, consistent with grazing.
- Background z-scores are within ±2 except s086 3639.806 (+5.2). That event is in the orbit-start scattered-light ramp and is compromised.
- s086 3648.92 is 0.4 d from the listed 3649.3 systematic and has 10 flagged cadences, but it is on ephemeris.
- No bit-32 momentum dumps within 0.5 d of any event.
- Blind dip census: nothing else in s059 or s073. The s086 3641.3–3641.5 dips are inside a pre-gap ramp flagged 2^30 (`look_s086_3641.png`).

**3. Ephemeris**

| Kind | N | P (d) | T0 (BTJD) | O−C rms |
|---|---|---|---|---|
| Even | 21 | 4.551255 ± 2e-6 | 1819.32698 | 9.1 min |
| Odd | 10 | 4.551246 ± 5e-6 | 1819.33291 (half-integer epochs) | 5.2 min |
| Joint | 31 | 4.551256 ± 2e-6 (×3.4 for red noise) | 1819.32778 | — |

- Joint P vs Gaia: +1.6σ.
- Gaia's nominal conjunction B is at phase +0.007 of the even eclipses and A at −0.495. The Gaia period error alone grows to 0.009 phase by the TESS epochs.
- e cos ω = 0.002 ± 0.0014. The duration difference (2.35 vs 2.50 h) gives e sin ω ≈ 0.03 ± similar. Both are consistent with a circular orbit.
- SPOC minus QLP mid-times: −0.4 min median, 2.8 min rms.

**4. Independence** (`vet2-out.txt`)

TESS-SPOC (aperture 10–13 px, CROWDSAP 0.91–0.94):

| | Even | Odd |
|---|---|---|
| SAP depth (ppt) | 3.85 | 3.93 |
| PDCSAP depth (ppt) | 4.18 | 4.17 |

- Stacked centroid shift: −0.02 ± 0.03 and +0.01 ± 0.03 millipixel (30 events).
- Neighbours (G < 17): G 16.05 at 27″ needs 57%; G 13.90 at 41″ needs 7.8%; G 13.58 at 45″ needs 5.8%. All are excluded by the matching depths in two very different apertures plus the centroid null, and independently by the SB2 match.

**5. Physics** (`phys.py`)
- M1 sin³i = 1.356 and M2 sin³i = 1.315 Msun; a sin i = 16.04 Rsun.
- For ~1.5 Msun F stars: i ≈ 75°, a ≈ 16.6 Rsun, luminosity radius 2.16 Rsun each.
- b/(R1+R2) ≈ 0.96 reproduces T14 = 2.45 h, and the crude overlap depth is 2–3 ppt against 4.1 observed. This is consistent.
- Out-of-eclipse: ellipsoidal cos2φ = −1.14 ± 0.01 ppt (−1.13 / −1.16 / −1.08 per sector). No reflection or beaming asymmetry (< 0.15 ppt).
- Mild tension: the predicted ellipsoidal amplitude is ~2.5 ppt. ~30% third light would explain it (RUWE 1.79 allows it).
- The two kinds are interchangeable; each star is in front at one conjunction.

**6. Next eclipses** (BTJD, ±5 min)
- Even: 4336.1725, 4340.7237, 4345.2750, 4349.8262
- Odd: 4338.4481, 4342.9993, 4347.5506, 4352.1019

**Paper row:** keep it. Note: "SB2 twin (q 0.97); equal grazing eclipses at both conjunctions; ellipsoidal 1.1 ppt; TESS-SPOC confirms. Trapezoid depth 4.1 ppt."

**What would settle it further:** a light-curve model (i, R1, R2, third light) fitted jointly with K1/K2.
