# TIC 423927429 (UCAC4 797-029409, Gaia DR3 2247293469576926336): per-object vet

Opus 5.5 subagent, 2026-10-21. This resumes a session that was killed with no progress.md; its vet.py, Gaia, catalogue and background outputs were reused and checked. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A detached, circular, partially eclipsing SB1 with both eclipse kinds detected.

Deciding numbers:
- **Primary eclipses:** 353 individual events in 23 sectors (s015–s086). Depth 17.41 ± 0.03 ppt, T14 2.04 h, T12/T14 0.35.
- **Period:** P = 1.4271182 ± 0.0000001 d against Gaia's 1.427080 ± 0.000047 d, a difference of **+0.82σ**.
- **Timing:** the primary falls on Gaia conjunction A (primary eclipsed) at +0.16σ to +0.46σ in every sector. Conjunction B is 6σ to 14σ away.
- **Secondary eclipse:** 1.34 ± 0.05 ppt, S/N 24, at phase **0.50050 ± 0.00103**. That gives e cos ω = +0.0008 ± 0.0016, against Gaia's −0.008 ± 0.039 (e = 0.025 ± 0.045). The secondary falls where Gaia's B − A = 0.495 ± 0.025 puts it.
- **Doppler beaming matches Gaia's orbit:** sin φ = +0.30 ppt against about +0.35 ppt expected from K1 = 38.8 km/s. The sign independently confirms that the luminous star is the RV primary moving as Gaia says.
- **On target:** TESS-SPOC PDCSAP gives 16.8–18.2 ppt in all 13 sectors checked. The target is the best fit in the difference images by Δχ² > 13,000 over any neighbour.

## 1. Archives
- **cats.py --r 60** (2026-10-20; re-run 2026-10-21, identical result — `cats-out2.txt`):
  - No hits in VSX, ASAS-SN, Prša+2022, IJspeert+2024, or Kostov t3/t4.
  - The only hit is Kostov+2025 **table2**, an unvetted ML flag list (0.001″ match). It does not count as catalogued.
  - SIMBAD has only UCAC4 797-029409, typed [SB*].
- **Gaia DR3** vari_summary and vari_eclipsing_binary: empty.
- **SB9, WDS, J/AJ/160/111:** no entry.
- **ExoFOP:** no TOI, CTOI, imaging or spectra.
- **Extra VizieR cones at 30″** (ATLAS, ZTF, WISE variables, GCVS, VSX copy, ROSAT, 2RXS, 4XMM, ASAS-SN, LAMOST, APOGEE, Prša+2022): no rows; each control cone returned rows, so the queries worked. J/A+A/674/A16 is not an EB table.
- **Web search** on the TIC, UCAC4 and Gaia IDs: no relevant hits.
- **Batch receipts:**
  - c4-vetsum: dphi +0.009/−0.477, ATTR.
  - diffrun-c4 s056: peak on target, deficit−target 2.44″.
  - c4-ebcats: Kostov table2 only.
- **No prior art** beyond the ML flag.

## 2. Measurements (vet-out.txt, sec2-out.txt; QLP SAP, Q==0, no trimming)
- **Primary depth per sector:** 16.2–18.3 ppt. χ²/dof of depth constancy is 1267/352, a modest sector-to-sector scatter of about 0.5 ppt, typical of QLP dilution.
- **Odd vs even primaries:** 17.29 ± 0.04 vs 17.54 ± 0.04 ppt. The 4σ split is small and can't be a period-halving effect, because a real secondary is seen.
- **Fold fit with orbital harmonics:**
  - Primary: T14 2.04 h, T12/T14 0.35, depth 17.6 ppt.
  - Secondary: T14 1.84 h, T12/T14 0.30, depth 1.34 ppt.
  - e sin ω from the duration ratio is about −0.05 ± 0.03. The 0.08 h duration grid limits this, and partial-occultation shape is degenerate with duration, so it is uninformative but consistent with 0.
- **Harmonics** (ppt, median over 23 sectors; sector scatter ~0.2):

  | term | amplitude | meaning |
  |---|---|---|
  | cos 2φ | −4.17 | ellipsoidal |
  | cos φ | −0.25 | reflection, brightest at phase 0.5 |
  | sin φ | +0.30 | beaming |
  | other terms | ≤ 0.14 | — |

  TESS-SPOC independently gives an ellipsoidal amplitude of 3.5–4.4 ppt in every sector.
- **Background:** the regression (bkgreg-out.txt) implies |ΔF| ≤ 0.17 ppt per sector, against a 13–15 ppt dip in the same windows. vet.py's dBKG column in s015 shows the known broken units and is ignored.
- **Centroids:** dX −0.14 ± 0.10 mpix, dY −0.22 ± 0.12 mpix.
- **Quality flags:** 10 of 353 events touch a bit-32 cadence and one is near a listed systematic. With 353 events none of them matter.
- **Blind dip census:** 348 dips on the ephemeris. The five off-ephemeris dips at 9.7–13.3 ppt (2916.733, 2860.808, 2903.617, 3437.624, 3629.997) all sit about 3.2 h from a primary at the edge of a data gap.
  - Example: dip_2916.7.png shows a clean primary followed by a gap. The matched-filter baseline is corrupted by the eclipse.
  - None repeats at the same phase in neighbouring cycles.
  - They are artefacts. The many 2–4 ppt dips at phase ±0.5 are the secondary.
- **Control phases:** 0.125, 0.25, 0.75 and 0.875 give |depth| ≤ 0.18 ppt. Phases 0.375 and 0.625 give +0.25 ppt from ellipsoidal leakage in vet.py's estimator; sec2.py fits the harmonics properly.

## 3. Ephemeris
- **Primary (conjunction A):** T0 = 2967.97498 ± 0.00004 BTJD (E = 880), P = 1.4271182 ± 0.0000001 d.
  - χ²/dof 1694/351 (errors scaled ×2.2); O−C rms 1.5 min against a median timing error of 0.7 min.
  - The excess is mostly from the noisy 30-min s016 events. Small eclipse-timing variations are not excluded, which is worth a look if anyone revisits.
- **Against Gaia's A prediction** (Monte Carlo with corr_vec): +0.17 h at s015 to +1.14 h at s086, i.e. +0.16σ to +0.46σ. The drift is Gaia's P being 0.8σ short.
- **Secondary − primary:** 0.50050 ± 0.00103 (jackknife over 23 sectors), against Gaia's 0.4950 ± 0.0247 (+0.2σ).

## 4. Independence
- **TESS-SPOC FFI** (13 sectors, indep-out.txt): PDCSAP 16.80–18.16 ppt, SPOC-SAP 16.25–17.14 ppt, ellipsoidal amplitude 3.46–4.43 ppt.
- **Difference images** (tpfdiff-out.txt, 200-s TPFs s059 and s079; the 30-min TPFs are too coarse for the in-window estimator):
  - The pixel with the largest flux loss is the target pixel, at S/N 67 and 81.
  - The best fit is the target, with implied own dips of 17.2 and 17.1 ppt.
  - The next-best star (G 15.83 at 22″) is worse by Δχ² +13,800 and would need a 190–340 ppt dip.
- **Dilution table** (needed dip = 17.4 ppt × 10^(0.4ΔG)):

  | neighbour | ΔG | needed dip |
  |---|---|---|
  | G 15.83 at 22.3″ | 4.33 | 940 ppt |
  | G 16.92 at 43.8″ | 5.42 | 2540 ppt |
  | G 15.35 at 67.3″ | 3.85 | 600 ppt (outside 60″) |

  None of them can produce the signal.

## 5. Physics (occfit-out.txt)
- **Mass function** f(M) = 0.0086 M☉. With M1 ≈ 0.94 M☉, m2 is about 0.23 M☉, an M dwarf with R ≈ 0.24 R☉. q ≈ 0.24, a ≈ 5.6 R☉, v_t = 24.7 R☉/d.
- **Transit at A** (companion in front, as Gaia's ω implies), from a physical fit to 207 events at 200-s cadence:
  - k = 0.165, b = 0.895 R1, amplitude 0.93.
  - That gives **R1 ≈ 1.50 R☉ and R2 ≈ 0.25 R☉**, exactly an M dwarf of the f(M) mass.
- **Occultation at A:** needs the companion to supply 3.8% of the light, impossible for a 0.23 M☉ dwarf next to a G star (about 0.2% expected). This agrees with Gaia's convention.
- **Secondary:** at b ≈ 0.9 the M dwarf is about 70% occulted. With a TESS-band light ratio of about 2.4 ppt, the predicted depth is about 1.6 ppt; observed 1.34 ppt.
- **Ellipsoidal:** 1.3 × q × (R1/a)³ = 4.17 ppt gives R1/a ≈ 0.24, so R1 ≈ 1.33 R☉. This agrees with the eclipse fit.
- **The radius tension** (the one open item):
  - Eclipse and ellipsoidal fits independently give R1 ≈ 1.3–1.5 R☉.
  - TIC gives 2.06 ± 0.11 R☉ (Teff 5400 K, L 3.26 L☉). An own G-band estimate of L ≈ 3.1 L☉ at about 5600 K gives about 1.9 R☉.
  - With R1 = 2.06, a 2.04 h transit of a 0.25 R☉ companion would have to be a deep graze far shallower than 17 ppt, and the ellipsoidal amplitude would be about 15 ppt.
  - Possible causes: a hotter, smaller primary (Gaia gspphot gives Teff 6712 K, logg 4.03, though bp_rp 0.98 argues against it), a modest third light, or the TIC luminosity.
  - None of these affects whether the eclipses are real or belong to the binary.
- **Not a heartbeat or tidal artefact:** the orbit is circular, and both eclipses are short and sharp.

## 6. Next predicted times (BTJD)
- **Primary** (M dwarf transits the primary, conjunction A): **4335.1543, 4336.5814, 4338.0085** (± 0.0001 d; allow ±2 min for the χ² excess), then every 1.4271182 d.
- **Secondary** (M dwarf occulted, conjunction B): **4335.8685, 4337.2956, 4338.7228** (± 0.0015 d).

## What would settle it further
- A spectroscopic Teff and log g for the primary would resolve the radius tension. So would high-resolution imaging for a possible third light.
- An eclipse-timing analysis restricted to the short-cadence sectors would test the 1.5-min O−C excess.
- RVs at quadrature would check K1 and allow a joint fit.

## Files
- **Scripts:** vet.py, vetlib.py, indep.py, tpfdiff.py, secA.py, sec2.py, occfit.py, bkgreg.py, gaiatap.py, mastlc.py, morecats.py, extracats.py.
- **Outputs:** vet-out.txt, indep-out.txt, tpfdiff-out.txt, tpfdiff_59.png, tpfdiff_79.png, dips-out.txt, dip_*.png, sec2-out.txt, sec2.png, occfit-out.txt, occfit_ph0.00.png, extracats-out.txt, cats-out2.txt.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet423927429\`.
