# Independent Terra audit ? exact seven



Reviewed the current section 2.7 definitions and candidate-review-delegation guidance. Physical review remains separate from novelty. No ledger or public edits.



## Evidence review



- E001 / TIC 12319637: three discrete raw-SAP eclipses, centered deficit in S18 cutout and independent aperture recurrence. Same-kind timing and covered-null alias artifact support 25.0127052 d. Only this integer clock survives both timing compatibility and covered-null checks in tested grid. The nearby catalogue EB has a different 1.76684 d clock; retain explicit source attribution rather than treating cone match as target identity.

- E004 / TIC 55662895: S1/S2/S95 broad but bounded eclipses have identifiable ingress and egress; S98 is a step and excluded. Independent pixel check places positive deficit on target pixel (4,4), +16.1105 flux units / 0.8882%, whereas bright G11.35 neighbor pixel (2,5) has negative deficit -7.1301 / -0.2582%. Different pixel dilution precludes interpreting these as intrinsic source depths, but signs and spatial morphology support target origin. Conservative 0.06 d event allowance is appropriate for broad-shape scatter; do not label it a formal trapezoid error. Adopted revised period 36.9723882178 d, covariance period allowance 0.0010726835 d.

- E005 / TIC 141428309: S1/S93 shallow minima and S2/S98 deep minima are distinct kinds; S94 isolated extreme is not a timing datum. Primary interval49 gives 54.5246952 d, secondary interval46 independently gives approximately54.5247 d. Confirmed requires explicit combined-kind alias elimination; primary-only alias artifact admits other integers.

- E006 / TIC 144157102: S100 deep event is convincingly target-centered. Shallow S64 and sparsely sampled S10 are compatible with the other conjunction. S10 fit is unusable and must not supply a precision ephemeris. Many integers survive shallow-pair coverage; PLAUSIBLE is warranted pending a better same-kind clock, even though Gaia association is consistent and eclipses appear real. This is completed uncertain science, not an unperformed check.

- E007 / TIC 149477061: S2 shallow event produces target-centered deficit and is credible; the other viewed features are broad, baseline-dependent or gap/step affected and do not establish a unique recurrence. PLAUSIBLE single-event interpretation; current-sector receipt does not turn a coverage gap into a null.

- E008 / TIC 149847663: deep S4/S5 events and shallow S4/S5 events repeat separately with matching approximately31.547 d intervals. Pixel image supports target origin and custom aperture recovers eclipse. Full nonlinear Gaia covariance confirms modest but real primary conjunction tension; PROBABLE, not confirmed. Relevant A offsets have 99.73% intervals[0.1256,2.7401] and[0.1353,2.8228] d, two-sided sign tails0.00090/0.00082. Secondary B offsets include zero at3sigma. This is orbital-association tension, not evidence that the eclipses are detector artifacts.

- E009 / TIC 168983144: three bounded eclipses, target-centered S61 deficit, repeated morphology. The raw-only timing grid retains 53.4617 and26.7309 d aliases as well as35.6411 d because cycle gaps have gcd3. Gaia source-specific period supports35.6411 d association; report that support explicitly and do not claim a uniquely measured photometric integer count.



## Independent numerical checks



helper_hash_pixels.py recomputed all39 source hashes and7 cutout hashes: 46/46 match. helper_nonlinear_gaia.py uses100000 draws per target, seed50701 and each source SB1 covariance with P,e,omega,Tp subindices0,3,4,5 from Gaia lower triangle. Fixed nominal integer cycles avoid half-cycle wrap artifacts. Gaussian covariance draws and edge-on conjunction geometry are model assumptions; no inclination is measured. Helper files preserve numeric receipts. Final results/clock cross-check completed: exact seven rows in queue order; four confirmed, one probable, two plausible; all five populated periods/errors exactly match frozen clocks, two unresolved clocks blank. All seven reports match their row tiers. helper-final-freeze-audit.json records final hashes. E009 explicitly discloses photometric integer ambiguity and Gaia-assisted choice.



Contributor note: Thank you, the project coordinator. Keeping the ambiguous clocks visible preserves the value of the observations without making the count decide the classification.

