# TIC 324273420 (TYC 8977-7461-1): per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19 (wave 3b). Batch row: G 11.02, P 3.91587 d, 14.7 ppt, 32 events, dphi +0.011, diffimg offset 3.59″ (peak on target).

## Verdict: CONFIRMED. This is an eccentric, grazing, double-eclipsing binary, and it is the Gaia SB1 itself. Both eclipses fall at their Gaia conjunctions, the secondary sits at phase 0.559, and a heartbeat model is excluded.

**Deciding numbers**
- **Both eclipse kinds land on Gaia's conjunctions.** The comparison is made at the Gaia epoch with the full covariance; corr(ω, t_p) = 0.994, so σ(conj) = 0.026 / 0.023 d.
  - Primary minus conj A: +0.009 d (+0.0023 phase, +0.35σ).
  - Secondary minus conj B: −0.003 d (−0.15σ).
  - Swapping the two attributions is excluded at 66–77σ.
  - Without the correlation the conjunction errors would be 0.146 / 0.132 d, about 6× larger.
- **Secondary eclipse:** 14.7 ppt (QLP fold), against 16.3 ppt for the primary. It sits at phase 0.55932 ± 0.00014 and is seen 38 times.
  - The exact Keplerian inversion gives e cos ω = +0.0932 ± 0.0002. Gaia gives +0.098 ± 0.017 (0.3σ), and the Gaia MC predicts a secondary phase of 0.5615 ± 0.011.
- **Period:** P(joint, both kinds) = 3.9158631 ± 0.0000005 d (formal; ±0.0000015 with the ETV scatter folded in). Gaia has 3.9157408 ± 0.0001487 (+0.8σ).
- **Heartbeat check:** periastron falls at phase 0.71, and the conjunctions are at ν = 117° (A) and 297° (B), so neither is near periastron. A Kumar-type heartbeat model fitted to the folded SAP, with e, periastron phase and i all free, runs off to e = 0.74 and still fits worse than two trapezoids by Δχ² = 5054 over 500 bins. It cannot produce the secondary at all.
  - A heartbeat term at Gaia's e and periastron, added on top of the eclipses, only absorbs the ~2 ppt out-of-eclipse ellipsoidal/periastron modulation. That modulation is itself physical (heartbeat.png).

**Archives (queried 2026-10-19)**
- cats.py r = 60″ (APPOINTMENTS_DATA set):
  - Nothing at the target in VSX, ASAS-SN, Prša, IJspeert or Kostov t2/t3/t4.
  - Nearby VSX entries are all faint field variables 17–53″ away: an RRC of G 19.7 at 17″, an L of G 18.6 at 19″, a VAR at 29″ and an L at 53″.
  - SIMBAD has only TYC 8977-7461-1 [SB*].
- VizieR battery: WDS, SB9, Gaia DR3 vari_classifier / veb / vartot / vst, Hipparcos, RAVE and GALAH all returned nothing. Gaia phot_variable_flag is NOT_AVAILABLE and RUWE is 0.92.
- ExoFOP JSON: no TOI, no CTOI, no notes, no files.
- Web search on the TYC/TIC names: nothing.
- MAST has TESS-SPOC (s10, 11, 37, 38), TGLC (s10, 11), eleanor-lite, TARS and T16 light curves, but no SPOC 2-min data or DV.
- Prior art: none.

**Eclipses and ephemeris** (QLP SAP, QUALITY==0, no trimming; events_324273420_p/s.txt)
- **Primary:** 33 events fitted (the s11 E12 fit is degenerate and gets no weight).
  - T0 = BTJD 3200.00630 ± 0.00037, P = 3.9158610 ± 0.0000015.
  - Per-event depth 14.3–19.3 ppt. T14 = 3.3–3.9 h (fold 3.48 h), T12 ≈ 1.3 h: grazing, U/V-shaped.
  - Sector means range from 14.9 (s100) to 17.9 ppt (s64); this follows QLP aperture dilution (contratio 0.70).
- **Secondary:** 38 events. T0 = BTJD 3315.75654 ± 0.00038, P = 3.9158664 ± 0.0000016. Depth 10.9–16.8 ppt, T14 3.4–4.4 h (fold 4.10 h), so it is longer than the primary.
- **Systematics:**
  - Background change through the events is tens to a few hundred e/s, random in sign.
  - Centroid shifts are ≤ 0.008 px.
  - No event is near a listed sector-wide systematic.
  - Only one event core contains a bit-32 dump (s38 E195, one cadence), and that event agrees with the rest.
- **Blind dip census** (eclipses masked ±0.12 d, 3.5-h box):
  - Nothing deeper than 6.1 ppt anywhere; nothing above 3 ppt in s99/s100.
  - Every 3–6 ppt hit is either within 0.33 d of an eclipse (mask-edge leakage of the 1-d median detrend) or a residual of the ~2 ppt out-of-eclipse modulation or an orbit edge.
- **ETV (new finding):** the O−C is curved and the curve is common to both eclipse kinds.
  - Season means for the primary: Y2 −3.3 ± 0.9, Y4 +4.2 ± 0.7, Y5 +1.4 ± 0.7, Y8 −1.5 ± 0.4 min.
  - The secondary moves in step with it.
  - A joint quadratic improves χ² by 155 (68 → 67 dof; χ²/dof is still 2.9).
  - TESS-SPOC SAP and PDCSAP independently show the same offsets: s10/11 −1.6 to −4.5 min, s37/38 +4.5 min. So this is not a QLP artefact.
  - Interpretation: likely light-travel time from a third body (a sin i ≳ 0.5 AU), or a period change. It is not resolvable with four seasons.
- **Possible apsidal motion (not claimed):** the secondary phase drifts from 0.55888 ± 0.00027 (Y2) to 0.55960 ± 0.00011 (Y8). That is P_sec − P_prim = 0.46 ± 0.09 s raw, about 3σ after error scaling, or roughly 0.2°/yr in ω.

**Independence**
| Pipeline / sectors | Primary depth (ppt) | Secondary depth (ppt) |
|---|---|---|
| TESS-SPOC SAP, s10/11/37/38 (smaller aperture) | 13.5–14.2 | 10.8–11.7 |
| TESS-SPOC PDCSAP, de-crowded (CROWDSAP 0.64–0.71) | 19.9–21.2 | 16.3–18.0 |
| TGLC s10 aperture | 18.5 | 15.2 |
| TGLC s10 PSF | 17.6 | 14.7 |
| TARS s64 | 16.2 | 13.8 |

- Timing in every pipeline matches QLP's to within a few minutes.
- **Undiluted depths:** about 18–21 ppt for the primary and 15–18 ppt for the secondary.
- **Localisation:**
  - The batch difference image (s38, 6 events) puts the deficit 3.59″ from the target with the peak on target (diffimg/diffrun-c4.jsonl). I did not re-derive it; nothing here contradicts it.
  - Neighbour table (neighbours_out.txt): Galactic plane (b = −0.7°), 257 Gaia sources within 60″. The cheapest hosts would need large dips: G 12.95 at 41″ needs 8.6%, G 14.62 at 22″ needs 40%, G 15.11 at 25″ needs 63%.
  - The decisive point is that both eclipses sit at the SB1's own two conjunctions and reproduce its e cos ω, which a background EB cannot do.

**Physics**
- f(m) = 0.0831 M☉ (K = 59.3 km/s, e = 0.110).
- With M1 = 1.19 M☉ (TIC; Teff 6193, logg 3.68, R1 2.62 R☉), m2 = 0.66–0.68 M☉ (i ≈ 77–80°) and a = 12.9 R☉. A central eclipse would last 7.8 h; the observed 3.5–4.1 h makes both eclipses grazing.
- **Which star is in front:** the deeper eclipse is at conj A, so the companion is in front at primary eclipse.
- **One-geometry fit** (geom2.py: numerical limb-darkened overlap, eccentric orbit, e cos ω fixed, fitting both T14 values and the undiluted depths). It fits at χ² ≈ 0 with:
  - R1 ≈ 1.9–2.0 R☉,
  - a K-dwarf companion (R2 0.8–0.9 R☉, L2/L1 0.03–0.06 in the TESS band),
  - e sin ω −0.04 to −0.12, against Gaia's −0.050 ± 0.017.
  - The "nearly equal" depths (ratio ~0.85) come from geometry: at B the separation is smaller, so b is smaller, and the primary covers 25–50% of the K dwarf, while at A only ~2% of the big star is covered.
- **Tension (flagged, not decisive):** the fit's R1 is ~25% below the TIC's 2.62 R☉. With R1 fixed at 2.62 the primary comes out too shallow (11 vs 18–21 ppt). Two systematics push in this direction: trapezoid T14 is biased low for V-shapes, and the TIC radius uses the DR2 distance (the DR3 parallax 2.20 mas makes it 5% smaller). A third light from the ETV body would also enter here.

**Changes to the paper row**
- Keep the row.
- Period: P = **3.9158631(15)** d (joint, both kinds; ETV scatter included).
- Primary T0 = BTJD **3200.0063(4)**.
- Add the secondary: 14.7 ppt QLP (15–18 ppt undiluted) at phase **0.5593**. e cos ω = +0.0932 agrees with Gaia.
- Depth: QLP 14.7–16.3 ppt diluted; undiluted ~18–21 ppt (PDCSAP/TGLC-PSF).
- Event count: 33 primaries + 38 secondaries measured in QLP (the ledger's 32 counts primaries only).
- dphi: +0.0023 from conj A at +0.35σ with full covariance (the batch's +0.011 used the 3.4-yr-extrapolated phase).
- Diffimg 3.59″: keep it, annotated "peak on target".
- Add the note: "common-mode ETV ±4 min (third body?)".

**Next eclipses (BTJD; ±6 min, dominated by the ETV, not by the period error)**
- Primary: 4335.6055, 4339.5214, 4343.4373, 4347.3531
- Secondary: 4337.7969, 4341.7127, 4345.6286, 4349.5444

**What would settle it further:** RVs that resolve the K-dwarf lines (SB2) would give the masses and fix R1. More TESS seasons, or ground-based minima timings, would characterise the ETV (an LTTE orbit) and the apsidal drift.

Files: overview.png, heartbeat.png, events_324273420_{p,s}.{txt,png}, ephem_324273420_{p,s}.png, conj.py, season.py, etv_out.txt, geom2_out.txt, physics_out.txt, cats_out.txt, archives_out.txt, mast_inventory.txt, neighbours_out.txt, census_out.txt, census_dist.txt, exofop.json, next_eclipses.txt. Second-pipeline FITS are in C:\Home\sky\data\qlp-sb-p20-60\pervet-324273420\.
