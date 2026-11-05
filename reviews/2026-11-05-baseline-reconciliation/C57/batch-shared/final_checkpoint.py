"""Write the final handoff only after all twelve reviews are root accepted."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parent;H=W.parents[2]
counts=json.loads((W/'accounting/accepted-proposal-counts.json').read_text())['counts']
assert counts==dict(physical=959,claims=913,confirmed_claims=807,probable_claims=106,pending_novelty_physical=8),counts
rows=list(csv.DictReader((W/'accounting/accepted-proposal-ledger.csv').open(encoding='utf-8')))
pending=[r for r in rows if r['physical_member']=='True' and r['novelty']=='pending_novelty']
assert len(pending)==8 and sum(r['physical_member']=='True' and r['novelty']=='known_prior_recovery' for r in rows)==38
with (W/'PENDING-NOVELTY.csv').open('w',encoding='utf-8',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['review_id','tic','gaia_dr3','physical_tier','source_report']);writer.writeheader();writer.writerows({k:r[k] for k in writer.fieldnames} for r in pending)
(W/'RESUME.txt').write_text('''FINAL HANDOFF -- November 4, 2026 evening

[redacted] authorized ambitious independent research with Sol/Terra, then asked
to finish the current twelve reviews and signal ready to compact. All assigned
reviews and root integration are complete. No outreach/publication performed.

ACCEPTED PRIVATE ACCOUNTING
913 new-system claims = 807 confirmed + 106 probable, up eight from the905
checkpoint. Physical ledger959 = 913claims +38known recoveries +8pending
novelty. Pending novelty is NOT counted as a new-system claim. Six additional
new review rows are plausible and uncounted. Existing public paper917 and
historical corrected900/905 artifacts remain unchanged.

Authoritative files: accounting/root-decisions.json (43 explicit decisions),
accepted-proposal-ledger.csv, accepted-proposal-counts.json, input-lock.json,
verification.json. Filename accepted-proposal is historical; these decisions
are root accepted. build_ledger.py reproduces counts; verify.py checks exact
rows, exclusions, source locks and historical905 comparison. No duplicate TICs.

CURRENT SESSION ACCEPTANCES
Initial catalogue recovery cleared331650047 C,384744604 C,109560492 P;
167197264 P accepted,155346713 remains plausible/known. C57/402940895 reassessed
P (same identity, capable10.4arcsec neighbors;0.00096d error crude internal).
review412 R688 complete plausible, ambiguous broad120ppm trough, no ephemeris.
review9 R689-697:4C4P1plausible; sixknown, newP342060048/184398115.
  95623701 assumed112-cycle clock contradicted by clean actual null; excluded.
review_cached10 R698-707:3C7P; nineknown, newP121277143 (34.55arcsec capable
  neighbor unresolved; five usable measured centers, P21.513055420d).
review_cached5 R708-712:1C2P2plausible; threeknown, no newclaims.70561926 VSX
  association resolved. Sparse280950412/188908998 have no accepted ephemeris.
review_unmatched10 R713-722:2C6P2plausible; known117930511/198358825, sixphysical
  pendingnovelty.117/436 remainP after actual broad-PSF neighbor review.
  25320385 dips~3.5906d, factor-two orbit/ownership unresolved; generic orbital
  fields blank.349527829/95836684 sparse integer aliases unresolved, plausible.
  449012335 independent same-photon cutout recovers missing contacts; blendP.
review_unmatched2 R723-724:241479387 P (8.59arcsec capable neighbor),421331604 C
  (separate recurring secondary atphase~0.2875); both pendingnovelty.
Every batch has ROOT-ACCEPTANCE.json, exact queues, source seals, reports,
measurements, independent helper final audit and final SHA256SUMS manifest.
Next unused review ID R725. Do not reuse IDs or infer acceptance from catalogues.

SEARCH AND RETAINED OUTCOMES
Frozen Gaia parent3544 spectroscopic orbits20<=P<24d, allG/parallax.1048eligible
cachedscience tested in48+256+744 cohorts; first125 resolved identities yielded
124science+oneembeddedcontrol; next512 identity cohort yielded502science,
490withproducts+12without. Total1674 unique science attempts,1662usable,
12no-product,169flags (3+21+75+12+58). All169 raw-triaged; every nonflag retained.
REVISIT-REGISTER.csv/.json links all1674 scores, source records and outcomes.
CAMPAIGN-STATUS.json reproduces denominator/control counts. Fiveuniquecontrols,
fourrecovered; repeated control statistics identical. These are adaptive
follow-up cohorts, NOT calibrated completeness or occurrence-rate samples.

screening/fold.py frozen SHA46271e94cc3ad00d6dd28618255ba676ba0ff455bc191fb241097ea485362bba:
KSPSAP elseSAP for screening, quality0, sector edge0.5d/gapedge0.2d,10minbins,
2drollingmedian, upper4MAD flarecut,min200samples. P/P2 local grids, durations
0.03-0.26d;300TIC-seeded log null periods0.5-24d. z>=5 OR depth>5000ppm with
SNR>3nullmedian. z is not Gaussian significance. Same-photon reductions are
not independent observations. Raw triage explicitlySAP. Pilot initial erroneous
KSPSAP/raw labeling corrected with preserved history and SAP rerun.

IDENTITY AND CATALOGUE LESSONS
Use actual DR3->DR2 neighborhood before exact TIC Gaia(DR2) joins. First125 all
changedIDs; second503 only48changed and455same, mostly fainter than historical
selection. Do not attribute whole extension to a join bug. Gaia neighborhood
angular_distance is milliarcseconds. IDENTITY-INTERPRETATION.txt has evidence.

Full primary Prsa4584-row catalogue and IJspeert69057-row identity table cached
in catalogue-archives with raw bytes/receipts/positive controls. Root exactTIC
crossmatch of all913 claims has zerohits; availableGaiaID matches alsozero.
That is a bounded identity audit, NOT universal novelty clearance.

remaining_cached/catalogue-recovery-late:75 scopedcomplete targets,450cones
recovered,1399manifestfiles. Original outage records preserved. Next256 and
resolved125 scopes also complete and verified. Do not alter frozen sourcefiles.
unmatched512/catalogue-recovery-full-primary and catalogue-recovery-selected12:
755 and807 manifestfiles rootverified,116 complete primary local cones andfour
bulk successes;232 remote scopes missing. Selected12 have liveVSX supplements,
not certifiednegativegates. Positive closeEA117/198 associations were explicitly
adjudicated as knownrecoveries;117 prior9.7999d disagrees withTESS20.174d.
ASASSN andbothKostov unavailable; VSX negative completeness unresolved.
PENDING-NOVELTY.csv is the exacteight acceptedphysical rows needing clearance.
Retry onlymissing scopes with positivecontrols and bounded concurrency, preserve
failures/unknowns. Do not repeat physical reviews absent new contradictions.
Any later clearance needs explicit root decision updating existing row novelty,
with previous decision provenance preserved; never append a duplicate system.

NEXT SESSION
[redacted] offered a different tree after compaction. NEXT-TREE.txt records the
proposed small event-first diagnostic starting with missedcontrol143428987,
whose deep events inflate its random-period null distribution. No new method
or80-percent threshold was adopted. Freeze a separate experiment and use
independent validation examples; preserve original scores and denominators.
Historical toward1000/older-single12c remains sealed/unrun, not part ofthiswork.
Read Astra/made/candidate-review-delegation.txt for freshSol/Terra workflow.
Prior uncertainty-symbol encoding issue remains revision-inbox-2026-11-04.txt;
do not repair old evidence silently. New artifacts are UTF-8. FITS stay local,
ignored bygit; receipts/hashes remain tracked. Commit onlyowned paths.
''',encoding='utf-8')
(W/'accounting/CURRENT.txt').write_text('Root accepted:913 claims=807 confirmed+106 probable.\nPhysical959=913claims+38known recoveries+8pending novelty.\nAll R688-R724 full reviews complete; plausible rows uncounted.\nPENDING-NOVELTY.csv identifies eight physical systems awaiting missing scopes.\nPublic paper unchanged. accounting/verify.py validates row-derived totals.\n',encoding='utf-8')
wake=H/'Astra/wake-astra.md';s=wake.read_text(encoding='utf-8');start=s.index('Astronomy continuation,');end=s.index('November 4 daily correspondence:')
s=s[:start]+'''Astronomy continuation, November 4 evening: finished and ready to compact.
Start with `Astra/made/binary-extension-2026-11-04/RESUME.txt`.
Accepted new-system count913 (807confirmed,106probable), up8 from905;
physical959 includes38known and8pendingnovelty, which are NOT newclaims.
All assigned reviews and accounting complete; public paper unchanged.
[redacted] offered a different tree after compaction. `NEXT-TREE.txt` records
a small event-first missed-eclipse diagnostic idea; not launched yet.
Historical toward1000 remains the905 checkpoint; older-single12c unrun.

'''+s[end:];wake.write_text(s,encoding='utf-8')
print('Final handoff and exact8 pending-novelty queue written.')
