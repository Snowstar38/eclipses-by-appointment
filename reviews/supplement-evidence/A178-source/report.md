# TIC 323007878 (TYC 9406-845-1, Gaia DR3 5196347929180662272): per-object vet

Opus 5.5 subagent, wave 5, 2026-10-21. Fresh folder; every number below comes from a file in it:
- Outputs: `vet-out.txt`, `ecl2-out.txt`, `sec2-out.txt`, `bkgreg-out.txt`, `indep-out.txt`, `tpfdiff-out.txt`, `geom-out.txt`, `dips-out.txt`.
- Archive and query outputs: `gaiatap-out.txt`, `cats-out*.txt`, `morecats-out.txt`, `extracats-out.txt`, `mastlc-*.txt`.
- Downloads: `C:\Home\sky\data\qlp-sb-p20-60\pervet323007878\`. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. A detached, circular, grazing eclipsing SB1 (F primary with a K-dwarf companion); both eclipse kinds detected.

Deciding numbers:
- **Primary eclipse:** 52 events in 11 QLP sectors (s011–s094).
  - Each is S/N 13–87, apart from one event lost in the noisy QLP s027.
  - Depth 25.5 ± 0.07 ppt, T14 3.36 h, T12/T14 0.40. The shape is V-like, as a graze should be.
- **Secondary eclipse:** 50 events, 9.32 ± 0.06 ppt, T14 3.40 h. It is seen individually at S/N 20–33 in every sector.
- **Period:** P = 4.7034219 ± 0.0000005 d against Gaia's 4.703408 ± 0.000134 d, a difference of **+0.11σ**.
- **Timing:** the primary falls **+0.10σ** from Gaia conjunction A in every sector. The offset runs from +0.09 h at s011 to +0.24 h at s094 (Monte Carlo with corr_vec). Conjunction B is 24–65σ away.
- **Circular orbit:** the secondary falls at phase **0.50019 ± 0.00005**.
  - That gives e cos ω = +0.0003 ± 0.0001, of which about +0.00008 is the ~21 s light-travel delay.
  - Gaia gives e cos ω +0.000 ± 0.009 and e sin ω +0.001 ± 0.009.
  - The duration ratio gives e sin ω +0.006 ± 0.017.
- **On target:** SPOC TPF difference images (s038, s065, s067) put the flux loss on the target pixel at S/N 35–116.
  - The target fits better than any neighbour by Δχ² 4,600–24,000.
  - The field is isolated: only 3 Gaia sources with G < 17 lie within 90″, and the nearest is at 59.6″.

## 1. Archives
- **cats.py --r 60** (APPOINTMENTS_DATA set): no hits in VSX, ASAS-SN, Prša+2022, IJspeert+2024 or Kostov+2025 (any table). SIMBAD has only TYC 9406-845-1, typed [SB*] (first run timed out; re-run is `cats-out2.txt`).
- **Gaia DR3 TAP:** vari_summary and vari_eclipsing_binary empty; phot_variable_flag NOT_AVAILABLE. RUWE 0.84, ipd_frac_multi_peak 0. gspphot Teff 6347 K, logg 3.80.
- **SB9, WDS and J/AJ/160/111:** no entry.
- **ExoFOP:** no TOI, CTOI, imaging, spectroscopy or stellar companions.
- **Extra VizieR cones at 30″** (ATLAS, ZTF, WISE, GCVS, VSX, ROSAT, 2RXS, 4XMM, ASAS-SN, LAMOST, APOGEE, Prša): no rows. The ATLAS, ZTF, GCVS, ROSAT, LAMOST, APOGEE and Prša control cones were also empty — those catalogues simply don't cover dec −81° well.
- **Web search** on "TYC 9406-845-1" and "TIC 323007878": nothing relevant.
- **SPOC:** no 2-min target and no CAOM TESS-mission product, so no SPOC DV/TCE. TESS-SPOC FFI products don't run DV.
- **Gaia orbit:** SB1, P 4.703408(134) d, e 0.006(10), ω 84(107)°, K1 57.47(56) km/s, significance 102.
- **TIC:** Teff 6499 K, R 2.08 R☉, M 1.33 M☉, d 497 pc, contratio 0.012.
- **Batch receipts:** c4-vetsum dphi +0.000/+0.500 ATTR; diffrun-c4 s064 peak on target, 0.71″; c4-sapdepth 24–26.5 ppt per event.
- **Prior art:** none found.

## 2. Eclipse measurements (QLP SAP, QUALITY==0, untrimmed)
- **Global trapezoid** (`vet-out.txt`): 25.2 ppt, T14 3.36 h, T12 1.34 h, flat bottom 0.67 h. A box shape (T12/T14 0.1) is worse by Δχ² +1899.
- **Individual primaries** (`ecl2-out.txt`, local quadratic baseline): weighted mean **25.51 ± 0.07 ppt**.
  - Odd 25.94 ± 0.08 and even 25.70 ± 0.08 ppt.
  - Per sector the depth is 24.8–27.4 ppt, except s094 at 23.1 ppt. In s094 the four primaries (22.8–23.6 ppt) and the secondaries (7.8–8.1 ppt) are all scaled by the same ×0.87. That is a QLP s094 dilution step, not the star.
  - The depth-constancy χ²/dof of 434/51 reflects this sector-level QLP scaling of about ±1 ppt.
- **Individual secondaries:** 9.32 ± 0.06 ppt, χ²/dof 137/49.
- **Background** (unit-free regression): |ΔF| ≤ 0.22 ppt in 10 sectors and 0.91 ppt in s066, against 13–17 ppt dips in the same windows. The dBKG columns have the known broken units and are ignored.
- **Centroids:** dX −2.0 ± 0.4 mpix, dY −1.4 ± 0.5 mpix — tiny, consistent with an on-target dip in a nearly empty aperture.
- **Quality flags and systematics:** 2 primaries touch a bit-32 cadence, depths normal. No event within 0.5 d of a listed sector-wide systematic.
- **Control phases:** |depth| ≤ 0.13 ppt. Phase 0.5 holds the real secondary.
- **Blind dip census:** 132 peaks at S/N ≥ 4. 56 are primaries and ~46 are secondaries at phase ±0.500. Five off-ephemeris dips are ≥ 12.9 ppt, and none is real:
  - Four are in QLP s027 (15.7 ppt rms, scattered-light dominated; e.g. 2047.98 is a −108 ppt SAP step with a 0.05 px centroid jump; SPOC's s027 is clean).
  - The fifth, 3138.21, is a primary egress against a QLP bit-30-flagged gap; SAP is actually higher inside that window.
  - None repeats at the same phase in neighbouring cycles (`dips-out.txt`).
- **Fold with harmonics** (`sec2-out.txt`): primary 24.9 ppt / 3.36 h; secondary 9.34 ± 0.17 ppt / 3.40 ± 0.11 h at phase 0.5000.

## 3. Ephemerides (`ecl2-out.txt`; events with S/N > 3; the 5σ clip removed nothing)

| kind | P (d) | T0 (BTJD) | n | χ²/dof | O−C rms |
|---|---|---|---|---|---|
| primary (conj. A) | 4.7034219 ± 0.0000005 | 2822.87791 ± 0.00009 | 52 | 76/50 | 2.1 min (median error 0.7 min) |
| secondary (conj. B) | 4.7034239 ± 0.0000015 | 2834.63735 ± 0.00023 | 50 | 67/48 | 3.1 min (median error 1.9 min) |

- **Period difference:** P(sec) − P(pri) = +0.17 s (+1.25σ). No apsidal motion.
- **Phase separation:** 0.50019 ± 0.00005. Gaia predicts B − A = 0.5000 ± 0.0058. (sec2's fold gives 0.4998 ± 0.0002, but its phase grid is 0.0005.)
- **e cos ω:** removing the light-travel delay (≈21 s) leaves about +0.0002. The orbit is circular.
- **Comparison with Gaia:** conjunction A matched at +0.10σ throughout, P at +0.11σ. Even with σω = 107°, using corr_vec gives a conjunction-time error of only 0.04–0.10 d — small enough to pin the attribution.

## 4. Independence
- **Other pipelines** (`indep-out.txt`): TESS-SPOC PDCSAP in s011, s013, s027, s038, s039, s065, s067 gives **25.3–26.1 ppt**; SPOC-SAP 25.1–25.7 ppt; GSFC-ELEANOR-LITE CORR 25.8 (s011) and 25.4 ppt (s013). SPOC's ellipsoidal amplitude A2 is 1.1–1.5 ppt in every sector.
- **Eleanor s012** (a sector QLP lacks) shows 8.2 ppt primaries and ~2 ppt secondaries at the right times. Its raw flux is one third of s011/s013 — a 4-pixel square aperture on another CCD with twice the background. A product problem; the timing still matches.
- **Difference images** (`tpfdiff-out.txt`):

  | sector | max-loss pixel | S/N | χ² target | χ² best neighbour |
  |---|---|---|---|---|
  | s038 | target (5,5) | 77 | 1007 | 18,055 |
  | s065 | target (5,5) | 116 | 1848 | 25,831 |
  | s067 | adjacent (5,6) | 35 | 651 | 5,230 |

  The target's implied own dip is 21.6–21.9 ppt, and the loss-weighted centroid is within 0.1–0.3 px of the target.
- **Neighbour dilution table** (needed dip = 25.5 ppt × 10^(0.4ΔG)): G 16.58 at 59.6″ → 2.85 (impossible); G 12.96 at 64.5″ → 101 ppt (excluded by the difference images); G 15.99 at 74.5″ → 1.64 (impossible).

## 5. Physics (`geom-out.txt`)
- **Mass function:** f(M) = 0.0925 M☉. With M1 = 1.2–1.45 M☉ and i ≈ 81–82°, m2 = 0.70–0.78 M☉, a K dwarf. a = 14.6–15.4 R☉.
- **Which star is in front:** at conjunction A the RV primary is behind, so the K dwarf transits the F star — the deep eclipse, as observed. At B the F star occults the K dwarf.
- **One geometry fits both eclipses:** two limb-darkened spheres on a circular orbit, m2 from f(M) at each i, reproduce both (primary 25.5 ppt / 3.36 h; secondary 9.2–9.5 ppt / 3.31–3.41 h; χ² < 3 for 10 combinations). Fitted: R1 1.8–1.95 R☉, R2 0.65–0.90 R☉ (poorly constrained in a graze), **T2 ≈ 4800 K** (4600 and 5000 K both fail), L2/L1 4–8% in TESS. Geometry: i 81.2–82.0°, b 1.10–1.29 R1 — a graze; a central chord would last ~6.6 h.
- **Depth ratio:** 9.32/25.5 = 0.365 is the TESS surface-brightness ratio of a ~4820 K star to a 6500 K star — right for 0.72–0.78 M☉.
- **Ellipsoidal:** ~1.3 ppt predicted, 1.1–1.5 ppt observed in SPOC.
- **Mild tension:** fitted R1 ≈ 1.8–1.95 R☉ is 1.5–3σ below TIC's 2.08 ± 0.09 — same direction as 423927429; doesn't affect the verdict.
- **Not a heartbeat:** e ≈ 0, symmetric eclipses at both conjunctions.

## Row fixes for the paper table

| field | batch | fix |
|---|---|---|
| P (d) | 4.70343 | **4.7034219 ± 0.0000005** |
| T0 (BTJD) | 1599.9843 | **2822.87791 ± 0.00009** |
| depth (ppt) | 24.6 | **25.5 ± 0.1** (QLP SAP per event; SPOC PDCSAP 25.3–26.1) |
| T14 (h) | 1.9 (search box) | **3.36** (grazing, T12/T14 0.40) |
| n events | 43 | 52 Q0 primaries + 50 secondaries |
| dphi | +0.000 | +0.0008 to +0.0021 across sectors; **+0.10σ** from conjunction A throughout |
| secondary | — | **9.32 ± 0.06 ppt at phase 0.50019 ± 0.00005** (e cos ω ≈ 0) |
| prior art | — | none (no EB catalogue, TOI, CTOI or SPOC TCE) |

## Next predicted eclipses (BTJD)
- **Primary** (K dwarf transits, conjunction A): **4403.2277, 4407.9311, 4412.6345**, then every 4.7034219 d. Formal ±0.5 min; allow ±2 min.
- **Secondary** (K dwarf occulted, conjunction B): **4400.8775, 4405.5809, 4410.2843**. Formal ±1 min; allow ±3 min.

## What would settle it further
Already settled as an eclipsing SB1. For better parameters:
- A spectrum (Teff, logg) to fix R1 and test the R1 tension.
- An SB2 detection of the K dwarf (expected K2 ≈ 103 km/s, L2/L1 ≈ 6% in TESS and more in the red) would give model-independent masses.
