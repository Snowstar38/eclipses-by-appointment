"""Rebuild compact batch-02 evidence and provisional reports from frozen inputs."""
import csv
import hashlib
import json
import math
import os
from pathlib import Path

B = Path(__file__).resolve().parent
ROOT = B.parent
SB = Path('[local path omitted] 5/made/sb1-scale')
SKY = Path('[local path omitted]')
queue = list(csv.DictReader(open(B / 'queue.csv', newline='')))
targets = json.load(open(ROOT / 'targets-selected.json'))
geometry = json.load(open(B / 'gaia-geometry.json'))
catalogue = {r['tic']: r for r in csv.DictReader(open(ROOT / 'shared-catalogues/coverage-compact.csv'))}


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def rel(p):
    return Path(os.path.relpath(p, B)).as_posix()


source_receipts = {}
rows = []
for row in queue:
    tic = row['tic']
    m = json.load(open(B / tic / 'measurements.json'))
    g = geometry[tic]
    pxfile = next((SB / 'diffimg' / tic).glob('diff_s*.json'))
    px = json.load(open(pxfile))
    cut = SKY / ('vet' + tic) / f"tesscut_s{px['sector']:03d}.fits"
    oldfiles = [pxfile, pxfile.with_suffix('.png'), pxfile.parent / 'gaia.json', cut]
    rawfiles = [Path(s['path']) for s in m['sources']]
    source_receipts[tic] = [{'path': rel(p), 'sha256': sha(p), 'bytes': p.stat().st_size,
                             'role': 'QLP raw SAP FITS' if p in rawfiles else 'historical pixel or Gaia evidence'}
                            for p in rawfiles + oldfiles]
    capable = sorted([n for n in px['neighbours_60'] if n['possible']], key=lambda n: n['sep'])
    pixel_summary = {
        'tic': tic, 'source_json': rel(pxfile), 'pixel_sector': px['sector'],
        'stacked_events': px['n_events'], 'deficit_minus_target_px': px['deficit_minus_target_px'],
        'deficit_target_distance_px': math.dist(px['deficit_centroid'], px['target_px']),
        'target_pixel': px['target_pixel'], 'peak_deficit_pixel': px['peak_deficit_px'],
        'aperture_depth_ppt': {str(i): px[f'depth_ap{i}'] * 1000 for i in (1, 3, 5)},
        'capable_neighbours': [{k: n[k] for k in ('source_id', 'sep', 'G', 'depth_needed', 'px', 'frac_loss_at_pixel')}
                               | {'distance_to_deficit_px': math.dist(px['deficit_centroid'], n['px'])}
                               for n in capable],
        'all_neighbours_examined': px['n_neighbours_60'],
        'capability_rule': 'The historical depth_needed compares intrinsic neighbor eclipse to blended target light; possible when <=1. Pixel fractional loss is a separate statistic.'
    }
    (B / tic / 'pixel-evidence.json').write_text(json.dumps(pixel_summary, indent=2))
    good = [e for e in m['events'] if e.get('timing_usable')]
    sectors = sorted({e['sector'] for e in good})
    ncap = len(capable)
    nearest = capable[0] if capable else None
    if tic == '368260545':
        verdict = 'confirmed'
        limitation = 'A similarly bright G=12.30 Gaia neighbor 22.87 arcsec away is flux-capable, but the deficit is 0.206 pixel from the target versus 0.92 pixel from that neighbor and peaks on the target pixel. A targeted recomputation of all four stacked windows puts every event deficit closer to the target (0.13–0.47 pixel) than the neighbor (0.75–1.07 pixel). Positional uncertainty remains descriptive rather than calibrated.'
        next_check = 'Additional pixel orientations or spatially resolved photometry can strengthen attribution and refine the ephemeris.'
    elif tic == '251731963':
        verdict = 'probable'
        limitation = 'A G=12.27 Gaia star 3.69 arcsec away can produce the dip with a ~27% intrinsic eclipse; the TESS pixel centroid cannot resolve the pair.'
        next_check = 'Resolve the two stars in higher-spatial-resolution time-series photometry at predicted eclipse times.'
    elif tic == '409852500':
        verdict = 'probable'
        limitation = 'Two G~16.3 neighbors at 7.3 and 9.5 arcsec are capable in flux and share a TESS pixel; the deficit centroid favors the target but does not securely resolve them. The sector-104 cycle-294 egress gap excludes that center from timing.'
        next_check = 'Obtain spatially resolved eclipse photometry, or a stronger difference image in a suitable sector.'
    else:
        verdict = 'confirmed'
        limitation = 'Representative-sector timing and pixel evidence; period uncertainty is formal fit/cadence with scatter inflation where needed, not calibrated total coverage.'
        next_check = 'Additional independent observations can refine the ephemeris and source attribution.'
    if tic in ('142427408', '247204810'):
        limitation += ' Alternating half-period events were separated by eclipse kind before orbital timing.'
    if tic == '142427408':
        limitation += ' Crowded pixel PSF fit is poor, but all flux-capable neighbors are at least 27 arcsec from the target and farther from the deficit.'
    if tic == '21455449':
        limitation += ' Gaia duration estimate is crude and exceeds the observed narrow event; geometry phase and period remain consistent.'
    mperiod = float(m['period_days'])
    lines = [f'# TIC {tic}: batch 02 review', '',
             f'**Physical verdict:** {verdict}. **Full bounded review:** complete. **Catalogue scope:** {catalogue[tic]["scoped_prior_eb_status"]}; seven-group coverage complete. Catalogue status is separate from physical classification.', '',
             f'Frozen queue position {row["queue_index"]}; Gaia DR3 source {g["gaia_source_id"]}; actual DR3 G={row["actual_gaia_dr3_g"]}. No replacement was made.', '',
             '## Deciding evidence', '',
             f'- Raw QLP SAP flux: {len(good)} usable measured eclipse centers across sectors {", ".join(map(str, sectors))}; {m["timing_event_count"]} selected same-kind centers enter the orbital timing fit. Sampled FITS and their hashes are in `../source-receipts.json`. Measured depths for the selected kind have median {m["depth_ppt"]:.2f} ppt. `measurements.json`, `raw-windows.csv` and `raw-events.png` retain each fit and local flux.',
             f'- Timing: measured same-kind centers give P={mperiod:.9f} ± {m["period_error_days"]:.9f} d and reference center BTJD {m["primary_epoch_btjd"]:.6f}. Epoch kind: {m["epoch_kind"]}. This is a linear timing fit to actual centers, with per-event max(formal trapezoid covariance error, half cadence) and covariance inflated for residual scatter. It does not include calibrated pipeline or shape systematics. Gaia SB1 P={g["period_days"]:.9f} d; difference={g["period_difference_days"]:+.6f} d.',
             f'- Pixel attribution and alternative reduction: historical TESScut sector {px["sector"]} stacked {px["n_events"]} eclipse windows; the flux-deficit centroid is {pixel_summary["deficit_target_distance_px"]:.3f} pixel from the Gaia target and the peak deficit pixel is {px["peak_deficit_px"]} versus target pixel {px["target_pixel"]}. Custom 1×1/3×3/5×5 pixel apertures give {px["depth_ap1"]*1000:.1f}/{px["depth_ap3"]*1000:.1f}/{px["depth_ap5"]*1000:.1f} ppt. This is an alternative extraction of the same TESS photons. All {px["n_neighbours_60"]} Gaia neighbors within 60 arcsec were tested for flux capability; {ncap} {'is' if ncap == 1 else 'are'} capable. ' + (f'Nearest capable: G={nearest["G"]:.2f}, {nearest["sep"]:.2f} arcsec, requiring {nearest["depth_needed"]*100:.1f}% intrinsic eclipse, {math.dist(px["deficit_centroid"], nearest["px"]):.2f} pixel from the deficit.' if nearest else 'No Gaia neighbor is flux-capable.'),
             f'- Gaia geometry: selected edge-on conjunction offset {g["closest"]["offset_phase"]:+.5f} in orbital phase, linear covariance scale {g["closest"]["gaia_covariance_linear_error_days"]:.3f} d. Approximate central duration {g["central_duration_hours_approx"]:.2f} h versus observed median {g["observed_duration_hours"]:.2f} h. The duration estimate assumes TIC radius and a minimum-mass main-sequence companion; it is a plausibility check, not a fit.', '',
             '## Limitations and next check', '', limitation, '', next_check, '',
             '## Source provenance', '',
             f'Historical screening: `{row["source"]}` and `[local path omitted] 5/made/sb1-scale/c6-vetsum-out.txt`. Historical pixel stack: `{rel(pxfile)}` and adjacent PNG/Gaia JSON, computed by `diffstack.py` from `{rel(cut)}`. Current measured evidence: this folder, `../gaia-geometry.json`, `../source-receipts.json`, `../download-receipts.json`; central scoped catalogue: `../../shared-catalogues/coverage-compact.csv`. Raw QLP URI and hashes appear in `../download-receipts.json`.', '']
    if tic == '368260545':
        lines[-2] += ' Targeted four-window centroid audit: `pixel-event-audit.json`, reproduced by `../audit_368_pixels.py`.'
    (B / tic / 'REPORT.md').write_text('\n'.join(lines), encoding='utf-8')
    rows.append(dict(tic=tic, physical_verdict=verdict, full_review_completion='complete',
                     period_days=f'{mperiod:.9f}', period_error_days=f'{m["period_error_days"]:.9f}',
                     primary_epoch_btjd=f'{m["primary_epoch_btjd"]:.6f}', depth_ppt=f'{m["depth_ppt"]:.2f}',
                     limitations=limitation, next_check=next_check, source_report=row['source'], report=f'{tic}/REPORT.md'))

source_receipts['_shared'] = [
    {'path': rel(p), 'sha256': sha(p), 'bytes': p.stat().st_size, 'role': role}
    for p, role in [
        (ROOT / 'targets-selected.json', 'frozen target metadata and QLP inventory'),
        (ROOT / 'shared-catalogues/coverage-compact.csv', 'scoped seven-group catalogue status'),
        (ROOT / 'shared-catalogues/gaia-nss-full.csv', 'Gaia NSS orbit and covariance'),
        (SB / 'search.jsonl', 'historical search branch and duration'),
        (SB / 'c6-sapdepth.json', 'historical SAP ephemeris')]]
(B / 'source-receipts.json').write_text(json.dumps(source_receipts, indent=2))
with open(B / 'RESULTS.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print('Wrote', len(rows), 'reports; verdicts', {v: sum(r['physical_verdict'] == v for r in rows) for v in ('confirmed', 'probable')})
