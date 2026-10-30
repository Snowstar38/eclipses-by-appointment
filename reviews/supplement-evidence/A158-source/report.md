# TIC 268342242

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent). Batch row: G 11.08, P 14.62018 d, 121.7 ppt, 10 events, dphi +0.012, diffimg offset 2.23" (peak not on target, s7).

TYC 8142-243-1, Gaia DR3 5493180643792180352, G 11.08, Teff 6129 K (TIC; Gaia GSP-Phot 5827 K), R 1.92 R☉, contratio 0.055. Gaia SB1: P 14.621257 ± 0.001851 d, e 0.2181 ± 0.0107, ω 264.45 ± 2.77°, K1 39.06 ± 0.47 km/s, significance 83.

## Verdict: **CONFIRMED.** The target is a detached, eccentric EB with both eclipses, on Gaia's orbit, and the difference-image flag is an artefact.

Deciding numbers:
- **Event count.** This is not a 2–3-event detection. The diffimg sector s7 alone holds 2 primaries and 1 secondary. In total there are **13 measured primaries** (9 fully covered and 4 partial) and **14 secondaries** (13 full and 1 partial), from 9 QLP sectors. Three more primary epochs and one more secondary fall only in flagged cadences.
- **Gaia orbit.**
  - P: TESS 14.6202005 ± 0.0000021 d vs Gaia 14.621257 ± 0.001851 d, −0.57σ.
  - Primary timing: at the Gaia epoch the primary is −2.10 h = −1.28σ from conjunction A.
  - Secondary timing: at the Gaia epoch the **secondary is +0.01 h = 0.0σ** from conjunction B (predicted 391.3802 ± 0.054, TESS 391.3807).
  - Phase separation 0.4924 vs Gaia 0.4863 ± 0.0069 (+0.9σ). That gives e cos ω = −0.0117 ± 0.001 (exact Sterne relation) vs Gaia −0.021 ± 0.011 (+0.9σ).
  - With Gaia's e and ω fixed, the four measured durations (T14 / T23 at A and B) are reproduced to χ² = 0.72. Freeing e sin ω gives −0.225 vs Gaia's −0.217 ± 0.011 (0.7σ).
- **Attribution.**
  - Flux budget: every Gaia neighbour within 90″ would need an eclipse of **≥ 206%** to make the 122-ppt primary (the brightest is G 14.15 at 56″). Only the target can host it.
  - The VSX/SIMBAD EB at 29″ (Gaia DR3 5493180536415078656, G 16.80, P 0.2452 d) would need more than 1000%.
  - **The SPOC DV report (TESS-SPOC s56–s69) independently puts the eclipse on target.** TCE 1 (P/2 = 7.31007 d fold, 33 ppt) has a difference-image offset from the TIC position of **4.4 ± 3.8″ (1.2σ)**.
  - The same DV report puts TCEs 2 and 3 (0.2453 d, 0.8 ppt) at 28.8 ± 2.8″, which is the 29″ contact EB. So that machinery does separate sources here.
  - My own difference images cover 16 products (TESScut s7/s88/s89; TESS-SPOC TPFs s7/s8/s9/s34/s35/s61/s62; primaries and secondaries separately). The deficit centroid lies **0.4–3.6″ from the Gaia target in 15 of 16**, and 5.1″ in the single-event tpf s9 primary. It is always closer to the target than the light centroid (1.8–7.4″ off, pulled by the box pedestal). The fractional loss at the target pixel is 95–124 ppt for the primary and 25–35 ppt for the secondary.
- **Physics.**
  - f(m) = 0.0839 ± 0.0030 M☉, so m2 ≈ 0.65 M☉ for M1 = 1.16 (0.60–0.71 for M1 1.0–1.35); a = 30.7 R☉.
  - The duration solution gives R1 1.76 R☉ (TIC 1.92 ± 0.09), k 0.30 (R2 0.53 R☉), i 88.3°, b_A 0.62 and b_B 0.40, so the secondary is a total occultation.
  - The depth ratio of 0.264 implies a surface-brightness ratio of about 0.3, so T2 ≈ 4300 K. That is what a 0.65 M☉ K dwarf should be.
  - A 12.5% primary from a K1 = 39 km/s orbit is fully self-consistent.

## What was done
1. **Archives** (`cats-out.txt`, `gaiatap-out.txt`): cats.py --r 60 found only the VSX "E" star at 29″ (above).
   - No ASAS-SN entry, and the target is not in Prša+2022, IJspeert+2024 or Kostov+2025.
   - SIMBAD has the target as SB*; its only bibcode is Gaia DR3 NSS.
   - Gaia vari tables: none. ExoFOP: no TOI or CTOI, no spectra or imaging. The web search found nothing.
   - The SPOC DV report (`dvr.xml` in `sky\data\qlp-sb-p20-60\pervet-deep-268342242\`) is a pipeline TCE, not a catalogue entry.
2. **Measurement** (`measure.py` with W 0.6 d, a quadratic baseline and a 7-point supersampled trapezoid for the 30/10-min FFIs; `events_pri/sec.json/png`; the per-epoch ledger `partial.py` → `partial-out.txt`).
   - Primary: T14 **9.14 h**, ingress 0.36 of T14, QLP depth 120–128 ppt (per-sector aperture).
   - Secondary: T14 **6.33 h**, ingress 0.26, 30–34 ppt.
   - The ledger gives, per epoch, the coverage fraction for QUALITY == 0 and for all cadences, the flag bits, the baselines on each side, and the depth with and without flagged cadences (changes ≤ 6 ppt).
   - Background gate (unit-free regression): at most 0.73 ppt.
   - Blind census: every dip deeper than 8 ppt at SNR > 7 is a primary, a secondary, or a baseline-window wing of one. There is no third family.
   - The broad 1–2-d dips in s61 (2963–2964, 2975–2976) are scattered-light systematics, not eclipse-shaped.
3. **Ephemerides** (`ephem.py`, `ephem-pri-out.txt`, `ephem-sec-out.txt`, `oc_pri.png`, `oc_sec.png`):
   - Primary: χ²/dof 1.48, O−C rms 0.50 min.
   - Secondary: P 14.6202157 ± 0.0000041, T0 2730.61517 ± 0.00022, χ²/dof 1.16, rms 1.17 min.
   - P_sec − P_pri = +1.3 s/cycle (3.3σ). This is possibly slow apsidal motion and is unconfirmed.
4. **Second pipeline** (`indep.py`, `indep-out.txt`): TESS-SPOC PDCSAP (crowding-corrected, CROWDSAP 0.93–0.94) gives primary depths **126.5 / 125.4 / 126.4 / 119.0 ppt** (s7/8/9/61) and secondary depths **33.1–33.3 ppt** (30.7 in s61). Times agree with QLP to under 1 min, and MOM_CENTR shifts are small.
   - Difference images: `pixfit2.py`, `pixfit2-out.txt`, `pixfit2-summary.txt`. The Gaussian-PSF variant (`pixfit.py`, `pixfit-out.txt`) is unusable here: 2 events per product on a bright star.
5. **Physics:** `physics.py`, `physics-out.txt`.

**Why the batch flag fired.** 2.23″ is about 0.1 px of box-centroid systematics; my box centroids show the same 1–3″ scale. With n_possible = 0 by flux budget, and the SPOC DV offset at 1.2σ, it was a flag in name only.

## Next eclipses (BTJD)
- Primary (~125 ppt, 9.1 h): 4346.2565, 4360.8767, 4375.4969, 4390.1171, 4404.7373 (±0.4 min).
- Secondary (~33 ppt, 6.3 h): 4338.8389, 4353.4591, 4368.0793, 4382.6995, 4397.3198 (±0.7 min).

## What would settle it further
- An RV pair, to obtain K2 and absolute masses. This is a clean double-eclipse system with total secondaries, so it is a good benchmark candidate.
- A limb-darkened joint fit for k, i and R1.
- More sectors, to test the 3.3σ primary/secondary period difference (apsidal motion).

## Row fixes for the paper table
| field | batch row | per-object value |
|---|---|---|
| P (d) | 14.62018 | **14.6202005 ± 0.0000021** (secondary ephemeris 14.6202157 ± 0.0000041) |
| T0 (BTJD) | 1495.3175 | **2840.37583 ± 0.00012** (primary); secondary T0 2730.61517 ± 0.00022 |
| depth (ppt) | 121.7 | QLP 120–128 (median ~124); **PDCSAP 119–126.5 (≈125 dilution-corrected)** |
| secondary | — | **33 ppt** (PDCSAP 30.7–33.3) at phase **0.4924**; total occultation |
| duration | 6.3 h (box) | **primary T14 9.14 h** (flat 2.6 h); **secondary T14 6.33 h** (flat 3.0 h) |
| events | 10 (2 in the diffimg sector) | **13 primaries (9 full + 4 partial) + 14 secondaries (13 full + 1 partial)**; 3 primary and 1 secondary epochs only in flagged cadences |
| conj. offset | +0.012 | primary −1.28σ from conjunction A; secondary 0.0σ from conjunction B at the Gaia epoch |
| diffimg flag | 2.23″, peak not on target | **artefact: on target.** No neighbour can make the dip (needs ≥ 206%). SPOC DV offset 4.4 ± 3.8″. Own deficit centroids 0.4–3.6″ (15/16). |
| note | — | K-dwarf companion: m2 ≈ 0.65 M☉, R2 ≈ 0.53 R☉, T2 ≈ 4300 K; i 88.3°. TESS e cos ω −0.012, e sin ω −0.225. SPOC TESS-SPOC TCE exists (s56–s69 DV, at P/2). |
