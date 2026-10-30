# vet11: Gaia-period folds of five sinusoidal c9a candidates

Independent check (Opus 5.5 subagent, 2026-10-30, for Fable 5.1). I resumed a predecessor that was killed by a container restart. Its downloads, s3 light-curve fits, s4 pixel maps and the first half of the catalogue cones were reused. I added: s2b (the rest of the catalogue cones and the Gaia DR3 variability tables), s5b (the Roche toy model, crash fixed), s6 (a refold at P_phot, which removes the phase-drift artefacts of the Gaia-P fold), s8 (a narrow-dip test at min I), s7 (TIC 62328710 frequencies and ZTF), s9/s9b (Gaia covariance and conjunctions) and s10 (ExoFOP). Data are QLP SAP only, QUALITY==0, 10-min bins, with a per-segment cubic baseline. No TESS-SPOC light curves exist for any of the five. Depths are in ppt, measured from the mean of the two maxima, with per-sector SEM errors. Phases are at P_phot with 0 = min I (the deeper minimum). "Conj A" = the primary at superior conjunction (companion in front). Conjunction errors come from 40000 draws with the full Gaia corr_vec. The earlier independent-draw MC ignored corr(omega,Tp) of about 0.99 and overstated the errors. Coverage was cut short by a budget limit: one pixel sector per star, no difference images of the min-I dip, and no TESS-SPOC or TESScut-aperture depth comparison.

## TIC 372683900 (Gaia P 1.476502 +- 0.000081 d, e 0.30)
| quantity | value |
|---|---|
| LS top peak / P_phot (chi2 scan) | 0.73825 d (=P/2); 1.476507 +- 0.000001 d, ratio 1.000003 (+0.05 sigma) |
| min I / min II depth | 31.07 +- 0.31 at 0 / 28.18 +- 0.19 at 0.5011 +- 0.0008; diff 2.88 +- 0.35 (8.3 sigma), 11/12 sectors |
| harmonics K=6 | A1 2.35, A2 14.79, A3 0.67, A4 0.27 (+-0.05); min widths 0.271 / 0.244 (cos2phi = 0.250) |
| narrow dip at min I | 0.63 ppt, empirical 1.7 sigma (none) |
| conjunctions | min I - conj B +0.087 +- 0.117; min II - conj A -0.042 +- 0.127; min I at conj A excluded at 3.6 sigma |
| minima separation | 0.5007 +- 0.0018 vs Gaia-predicted 0.372 +- 0.039 (3.3 sigma): photometry says e cos w ~ 0, Gaia says -0.21 |
| pixel (s57) | amplitude centroid 0.9" from target. A G=15.23 star at 1.8" is unresolved, but it would need 128 ppt intrinsic and would have to match Gaia P to 1e-4 d |

**ELLIPSOIDAL**: a smooth double wave at the Gaia period with no eclipse narrowing. The unequal minima are deeper at conj B, which matches the Morris A1 sign reversal at low i. The s5b toy model at i ~ 20 deg gives A1 1.74, A2 14.87, deeper at B by 2.69 ppt. Caveat: with the TIC R1 that needs a dark M2 ~ 4 Msun, so R1 is probably overestimated. Gaia's e = 0.30 conflicts with the minima separation.

## TIC 13106408 (Gaia P 2.637505 +- 0.000401 d)
| quantity | value |
|---|---|
| LS top / P_phot | 1.31884 d (=P/2); 2.637721 +- 0.000002, ratio 1.000082 (+0.54 sigma) |
| min I / min II depth | 46.85 +- 0.33 at 0 / 40.63 +- 0.26 at 0.5009 +- 0.0010; diff 6.22 +- 0.39 (15.8 sigma), 7/7 sectors |
| harmonics K=6 | A1 2.06, A2 21.77, A3 1.40, A4 0.72 (+-0.03); widths 0.252 / 0.272 (min II flattened) |
| narrow dip at min I | 0.36 ppt, 2.3 sigma (not significant) |
| conjunctions | min I - conj A +0.079 +- 0.166; min I - conj B -0.427 +- 0.167 (2.6 sigma) |
| pixel (s58) | on target (1.9"). The best neighbour (G 14.4, 15") would need 91 ppt |

**ELLIPSOIDAL**: a large-amplitude, near-Roche-filling double wave at the Gaia period with unequal minima and a flattened min II. The K=6 residuals are white and there are no eclipse features. The conjunction test only mildly prefers min I at conj A.

## TIC 372683622 (Gaia P 3.809006 +- 0.000179 d)
| quantity | value |
|---|---|
| LS top / P_phot | 1.90468 d (=P/2); 3.809282 +- 0.000014, ratio 1.000073 (+1.5 sigma) |
| min I / min II depth | 7.73 +- 0.16 at 0 / 6.45 +- 0.19 at 0.4943 +- 0.0061; diff 1.28 +- 0.30 (4.2 sigma) but variable, 0.3-3.2 ppt between sectors |
| harmonics K=6 | A1 0.78, A2 3.23, A3 0.13, A4 0.12; per-sector A3/A4 ~0.5 and incoherent (spots) |
| narrow dip at min I | 0.24 ppt, 2.1 sigma (none) |
| conjunctions | min I - conj B +0.075 +- 0.040; min II - conj A +0.044 +- 0.036; min I at conj A excluded at 12.5 sigma |
| pixel (s56) | on target (2.6") |

**ELLIPSOIDAL**: a double wave locked to the Gaia period with minima at the two conjunctions. The deeper minimum is at conj B, as for low-i ellipsoidals; the toy model at i ~ 20 deg gives A2 3.2 and deeper at B by 1.7 ppt. On top of this there is variable spot modulation, and no eclipse.

## TIC 319185391 (Gaia P 2.677901 +- 0.000187 d)
| quantity | value |
|---|---|
| LS top / P_phot | 1.33902 d (=P/2); 2.678053 +- 0.000009, ratio 1.000057 (+0.8 sigma) |
| min I / min II depth | 8.46 +- 0.30 at 0 / 6.57 +- 0.14 at 0.5102 +- 0.0040; diff 1.89 +- 0.23 (8.3 sigma), 6/6 sectors |
| harmonics K=6 | A1 0.70, A2 3.64, A3 0.23, A4 0.04 |
| **narrow dip at min I** | box 1.15 +- 0.17 ppt, centre +0.007, core 0.012 phase (0.8 h), profile about 0.03 phase (about 1.9 h). Empirical S/N 5.3; 0/400 random phases as deep; per sector 0.46/0.84/2.01/0.85/0.96/1.48 (6/6 > 0, weighted 1.04 +- 0.17); even 1.26 +- 0.25, odd 1.04 +- 0.29; at min II -0.03 +- 0.21. The same test on the other three stars gives 1.7-2.3 sigma |
| conjunctions | min I - conj A +0.057 +- 0.084 (conj B excluded at 6.0 sigma); separation 0.511 +- 0.003 vs Gaia 0.529 +- 0.028 |
| pixel (s85) | the ellipsoidal signal is on target (5.2"). The dip itself has no pixel test |
| other | Gaia DR3 also has an astrometric orbit for this source, P = 434.5 +- 8.2 d, e = 0.70 (likely a triple) |

**DETACHED-EB** (grazing, fold-only): an ellipsoidal double wave plus a phase-locked 1 ppt, about 2 h dip at min I, which sits at Gaia conj A (companion in front). This is the eclipse that the flattened P/2 fold hid. Individual events are about 1 sigma, so they cannot be seen singly, and the dip has no difference image. That puts it at probable-level evidence.

## TIC 62328710 (Gaia P 0.938088 +- 0.000042 d)
| quantity | value |
|---|---|
| dominant signal | f1 = 6.390610 +- 0.000005 c/d (0.156480 d), 3.09 ppt; f1/f_orb = 5.9950, not an orbital harmonic (19 sigma in P). Second frequency f = 5.806788 c/d, 1.26 ppt. Both are stable in all 7 sectors |
| Gaia-P signal | after prewhitening, A2 = 0.058 +- 0.046 ppt (< 0.15 ppt, 2 sigma). Minima: none |
| pixel (s56) | amplitude centroid 45" from target, on Gaia DR3 2165710355333626240 (G 13.38, 44.3"; next source worse by dchi2 642). f = 5.807 c/d also peaks there |
| ZTF | neighbour: top peak 6.39060 c/d, 9.6 (g) / 8.9 (r) mmag, noise 99th percentile 2.3/4.6; 5.807 c/d 4.2/5.1 mmag. Target: 0.16/0.70 mmag at f1 (noise 1.5/1.7) |
| catalogue | the neighbour is Gaia VarFlag VARIABLE (vari_short_timescale). Target not in VSX/Gaia-EB within 60" |

**OTHER**: the "P/3" wave is a multiperiodic delta Scuti-type pulsator, the neighbour 44" away, diluted into the QLP aperture. The target is flat at the Gaia period. With any R1 >= 1.8 Rsun, ellipsoidal A2 < 0.15 ppt would require i < 5 deg, so the Gaia 0.938 d SB1 orbit is suspect.

## Summary
| TIC | class | P_phot / P_Gaia | min1 (ppt, phase) | min2 (ppt, phase) | pixel | catalogues |
|---|---|---|---|---|---|---|
| 372683900 | ELLIPSOIDAL | 1.000003 | 31.07 at conj B | 28.18 at conj A | on target (1.8" nbr unresolved) | none; SIMBAD SB* |
| 13106408 | ELLIPSOIDAL | 1.000082 | 46.85 | 40.63 | on target | VSX only an SR at 29"; SB* |
| 372683622 | ELLIPSOIDAL | 1.000073 | 7.73 at conj B | 6.45 at conj A | on target | none; SB* |
| 319185391 | DETACHED-EB | 1.000057 | 8.46 + 1.0 ppt dip at conj A | 6.57 at conj B | on target (dip untested) | none; SB*; Gaia astrometric 434 d |
| 62328710 | OTHER | f1 = 5.995 f_orb | none (A2 < 0.15) | none | neighbour 44" | nbr Gaia VARIABLE |

TIC 372683900: ELLIPSOIDAL; P_phot=1.476507 d (1.000003); min1=31.07+-0.31 ppt at phase 0 (conj B +0.09+-0.12); min2=28.18+-0.19 at phase 0.5011 (conj A -0.04+-0.13); pixel: on target; catalogue: not in VSX/Gaia-EB/Prsa/IJspeert/SB9, SIMBAD SB*
TIC 13106408: ELLIPSOIDAL; P_phot=2.637721 d (1.000082); min1=46.85+-0.33 ppt at phase 0 (conj A +0.08+-0.17); min2=40.63+-0.26 at phase 0.5009; pixel: on target; catalogue: none (VSX SR at 29" unrelated), SIMBAD SB*
TIC 372683622: ELLIPSOIDAL; P_phot=3.809282 d (1.000073); min1=7.73+-0.16 ppt at phase 0 (conj B +0.075+-0.040); min2=6.45+-0.19 at phase 0.4943 (conj A +0.044+-0.036); pixel: on target; catalogue: none, SIMBAD SB*
TIC 319185391: DETACHED-EB (grazing, fold-only); P_phot=2.678053 d (1.000057); min1=8.46+-0.30 ppt at phase 0 (conj A +0.06+-0.08) with a 1.04+-0.17 ppt, about 2 h dip; min2=6.57+-0.14 at phase 0.5102; pixel: on target (ellipsoidal signal; dip untested); catalogue: none, SIMBAD SB*, Gaia astrometric 434 d orbit
TIC 62328710: OTHER (delta Sct neighbour); P_phot=0.156480 d (1/5.995 of Gaia P); min1=none (Gaia-P A2<0.15 ppt); min2=none; pixel: neighbour Gaia DR3 2165710355333626240 at 44" (ZTF confirms 6.3906 c/d there, not on target); catalogue: neighbour Gaia VARIABLE

## Caveats
Only QLP is available, so there is no second pipeline. The Gaia-P fold in s3 has phase drift: its residual "dips" flip sign between sectors, so use the s6/s8 numbers, which are at P_phot. The s5b Roche model is a toy (blackbody at 800 nm, no reflection) and uses TIC radii, which look overestimated (13106408 and 62328710 overfill their Roche lobes). ExoFOP: no TOI or CTOI for any of the five (s10). The ms_oscillator TAP query failed.

## Files
s1_download.py/.log, s2_catalogs.py/.txt (+s2_err.log), s2b_catalogs.py/.txt, s3_lc.py + s3_<tic>.txt/.json + fold_<tic>.png, s4_pixels.py + s4_<tic>_s<sec>.txt/.npz + pix_<tic>_s<sec>.png, s5b_roche.py/.txt (s5_roche.* crashed), s6_pphot.py + s6_<tic>.txt/.json, s7_62328710.py/.txt/.json, s8_dip319.py + s8_<tic>_b10.txt/.json + dip_319185391.png, s9_gaia_corr.py + s9_gaia_nss.csv, s9b_conj_corr.py/.txt, s10_exofop.sh/.txt, common.py.
