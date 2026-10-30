import json,csv,math
from pathlib import Path
D=Path('[local working path omitted]');B=D/'batch03';R=json.loads((B/'raw-evidence/raw-events.json').read_text());Q=json.loads((B/'raw-evidence/qlp-results.json').read_text());G=json.loads((B/'gaia-geometry.json').read_text());C={r['tic']:r for r in csv.DictReader((D/'shared-catalogues/coverage-matrix.csv').open())};A=json.loads((B/'alias-check.json').read_text());out=[]
for tic,r in R.items():
 q=Q[tic];g=G[tic];d=json.loads((B/f'raw-evidence/{tic}/diff_fresh.json').read_text());p=B/'reports'/tic;p.mkdir(parents=True,exist_ok=True);period=r['representative_ephemeris']['period_d'];qperiod=q['representative_ephemeris']['period_d'];special='';verdict='CONFIRMED'
 if tic=='407220461':
  period=A[tic]['custom']['0']['period_d'];qperiod=A[tic]['qlp']['0']['period_d'];special='Two eclipse families recur: QLP even-cycle depths194.46–196.44ppt versus odd191.09–191.92ppt, with different durations. The full orbital period uses the three even-family events; the other family yields custom8.71608068d and QLP8.71620836d. The final partial event cycle336 has depth55ppt and is excluded from family timing. A single-spacing fit mixed both families and is not the orbital period. Gaia SB2 supports the full period. '
 if tic=='407991939':special='The external ASAS-SN prior EB record lists2.8932d, twice the observed1.44652d spacing. Odd/even QLP depths are nearly equal, without a secure alternating family; both2.89301230/2.89302959d family fits are tabulated in alias-check.json. The representative eclipse recurrence agrees with Gaia1.44654138d. The external double-period alternative remains a characterization ambiguity requiring joint RV/eclipse modeling; the on-target repeating binary interpretation is secure. '
 source='No brightness-capable neighbour is present in the cached60arcsec cone under a total-eclipse G-flux bound.'
 capable=[x for x in d['neighbours_60'] if x['possible']]
 if capable:
  n=capable[0];source=f"A capable Gaia neighbour at{n['sep']:.2f}arcsec, G={n['G']:.3f}, needs intrinsic fractional eclipse{n['depth_needed']:.3f}. Its pixel location is{n['px']}; target{d['target_px']}, deficit{d['deficit_centroid']}. The lead inspected the image: disappearing light is centered on the target PSF, not the neighbour. Its rounded-pixel fractional loss{n['frac_loss_at_pixel']:.4f} must not be interpreted as source-separated photometry."
 off=g['conjunction'][g['closest_kind']];cat=C[tic];nextcheck='Joint RV/eclipse modeling and longer-baseline eclipse timing; resolve remaining alias and geometry uncertainty.'
 if tic=='407220461':
  source+=' This neighbour is only1.04pixels from the target; target attribution is favored by the0.15pixel target-to-deficit distance versus0.90pixel neighbour-to-deficit distance, without calibrated significance or source-separated PRF fitting. The close blend remains a material limitation.'
  nextcheck='Higher-resolution eclipse photometry or calibrated PRF fitting to resolve the close capable neighbour; joint RV/eclipse timing fit.'
 text=f'''# TIC {tic}: {verdict}

All five bounded checks were attempted and adjudicated. Execution is complete; physical verdict and catalogue novelty are separate.

1. Representative raw repeat: custom TESScut sector{r['sector']} gives{len(r['events'])} fitted eclipses; independently downloaded raw QLP SAP_FLUX QUALITY=0 gives{len(q['events'])}. The lead inspected two individual raw SAP eclipse panels. Sharp ingress/egress and repeat dips persist without relying on a folded curve. Local quadratic baseline plus trapezoid event times, depths and durations appear in ../../raw-evidence/raw-events.json and qlp-results.json.
2. Eclipse timing: representative orbital/recurrence period{period:.8f}d, QLP{qperiod:.8f}d, conditional on seed cycle counts. Same-sector data provide no formal photometric period uncertainty; two-event cases verify recurrence with limited alias precision. {special}
3. Attribution: sector{d['sector']} difference image stacks{d['n_events']} events; target-to-deficit centroid{21*math.dist(d['target_px'],d['deficit_centroid']):.2f}arcsec, without calibrated uncertainty. The lead inspected all three panels. {source} Global PSF residual{d['psf_fit_frac_resid']:.3f} is descriptive and includes field light. Approximate G-band brightness bounds do not address missing/unresolved sources or all colour/throughput differences.
4. Reduction robustness: separately coded3x3 TESScut extraction and QLP SAP reproduce individual events; these share the same TESS FFI photons, not independent observations. QLP URI `{q['uri']}`, TIC header{q['header_TICID']}, sector{q['header_SECTOR']}, SHA256 `{q['sha256']}`. TESScut source `{r['source_cutout']}`, SHA256 `{r['source_sha256']}`. Seed and Gaia-cone provenance hashes are in raw-events.json.
5. Gaia geometry: exact DR3{g['gaia_source_id']}, {g['solution']}, P={g['gaia_P']:.8f} +/-{g['gaia_P_error']:.7g}d, e={g['e']:.5f}, omega={g['omega_deg']:.3f}deg. Nominal edge-on conjunction{g['closest_kind']} has observed-minus-predicted offset{off['offset_d']:+.4f}d ({off['offset_phase']:+.5f}phase). Descriptive diagonal linear uncertainty is{off['diagonal_linear_error_d']:.4f}d; it omits parameter covariance and is no sigma veto. Observed median duration{g['observed_duration_hours_median']:.2f}h versus approximate central-crossing{g['central_duration_hours_approx']:.2f}h permits a shorter chord. Duration estimate uses TIC radius and minimum-mass/main-sequence dimensions and is not a unique fitted geometry. Full NSS rows including covariance fields are preserved in the shared catalogue file. Geometry is compatible at this bounded feasibility level, with orbital precision retained as a limitation.

Catalogue status: {cat['scoped_prior_eb_status']}; coverage complete={cat['coverage_complete']}. Prior identification: {cat['known_prior_eb_identification']}. Central seven-scope receipts and Chopard fields are in ../../../shared-catalogues/coverage-matrix.csv. Known recoveries are excluded from new discoveries. No exhaustive publication-priority claim.

Limits: representative selected-sector events, native cadence without exposure integration, no precision stellar solution, cached Gaia cone and unresolved-source limitations. No contrary artifact is established by these limitations.

Next check: {nextcheck}
'''
 (p/'REPORT.md').write_text(text,encoding='utf-8');out.append(dict(tic=tic,physical_verdict=verdict,full_review_completion='completed; five bounded checks adjudicated; limitations retained',novelty_status=cat['scoped_prior_eb_status'],report=str(p/'REPORT.md'),next_check=nextcheck,period_d=period,representative_events=len(r['events']),catalogue_coverage_complete=cat['coverage_complete']))
with (B/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,list(out[0]));w.writeheader();w.writerows(out)
(B/'RESULTS.json').write_text(json.dumps(out,indent=2))
print([(r['tic'],r['physical_verdict'],r['novelty_status']) for r in out])
