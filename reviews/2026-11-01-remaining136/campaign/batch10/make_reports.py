from pathlib import Path
import json,csv,hashlib,numpy as np
b=Path(__file__).parent.resolve();g=json.load(open(b/'gaia-geometry.json'));s=json.load(open(b/'secondary-phases.json'));notes={
'165992260':'Seven narrow repeated primary eclipses and unequal secondary. Capable47.42arcsec neighbor is well separated from compact deficit.',
'31816149':'Six deep repeated primary eclipses and unequal secondary; no capable neighbor within60arcsec.',
'116849606':'Five deep repeated primary eclipses and unequal secondary. Capable36.35arcsec neighbor lies away from the compact deficit core.',
'45914154':'Six narrow repeated primary eclipses and unequal secondary near0.4498; the initial near-half-phase secondary fit failed and was replaced using observed morphology. Capable43.95arcsec neighbor is separated from deficit core.',
'295546522':'Thirteen deeper odd historical cycles define primary; eleven shallower even cycles remain in raw data. Unequal populations require doubling historical SAP period. No capable neighbor within60arcsec.',
'398837588':'Five repeated narrow eclipses despite substantial sector baseline changes. No secure secondary. Capable7.28arcsec neighbor shares footprint, so target ownership remains unresolved; other capable sources are listed individually below.',
'94220952':'Three deep repeated eclipses including consecutive cycles66/67 in sector81. No secure secondary. Capable9.28arcsec neighbor shares footprint and prevents secure ownership.',
'84122354':'Six deeper odd historical cycles define primary, with persistent unequal even secondary population. Historical SAP period is doubled. Capable11.81arcsec neighbor overlaps footprint; ownership remains unresolved.',
'340860427':'Thirty-eight deeper even historical cycles define primary; unequal secondary population requires doubled historical SAP period. Crowded field includes capable3.19/15.87/18.74arcsec sources; ownership unresolved. Nearby catalogued EB Gaia5857683145142215424 at38.54arcsec has period0.474888d, different from measured1.309840d; this is a contamination alert, not a target known-catalogue match. Its G18.753315 gives required intrinsic loss proxy11.36445 (above unity); actual pixel[8.38597,5.87954] is displaced from the compact deficit. Thus this known EB cannot explain the measured loss under the stated brightness screen, while closer capable sources remain unresolved.',
'237092634':'Two deep consecutive sector24 eclipses establish local recurrence, with zero-dof timing chi-square null. Current availability query found only24/51/78; later predicted primary centers are flagged or gapped, not clean nulls. Bounded shorter integer-alias tests and coverage are retained in coverage-alias-check.json. No secure secondary; shallow phase0.625 modulation is not assigned as its counterpart. No capable neighbor within60arcsec; compact deficit supports target.'}
rows=[]
for q in csv.DictReader(open(b/'queue.csv')):
 t=q['tic'];p=b/t;m=json.load(open(p/'measurements.json'));d=json.load(open(p/'fresh-pixels/diff_fresh.json'));geo=g[t];sec=s[t];v='PROBABLE' if t in ['398837588','94220952','84122354','340860427'] else 'CONFIRMED';ev=[e for e in m['events'] if e.get('timing_usable')];n=np.array([e.get('orbital_cycle',e['cycle']) for e in ev]);er=np.array([e['timing_error_days'] for e in ev]);X=np.column_stack([np.ones(len(n)),n-n.min()]);cov=np.linalg.inv((X/er[:,None]).T@(X/er[:,None]))*max(m['reduced_chi_square'] or 1,1);m['epoch_error_days']=float(np.sqrt(cov[0,0]));m['epoch_error_meaning']='Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics.';m['epoch_kind']='Deeper primary established by unequal observed secondary' if sec['secure_secondary'] else 'Selected repeating eclipse; deeper/secondary identity not established';json.dump(m,open(p/'measurements.json','w'),indent=2)
 nb='\n'.join('| '+ ' | '.join(str(n[k]) for k in ['source_id','sep','G','depth_needed','px','frac_loss_at_pixel'])+' |' for n in d['neighbours_60'] if n['possible']) or '| None | | | | | |'
 timing='\n'.join(f"| {e['sector']} | {e.get('orbital_cycle',e['cycle'])} | {e['mid_btjd']:.9f} | {e['formal_timing_error_days']:.9g} | {e['timing_error_days']:.9g} | {e['depth_ppt']:.5f} |" for e in ev)
 secondary=(f"Measured secondary phase {sec['phase']:.8f}, formal phase error {sec['formal_phase_error']:.8g}, realized depth {sec['depth_ppt']:.5f}ppt. {sec['error_meaning']}" if sec['secure_secondary'] else 'No secure secondary; exploratory fit is not interpreted as an eclipse timing or counterpart.')
 text=f'''# TIC {t}: {v}

Full bounded physical review: COMPLETE. {notes[t]}

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. {len(ev)} identifiable free-center timings define P={m['period_days']:.12f} +/- {m['period_error_days']:.12f}d, reference BTJD={m['primary_epoch_btjd']:.9f} +/- {m['epoch_error_days']:.9f}d. Epoch error meaning: {m['epoch_error_meaning']} Epoch kind: {m['epoch_kind']}. {m['error_meaning']} Reduced chi square={m['reduced_chi_square']}; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. {m.get('timing_selection','Selected same-kind recurring eclipse family; parity and P/2 coverage checked.')}

Depth={m['depth_ppt']:.6f}ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in measurements.json. {secondary} Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in secondary-windows.csv and ../secondary-phases.json. No exhaustive blind alias search asserted. ../alias-audit.json and ../half-period-coverage.json retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector{d['sector']} stacks{d['n_events']} core/bilateral-sideband events. Target pixel={d['target_px']}, deficit={d['deficit_centroid']}; descriptive offset={np.hypot(*d['deficit_minus_target_px']):.5f}pixel, field PSF residual={d['psf_fit_frac_resid']:.5f}. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
{nb}

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths={d['depth_ap1']*1000:.5f}/{d['depth_ap3']*1000:.5f}/{d['depth_ap5']*1000:.5f}ppt; QLP median={m['depth_ppt']:.5f}ppt. Pixel sector{d['sector']} {'shares the same TESS photons with retained QLP and checks extraction robustness' if d['sector'] in [x['sector'] for x in m['sources']] else 'is a distinct observing occasion on the same TESS instrument; no same-sector QLP comparison claimed'}. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source{geo['gaia_source_id']}: period={geo['period_days']:.9f}+/-{geo['period_error_days']:.9f}d; e={geo['eccentricity']:.7f}; omega={geo['omega_deg']:.7f}deg; periastron BTJD={geo['t_periastron_btjd']:.8f}. Closest conjunction offset={geo['closest']['offset_days']:.7f}d ({geo['closest']['offset_phase']:.7f}phase), source-specific full-covariance linear error={geo['closest']['gaia_covariance_linear_error_days']:.7f}d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in ../gaia-geometry.json. Mass function={geo['mass_function_solar']:.7g}solar, assumed M1={geo['assumed_m1_solar']}, minimum M2={geo['minimum_m2_solar']:.6g}; approximate central duration={geo['central_duration_hours_approx']:.4f}h versus observed={geo['observed_duration_hours']:.4f}h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
{timing}

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.
'''
 (p/'REPORT.md').write_text(text)
 limitation='Approximate Gaia geometry and G-band blend screen; timing errors exclude uncalibrated model systematics.'+(' Close capable neighbor leaves attribution unresolved.' if v=='PROBABLE' else '')+(' Local sector24 ephemeris only; later primary windows flagged/gapped.' if t=='237092634' else '')
 rows.append(dict(tic=t,physical_verdict=v,full_review_completion='COMPLETE',period_days=m['period_days'],period_error_days=m['period_error_days'],primary_epoch_btjd=m['primary_epoch_btjd'],depth_ppt=m['depth_ppt'],limitations=limitation,next_check='Resolved eclipse photometry or multi-source PRF attribution.' if v=='PROBABLE' else 'Optional additional clean epochs and resolved photometry.',source_report=str(p/'measurements.json'),report=str(p/'REPORT.md')))
with open(b/'RESULTS.csv','w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
json.dump(notes,open(b/'review-notes.json','w'),indent=2)
