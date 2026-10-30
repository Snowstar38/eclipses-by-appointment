# TIC 309861809 (TYC 8925-649-1): adversarial check

Checker: Opus 5.5 subagent, 2026-10-21, resuming the 2026-10-20 checker killed by a usage limit. The file tool refused REPORT.md; this is the checker's full final-message text, saved by Fable 5.1. `report.txt` is the checker's own short version; `progress.md` has every number.

**Verdict: CONFIRMED.** Eclipses of one kind only (the companion transiting the star Gaia measured, at conjunction A), on this star. Seven full events plus one ingress, 1.0–1.1% deep, lasting 9.1 h, grazing. The missing secondary is expected from the orbit. VSX should add EA to the existing ROT rather than replace it.

**Archives**
- VSX lists ASASSN-V J082704.63-613929.2 as ROT, P 72.82 d (amplitude 0.09 in g).
- SIMBAD lists it only as a spectroscopic binary (SB*).
- Gaia: no variability or eclipsing-binary entry.
- Not in SB9, WDS, or ExoFOP (no TOI or CTOI), nor in the eclipsing-binary catalogues. A web search found nothing.
- Rerunning `cats.py` gave byte-identical output.

**A-eclipse times (BTJD)**

| Sector | Time | Error (d) | Note |
|---|---|---|---|
| s35 | 2272.5966 | ±0.0013 | |
| s37 | 2310.9820 | ±0.0021 | QLP flags the whole event |
| s62 | 3001.9347 | ±0.0048 | QLP flags the whole event |
| s63 | 3040.3213 | ±0.0038 | QLP flags the whole event |
| s68 | 3155.4813 | ±0.0030 | QLP background problem; SPOC is clean here |
| s89 | 3731.2698 | ±0.0013 | |
| s90 | 3769.6549 | ±0.0016 | |

- In every sector: T14 8.9–9.6 h, ingress 3.3–3.9 h, depth 0.97–1.12%.
- The s10 ingress lands exactly on the predicted 1581.6464 (Δχ² 2277).
- Other stars on the same detectors show nothing (median −0.06% to +0.07%).
- The blind dip search is clean apart from sector-edge ramps. A deep "dip" at s61 2974.87 is flagged scattered light that also appears in 93 other stars.
- Several events sit next to data gaps, but s90 is mid-orbit and clean. All seven times fit one linear ephemeris to 2.2 min rms over 1500 days, which rules out gap artefacts.

**Ephemeris**
- **T0 = 3769.65585 ± 0.00099 BTJD, P = 38.386132 ± 0.000039 d** (χ² 2.29/5).
- P differs from Gaia's by −0.0066 d (−1.17σ). That accounts for the claimed −1.1σ offsets; at Gaia's own epoch the eclipse ephemeris matches Gaia's A to −0.09σ.

**Secondary search at B** (Gaia phase 0.7626 ± 0.006; searched phases 0.70–0.83 with durations of 6, 9 and 12 h)
- Strongest signal S/N 2.4, i.e. nothing; 3σ upper limit 0.024% (worst case 0.05%).
- A blind scan over all phases peaks at S/N 3.9.
- With only one kind of eclipse, e cos ω and e sin ω cannot be measured, so Gaia's e = 0.433 and ω = 11.35° are adopted.

**Independent checks**
- TESS-SPOC SAP: s62 3001.9298, s63 3040.3257 (unflagged cadences), s68 3155.4778 (unflagged, 0.97%).
- TARS: s35 2272.5969, s37 2310.9828, s62 3001.9393, s63 3040.3188, s68 3155.4826, s89 3731.2692, depths 0.88–1.20%.
- My own TESScut photometry: s90 3769.6546 (1.10%) and s89 3731.2696 (1.05%).
- Difference images: the lost light is centred 0.22 px (s90) and 0.39 px (s89) from the target.
- Neighbours:

| Neighbour | Separation | Would need | Verdict |
|---|---|---|---|
| G 14.68 | 36.3" | 31% | Its pixel dims only 0.4–0.5%, against 1.2% on the target |
| G 16.72 | 8.3" | 203% | Impossible |

**Physics**
- Mass function f(M) = 0.1524 M☉. Companion mass at i = 85° is 0.79 / 0.87 / 0.95 / 1.02 M☉ for a primary of 1.0 / 1.2 / 1.4 / 1.6 M☉; separation 58–66 R☉.
- My model, with Gaia's e and ω fixed, gives inclination 84.4–86.0° and primary radius 0.058–0.065 a. That is 3.5–4.1 R☉, which agrees with the TIC's 3.77 R☉.
- The companion-to-primary size ratio is not pinned down (0.11–0.28). The best fit, 0.275, means a companion of about 1.1 R☉, which matches a ~0.9 M☉ dwarf.
- **Why no secondary:** the two stars are 1.186× farther apart at B than at A. Measured against the sum of the radii, the sky separation at B is 0.97–1.05 across the model family:
  - the physically matching solutions (size ratio 0.15 or more) miss entirely at B;
  - the small-companion solutions graze at most.
  - So a secondary below 0.03% is predicted.
- At A the companion passes in front of the subgiant.
- A 1% eclipse cannot produce VSX's 72.8 d, 0.09-mag variation, so that is probably real rotation of the subgiant. Hence ROT+EA.

**Next predicted times (BTJD)**
- **A eclipses:** 4345.4478, 4383.8340, 4422.2201, 4460.6062, 4498.9924 (±0.0016)
- **B, where no eclipse is expected:** 4336.33, 4374.72, 4413.10, 4451.49, 4489.88 (±0.23)

**What would settle it further**
- High-cadence photometry of the 4345.45 or 4383.83 eclipse to break the size/inclination degeneracy.
- Deep photometry at B (e.g. 4374.72) to test a graze of 0.03% or less.
- Gaia DR4 epoch RVs to refine e and ω.
- An ASAS-SN/VSX revision to ROT+EA with this ephemeris.
