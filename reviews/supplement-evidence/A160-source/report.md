# TIC 142240367 (TYC 7558-731-1, Gaia DR3 4945899177740273920): per-object vet

**Verdict: CONFIRMED.** The eclipsing binary is the Gaia SB1 itself. It is grazing, with both eclipses detected.

Wave 4, 2026-10-20/21. A first Opus 5.5 subagent got as far as the secondary and ephemeris stage and was killed. A second one checked its receipts and re-measured the raw SAP independently (`check.py`), then did the physics (`check.py`, `esinw.py`) and this report. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Deciding numbers
- **Primary eclipse, 11 events (s003, s097, s104):**
  - Every event has S/N 39–81.
  - Own-aperture TESScut depth is **19.1 ± 0.1 ppt** in all three sectors (`cutphot-out.txt`).
  - QLP SAP gives 18.5 ppt in s003 but 16.2 in s097/s104. That step is QLP dilution in the 200-s products, not a real change. TESS-SPOC s3 gives 19.0 (PDCSAP) and 18.8 (SAP).
  - T14 is 3.42 h; the best T12/T14 is 0.4, so the shape is nearly a V.
- **Secondary eclipse, 9 events, S/N 15–26 each:**
  - Phase **0.50120 ± 0.00005**.
  - Depth 4.2 ppt in QLP, 4.7–5.1 ppt in the own aperture; T14 3.76 h.
  - Fixed-shape test: S/N 26.9 at the measured phase, 16.9 at Gaia's predicted phase. The look-elsewhere controls (518 phases) have rms 1.5 and a maximum of 3.7.
- **Ephemerides:**
  - Primary: P = 7.541350 ± 0.000002 d, T0 = 3464.17253 ± 0.00033 BTJD (E = −49), O−C rms 1.4 min.
  - Secondary: P = 7.541351 ± 0.000008 d; P2 − P1 = +0.17σ.
  - Against Gaia's P = 7.541328 ± 0.000329 d: **+0.07σ**.
- **Gaia conjunctions (Monte Carlo using `corr_vec`):**
  - The primary sits on **conjunction A**: +0.60 h (+0.76σ) at the Gaia epoch, and +0.21 to +0.49σ in each sector.
  - The secondary sits on conjunction B: −0.25 h (−0.43σ).
- **Orbit shape:**
  - e cos ω = +0.0019 ± 0.0001, against Gaia's +0.0089 ± 0.0110 (−0.63σ).
  - The duration ratio T_B/T_A is 1.10. The model lets the impact parameter scale with the separation at each conjunction, which matters for a grazing eclipse. It gives **e sin ω ≈ −0.016**, against Gaia's −0.022 ± 0.011 (about 0.5σ, same sign).
- **Which star is in front:** at conjunction A the primary is farthest away, so the companion is in front. The deeper eclipse is at A, as expected for a luminous primary.
- **Background and systematics:**
  - The unit-free background regression gives |fake| median 0.02 ppt and maximum 0.39 ppt for the primaries; at most 0.10 ppt for the secondaries.
  - Two primaries include bit-32 cadences (E −324 and E 16); their depths agree with the rest.
  - No event falls within 0.5 d of a listed sector-wide systematic, and centroid shifts are under 1 mpix.
- **Blind dip census:** of 23 dips at S/N ≥ 4, 12 are primaries and 9 are secondaries. None of the off-ephemeris dips is deeper than half the eclipse; the largest is 1.2 ppt.
- **Raw re-check (`check-out.txt`):**
  - Primaries: s003 18.9 ppt, s097 15.8, s104 15.9.
  - Secondaries: 4.4, 4.0 and 4.0 ppt.
  - The earlier cutout pass showed a 22–29 ppt "secondary" at s104 E = 47. It falls in a QLP data gap with no usable Q0 coverage, so it is an edge artefact, not an event.

## Archives
- `cats.py --r 60`:
  - VSX: none.
  - ASAS-SN: none.
  - Prša / IJspeert / Kostov: none.
  - SIMBAD: TYC 7558-731-1, listed only as [SB*].
- SB9, WDS and J/AJ/160/111: none.
- ExoFOP: no TOI or CTOI; no imaging, spectroscopy or companions.
- Gaia DR3: vari_summary and vari_eclipsing_binary are empty; phot_variable_flag is NOT_AVAILABLE.
- A web search for "TYC 7558-731-1" (2026-10-21) found nothing about this star.
- **There is no prior eclipse record, so this is new.**

## Independence
- **Other pipelines, s3, 3 events each:**
  - TESS-SPOC PDCSAP: 18.98 ± 0.14 ppt.
  - SPOC-SAP: 18.83 ppt.
  - TGLC aperture: 22.5 ppt; TGLC PSF: 22.9 ppt.
- **Difference image (TESS-SPOC s3 TPF):**
  - The flux loss peaks at S/N 32.8, and the loss-weighted centroid is on the target.
  - The single-star fit gives χ² 1803 for the target and 6487 for the neighbour.
  - The batch diffimg for s104 puts the deficit 0.71″ from the light centroid, with the peak on target.
- **Neighbour dilution:**
  - The only G < 15 star within 60″ is Gaia 4945899212100013056: G 14.38, 74″ away, Δm 3.31.
  - To produce these eclipses it would need dips of about 350 ppt (primary) and 90 ppt (secondary), and the difference-image fit rejects it.
  - TIC contratio is 0.0009.

## Physics
- **Mass function and companion:**
  - f(m) = 0.0643 M☉.
  - With M1 = 1.07 ± 0.13 and R1 = 1.77 ± 0.08 (a slightly evolved G star, Teff 5898 K): m2(i = 90°) = 0.51–0.59 M☉ and a ≈ 19 R☉.
- **Grazing geometry:**
  - A central chord would last about 7.2 h.
  - The observed 3.42 h gives b ≈ 1.17 and i ≈ 84°.
- **Predicted against observed depths (uniform disks, main-sequence companion with R2 ≈ 0.59 R☉, Teff ≈ 3860 K):**
  - Primary: 16–21 ppt predicted, 19 observed.
  - Secondary: 3–4.6 ppt predicted, 4.3–4.9 observed.
- **Companion temperature and light:**
  - The depth ratio of 0.256 implies Teff2 ≈ 4160 K.
  - L2/L1 is about 2%, which fits a single-lined (SB1) spectrum.
- **Out-of-eclipse terms are small:** ellipsoidal about 0.04 ppt, c1 about −1.9 ppt.
- **No heartbeat:** e = 0.026, so heartbeat can be excluded.
- **One geometry fits everything:** a companion of about 0.55 M☉ grazing a 1.8 R☉ primary.

## Next predicted eclipses (BTJD)
Errors are formal; the O−C rms is 1.4 min for the primary and 5 min for the secondary.
- **Primary (conjunction A):**
  - 4338.9691, 4346.5105, 4354.0518 (±0.6 min).
  - 4406.8413, 4414.3826, 4421.9240.
- **Secondary (conjunction B):**
  - 4335.2079, 4342.7492, 4350.2906 (±2.2 min).
  - 4403.0800, 4410.6214, 4418.1628.

## What would settle it further
It is settled at the level the brief asks for. Two optional checks:
- An RV phase check: the RV curve should cross γ, going from approaching to receding, at the primary eclipse.
- Multi-colour photometry of a primary eclipse, to pin the grazing geometry and the companion's temperature.
