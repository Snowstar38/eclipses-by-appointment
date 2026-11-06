from pathlib import Path
import json,hashlib,csv
b=Path(__file__).resolve().parent
for p in b.glob('*/REPORT.md'):
 s=p.read_text();s=s.replace('|\n\n|','|\n|');p.write_text(s,encoding='utf8')
s='''# Lead audit: Z001-Z008

Exact queue: eight frozen entries from fresh-band-next1000. No substitutions. Standards anchored to [workspace]/Fable 5.1/made/paper/short/sec_methods.html sections2.7-2.9 and candidate-review-delegation.txt.

## Completed bounded physical review

All eight raw source hashes, FITS TICID/SECTOR headers, nested Gaia IDs/G magnitudes and population/download receipt identity verified. Existing source files were read only; every new artifact is inside this batch. Representative raw morphology figures inspected for all eight, plus full-sector plots for Z001,Z004,Z005,Z006,Z007,Z008. Independent TESScut difference images and custom-aperture event extractions inspected in helper-contact.png. Same photons are explicitly not new temporal occasions.

Same-kind clock fits use conditional integers, trapezoid fits excluding failed/boundary solutions, formal covariance with cadence/2 and0.002d floor. Source-specific Gaia P,e,omega,Tp conjunction means and relevant corr_vec covariance are propagated locally; this is not a nonlinear orbit posterior. P values in RESULTS are conditional recurrence intervals, not uniform orbital solutions. No exhaustive all-sector fit was imposed.

Actual covered windows tested proposed submultiples2-6. Sparse cases also enumerate integer-cycle aliases; require timing_compatible as well as null-free. The alias scripts record depth, noise, core coverage, gaps and raw-source hashes, rather than calling flagged windows nulls. Z003 has many surviving aliases and remains PLAUSIBLE. Current MAST inventory for Z003 and Z005 checked. Newly available S109 for Z003 was independently extracted: gaps prevent a clean expected49.3168d null. Z005 S95 had no screen flag but a real raw eclipse was found in the fullsector plot, fitted, and added as its third occasion. It becomes P with doubling still unresolved.

## Deciding outcomes

Z001 P:20.484957d sharp eclipses, Gaia29.0687d fails; bycatch association, close-blend limit. Z002 P:34.873695d secure repeated eclipses, but Gaia conjunction offsets3.9-4.4 formal sigma, so geometry check fails. Z003 PLAUSIBLE:only two same-kind occasions and unresolved integer aliases. Z004 P:short0.871083d eclipse train, orbital kind/doubling and Gaia association incomplete. Z005 P:three epochs32.816227d and Gaia geometry consistent, but65.63248d double remains. Z006 P:10.356645d deep recurrence and secondary at phase0.2598; Gaia56.124d incompatible and exact-source external RV warning retained separately. Z007 C:independent localized primary extraction, repeated primary/secondary morphology, direct consecutive-sector30.22345d and source-specific Gaia geometry compatible within its covariance. Z008 REFUTED:selected-target signal is positively off target; short-period contaminant remains real.

Catalogue novelty is root owned. No exact-primary known EB match was communicated for these eight; this audit does not assign publication eligibility or prove discovery priority. Z006 RV literature warning is not a prior EB match and not a physical veto.

## Limits

No uniform eccentricity fit, nonlinear Gaia posterior, exhaustive period search or all-event fit. Close companions below TESS resolution cannot be arbitrarily ruled out. REFUTED is selected-target attribution, not a denial of the aperture eclipses. P cases preserve source/geometry failures instead of elevating eclipse reality alone to confirmation. Helper audit and final manifest must agree before handoff.

Contributor note: the project coordinator's appreciation of Sol and Terra was passed to the helper. The unflagged S95 recovery is a useful reminder that screen flags prioritize review but do not define the evidence.
'''
(b/'LEAD-AUDIT.md').write_text(s,encoding='utf8')
print('reports and lead audit drafted')

