# TIC 197484019 (TYC 3619-1706-1): adversarial check

Checker: Opus 5.5 subagent, 2026-10-21, resuming the 2026-10-20 checker killed by a usage limit. The file tool refused REPORT.md; this is the checker's full final-message text, saved by Fable 5.1. `report.txt` is the checker's own short version; `progress.md` has every step checkpointed.

**Verdict: CONFIRMED.** It is a two-eclipse binary, the eclipses are on this star, and they fall at Gaia's period and conjunctions. The VSX type should change from ROT to EA.

**What changed from the claim**
- **Deep eclipse at Gaia conjunction B.** Four events, 7.1–7.3% deep, lasting 30.0 h in total. The 17.5 h in the claim was the width at half depth. The bottom is rounded, so the eclipse is partial.
- **The secondary is real.** A 0.3–0.5% eclipse sits at phase 0.5001 (Gaia conjunction A), seen in s17, s57, s76 and s84. The suspected s076 dip near 3380 is one of these, at 3379.98.
- **Why it was missed before:** the earlier fits looked at Gaia's predicted phase 0.512, which is 0.6 d away from where the eclipse actually is.

**Archives**
- VSX lists ASASSN-V J222216.80+514740.9 as ROT, P 49.65 d, at 0". ASAS-SN also gives ROT 49.655 d.
- SIMBAD lists it only as a spectroscopic binary (SB*).
- Gaia: no eclipsing-binary entry. The variability summary says VARIABLE, range 0.150 mag, skewed toward faint (as eclipses would make it), with no class assigned.
- Not in Prša, IJspeert or Kostov, SB9, WDS, or ExoFOP (no TOI or CTOI). A web search on its names found nothing.
- MAST has only QLP light curves (s16, 17, 56, 57, 76, 77, 83, 84).
- Rerunning `cats.py` gave byte-identical output to the earlier checker's.

**Deep eclipses** (trapezoid fits, stable across window 1.2–2.5 d, baseline order, and flagged or unflagged data)

| Sector | Mid-time (BTJD) | Error (d) | Depth | Note |
|---|---|---|---|---|
| s16 | 1745.662 | ±0.007 | ~7.0% | Egress is flagged during a background excursion, so all cadences were used |
| s56 | 2835.1828 | ±0.001 | 7.14% | T14 30.1 h, ingress 11.5 h |
| s77 | 3405.8875 | ±0.001 | 7.3% | |
| s83 | 3561.5374 | ±0.001 | 7.23% | |

**Shallow eclipses** (shape fixed to the deep one)

| Sector | Mid-time (BTJD) | Error (d) | Depth |
|---|---|---|---|
| s17 | 1771.659 | ±0.036 | 0.49 ± 0.07% |
| s57 | 2861.050 | ±0.038 | 0.46 ± 0.08% |
| s76 | 3379.981 | ±0.014 | 0.46 ± 0.04% (baseline on one side only, before a data gap) |
| s84 | 3587.409 | ±0.023 | 0.31 ± 0.05% |

- A blind scan over all phases has its strongest signal at phase 0.5015. Three sectors each peak on their own at 0.498–0.501.
- Stacks at four control phases give 0.00–0.04 ± 0.01%.
- Other stars on the same detectors show no matching dip at any of the event times (median −0.02% to +0.002% across 374–465 stars).
- A blind search for other dips found nothing above 1% apart from the four deep eclipses.

**Ephemeris**

| | T0 (BTJD) | P (d) | Fit |
|---|---|---|---|
| Deep alone | 2835.1829 ± 0.0015 | 51.88236 ± 0.00015 | χ² 5.5/2; O−C +12.5 (s16), −0.2, −2.1, +2.0 min |
| Joint, deep (B) | 2835.1830 ± 0.0021 | 51.88235 ± 0.00021 | |
| Joint, shallow (A) | 2861.1286 ± 0.025 | same P | phase 0.50008 ± 0.00048 after B |

- P differs from Gaia's by −0.36σ.
- Gaia's predicted times: B 2835.17 ± 0.85 (observed 2835.18); A 2861.77 ± 0.85 (observed 2861.05–2861.13, −0.8σ).
- e cos ω from timing is −0.0001 ± 0.0008 (Gaia −0.019 ± 0.012, 1.6σ).
- From my eclipsing-binary model, for the giant's ω: e sin ω = −0.0077 ± 0.0014 (Gaia −0.012 ± 0.012). So e ≈ 0.008 against Gaia's 0.026 ± 0.013, all within 2σ.

**Independent checks**
- No other pipeline exists in MAST, so I did my own photometry on TESScut cutouts.
  - Deep eclipses: s56 at 2835.1832 and s83 at 3561.535–3561.537, depth 6.1–6.7% (more dilution in my aperture), T14 30.0 h.
  - Shallow eclipses: s57 at 2861.006 (0.345%) and s84 at 3587.402 (0.243%).
- Difference images for s56, s77 and s83:
  - The lost light is centred 0.07–0.28 px (1.5–5.9") from the target.
  - The bright neighbour's pixel dims only 1.8–2.2%, against 6.2–7.1% on the target.
- Neighbours:

| Neighbour | Separation | Deep eclipse would need | Shallow would need | Verdict |
|---|---|---|---|---|
| G 11.98 | 36.6" | 11.6% | 0.69% | Excluded by the difference images |
| G 14.17 (VSX δ Sct) | 25.3" | 87% | — | Excluded by the difference images |
| G 15.03 | — | 191% | — | Impossible |

**Physics**
- Mass function f(M) = 0.4595 M☉, using Gaia K1 44.05 km/s.
- My two-sphere model gives:
  - inclination 80.6° and giant radius 0.149 a;
  - companion radius 0.031 a (range 0.021–0.038) and surface-brightness ratio 0.083;
  - the companion supplies 22–35% of the light in the TESS band;
  - both eclipses are partial, and a total-occultation fit is worse by Δχ² ≈ 140.
- Companion mass is 1.40 / 1.96 / 2.41 / 2.81 M☉ for a giant of 1 / 2 / 3 / 4 M☉. That gives a separation of 78–111 R☉, giant radius 11.7–16.5 R☉ and companion radius 2.5–3.5 R☉.
- **Which star is in front:**
  - At B (deep), the giant, which is the star Gaia measured, partly hides the companion.
  - At A (shallow), the companion crosses the giant's edge.
  - Equal durations and a depth ratio equal to the brightness ratio mean one geometry explains both.
- **Temperature:** the companion is about 12× (8–20×) brighter per unit area, so about 14,000 K for a 5383 K giant (11,000–19,000 K across plausible giant temperatures).
  - A late-B/B9 companion of 2–3 M☉ with a 3–4 M☉ giant fits roughly.
  - There is mild tension, because the companion is hot for the mass allowed. Not a refutation.
- The star is reddened (galactic latitude −4.6°), so the TIC temperature is uncertain.
- VSX's 49.65 d "rotation" is probably an alias of the eclipses plus slow variability in the light curve. That is not settled.

**Next eclipses (BTJD; today is about 4334.5)**

| Kind | E29 | E30 | E31 | E32 | E33 |
|---|---|---|---|---|---|
| Deep B (±0.005 d) | 4339.771 | 4391.654 | 4443.536 | 4495.418 | 4547.301 |
| Shallow A (±0.026 d formal) | 4365.717 | 4417.599 | 4469.481 | 4521.364 | 4573.246 |

The shallow eclipses' real timing scatter is about 1.5 h, and each eclipse lasts about 30 h.

**What would settle it further**
- A UV measurement or spectrum (GALEX NUV, Swift/UVOT, Gaia XP) to see the hot companion and pin its temperature.
- Photometry of the 4339.77 and 4391.65 deep eclipses, and of the 4365.72 shallow one.
- Gaia DR4 epoch radial velocities and photometry.
- A VSX revision: ROT → EA, P 51.88235 d, epoch BTJD 2835.1830, depths about 0.08 and 0.005 mag.
