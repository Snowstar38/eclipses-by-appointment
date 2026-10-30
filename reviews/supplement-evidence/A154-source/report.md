# TIC 375302184

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent). Batch row: G 11.18, P 2.54558 d, 27.4 ppt, 65 events, dphi +0.017, diffimg offset 9.7" (peak not on target, s93).

TYC 9075-1173-1, Gaia DR3 6445014184777521024, G 11.18, Teff 7060 K, R 1.50 R☉ (TIC). Gaia SB1: P 2.545525 ± 0.000084 d, e 0.307 ± 0.047, ω 288.3 ± 8.0°, K1 33.3 ± 1.8 km/s.

## Verdict: **CONFIRMED.** The target is an eclipsing binary on Gaia's orbit, and the difference-image flag is an artefact.

Deciding numbers:
- **Attribution.** I made my own per-pixel difference images from 8 independent sector products: TESScut s27, s67, s93, s101 and s104, plus TESS-SPOC TPFs s13, s27 and s67. Each pixel's flux around each eclipse is fitted with the same cubic-baseline + trapezoid model as the light curve, so the 3% pulsation is modelled per pixel. A Gaussian PSF calibrated on the out-of-eclipse image was then fitted to the deficit.
  - The deficit sits **0.24–1.59″ from the target in 7 of 8 products**. s93 gives 3.45″, but that fit has a PSF σ of 0.98 px and χ²/dof 2.4, so the offset is a PSF-model systematic. Every offset is below 0.17 px.
  - Putting the eclipse on the only neighbour that could host it is rejected in every sector, by Δχ² = +124 (s101), +1318 (s93), +1834 (s104), +4560 (s27), +5567 (s67), and +3120 / +10524 / +17210 in the TPFs. That neighbour is Gaia DR3 6445014253499167744: G 12.45, 33.3″ away, needs an 11% eclipse. It is also ASAS-SN SR P = 330 d and SIMBAD LP* with RV +277 km/s, a halo giant.
  - Every fainter Gaia star is worse, and any G ≥ 15 star would need an eclipse deeper than 100%.
  - The deficit flux is 32.4 ppt (median) of the PSF-fitted *target* flux.
- **Gaia orbit.**
  - P: TESS 2.5455862 ± 0.0000005 d vs Gaia 2.5455249 ± 0.0000843 d, **+0.73σ**.
  - Timing: the primary falls on Gaia conjunction A (companion in front) **+0.32 h = +0.20σ** from prediction at the Gaia epoch.
  - **Secondary eclipse detected:** 1.9 ± 0.24 ppt at phase **0.580 ± 0.003**, against the Gaia prediction of 0.563 ± 0.031 (+0.55σ).
    - It is 10.7σ above a look-elsewhere control: z std 1.26 over the 233 clear phases.
    - It is positive in all 9 sectors.
    - It gives e cos ω = 0.126 ± 0.006, against Gaia's 0.096 ± 0.046 (+0.7σ). TESS therefore confirms the eccentricity independently.
- **Physics.**
  - f(m) = 0.0084 M☉, so m2 ≈ 0.31 M☉ for M1 = 1.56 (0.28–0.34 for M1 1.3–1.8): an M dwarf.
  - The trapezoid geometry gives k ≈ 0.18, b_A ≈ 0.76, i ≈ 85.5°, and R1 = 1.29 R☉ (TIC 1.50) from T14 and the eccentric orbital speed at conjunction A.
  - That predicts a *total* occultation at B (b_B 0.42) lasting 2.1 h, observed 1.5–3 h.
  - The secondary depth implies T2 ≈ 3500 K, which is what a 0.3 M☉ dwarf should be.
  - A 3% primary eclipse with K1 = 33 km/s is exactly the self-consistent case: a ~0.23 R☉ dwarf transiting a 1.3–1.5 R☉ F star.

## What was done
1. **Archives** (cats.py --r 60 with APPOINTMENTS_DATA, Gaia TAP, SIMBAD TAP, ExoFOP JSON, a web search): see `cats-out.txt`, `gaiatap-out.txt`, `progress.md`.
   - VSX/ASAS-SN list the target as **ASASSN-V J191934.99-620008.1, type ROT, P = 0.884 d**. That is a type revision (the pulsation below), not prior art.
   - Neither star is in Prša+2022, IJspeert+2024, Kostov+2025 or Gaia vari_eclipsing_binary.
   - Gaia vari_summary flags the target as a short-timescale + MS oscillator (G std 0.034 mag, range 0.15 mag).
   - ExoFOP: no TOI or CTOI, no spectra; contratio 0.30. The web search found nothing on any of the star's names.
   - SIMBAD has the target as SB* from Gaia DR3; its other bibcodes are RAVE survey papers.
2. **Light curve** (`look.png`): the raw SAP flux carries a **±3% multiperiodic ~0.9-d beating pulsation** (γ Dor-like). It is the target's own, given Gaia's 0.034-mag scatter and that the neighbour is a 330-d SR.
   - The eclipses are superposed on it. I measured every covered event with a cubic baseline over ±0.25 d plus a trapezoid (`measure.py`, `events_W0.25_d3.json/png`).
   - That gives **74 primaries in 9 sectors** (13, 27, 67, 93, 94, 101–104). Global T14 = **3.16 h** (per-event 3.18 ± 0.15 h); ingress is 0.33 of T14, so the flat bottom is about 1.1 h.
   - Background, unit-free regression (`scan.py`): median fake signal +0.003 ppt. Only one event (s93 n861, already discrepant at 15.8 ppt with β = 3.5) has a large background term (13 ppt).
   - QLP centroid shifts in eclipse are a few mpx, as a 30%-contaminated aperture produces. TESS-SPOC MOM_CENTR shifts are ≤ 1.3 mpx.
   - Blind census: 71 of 95 distinct dips deeper than 8 ppt are the predicted primaries. The other 24 are 8–15 ppt at scattered phases during beat maxima (baseline failures). Nothing else of primary depth is present.
3. **Ephemeris** (`ephem.py`, `ephem-out.txt`, `oc.png`): 70 events give χ²/dof = 8, O−C rms 1.8 min.
   - The sector-mean O−C wanders between −2.4 and +2.1 min. The same offsets appear in TARS, so the structure is in the data. It is either pulsation-induced timing noise or a slow ETV and is not resolved here.
4. **Second pipelines** (`indep.py`, `indep-out.txt`): TESS-SPOC SAP / PDCSAP for s13, s27 and s67, and TARS for s13, s27, s67, s93 and s94. Every eclipse is recovered at the same times.
   - The crowding-corrected PDCSAP depths are **31.6 / 32.2 / 33.0 ppt** (CROWDSAP 0.93 / 0.89 / 0.83).
   - Difference images: `pixfit.py`, `pixfit_*.png/json`, `pixfit-out.txt`, `pixfit-tpf-out.txt`.
5. **Physics:** `physics.py`, `physics-out.txt` (numbers above).

**Why the batch flag fired (probable).** The batch `diffstack` built its out-of-eclipse windows from the 1.9-h search box. The true T14 is 3.16 h, so those windows sat 1.4–3.3 h from mid-eclipse and partly inside the eclipse. Median windows do not cancel a 3% pulsation. And its 5×5 positive-clipped centroid has the G 12.45 neighbour 1.6 px away. Modelling the pulsation per pixel and fitting a PSF puts the deficit on the target.

## Next eclipses (BTJD)
Formal error ±0.3 min; allow about ±5 min for the O−C wander.
- Primary: 4334.8116, 4337.3572, 4339.9028, 4342.4483, 4344.9939, 4347.5395.
- Secondary (phase 0.580 ± 0.003, ±9 min, ~2 ppt): 4333.7425, 4336.2880, 4338.8336, 4341.3792, 4343.9248, 4346.4704.

## What would settle it further
- A few RVs at the quadratures, to tie K1 and γ to the TESS ephemeris.
- A joint pulsation + eclipse model with limb darkening, for k, b, R1 and e sin ω (the secondary's duration is poorly constrained at 1.5–3 h).
- An O−C analysis with the pulsations prewhitened, to tell whether the ±2-min sector-to-sector timing structure is a third body.

## Row fixes for the paper table
| field | batch row | per-object value |
|---|---|---|
| P (d) | 2.54558 | **2.5455862 ± 0.0000005** |
| T0 (BTJD) | 1656.8543 | **3571.13574 ± 0.00015** (1656.85633 in the batch-epoch global fit) |
| depth (ppt) | 27.4 (box) | QLP trapezoid 28.5 median (25.3–31.7, aperture-dependent, declining with sector); **dilution-corrected ≈ 32** (PDCSAP 31.6–33.0; PSF deficit 32.4) |
| secondary | — | **1.9 ± 0.24 ppt at phase 0.580** (10.7σ vs control), T ≈ 1.5–3 h |
| duration | 1.9 h (box) | **T14 3.16 h**, ingress/egress 1.03 h each, flat ~1.1 h |
| events | 65 | **74 covered primaries in 9 sectors** (70 in the ephemeris fit); secondary stacked over 72 cycles |
| conj. offset | +0.017 | primary = conjunction A, +0.20σ at the Gaia epoch; secondary phase +0.55σ from Gaia conjunction B |
| diffimg flag | 9.7″, peak not on target | **artefact: on target.** 0.24–1.59″ in 7 of 8 sector products (s93 3.45″, PSF-model systematic). G 12.45 neighbour rejected by Δχ² ≥ 124 in every sector. |
| note | — | Target pulsates at ±3% (γ Dor-like; ASAS-SN "ROT 0.884 d" is this). Companion is an M dwarf (m2 ≈ 0.31 M☉, T2 ≈ 3500 K). e cos ω = 0.126 from TESS. |
