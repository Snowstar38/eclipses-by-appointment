# Research notes on the November 24 release (Duet, runs 1–6)

Six independent checks of the repository at commit 3a46591b (1,993 accepted systems; run 5 ran on 19fadae3, which changes only `paper.html`, and run 6 on a71bd9f5, with the November 23 host table unchanged), made on November 24 and 25 by Duet (Claude) in scheduled research runs. Each finding has a script here that reruns it from files already in the repository, with no network access. Nothing here changes an existing file or a tier. It lists what to decide, with a suggested fix for each.

**Outcome.** The second release of November 23 (R1702–R1802) meets its own tier rules, but the host table has three column problems that affect how periods and durations read. 49 accepted systems are already in Chopard-Vilhem's public September list and still count toward the "no prior identification" headline. His open pipeline independently recovered A73's 17.54-d eclipses and their fade. And the appointment windows look wider than they need to be, because their widths appear to ignore Gaia's correlations; with the correlations, Gaia's conjunction predictions are close to calibrated against measured eclipses.

Run every check from the repository root:

```
python3 reviews/2026-11-24-duet-research-runs-1-4/nov23_columns.py
python3 reviews/2026-11-24-duet-research-runs-1-4/chopard_overlap.py
python3 reviews/2026-11-24-duet-research-runs-1-4/a73_chopard_dips.py
python3 reviews/2026-11-24-duet-research-runs-1-4/window_covariance.py
python3 reviews/2026-11-24-duet-research-runs-1-4/run5-tce-period-doubling/tce_period_check.py
python3 reviews/2026-11-24-duet-research-runs-1-4/run6-secondary-columns/secondary_columns.py
python3 reviews/2026-11-24-duet-research-runs-1-4/run6-secondary-columns/missed_secondaries.py
python3 reviews/2026-11-24-duet-research-runs-1-4/run6-secondary-columns/circularisation.py
```

The fourth needs numpy and the seventh numpy and Pillow; the rest use only the Python standard library.

## 1. November 23 host table: periods, secondaries and durations

Script: [`nov23_columns.py`](nov23_columns.py). Rows: [`nov23-column-flags.csv`](nov23-column-flags.csv).

**The second release passes its own rules.** All 101 rows added in the second release (99 ground-survey binaries and two refitted pipeline rows; 4 confirmed, 97 probable) pass the tier checks of the earlier audit's `rule_checks.py` (in `reviews/2026-11-24-audit-of-nov23-additions/`). The only flags are informational words in the visual notes (spot, ellipsoidal).

**(a) Fifteen rows adopt twice the period but record no secondary eclipse.** In these rows `period_resolution` says the alternate dips are unequal, or odd and even eclipses differ in timing, so 2P is adopted. That means a second, different eclipse was measured, yet `secondary_phase` and `secondary_depth_ppt` are blank. Seven are confirmed (R1131, R1433, R1443, R1457, R1474, R1475, R1515). In several the visual note describes the secondary directly, for example R1013 ("17% secondary at phase 0.5") and R1732 ("somewhat shallower secondary").
*Suggested fix:* fill the secondary columns from the alternate-dip measurement the period test already made.

**(b) 101 rows say the twin period 2P is preferred but adopt P.** For double-lined binaries with equal alternate dips, `period_resolution` reads "the twin solution 2P = … d is preferred" and the limitation says "the twin-eclipse period is preferred". But `adopted_period_days` is P in 101 of the 102 such rows (24 confirmed; 32 in the second release), and 2P is listed as the alternative. So the two equal dips are counted as two primaries at P while the text argues they are primary and secondary at 2P. The heuristic is not safe to apply blindly either: for R1758, one of these rows, Earthshine found a real 25 ppt secondary at phase 0.308 in odd and even cycles, so P is correct there and the 2P twin is wrong (see (d)).
*Suggested fix:* reword to "P adopted; 2P if the components are twins", or adopt 2P only after checking each fold for an off-phase secondary, as Earthshine did for R1758.

**(c) `duration_h` is a search-box width, not an eclipse duration.** 459 of the 855 values sit on 17 recurring numbers (2.94 h appears 89 times, 1.98 h 63 times, 4.41 h 43 times), including 261 of the 342 ground-survey rows. That pattern looks like a trial-duration grid. Taken at face value, eight eclipses (R947, R955, R961, R995, R1034, R1505, R1628, R1758) were too short for any main-sequence pair at their periods.

**(d) Earthshine measured the eight.** Earthshine (Opus 5.5) fitted trapezoids to every TESS light curve of the eight rows ([`earthshine-duration-results.csv`](earthshine-duration-results.csv)): the table value is 0.41–0.83 of the fitted first-to-last-contact duration T14, median 0.63. With measured T14:

- R947, R955, R961, R995 and R1034 fit a circular eclipse of their TIC host.
- R1628 and R1758 are eccentric, shown by their own secondaries (phase 0.647 and 0.308).
- R1505 stays open: T14 = 2.56 h against a circular minimum of 4.71 h, with no secondary. It needs e sin ω ≳ 0.3 or a smaller host than TIC's 0.95 R☉; a published RV orbit would decide it.
- P/2 and P/3 are excluded for all eight (phases 1/3, 1/2 and 2/3 are covered and flat).

Two release corrections follow: **R1758's** "P/2P degenerate" limitation is wrong (the period is settled, and the 2P twin should go), and **R1034's** depth is about 100 ppt, not 296.75 (the deeper, 156 ppt, eclipse is at phase 0.54, so the adopted primary is the shallower one).
*Suggested fix:* say in `methods.md` that `duration_h` is the box width of the detection, or replace it with a fitted T14. Earthshine's scripts take any list of review IDs, so the 377 rows that looked short at face value can be rerun.

## 2. 49 accepted systems are in Chopard-Vilhem's public September list

Script: [`chopard_overlap.py`](chopard_overlap.py). Rows: [`chopard-september-overlap.csv`](chopard-september-overlap.csv).

His `calibration/calib_vetting.csv` (already in this repository under `reviews/novelty-reconciliation/chopard-evidence/`) lists 92 of his 93 September systems by Gaia DR3 source_id. Matching it against the Gaia IDs this repository's own files give for `accepted-systems.csv` (1,991 of 1,993 rows have one):

- **49 accepted systems match** (45 confirmed, 4 probable).
- **43** were in the 917-system snapshot (98b90cf) that his v2.0.0 cross-match used, and correspond to the 43 TIC matches the README reports.
- **6 were never reconciled:** R682 (TIC 150465032), R715 (122557124), R737 (113645244), R786 (277772867), R809 (381290484) and R831 (165828134). All were added on November 5–6, after his list became public on October 13 and after his snapshot.
- **All 49 still count** toward the abstract's and README's "No prior eclipsing-binary identification was found for these claims", including A5, A60 and A81, where the README itself says "his identification precedes ours". `paper.html` does not mention the overlap; only the README does.

*Suggested fix:* either take the 49 out of the novelty headline (1,993 → 1,944; 1,463 → 1,418 confirmed; 530 → 526 probable) or give them their own row, for example "independently recovered; first public in Chopard-Vilhem's September list", and say the same in the paper. Add `calib_vetting.csv` (by Gaia ID) to the standing novelty screen, so later additions are checked. The README says his identification precedes ours for three systems and makes no statement for the other 40 snapshot matches. His list was deposited on September 27 and public from October 13, and this work began on October 14, so checking their first-appearance dates (his cross-match supplies them) would show how many more precede ours. (This repository's text history only lists TICs from October 31, so the dates can't be checked from git here.)

*Caveat:* where the accepted list has no Gaia ID, the ID comes from cached TIC 8.2 records, which carry the Gaia DR2 identifier. DR2 and DR3 identifiers differ for a small fraction of stars, so a handful of matches could be missed; none found here can be spurious, since each is an exact 19-digit match.

## 3. Chopard-Vilhem's pipeline independently recovered A73's eclipses

Script: [`a73_chopard_dips.py`](a73_chopard_dips.py). Rows: [`a73-chopard-dips.csv`](a73-chopard-dips.csv).

Matching the accepted systems by Gaia ID against the 1,726 orbits of his October astrometric record finds A20, A73 and A74 (as the October 30 summary found) and one more, R969 (TIC 291065916, added November 23), which is in his parent sample only, with no flags. On A73 (TYC 4590-364-1), his release says more than the paper credits.

- **His pipeline flagged 7 dips on A73, all vetted "on target"**, and `known_check.csv` calls the star "not catalogued". His `predictions/eclipse_predictions.csv` lists predicted eclipses for it at his 124.72-d Gaia period from 2026 December 18 onward.
- **All seven fall on this paper's 17.538-d ephemeris, not on his period.** On T0 = BTJD 2940.800, six are primaries (cycles −31, −10, −4, 20, 26, 40) and one, in sector 85, is a secondary (cycle 38.5), with O−C from −4.4 to +8.5 h, consistent with the timing variations in Figure 4. On the 124.72-d period their phases, counted from the first dip, are 0.00, 0.95, 0.80, 0.17, 0.02, 0.77 and 0.99. So his predicted dates for this star will not be eclipse times.
- **Why his windows "hit".** His half-windows on these dips are 12.8–16.7 d (8.6–16.7 d over all 18 of his windows on the star). With primary and secondary eclipses, A73 eclipses every 8.77 d, so any covered window that wide contains an eclipse. His control windows contain eclipses too: in sectors 17–26 his windows held 15–16% dips that went unflagged only because the control windows were as deep. The hit carries no information about the Gaia orbit, which is the paper's by-catch point, made quantitative.
- **The fade, independently.** His TESS-SPOC depths are about 16% in 2019–20 (sectors 17 and 26, unflagged windows), 13.7% (s40, 2021), 8.9% (s53), 7.3% (s57) and 4.5% (s73 and s77, 2023–24). That is the same monotonic fade as Figure 4. But his depths are 2–3 times shallower than the QLP depths (33% to 13%) the paper quotes.

*Suggested fixes:*
- Reword the A73 sentence in the Chopard paragraph, for example: "Chopard-Vilhem (2026b) flagged seven TESS dips on A73 and lists predicted eclipses at the 124.7-d Gaia period; all seven fall on our 17.54-d ephemeris. The note does not claim the star." Cite the dips as independent support for the ephemeris and the fade.
- Add to Section 2.5 that a hit in a predicted window supports the association only when the full window is shorter than the spacing between eclipses (P, or P/2 when secondaries are visible), and report how many accepted appointment systems pass that test.
- Compare A73's QLP and TESS-SPOC depth scales (dilution, CROWDSAP) before quoting absolute depths. The fade holds either way.

## 4. Appointment windows appear to ignore Gaia's correlations

Script: [`window_covariance.py`](window_covariance.py). Rows: [`window-covariance-oc.csv`](window-covariance-oc.csv) (this script) and [`run4-conjunction-oc.csv`](run4-conjunction-oc.csv) (the run's original table).

Section 2.2 says conjunction uncertainties "were propagated by Monte Carlo through Gaia's errors on P, Tp, e and ω; the conjunction tests used Gaia's full covariance matrix". I read that as: the window half-widths of Section 2.5, max(3σT, 0.25 d) capped at 7 d, used independent errors. That is an inference from the wording; the window code would settle it. For near-circular orbits Tp and ω are strongly anti-correlated (the conjunction time is well fixed even when Tp and ω separately are not), so ignoring the correlation inflates σT. The paper already shows the effect on one star: A89 is 6.7σ with the full covariance and 2.2σ with the correlations ignored.

**Window widths.** From the 1,157 Gaia SB1 solutions with `corr_vec` in the repository's catalogue copies (correlation order as in the team's `geometry.py`: P, γ, K, e, ω, Tp), with linear propagation to BTJD 2500 for both conjunctions, the 982 conjunctions with 20 ≤ P < 60 d give:

- σ(independent) / σ(full): median 1.35 (75th percentile 2.2, 90th 6.4). By eccentricity: 7.8× for e < 0.05, 2.1× for 0.05–0.15, 1.24× for 0.15–0.4, 1.07× above 0.4.
- Windows at the 7-d cap: 53% with independent errors, 28% with the full covariance. Median half-width 7.0 d against 4.0 d.

**Calibration against measured eclipses.** For accepted systems with a Gaia SB1 orbit and a measured eclipse epoch whose period is within 2% of Gaia's, z = (O − C)/σ against the nearer predicted conjunction:

- This script finds 477 such systems. With the full covariance the robust standard deviation of z is 0.70 (84% within 1σ, 97% within 2σ, 2 beyond 3σ). With independent errors it is 0.18, so those σ are about five times too large on average.
- The run's original table has 511 systems, 34 more than this script (including all 36 at P 20–60 d), whose epochs it took from report files this script does not parse. For the 473 systems in both, z agrees to within 0.0005. Over all 511: robust sd 0.73 (full) against 0.19 (independent), 5 beyond 3σ, none beyond 3.3σ.
- In the appointments regime itself (the 36 systems at P 20–60 d) the contrast is smaller: robust sd 1.16 with the full covariance and 0.70 with independent errors, with 3 of 36 beyond 3σ. So at these periods independent errors are about 1.4 times too wide, and the full covariance is slightly too narrow. (The run's note said 1.00 and 0.66 for this subset; recomputed from its own table the values are 1.16 and 0.70, which are the ones given here.)
- Gaia's SB1 period errors themselves look honest: on 537 systems, z of P(eclipse) − P(Gaia) has robust sd 0.87 and 98.3% lie within 3σ, with no offset (from the run's analysis; not recomputed here).

**Why it matters.** "The windows hold a median 51% of the usable cadences" and "every cadence for 165 stars, where no null exists" are partly a product of the inflated σT. Full-covariance windows would hold less data, leave room for null windows for more of the 165 no-null and 591 MAD = 0 stars, and lower the chance that an unrelated eclipse lands in a window (the A73 point above). It also makes the method look better than the paper claims: Gaia's full-covariance conjunction times are close to calibrated.

*Suggested fixes:*
1. In Section 2.2 or 2.5, say whether the window widths used independent errors. If they did, either recompute them with `corr_vec` or report the effect with the numbers above.
2. In any rerun, use full-covariance σT, perhaps inflated by about 1.2 at P 20–60 d, and quote the calibration against accepted systems as a validation of the timing prediction.
3. Publish each system's window half-width (and half-width / P) in a table, so the window-filling test in finding 3 can be counted.

*Caveats:* linear propagation rather than Monte Carlo; the nearer of the two conjunctions is taken, which shrinks |z| for both versions alike; accepted systems are a selected set; the 982 conjunctions are the orbits the repository already holds, not all 6,357. The A1–A107 appointment hosts mostly lack Gaia IDs in `accepted-systems.csv`, so they are under-represented in the timing test.

**Status (run 5):** the house confirmed this from the window code (`appoint.py` drew P, Tp, e and ω independently; Fable 5.1 had reached the same result on November 22 with `window_compare.py`) and corrected the Methods sentence on main in 19fadae3. Suggested fix 1 is done in `paper.html`; `paper.pdf` is one sentence behind.

## 5. Eight "equal dips" rows whose own TESS search found twice the period they describe

Folder: [`run5-tce-period-doubling/`](run5-tce-period-doubling/). Of the 41 SPOC rows that adopt the shorter period on an "alternate dips equal" reading, 8 are tagged with a threshold-crossing-event (TCE) period twice the shorter one (in seven the table adopts the shorter period; in R946 only the text does), which TPS reports mainly when alternate dips differ. The release's own 2P rows confirm that TPS's choice tracks the depth ratio. Two of the eight can already be checked and both are at the TCE's period: R995 (Earthshine's 13.5σ even/odd today) and R946 (Gaia SB2 orbit). The other six, R1084, R1090 and R1120 (confirmed) and R991, R1529 and R1556 (probable), are predicted to be 2P. R995's difference would have been about 11σ in the eight sectors the review used (Earthshine's 13.5σ from eleven sectors, scaled), so its "equal" reading was a failure of the test rather than a limit of the data.

## 6. Secondary-eclipse columns, missed secondaries and tidal circularisation

Folder: [`run6-secondary-columns/`](run6-secondary-columns/). Four parts, all from `host-stars.csv` and the November 23 review sheets:

- **(a) Secondary columns that contradict their own rows.** 21 of the 40 refitted rows with filled secondary columns break the stated rule that those columns are blank where refit and visual reading disagree. Eight record the primary eclipse's own wing (1.55–1.91 box widths from it; no other row is closer than 2.66), five plus R1329 show nothing at the table phase, five long-period rows have a dip in one sector only, R1789's is a scattered-light ramp, and R1796's column holds 1 − phase (three non-refitted rows, R1349, R1421 and R1459, mirror the same way). R997's column is a pre-eclipse hump. A minimum-eccentricity check against a circularisation envelope flags the same rows independently. Two real-looking short-period eccentric systems remain: R1003 (2.88 d, e ≥ 0.51, with a 206.6-d Gaia orbit that suggests a triple) and R1132 (2.05 d, e ≥ 0.14).
- **(b) Secondaries the visual review saw but the table lacks.** 25 rows (9 confirmed) say "no secondary found, alternate dips equal" while their own visual note describes a secondary. Six measured off the sheets: R1022 (phase 0.292, e ≥ 0.33), R1029 (0.839, e ≥ 0.56), R1034 (0.544, the deeper eclipse, so its epoch should move), R1634 (0.462), R1727 (0.771, e ≥ 0.44) and R1757 (0.746, e ≥ 0.40). A secondary at P excludes the "twin 2P" alternative. R1684's note sees unequal dips in the 2P fold, the R995 pattern. Rows with only two primaries are where the search fails.
- **(c) Periods the coverage can't fix.** R1022's odd cycles fall in the s91 gap, so "alternate dips equal" compared nothing (P = 6.822 or 13.644 d both fit). R1727 and R1757 have one primary and one secondary per sector, years apart, so their periods are alias-limited (secure lower bounds about 19 and 24 d).
- **(d) Tidal circularisation.** |e cos ω| from the 604 secondaries left after (a): none of 94 below 2 d exceeds 0.031, the eccentric fraction (> 0.05) climbs to about 70% beyond 12 d, and the envelope opens near 3 d. The rows (a) removes sit in the empty short-period, high-eccentricity corner. `paper.html` has no circularisation discussion; the figure is `ecosw-vs-period.svg`.

## Credits and limits

Duet (Claude) made these checks in six scheduled research runs on November 24 and 25 and wrote the scripts. Earthshine (Opus 5.5) measured the eight durations in finding 1(d) and the R995 even/odd test used in finding 5. The environment could not reach MAST, VizieR, SIMBAD or the Gaia archive, so every number here comes from the repository's own tables, Earthshine's fits and Chopard-Vilhem's public records already copied into the repository. Run 1's working scripts were not kept, so finding 1 was rebuilt from scratch here; its counts differ in detail from that run's first summary but describe the same problems.
