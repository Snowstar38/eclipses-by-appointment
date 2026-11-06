"""Lead reports and exact queue results, provisional until independent helper seal."""
import json,csv,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
texts={
'352725084':'''# RS026 — TIC 352725084

Lead physical verdict: PLAUSIBLE target single eclipse. No publication claim. Fresh Terra helper independently agrees with the deciding morphology and pixel interpretation; see `HELPER-NOTE.md` and `helper-hash-identity-audit.json`.

## Identity, raw morphology and recurrence

Exact queue identity is Gaia DR3 2023283918354633344 (G 11.9167), not neighboring TIC 352725094. FITS TIC/sector headers and SHA256 checks accompany `lead-context.json`. Quality-zero, finite positive raw QLP SAP flux was examined in every available QLP sector: 14, 40, 54, 80 and 81. Full-sector plots show broad variability and offsets in the earlier data, with one convincing discrete event in S81. The event has sharp resolved ingress and egress and a rounded, approximately flat bottom. A local sloping-baseline trapezoid gives BTJD 3521.833249, formal covariance timing error 0.000715 d, depth 38.736 ppt, total duration 0.410736 d and ingress 0.079341 d. This is a descriptive single-event fit, with residual RMS 2.620 ppt; its formal error is not a calibrated timing-systematics allowance.

The current MAST Tesscut inventory independently lists only those five sectors; no newer available sector was silently ignored. An event-anchored Gaia-period recurrence check finds the earlier S40 center at 2404.616 d in a gap and no other fully covered repeat. Earlier full-sector curves do not supply another convincing same-kind eclipse. Missing coverage is not a clean null. There is no measured orbital period, no integer-cycle solution, and no basis for treating this singleton as probable merely because it occurs near a Gaia conjunction.

## Source pixels and alternative extraction

A seven-pixel S81 TESScut cube yields a sky-subtracted central 3x3 extraction recovering 35.391 ppt median core loss. The out-minus-in difference peaks at pixel (4,4), against target WCS (3.921,3.703). Positive-deficit centroid (3.829,3.733) is 0.0966 pixel from the target; this is a descriptive centroid, not a formal localization confidence region. The image supports target attribution. The independently chosen aperture uses the same TESS photons and is not another observing occasion.

The IJspeert neighbor TIC 352725094 / Gaia DR3 2023282440885901056 lies 45.285 arcsec away and around two pixels to the right in this sector. Its position does not host the S81 deficit peak. We do not substitute that neighbor for the target or automatically assign its prior classification to this event. Nearby unresolved sources and pixel calibration limit absolute attribution precision, but the resolved known neighbor does not explain this image. `lead-localization-81.png`, `lead-pixel-diagnostics.png`, neighbor table, cube hash and numerical extraction are retained.

## Gaia association and plausibility

The exact target SB1 orbit gives P=42.969910806 d, e=0.653118, mass function 0.03629 solar masses. Its conjunction-A extrapolation is BTJD 3523.04038, 1.20713 d after the event, with fixed-cycle local covariance sigma 1.47567 d. The event is consistent within that broad orbital uncertainty; this is not an ephemeris measurement, evidence of recurrence or secure association. The covariance uses the target's own P,e,omega,Tp correlations (SB1 parameter order documented in `lead-gaia-covariance.json`). The short finite eclipse shape is physically reasonable; no stellar-radius or inclination characterization is claimed. A nonlinear posterior and exhaustive alias search were not performed because no measured repeat exists.

## Catalogue scope and disposition

The shared sealed catalogue bundle is reused with hashes in `lead-central-catalogue-receipts.json`. Target VSX and ASAS-SN cones have no match; exact target Gaia DR3 EB query has no row; SIMBAD classifies the target SB*, not as eclipsing. Prsa and IJspeert have no exact-target eclipsing identity; the IJspeert neighbor is adjudicated above. Vetted Kostov tables 3/4 have no target match. The bounded 244-eprint identifier search has no exact TIC/Gaia hit, without establishing exhaustive discovery priority. These successful scoped checks do not promote a singleton. Keep the physical verdict separate from novelty.

Limitation and next check: observe another same-kind event and determine its clock; target-localized single events alone remain plausible under current methods 2.7/2.9. No addition to a confirmed/probable register is authorized by this report.
''',
'394405964':'''# RS027 — TIC 394405964

Lead physical verdict: REFUTED selected eclipse signal (background/extraction transient). No publication claim. Fresh Terra helper independently agrees with the deciding morphology and pixel interpretation; see `HELPER-NOTE.md` and `helper-hash-identity-audit.json`. This finding does not refute the existence of the Gaia spectroscopic binary or every possible eclipse on the star.

## Identity, morphology and available sectors

Exact identity is Gaia DR3 5853244721628454528, G 11.971833. Quality-zero finite positive raw QLP SAP flux was inspected across sectors 11, 12, 38, 65, 99, 100 and 101, with exact file hashes and headers. The S12 selected trough near BTJD 1625.68 looks rounded in QLP SAP but starts near the sector boundary, amid a large transient. A descriptive trapezoid fit gives center 1625.679609 d, depth 30.5 ppt and duration 1.121 d; the early baseline is inadequately bracketed for the stricter two-sideband reduction check. This fit is retained as an algorithm output, not accepted astrophysical timing. The other S99 flags near 4052.1 and 4068.15 are broad gap-split level structures, without convincing paired ingress/egress. The S100/S101 offsets similarly follow gaps. Smooth variability and level changes are not repeated same-kind eclipses.

Current Tesscut inventory includes S102 beyond the downloaded QLP inventory. The fresh helper extracted a seven-pixel S102 cube. At the S12-anchored Gaia-period center BTJD 4137.47237, the quality-zero core has 291 samples and both side windows have hundreds of samples, but severe background/noise and a steep neighboring brightening make the extraction unsuitable as a clean null or a repeat. The helper plot and exact FITS SHA256 12c103c63dc396f15cab10ee4c9d3267960631b1c7ac25277bf589a4d709fa2f are retained. Current sector inventory was therefore checked and the added sector attempted; its failure to constrain recurrence is not a non-detection. The refutation below concerns the selected S12 and S99 signatures, rather than claiming a complete all-sector eclipse exclusion. A fresh sector can matter to a different new signal, but does not turn the measured sky transient into an eclipse.

## Deciding pixels and alternative extraction

The seven-pixel S12 cube directly tests the selected event. At its center, raw central 3x3 flux brightens by approximately 146 ppt relative to the comparison sides and outer-pixel median background brightens by approximately 195 ppt. After subtracting that outer median background, the central 3x3 is flat with core loss -3.693 ppt, and the central pixel likewise has loss -5.351 ppt (negative means brightening). The approximately 30-ppt QLP SAP trough is absent. The out-minus-in target deficit is negative; positive-deficit weights within three pixels sum to zero, so the centroid is undefined (stored as null), not a localization. This is an invalid source centroid rather than a successful on-target attribution. The extraction status `aperture-measured-centroid-invalid` explicitly preserves this distinction; no valid centroid is asserted.

`lead-pixel-diagnostics.png` shows the sky pulse and raw pixel brightening, with stable background-subtracted source flux after initial settling. `lead-localization-12.png` shows the field background gradient. These independent aperture choices use the same photons. The combination supplies positive evidence for a background/extraction origin of the selected trough, beyond mere failure to repeat. There is no observed eclipse ephemeris and no warranted integer-cycle alias fit.

## Gaia and catalogue context

The exact target SB1 orbit has P=28.222390626 d, e=0.386578 and mass function 0.04044 solar masses. Its conjunction-B prediction 1625.02939 d is within 0.65022 d of the QLP fitted trough, with local covariance sigma 0.78703 d. Temporal consistency does not rescue a feature rejected by its pixels. S99 fitted centers are artifact descriptors; the fact that one happens to lie near another extrapolated conjunction is not repeated eclipse evidence.

Shared sealed catalogue checks identify the target as SIMBAD SB*, no exact Gaia EB row, no target Prsa/IJspeert prior identity and no vetted Kostov table3/4 match. The VSX 33.02-arcsec entry is Gaia DR3 5853243244160324480, type L and much fainter; it is a distinct generic variable, not an exact target eclipsing classification. ASAS-SN has no cone match. The bounded identifier literature search found no exact target hit, without exhaustive-priority claims. Catalogue novelty cannot make the selected instrumental signal physical.

Limitation and next check: obtain usable independent photometry or other new observations if searching for a different eclipse; no claim of a complete target non-detection is made. The present selected S12 trough and S99 level structures do not qualify as eclipses.
'''}
for tic,txt in texts.items():(B/tic/'REPORT.md').write_text(txt,encoding='utf8')
fields='sample_id,tic,gaia_dr3,completion,tier,period_d,period_error_d,source_association,gaia_association,catalogue_status,publication_eligible,report,limitation'.split(',')
with (B/'RESULTS.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in csv.DictReader((B/'queue.csv').open()):
  tic=r['tic'];singleton=tic=='352725084';w.writerow(dict(sample_id=r['sample_id'],tic=tic,gaia_dr3=r['gaia_dr3'],completion='complete',tier='PLAUSIBLE' if singleton else 'REFUTED',period_d='',period_error_d='',source_association='target-supported' if singleton else 'selected-background-artifact',gaia_association='consistent-with-broad-uncertainty-unproven' if singleton else 'selected-signal-not-astrophysical',catalogue_status='scoped-no-target-prior-EB',publication_eligible='false',report=f'{tic}/REPORT.md',limitation='Single event; no measured clock or repeat.' if singleton else 'Selected feature refuted; S102 extraction background/noise-limited; not an all-sector eclipse exclusion.'))
