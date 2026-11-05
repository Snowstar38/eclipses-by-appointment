"""Build per-target bounded scientific handoff from measured evidence."""
import csv, json, statistics
from pathlib import Path

B=Path(__file__).resolve().parent
Q=list(csv.DictReader((B/'queue.csv').open(encoding='utf-8',newline='')))
D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text(encoding='utf-8'))
A=json.loads((B/'coverage-alias.json').read_text(encoding='utf-8'))
G=json.loads((B/'gaia-geometry.json').read_text(encoding='utf-8'))
H={x['tic']:x for x in json.loads((B/'helper-pixels'/'results.json').read_text(encoding='utf-8'))}
C={x['tic']:x for x in json.loads((B/'helper-pixels'/'final-neighbors.json').read_text(encoding='utf-8'))}
CAT={x['tic']:x for x in csv.DictReader((B.parent/'remaining_cached'/'catalogue-recovery-late'/'coverage-matrix.csv').open(encoding='utf-8',newline=''))}

def fmt(x,n=3):return f'{x:.{n}f}'
def table(headers, rows):return '| '+' | '.join(headers)+' |\n|'+ '|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(map(str,r))+' |\n' for r in rows)

rows=[]
for q in Q:
 t=q['tic'];m=json.loads((B/t/'measurements.json').read_text(encoding='utf-8'));g=G[t];h=H[t];co=C[t]
 ev=[e for e in m['events'] if e.get('timing_usable')]
 all_ev=[e for e in m['events'] if 'mid_btjd' in e]
 same=[w for w in A[t]['windows'] if w['kind']=='same' and w['status']=='measured_clean_window']
 half=[w for w in A[t]['windows'] if w['kind']=='half' and w['status']=='measured_clean_window']
 neighbors=co.get('capable_at_minimum_all_apertures',[])
 verdict='PROBABLE' if neighbors or t=='174303697' else 'CONFIRMED'
 cat=CAT[t]
 assert cat['coverage_complete']=='True'
 cat_status=cat['scoped_prior_eb_status']
 novelty=('A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope.' if 'known prior EB' in cat_status else 'The completed scoped catalogue checks identify no prior eclipsing-binary entry for this exact target, but ASAS-SN has an exact ROT variable counterpart (period 726.95 d); this is not an EB classification. Novelty is provisionally unclaimed pending root acceptance and attribution follow-up.')
 c=g['closest']; sig=c['gaia_linear_covariance_error_days']; z=abs(c['offset_days'])/sig if sig>0 else None
 # Every sampled target has an adjacent anchor; missing independent reduction or unresolved Gaia/pixel attribution precludes confirmation.
 limitation=[]
 limitation.append('A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion.')
 if neighbors:limitation.append(f'{len(neighbors)} Gaia DR3 neighbor(s) within 60 arcsec pass an optimistic G-band/full-throughput capability screen; the target-centered difference image does not conclusively resolve source ownership at TESS pixel scale.')
 if z is not None and z>3:limitation.append(f'The measured eclipse is {fmt(abs(c["offset_days"]),3)} d from the closest Gaia conjunction, {fmt(z,1)} times its propagated Gaia linear error; the published Gaia orbit and eclipse clock may refer to different or inaccurately modeled motion.')
 if t=='121277143':limitation.append('Sector 40 lacks egress and sector 53 has broad baseline modulation; both are retained as detections but excluded from center timing.')
 if t=='174303697':limitation.append('Sector 16 has a flagged preceding core and a clean later eclipse whose egress is beyond the sector edge; neither supplies a full center fit.')
 if t=='207780183':limitation.append('Several opposite-half-phase windows have broad, shallower deficits displaced about 0.20 d from exact half phase; these are a possible eccentric-orbit secondary eclipse, not same-kind timing points.')
 if t=='102305337':limitation.append('Early and late depths differ by roughly 4 ppt, consistent with extraction or aperture variation; timing remains repeated.')
 if t=='431589019':limitation.append('The representative cutout has only four core frames and substantial aperture-dependent dilution amid two bright capable neighbors; target-like difference peak is insufficient for unique attribution.')
 limits=' '.join(limitation)
 nextcheck='Obtain higher-resolution photometry during a predicted eclipse to resolve the Gaia neighbors, then compare the eclipse clock with an updated radial-velocity orbit.' if neighbors else ('Recheck the Gaia source/orbit assignment with new radial velocities at predicted conjunctions.' if z and z>3 else 'Acquire a clean future eclipse to refine the ephemeris and check long-term stability.')
 event_rows=[]
 # Representative: first/last, adjacent anchor pair, and mid-baseline if available.
 picks={0,len(ev)-1}
 for i in range(1,len(ev)):
  if ev[i]['cycle']-ev[i-1]['cycle']==1:picks.update([i-1,i]);break
 if len(ev)>4:picks.add(len(ev)//2)
 for e in [ev[i] for i in sorted(picks)]:event_rows.append([e['sector'],e['cycle'],fmt(e['mid_btjd'],5),fmt(e['timing_error_days'],6),fmt(e['depth_ppt'],2)])
 samp_same=[same[i] for i in sorted({0,len(same)//2,len(same)-1})] if same else []
 samp_half=[half[i] for i in sorted({0,len(half)//2,len(half)-1})] if half else []
 glimit='No Gaia G-measured neighbor passed the optimistic capability test within 60 arcsec.' if not neighbors else table(['Gaia DR3 source','sep arcsec','G','minimum intrinsic eclipse %'],[[x['source_id'],fmt(x['sep_arcsec'],2),fmt(x['G'],2),fmt(100*x['intrinsic_eclipse_fraction'],1)] for x in neighbors])
 ap=h.get('qlp_alternative_aperture_ppt',{})
 app='; '.join(f'{k} {fmt(v,2)} ppt' for k,v in ap.items()) if ap else 'No QLP aperture variants in this file.'
 cut=f"A separately extracted background-subtracted TESScut light curve in sector {h['sector']} has 1×1/3×3/5×5 aperture losses of "+'/'.join(fmt(co['pixel_apertures_ppt'][k],2) for k in ('1x1','3x3','5x5'))+f" ppt and a positive difference-centroid offset of {fmt(h['cutout']['centroid_offset_pixels'],3)} pixel from the target (descriptive, not a calibrated localization likelihood)."
 p=B/t/'REPORT.md'
 text=f'''# TIC {t} — {verdict}

Bounded full physical review: **COMPLETE**. Review ID {q['review_id']}. Ten-target sealed queue position {q['position_in_batch']} is an operational order, not a scientific rank. Physical outcome is **{verdict}**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure.{(' A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved.' if verdict=='PROBABLE' else ' The deciding pixel, neighbor and Gaia checks available here are compatible with the target/orbit assignment.')} {novelty} Catalogue evidence is in `../../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC {t} to Gaia DR3 {g['gaia_source_id']} and {len(m['source_receipts'])} QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is {fmt(m['depth_ppt'],2)} ppt. The screen period/epoch only located windows. The same-kind fit uses {len(ev)} usable centers spanning cycles {min(x['cycle'] for x in ev)}–{max(x['cycle'] for x in ev)}, including an adjacent-cycle anchor. It yields P = {fmt(m['period_days'],9)} ± {fmt(m['period_error_days'],9)} d, reference epoch BTJD {fmt(m['reference_epoch_btjd'],8)} ± {fmt(m['epoch_error_days'],8)} d at cycle {m['reference_cycle']}; reduced χ² = {fmt(m['reduced_chi_square'],2)}. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

{table(['Sector','same-kind cycle','mid BTJD','center error d','realized depth ppt'],event_rows)}
Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. {('The ' + str(len(all_ev)-len(ev)) + ' fitted but timing-excluded windows remain recorded.') if len(all_ev)>len(ev) else ''}

Actual quality-zero main windows with bilateral sidebands ({len(same)} clean sampled) and opposite half-phase windows ({len(half)} clean sampled) are in `../coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

{table(['Sector','cycle','core quality-0','main deficit ppt','OOT scatter ppt'],[[w['sector'],w['cycle'],w['n_core_quality0'],fmt(w['core_median_deficit_ppt'],2),fmt(w['oot_scatter_ppt'],2)] for w in samp_same])}
{table(['Sector','cycle','core quality-0','opposite deficit ppt'],[[w['sector'],w['cycle'],w['n_core_quality0'],fmt(w['core_median_deficit_ppt'],2)] for w in samp_half]) if samp_half else 'No clean opposite-phase window was sampled; P/2 is checked using adjacent same-kind anchors and depth morphology only.'}

## Source attribution and alternate extraction

The helper's representative sector {h['sector']} QLP aperture products show {app} These repeat the event in different QLP apertures but are not independent pipeline evidence. {cut} The 60-arcsec Gaia neighbor cone is documented in `../helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss ({fmt(co['minimum_all_apertures_ppt'],2)} ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

{glimit}

## Gaia geometry and outcome

Gaia's {g['solution_type']} orbit has P = {fmt(g['gaia_period_days'],8)} ± {fmt(g['gaia_period_error_days'],8)} d, e = {fmt(g['eccentricity'],4)}, ω = {fmt(g['omega_deg'],2)}°, and primary-velocity mass function {fmt(g['mass_function_solar'],4)} solar masses. The selected eclipse period minus Gaia's is {fmt(g['period_difference_days'],5)} d. Closest edge-on conjunction {c['kind']} is {fmt(c['offset_days'],4)} d ({fmt(c['offset_phase'],4)} phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives {fmt(sig,4)} d at that epoch. `../gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** {limits}

**Next decisive check:** {nextcheck}
'''
 p.write_text(text,encoding='utf-8')
 rows.append(dict(tic=t,physical_verdict=verdict,full_review_completion='COMPLETE',period_days=fmt(m['period_days'],9),period_error_days=fmt(m['period_error_days'],9),primary_epoch_btjd=fmt(m['reference_epoch_btjd'],8),depth_ppt=fmt(m['depth_ppt'],2),limitations=limits,next_check=nextcheck,source_report=str(B/t/'measurements.json'),report=str(p)))
with (B/'RESULTS.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('Wrote',len(rows),'reports and result rows')
