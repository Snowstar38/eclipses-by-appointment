"""Draft evidence reports; root owns final acceptance and novelty decisions."""
import csv,json,statistics
from pathlib import Path
here=Path(__file__).resolve().parent
queue=list(csv.DictReader((here/'queue.csv').open()))
alts={x['tic']:x for x in json.loads((here/'alternative-comparison.json').read_text())}
pixels={r['tic']:json.loads((here/r['tic']/'pixels'/'pixel-difference.json').read_text()) for r in queue}
catalogues=[x for x in json.loads((here/'shared-catalogues'/'catalogue-results.json').read_text()) if 'tic' in x]
notes={
'24668377':('confirmed','Deep A and B eclipses recur across three separated sectors. Depth varies with aperture/sector; four A timings span 85 cycles and B timings are consistent. The exact Gaia/TIC entry in IJspeert et al. (2024) means this is a known EB recovery for the scoped novelty gate.',
            'VSX query was unavailable; the exact IJspeert EB catalogue row already makes the object a known recovery.'),
'150465032':('confirmed','Three A and three B events recur across sectors 34, 61 and 88. TESS-SPOC reproduces the eclipse. A crowded field contains two magnitude-feasible Gaia neighbors at 33 and 44 arcsec, but the independent pixel deficit is target-centered and displaced from both.',
             'Current six VizieR EB/variable catalogues returned successful empty exact-area results; root must complete final alias/novelty reconciliation.'),
'331650047':('confirmed','Four same-kind narrow eclipses, including adaptive older sector 59, recur with a 25.9936-d period. Three covered odd half-period windows contain no comparable eclipse, excluding the 12.9968-d equal-depth train. Difference image favors the target over a 51-arcsec capable neighbor. Gaia conjunction offset is marginal (~2.4 full-covariance 68%-halfwidth units), so association with the spectroscopic orbit is less secure than eclipse reality.',
             'VSX lists exact Gaia source as ROT, not an EB; this does not negate the observed eclipse. One Kostov table query remains unavailable; root must reconcile novelty.'),
'384744604':('confirmed','Three A events in sectors 13, 39 and 101 have distinct cycle spacings 13 and 32, rejecting adjacent cycle aliases; two shallow B events support the same orbital morphology. Difference image is target-centered. The older s13 observation is 30-min cadence and its timing error is floored at half cadence.',
             'Several catalogue services were unavailable in the initial pass; absence of rows is not a nonmatch. Root must complete novelty reconciliation.'),
'109560492':('probable','Three B eclipses in sectors 7, 61 and 88 span 47 and 23 cycles, rejecting adjacent cycle aliases. Two A-like dips also appear, but the sector-34 A event has a truncated left baseline and is excluded from timing. The s88 pixel deficit peaks near the Gaia target; a G≈9.9 source only ~22 arcsec away dominates the blended light. TARS reproduces the event at 18 ppt versus QLP 79 ppt, showing strong aperture dependence. Source attribution remains likely but not resolved to a calibrated level.',
             'Initial catalogue services were partly unavailable. The nearby brighter star and its aliases require explicit novelty/attribution checks.'),
}
results=[]
for row in queue:
    tic=row['tic'];m=json.loads((here/tic/'measurements.json').read_text());pix=pixels[tic]
    kind='B' if tic=='109560492' else 'A';fit=m.get('augmented_same_kind_fit') or m['same_kind_fits'][kind]
    period=fit['period_days'];perr=fit['period_formal_error_days'];epoch=fit['epoch_btjd']
    ev=[e for e in m['events'] if e.get('timing_usable') and e['kind']==kind]
    old=[e for e in json.loads((here/'older-events.json').read_text()) if e['tic']==tic and e['kind']==kind and 'center_btjd' in e]
    depth=statistics.median([e['depth_ppt'] for e in ev]+[e['depth_ppt'] for e in old])
    alt=alts[tic];alt_text=', '.join(f"{x['flux_column']} {x['depth_ppt']:.1f} ppt" for x in alt['columns'])
    cat=[x for x in catalogues if x['tic']==tic]
    cat_text='; '.join(f"{x['catalogue']}: {x['status']} ({len(x['rows'])} row{'s' if len(x['rows'])!=1 else ''})" for x in cat)
    physical,interpret=notes[tic][0],notes[tic][1];novelty=notes[tic][2]
    event_text='\n'.join(f"- s{e['sector']} {e['kind']}: BTJD {e['mid_btjd']:.5f}, {e['depth_ppt']:.1f} ppt, {e['duration_hours']:.1f} h, ±{e['conservative_timing_error_days']*24*60:.1f} min conditional timing floor" for e in m['events'] if e.get('timing_usable'))
    older_text='\n'.join(f"- adaptive older s{e['sector']} {e['kind']}: BTJD {e['center_btjd']:.5f}, {e['depth_ppt']:.1f} ppt, {e['duration_hours']:.1f} h, ±{e['conservative_timing_error_days']*24*60:.1f} min conditional timing floor" for e in old)
    if not older_text:older_text='- No older product needed to establish recurrence.'
    source_note='[pixel difference](pixels/pixel-difference.png)';event_note='[event montage](event-montage.png)';alt_note='[alternative reduction](alternative-event.png)'
    primary_uncertain=tic in ('331650047','109560492')
    body=f'''# TIC {tic} — appointment full review (lead draft)

**Physical verdict: {physical}.** {interpret}

The frozen queue identifies Gaia DR3 {row['gaia_dr3_source_id']} at ({row['ra_deg']}, {row['dec_deg']}) deg, G={row['gaia_dr3_g']}, SB1 period {float(row['gaia_period_days']):.6f} d. The measured **{kind} eclipse** ephemeris is BTJD {epoch:.5f} + E × {period:.7f} d, with conditional statistical period error {perr:.7f} d. The epoch names the observed {kind} event; deeper primary designation is {'uncertain because the opposite eclipse is not securely established' if primary_uncertain else 'supported by the observed shallower opposite eclipse'}. The period assumes the listed integer-cycle assignment. Timing covariance includes half-cadence floors and residual-scatter inflation, but not common pipeline offsets, model systematics, or all alias uncertainty.

Raw QLP quality-zero SAP eclipse fits ({event_note}):

{event_text}

Additional products were fetched adaptively after the 256-target screening was frozen; they do not alter its denominator or screening status:

{older_text}

The representative realized QLP central depth is {depth:.1f} ppt, the median of usable {kind} event fits. Each depth is the realized trapezoid loss, `amplitude × min(1,width/(2×ingress))`; aperture dilution changes across sectors. [Numeric measurements](measurements.json) preserve separate model amplitudes and event errors. {'[Half-period null windows](half-alias-windows.json) test the 331650047 alias.' if tic=='331650047' else ''}

Independent TESS processing of the **same photons** in sector {alt['sector']} ({alt['provenance']}) reproduces the dip: {alt_text}, compared with QLP {alt['qlp_depth_ppt']:.1f} ppt ({alt_note}). These are reduction cross-checks, not independent observing epochs. {'TARS has no QUALITY field in the s88 file; its event is visually continuous but its quality provenance is limited.' if tic=='109560492' else 'TESS-SPOC QUALITY=0 cadences were used.'}

TESScut sector {pix['sector']} shows a deficit {pix['deficit_target_offset_arcsec']:.1f} arcsec from the target coordinate and {pix['deficit_light_offset_arcsec']:.1f} arcsec from the local blended-light centroid ({source_note}). The cone contains {len(pix['neighbor_60arcsec'])} Gaia DR3 sources within 60 arcsec; {sum(x['feasible_under_two_star_G_approximation'] for x in pix['neighbor_60arcsec'])} meet a two-star G-band depth feasibility test. The difference image and each capable neighbor must be read together. A neighbor's required *intrinsic* eclipse depth cannot be compared directly with diluted pixel fractional loss. This is one FFI sector and uncalibrated centroid precision.

Source-specific full Gaia NSS covariance was independently sampled by Terra in [helper-gaia-covariance.json](../helper-gaia-covariance.json); all original usable event centers lie within 2.38 reported central-68%-halfwidth units of conjunction medians. Correlated predictions across cycles are not independent significance tests. [Helper audit](../helper-audit.md) checks the numeric and pixel evidence. The Gaia SB1 orbit supplies an appointment and physical plausibility, not automatic proof that the target is the eclipsing source.

Catalogue checks: {cat_text}. {novelty} [Shared receipts](../shared-catalogues/catalogue-results.json) and [source hashes](../SOURCE-SNAPSHOT.json) preserve provenance. Physical verdict and novelty gate are separate; root will decide count eligibility.

**Limitations / next check:** {novelty} {'Quantify crowded-source attribution using another sector or calibrated PSF basis if a definitive target assignment is needed.' if tic=='109560492' else 'Complete root catalogue gate and independent final audit.'}
'''
    (here/tic/'REPORT.md').write_text(body,encoding='utf-8')
    results.append(dict(tic=tic,physical_verdict=physical,full_review_completion='COMPLETE_LEAD_HELPER_ROOT_CATALOGUE_PENDING',
        period_days=f'{period:.9f}',period_error_days=f'{perr:.9f}',primary_epoch_btjd=f'{epoch:.6f}',
        epoch_kind=f'observed {kind} eclipse; primary designation '+('uncertain' if primary_uncertain else 'by depth'),
        depth_ppt=f'{depth:.2f}',limitations=novelty,
        next_check='Root novelty gate'+('; calibrated crowded-source attribution' if tic=='109560492' else ''),
        source_report=f'{tic}/REPORT.md',report=f'{tic}/REPORT.md'))
with (here/'RESULTS.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(results[0]));w.writeheader();w.writerows(results)
print('Wrote',len(results),'draft reports')
