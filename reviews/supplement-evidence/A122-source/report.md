# TIC 384525203 (TYC 3612-1132-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.68, P 4.05515 d, 3.0 ppt, 76 events, dphi +0.014.

**Verdict: CONFIRMED.** A grazing detached eclipsing binary on an evolved A star (Teff 7709, R 4.1 R☉) that is strongly ellipsoidal. Both eclipses are detected. Gaia SB1: P 4.055826 ± 0.000548, e 0.039 ± 0.046, K1 51.9 km/s.

**1. Archives**
- cats.py at r = 60″:
  - Nothing in VSX at the target. Within 60″: a ROT star at 46″, ZTF EW P = 0.27767 d at 49″, an SR at 53″. None has the 4.055-d period.
  - ASAS-SN: none. Prša, IJspeert, Kostov t2–t4: none.
  - SIMBAD: TYC 3612-1132-1 [SB*] only.
- Gaia DR3: no rows in vari_summary, vari_eclipsing_binary or vari_classifier. RUWE 1.12, duplicated_source true, ESP-HS type A.
- SB9 and WDS: none. ExoFOP: no TOI or CTOI.
- No separate web search was run; SIMBAD has nothing beyond the SB* entry. **New EB.**

**2. Eclipses** (raw SAP, QUALITY == 0; model is a per-orbit Legendre-2 plus 4 orbital harmonics fitted outside eclipse)
- Primary: 5.76 ± 0.13 ppt, total duration 3.22 ± 0.06 h, ingress 1.29 h, flat bottom 0.6 h (nearly V-shaped).
- Secondary: 3.39 ± 0.18 ppt, total duration 3.41 ± 0.09 h.
- Background is flat through the events. Folded in-minus-out background is +2.0σ at primary and −2.8σ at secondary; opposite signs can't produce two dips.
- Momentum-dump (bit-32) cadences: only 3, in s056 secondary windows.
- Depth by sector: primary 5.35–6.63 ppt, secondary 2.85–3.77 ppt.
  - Exception: s077 secondary 5.05 ppt (noisiest sector).
  - Exception: QLP s016 primary 11 ppt, on scattered-light ramps; TESS-SPOC s016 doesn't reproduce it.
- Blind census (3-h box, at least 2 ppt): 73 dips. 68 are eclipses; the other 5 all sit on s016/s077 ramps.
- The sector-systematic time s083 3564.5 overlaps one primary, which is a normal 5.0 ppt event.

**3. Ephemeris**

| | Events | T0 (BTJD) | P (d) | O−C rms |
|---|---|---|---|---|
| Primary | 35 | 2826.03683 ± 0.00076 | 4.055307 ± 0.000006 | 5 min |
| Secondary | 39 | 2827.98974 ± 0.0014 | 4.055285 ± 0.000010 | 10 min |

- Against Gaia's period: −0.95σ.
- Gaia conjunctions, using the ω–t_peri correlation (+0.999): conjunction A (primary eclipsed) is +0.031 ± 0.048 phase from the deep eclipse at the s016 epoch. The batch's dphi labels agree with this, because its t0 at 1741.251 is a secondary eclipse.
- e cos ω = −0.0289 ± 0.0006; Gaia gives −0.016 ± 0.055.
- e sin ω from the duration ratio comes out as +0.029. It isn't reliable for eclipses this grazing.

**4. Independence**
- TESS-SPOC s016 SAP: 4.86 ± 0.15 / 2.85 ± 0.16 ppt. PDCSAP: 6.10 / 3.49 ppt.
- Own TESScut s056 photometry, primary: 5.49 / 5.40 / 5.44 ppt at r = 1.0 / 1.6 / 2.5 px, so the depth does not change with aperture.
- s056 difference image: both eclipse kinds peak on the target pixel; the deficit centroid is within 1.7σ of the target.
- Per-sector centroids put the dimming source 1.4–6.7″ from the light centroid.
- Neighbours and the dip each would need: G 13.96 at 28.9″ needs 11.9%; G 14.34 at 38.4″ needs 16.7%; G 14.63 at 23.7″ needs 21.9%; G 14.84 at 46.4″ needs 26.7%. Anything fainter than G 16.3 would need more than 100%, including G 16.52 at 10.9″.
- None of the neighbours is a plausible source: centroids, aperture-invariance, and the eclipses landing on the SB1's own ellipsoidal minima all rule them out.

**5. Physics**
- Mass function f(M) = 0.0586 M☉. For M1 = 1.6–2.6, m2(i = 90°) = 0.67–0.90 M☉ and a = 14–16 R☉.
- Eclipses need i above about 70–72°. A central eclipse would last about 10 h; the observed 3.2 h means a strongly grazing chord.
- Ellipsoidal semi-amplitude: about 5.8 ppt undiluted, against a predicted 7–13 ppt × sin²i. That is consistent within the uncertainty.
- Beaming: +0.394 ppt observed, 0.39 ppt predicted, with the right sign.
- Which star is in front: at the deep eclipse (conjunction A) the companion crosses the A star's limb.
- Depth ratio 0.59: higher than a naive surface-brightness ratio would give for this companion. It is explained by the grazing-limb geometry plus irradiation from the 53 L☉ primary.

**6. Next eclipses** (BTJD)
- Primary: 4334.6109, 4338.6662, 4342.7215, 4346.7768 (±3 min)
- Secondary: 4332.5005, 4336.5558, 4340.6111, 4344.6664 (±6 min)
- What would settle it further: a joint ellipsoidal, beaming and eclipse light-curve model, which would give i and the light ratio.

**Paper row:** P = 4.0553 d (not the 2.03-d half period), depths 5.8 / 3.4 ppt, ellipsoidal (~9.6 ppt peak-to-peak) and beaming present, e cos ω −0.029. The "peak_on_target false" receipt is a half-period-box artefact, not an offset flag.
