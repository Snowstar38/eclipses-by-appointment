# Realized trapezoid depth correction — 2026-11-02

The cross-batch audit found that fitted trapezoid amplitude d overstates the actual model decrement when ingress k exceeds half-width w/2. Depth now means d*min(1,w/(2*k)). The original fit amplitude and ingress are retained explicitly. Original accepted evidence and prior SHA256SUMS/RESULTS bytes are preserved under ../depth-audit/originals/batch05/.

Exact original-function replay reproduced every event, timing, fit selection and secondary numeric field before correction. Across batches01–07, 11 primary event depths in eight targets and two median depths change; all 131 measured-secondary event/pooled values stay unchanged. No timing, width, quality mask, verdict or capable-neighbor membership changes. Pixel deficit images and extracted photon values stay unchanged; the two affected neighbor flux-budget proxies are rescaled only. Original helper audit attribution is retained; this note is a separate correction supplement.

See ../depth-audit/README.md, changed-events.csv, verification.json and neighbors.json for exact values, source mapping and materiality. Raw event plots/contact sheets are refreshed only where displayed depth annotations changed.
