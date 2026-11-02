# Cross-batch realized-depth correction audit

Completed 2026-11-02. Scope: accepted batches01?07, 70 targets. Original evidence was read only during audit. Root subsequently authorized the bounded correction of batches02/03/05/06/07. Exact pre-correction bytes, including all five previous manifests and RESULTS tables, are preserved in originals/ with originals-manifest.json. The original helper reports and attribution remain intact; separate DEPTH-CORRECTION.md supplements explain this review.

The trapezoid is baseline minus d*clip((w/2-abs(t-c))/k,0,1). When k>w/2, d is its amplitude parameter, while the actual peak decrement is d*min(1,w/(2*k)). Exact original-script AST replay retained original fit functions, bounds, masks, seeds and exceptions, while prohibiting artifact writes. All pre-correction primary events and timing/epoch/period fields reproduced exactly. Primary parity exceptions for371665307/314040568 and sector rejection427095568 were preserved.

## Changed primary medians

|Batch|TIC|Before ppt|Corrected ppt|Relative change|
|---|---|---:|---:|---:|
|batch03|290749976|2.406812247951|2.383432477400|-0.971%|
|batch05|47066501|22.857219166753|22.507649692484|-1.529%|

## All changed primary events

|Batch|TIC|Sector|Search cycle|Before ppt|Corrected ppt|Timing usable|
|---|---|---:|---:|---:|---:|---|
|batch02|62867537|56|394|20.623633669|19.701963040|True|
|batch03|386161311|90|258|23.168546340|17.673377246|True|
|batch03|427095568|85|216|0.412984412|0.100921242|False|
|batch03|427095568|85|218|1.855109461|1.709549799|False|
|batch03|290749976|97|603|2.745381553|1.140715397|True|
|batch03|290749976|97|604|3.365658690|2.998819787|True|
|batch05|47066501|42|4|25.802378850|18.476477587|True|
|batch06|306936928|33|217|21.330071875|20.930476341|True|
|batch06|306936928|87|672|22.349113967|22.228462632|True|
|batch07|374606776|85|206|32.996045732|32.357676661|True|
|batch07|338069871|85|477|14.284787825|12.399372197|True|

Eleven events in eight targets change. Two are previously rejected noise fits of427095568 and remain rejected. Seven dependent sector-parity entries are corrected in alias depth arrays/medians; alias cycles, pairs, masks, coverage and interpretations are unchanged. The largest individual relative changes concern the rejected noise fits and a shallow broad-dip target already classified PLAUSIBLE; they create no new sharp eclipse evidence.

## Secondary values and neighbor materiality

All131 measured-secondary event/pooled depth, phase, timing, width, selection and other numeric fields across25 targets replay exactly. No secondary depth correction is needed in batches01?07. Per-target original functions and measured-secondary records are in secondary.json and verification.json. The remaining targets have no deciding trapezoid secondary measurement; raw/box depth estimates are outside this amplitude bug.

There are60 direct fresh-pixel JSON neighbor-set comparisons; batch01 has10 differently organized/missing fresh-pixels paths and was not directly compared by this routine. Only two primary medians change, and both affected cases have direct neighbor checks. All other68 target thresholds stay identical because their median depths stay identical. Thus no affected neighbor membership changes are inferred from missing files.

- batch03 TIC290749976: stored approximate G limit 18.966667468 ? 18.977265868; capable sources remain 3. IDs: 4769034211197334912, 4769034211197335040, 4769034206900744064.
- batch05 TIC47066501: stored approximate G limit 16.589832519 ? 16.606565632; capable sources remain 1. IDs: 2586915362805716608.

The stored G-limit definition remains Gtarget-2.5log10(depth_fraction); the audit separately records exact pairwise flux-budget limits. Each neighbor required intrinsic-depth proxy scales by corrected/old median; its <=1 capability test does not change. Pixel arrays, deficits, centroids, aperture depths and image morphology are unchanged. No physical verdict changes: 0. Timing centers/errors/periods/epochs, event masks, durations and input photon/source bytes are unchanged. Source FITS SHA256s were checked against retained receipts.

## Applied files and reproducibility

applied-manifest.json is the authoritative47-path before/after list, with per-batch counts02:7,03:15,05:9,06:8,07:8. It supersedes the intermediate24-file staged overlay. originals-manifest.json hashes every preserved original; original/ additionally retains the first staging snapshots. post-correction-verification.json confirms all nondepth fields in eight changed measurement files remain exactly equal after removing allowed depth/ingress/provenance changes. All five frozen manifests verify. Mutable root/helper final verification receipts are excluded from the new manifests.

Primary scripts in the five affected batches now report realized depth and retain amplitude/ingress, so future primary reruns use the corrected formula. Original scripts are preserved under originals/. audit.py and finish.py document the pre-correction exact replay, and primary.json/secondary.json retain full fitted parameters and before/after events. Re-running the pre-correction audit against the corrected accepted tree is not a historical replay; use the preserved original scripts/evidence when reproducing the historical comparison. stage_corrections.py produced reviewable overlays, apply_corrections.py applied the authorized subset, and finalize_applied.py corrected dependent parity fields and verified/refroze manifests. No unrelated physical science was rerun.

Three raw-event images had affected displayed annotations, and the two corresponding raw contact sheets were refreshed. The other changed events were outside the six representative plot selections. Raw fit curves and retained window CSVs are unchanged. Reports include corrected event rows, medians and neighbor proxies; RESULTS changes only the two affected depth medians.
