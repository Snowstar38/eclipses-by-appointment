# TIC 299650500 (CD-23 4400, Gaia DR3 2925231689064510464): per-object vet

Opus 5.5 subagent, 2026-10-21. This session resumed work from a session that was killed on 2026-10-20. The killed session's receipts (`vet-out.txt`, `indep-out.txt`, `neighbours-out.txt`, `gaiatap-out.txt`) were checked and hold up. New work this session: `extra.py` → `extra-out.txt`, and `tpfdiff.py` on the three SPOC TPFs → `tpfdiff-out.txt`, `tpfdiff_*.png`. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: **CONFIRMED**: a grazing transit of an M-dwarf companion across the F primary, at Gaia conjunction A

The deciding numbers:
- **Ephemeris:** P = 18.337086 ± 0.000027 d and T0 = 3427.74767 ± 0.00092 BTJD, from 5 primary eclipses across s006, s007, s033 and s087, a 2200-d baseline. The O−C rms is 4.7 min. In the jackknife, each dropped event is predicted to within ≤ 12 min.
- **Agreement with Gaia:** Gaia's P is 18.33751 ± 0.01016, which is −0.04σ from ours. Every eclipse falls on the Gaia conjunction A predicted from the orbit (MC with corr_vec), at −0.6 to −1.9 h with σ = 15–44 h. The chance of a random 18-d event landing that close is about 0.5%.
- **On target:** in the SPOC TPF difference images, the target is the best single-star fit in all three sectors. Δχ² to the next-best star is +1970 (s006), +224 (s007) and +1470 (s033). The batch TESScut s087 diff image puts the deficit 1.7″ from the target. No Gaia neighbour within 60″ can make the dip: the brightest possible contaminant (G 14.13 at 32″) would need a 45% eclipse, and its diff-image fit is much worse.
- **Independent pipelines:** TARS (4 sectors), SPOC PDCSAP and SAP (3 sectors) and TGLC PSF and aperture (s006) all recover the event at 12–24 ppt. That includes the shallow s007 event, which every pipeline measures at 12–13 ppt.
- **Not a heartbeat:** conjunction A falls 27° of true anomaly before periastron, the attribution blind spot, so this was tested explicitly:
  - The free Gaussian σ per event is 1.0–1.1 h, against a periastron timescale τ of 1.32 d.
  - Tide+eclipse beats tide-only by Δχ² = 141 to 3500 per event.
  - The expected equilibrium-tide amplitude is about 0.3 ppt, against an observed 19 ppt.
- **Shape and physics are consistent with one geometry:**
  - f(M) = 0.0259 M☉, so m2 sin i ≈ 0.48 M☉ (an M dwarf, R2 ≈ 0.47 R☉, k ≈ 0.20) for M1 = 1.57 M☉ and R1 = 2.37 R☉ (TIC values, Teff 7090 K).
  - At conjunction A the separation is 24.9 R☉ and the transverse speed 143 km/s. A central chord would last 7.6 h; the observed T14 of 4.5 h with a V shape (T12/T14 = 0.4) implies the sky separation is 0.97 R1, so the transit is grazing and i ≈ 84.7°.
  - About half the M-dwarf disc crosses the limb, which predicts roughly 14–20 ppt, consistent with the measured 19.4 ppt.
  - Conjunction A has ν+ω = 90°, so the primary is farthest and the companion is in front: A is the transit.
- **No secondary, as predicted:** at conjunction B the separation is 47.3 R☉, so the sky separation is 4.36 R☉, larger than R1+R2 = 2.84 R☉. A full occultation would be ≤ 3.1 ppt in any case. Fixed-shape fit across all 5 B windows:
  - At Gaia-B nominal, the depth is −0.57 ± 0.28 ppt with T14 = 4.5 h, and −0.80 ± 0.22 ppt with T14 = 8.6 h (the duration scaled by the speed ratio).
  - The best peak in the ±3σ window has S/N 6.0, which sits below the median control peak of 9.7. Controls exceeded it 80% of the time.
  - Secondary: **not detected, consistent with the geometry.**

## Caveats worth carrying
- **The depth is not constant:** events measure 21.9, 13.3, 18.8, 21.9 and 18.1 ppt (χ² 154/4). The star is a hybrid pulsator. The residual periodogram shows 10.18 c/d at 1.15 ppt (δ Sct) and a group near 2.4–2.5 c/d at up to 1.7 ppt per sector (γ Dor), with 2.1–2.3 ppt rms. Over a 4.5-h window, beating at this level shifts single-event depths by several ppt. The low s007 event is real flux (every pipeline sees it), and the most likely cause is pulsation phase. A change in inclination over 2200 d cannot be excluded with 5 events.
- **e cos ω and e sin ω cannot be measured** from a single eclipse kind. The only orbital-shape test is that the eclipse lands on Gaia's conjunction A, with e = 0.349 ± 0.039 and ω = 117 ± 8°; the B phase falls 0.3945 ± 0.0255 after A.
- **Many off-ephemeris census features at 3–9 ppt** (white-noise S/N up to 18) are pulsation and red noise. None sits on the ephemeris, and none is as deep as the eclipses in the 10- and 3.3-min sectors.

## Archives (step 1)
- `cats.py 299650500 --r 60` (re-run this session): VSX none, ASAS-SN none, SIMBAD CD-23 4400 [SB*] at 0.0″. The ebcats battery (Prša+2022, IJspeert+2024, Kostov+2025) found none.
- Gaia DR3 vari_summary and vari_eclipsing_binary: no rows.
- SB9, WDS and J/AJ/160/111: none.
- ExoFOP: no TOI, CTOI, imaging, spectroscopy or stellar companions.
- A web search on "CD-23 4400", "TYC 6521-2291-1" and "TIC 299650500" found no mention.
- **Not previously catalogued as eclipsing.**

## Next predicted eclipses (BTJD)
| Kind | Times |
|---|---|
| Primary (A, transit) | 4344.6020, 4362.9391, 4381.2761, 4399.6132 (each ± 2–3 min); then +18.337086 d per cycle |
| B (Gaia phase; no eclipse expected) | 4351.84, 4370.17, 4388.51, 4406.85 (± 0.47 d) |

## What would settle it further
- **RVs at the primary eclipse:** a Rossiter–McLaughlin signal or a K1 phase check would pin down which star is in front.
- **A clean high-cadence eclipse:** fitting it jointly with a pulsation model would give a real depth and k.
- **A Gaia DR4 epoch-RV refit:** e and ω can then be tested against the transit duration.
