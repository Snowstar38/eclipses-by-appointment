"""Row-derived final report. No provisional row is represented as completed."""
from pathlib import Path
from collections import Counter
import csv,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parent
S=json.loads((W/'accepted-summary.json').read_text(encoding='utf8'))
assert S['root_accepted']==S['selected']==100
assert all(x['completed']==x['selected'] for x in S['strata'].values())
rows=list(csv.DictReader((W/'accepted-results.csv').open(encoding='utf8')))
assert len(rows)==len({r['tic'] for r in rows})==100
verdicts=['CONFIRMED','PROBABLE','PLAUSIBLE','REFUTED','NON_ECLIPSE_VARIABLE','UNRESOLVED']
counts=Counter(r['physical_verdict'] for r in rows)
labels={'cross_method_dip':'Both searches: dip leads','repeat_sector_dip':'Other multi-sector dips'}
keys=list(labels)
colors=['#137c66','#71b39e','#e4b454','#b7bdc7','#8d78b8','#df7758']
fig,ax=plt.subplots(figsize=(10.5,4.5));left=[0.]*len(keys)
for v,c in zip(verdicts,colors):
    ns=[S['strata'][k]['completed_verdicts'].get(v,0) for k in keys]
    if not sum(ns):continue
    widths=[100*n/S['strata'][k]['selected'] for k,n in zip(keys,ns)]
    ax.barh(range(len(keys)),widths,left=left,color=c,label=v.replace('_',' ').title(),height=.55)
    for i,(l,d,n) in enumerate(zip(left,widths,ns)):
        if n:ax.text(l+d/2,i,str(n),ha='center',va='center',fontsize=10)
    left=[l+d for l,d in zip(left,widths)]
ax.set_yticks(range(len(keys)),[f"{labels[k]} (n={S['strata'][k]['selected']})" for k in keys])
ax.invert_yaxis();ax.set_xlim(0,100)
ax.set_xlabel('Percent within selected group; labels are target counts')
ax.set_title('Physical outcomes: priority-selected 100',loc='left',fontweight='bold')
ax.spines[['top','right','left']].set_visible(False);ax.tick_params(axis='y',length=0)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.22),ncol=3,frameon=False)
fig.text(.01,.01,'Outcome-informed follow-up, not a random sample or survey completeness measurement.',fontsize=8)
fig.tight_layout(rect=[0,.08,1,1]);fig.savefig(W/'review-yield.png',dpi=160);plt.close(fig)
lines=['# Priority-selected 100: completed physical reviews','',
       'All 100 targets received completed bounded reviews and root acceptance. '+', '.join(f'{counts[v]} {v.lower().replace("_"," ")}' for v in verdicts)+'.','',
       '| Selected group | Reviewed | Confirmed | Probable | Plausible | Refuted selected signal | Other variable | Unresolved |',
       '|---|---:|---:|---:|---:|---:|---:|---:|']
for k in keys:
    s=S['strata'][k];c=s['completed_verdicts']
    lines.append('| '+labels[k]+' | '+str(s['selected'])+' | '+' | '.join(str(c.get(v,0)) for v in verdicts)+' |')
rates=[]
for k in keys:
    s=S['strata'][k];c=s['completed_verdicts'];positive=c.get('CONFIRMED',0)+c.get('PROBABLE',0)
    rates.append(f"{positive}/{s['selected']} ({100*positive/s['selected']:.1f}%) in {labels[k].lower()}")
lines+=['','Confirmed-or-probable fractions in this selected queue: '+'; '.join(rates)+'. These groups were selected differently, so the contrast is descriptive.','',
        'The ordering should not be read as a smooth probability gradient: membership in both searches came before contrast in the frozen queue. Future review priorities can test interleaving the strongest other multi-sector dips with cross-method leads; this campaign does not supply a validated score or justify discarding the remainder.']
lines+=['','![Physical outcomes within the two selected groups](review-yield.png)','',
        '## Outcomes along the priority order','',
        'These ten-target blocks describe this fixed queue only. The ranking was informed by earlier outcomes, and the selection changes search group after target 72; these counts do not validate a general ranking model.','',
        '| Queue positions | Confirmed | Probable | Plausible | Other outcomes |',
        '|---|---:|---:|---:|---:|']
ordered=sorted(rows,key=lambda r:int(r['sample_id'][1:]))
for start in range(0,100,10):
    c=Counter(r['physical_verdict'] for r in ordered[start:start+10])
    lines.append(f"| {start+1}-{start+10} | {c['CONFIRMED']} | {c['PROBABLE']} | {c['PLAUSIBLE']} | {10-c['CONFIRMED']-c['PROBABLE']-c['PLAUSIBLE']} |")
lines+=['','## Selection and interpretation','',
        'This is the first 100 of the frozen priority queue: all 72 remaining cross-method dip leads and the 28 highest-contrast other multi-sector dip leads. The choice was informed by the preceding stratified 100 review. Selection was committed at e62392520 before this campaign; there were no substitutions. T001-T100 are local review IDs, not accepted-system identifiers.','',
        'These are descriptive outcomes of this selected follow-up. Differences from the earlier random-within-stratum sample do not establish a validated classifier or survey-wide discovery rate. Contrast, flag counts, Gaia agreement and common-mode counts were not converted automatically into verdicts.','',
        'Initial source packets verified 931 cached light curves against frozen source hashes and TIC headers. Fresh Sol/Terra pairs reviewed each ten-target batch; shared catalogue queries were centralized. Root acceptance records identify deciding exceptions and follow-up work. Physical confirmation and catalogue novelty remain separate; no claim ledger or manuscript was changed during this campaign.','',
        'Confirmed requires supported recurring raw eclipses, measured timing with relevant aliases addressed, target attribution, an alternative reduction and compatible orbital geometry. Probable retains real recurrence with an unresolved check. Plausible includes single events or untested clocks. Refutation applies to the selected signal, not proof that the star cannot host a binary.','',
        '## Confirmed and probable signals','',
        '| Local ID | TIC | Tier | Photometric period (d) | Catalogue status | Evidence |','|---|---:|---|---:|---|---|']
for r in rows:
    if r['physical_verdict'] in ['CONFIRMED','PROBABLE']:
        p=Path(r['report']).relative_to(W).as_posix()
        lines.append(f"| {r['sample_id']} | {r['tic']} | {r['physical_verdict'].title()} | {r['period_days'] or 'Unresolved'} | {r['novelty_status']} | [Report]({p}) |")
lines+=['','Periods retain their source-specific precision and limitations; consult the linked reports.','',
        '## Catalogue status','',
        'Row-derived novelty status counts: '+json.dumps(dict(Counter(r['novelty_status'] for r in rows)))+'. See [shared catalogue report](shared-catalogues/REPORT.md) and target-specific receipts for scopes, matches and unavailable checks. Missing queries are not negative matches.','',
        '## Evidence and reproducibility','',
        'Raw FITS and downloaded cutout bodies remain in the local data cache and are excluded from Git. Source receipts retain paths or retrieval URLs and hashes; reproducing the analysis requires those raw inputs as well as the tracked scripts. A local hash check does not make the repository a self-contained data archive.','',
        '- `accepted-results.csv` and `accepted-summary.json`: root-accepted outcomes.','- `batch01` through `batch10`: per-target reports, measurements, source receipts, lead/helper audits and root acceptance.','- `queue.csv` and `queue-seal.json`: exact selection and hashes.','- `source-packets/`: original identity and light-curve verification.','- `FINAL-VERIFICATION.json` and `FINAL-SHA256SUMS.json`: integrity verification and artifact seal.','',
        '[redacted]\'s appreciation was passed to every helper.','']
(W/'REPORT.md').write_text('\n'.join(lines),encoding='utf8')
print(dict(counts))
