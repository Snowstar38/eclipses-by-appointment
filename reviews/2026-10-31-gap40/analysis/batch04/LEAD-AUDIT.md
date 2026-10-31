# Batch 04 lead audit

Exact frozen queue: ten TICs, positions 31-40; batch-only writes. All ten physical reviews are CONFIRMED with COMPLETE bounded execution. Catalogue novelty remains separate and centrally supplied. No public/canonical files edited.

I inspected the ten-target raw-event and difference-image contacts, numeric free-midpoint fits, Gaia comparison, capable-neighbour screens and helper exceptions. All show localized repeated raw eclipses; measured midpoints, rather than historical predicted centers, determine the periods. Timing input errors are max(formal covariance, half cadence), with regression covariance inflated for excess residual scatter. They are descriptive allowances, not calibrated coverage. At most three spread QLP sectors per target were reused with FITS hashes. Alternative cutout reductions share the TESS photons.

Corrections from independent helper audit: singular timing fits for 77176486 cycle188 and 37948318 cycle93 were removed from timing (raw windows retained). Sparse asymmetric 219033622 cycle32 was removed, leaving three measured events and a shorter S15/S23 timing baseline. No selected S76 usable window is called a null. Machine column primary_epoch_btjd is an observed reference eclipse, not a demonstrated deeper primary.

436724968 modest QLP parity depths required follow-up. Historical independent S43 cutout depths for eight odd/even events span35.34-37.19ppt without stable alternation; Gaia matches the2.73217d spacing. We retain that period with aperture/baseline depth limitations. Pooled300969635 parity is confounded by sector depths; no doubled period is established. No target here required a proven doubled-period correction.

37948318 absolute centroid offset15.1arcsec is material and explicitly preserved, distinct from3.51arcsec relative to blended light. The capable53.65arcsec neighbour is opposite the deficit displacement; helper per-event pixel losses favor the target. Attribution passes at TESS resolution with centroid/crowding limits.77176486 near TESS orbital timescale is assessed from actual raw events and localization, never automatically vetoed.

Full SB1 correlation matrix is read in P,gamma,K,e,omega,Tp lower-triangle order, with P,e,omega,Tp submatrix used for linear conjunction propagation. Approximate central durations are descriptive TIC/main-sequence comparisons, not hard bounds or detailed binary modeling. No arbitrary sigma veto or all-event Monte Carlo mandate is imposed.

Final scripts, numeric artifacts, raw/source/cutout hashes and helper evidence accompany the reports. Private paths are provenance for local review and require sanitization in publication export. Anonymous contributor note: thanks to the independent audit contributor for identifying unconstrained fits and checking crowded-field pixels. <3

Final771 background follow-up: background_check.py records per-event quality-zero target and both capable-neighbour pixel losses, outer-pixel common-mode levels and flags. Cycle187 has11.99electrons/s target deficit against -0.027outer median; later cycles have common-mode shifts that are explicitly disclosed. FLUX_BKG=0 is uninformative. The earlier-sector raw repeats and compact historical stack provide the supporting evidence. Helper numeric hashes refreshed after exclusions.
