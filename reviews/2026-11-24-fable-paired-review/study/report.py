"""Render the planned triage comparison and its uncertainty after all endpoints are adjudicated."""
from evaluate import HERE,ORDERS,counts,evaluate,read,wilson
import argparse,csv,hashlib,json
from pathlib import Path
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def plot(dest,colors):
    curves=read(dest/'cumulative-yield.csv')
    fig,axes=plt.subplots(1,2,figsize=(10.5,4),sharex=True)
    for ax,broader in zip(axes,[False,True]):
        for label,col in zip(ORDERS,colors):
            rows=[r for r in curves if r['order']==label]
            x=np.array([0,*[int(r['review_count']) for r in rows]])
            y=np.array([0,*[int(r['cumulative_additions'])+(int(r['cumulative_prior_eclipse_apertures']) if broader else 0) for r in rows]])
            ax.step(x,y,where='post',label=label,color=col,linewidth=1.9)
        ax.plot(x,x*y[-1]/x[-1],color='#555',lw=1,ls='--',label='Random-order expectation')
        for budget in [23,100]:ax.axvline(budget,color='#999',ls=':',lw=.8,zorder=0)
        ax.set(xlim=(0,402),xlabel='Original apertures reviewed',ylim=(0,None))
        ax.set_title('New hosts and earlier eclipse-like signals' if broader else 'Unique catalogue additions',fontsize=12)
        ax.spines[['top','right']].set_visible(False);ax.grid(axis='y',color='#ddd',lw=.5)
        ax.yaxis.get_major_locator().set_params(integer=True)
    axes[0].set_ylabel('Cumulative count')
    fig.legend(*axes[0].get_legend_handles_labels(),loc='lower center',ncol=4,frameon=False,fontsize=9)
    fig.subplots_adjust(left=.07,right=.985,wspace=.18,bottom=.25,top=.87)
    fig.savefig(dest/'triage-yield.png',dpi=175,facecolor='white')
    plt.close(fig)
def cell(r):
    return f"{r['accepted_unique']} / {r['n']} ({r['confirmed_unique']} confirmed)"
def md_row(values):
    return '| '+' | '.join(map(str,values))+' |'
def report(src,dest):
    frozen,budgets,features=evaluate(src,dest); overall=counts(frozen); plot(dest,('#137c83','#cb592c','#54458c'))
    sub=lambda name,cut:next(r for r in budgets if r['stream']=='all' and r['order']==name and r['budget_all_lanes']==cut)
    n=overall['n'];k=overall['accepted_unique'];h=overall['unresolved']+overall['insufficient']
    ftab={ (r['feature'],str(r['value'])):r for r in features}
    lines=['# Which preliminary measurements helped prioritize review?', '',
           f"The review added {k} unique hosts from {n} outstanding Fable apertures ({overall['confirmed_unique']} confirmed and {overall['probable_unique']} probable). It also identified previously reported eclipse-like signals in {overall['identified_prior_apertures']} apertures. {overall['ruled_out']} apertures had a directly identified alternative or a refuted signal, {overall['unresolved']} remained unresolved, and {overall['insufficient']} lacked adequate evidence.",'',
           '## Number recovered at a fixed review budget','',
           md_row(['Order frozen before review','New hosts in first 23','New hosts in first 100','Previously identified eclipse apertures in first 23 / 100']),
           '|---|---:|---:|---:|']
    for label in ORDERS:
        a,b=sub(label,23),sub(label,100)
        lines.append(md_row([label,cell(a),cell(b),f"{a['identified_prior_apertures']} / {b['identified_prior_apertures']}"]))
    lines+=['',f"A random ordering of this same cohort would average {k*23/n:.2f} additions in 23 reviews and {k*100/n:.2f} in 100. All orders reach the same {k} at the end. The random line shows the mathematical expectation over orderings.",'','![Cumulative yield of preliminary rankings](triage-yield.png)','','## Individual preliminary indicators','',
    md_row(['Indicator present','Additions / examined with indicator','Additions / examined without indicator','Holds with / without indicator']), '|---|---:|---:|---:|']
    for flag,label in [('clock_agrees','Blind search recovers original period'),('repeated_events','Four significant events covering half of measured cycles'),('narrow_with_alternation_or_secondary','Narrow profile with secondary or alternating depths'),('zero_capable_neighbours','No flux-capable neighbour within 42 arcsec'),('saved_photometry_cut','Passed earlier photometry cut'),('prior_position_and_period_clear','Clear in earlier position and period comparison')]:
        vals={value:r for (key,value),r in ftab.items() if key==flag};a=vals.get('1',vals.get('True'));b=vals.get('0',vals.get('False'))
        lines.append(md_row([label,f"{a['accepted_unique']} / {a['n']}",f"{b['accepted_unique']} / {b['n']}",f"{a['unresolved']+a['insufficient']} / {b['unresolved']+b['insufficient']}"]))
    lines+=['',f"Observed catalogue yield was {100*k/n:.1f}% (Wilson 95% interval {100*overall['yield_wilson_lo']:.1f}–{100*overall['yield_wilson_hi']:.1f}%). Treating all {h} unresolved or insufficient apertures as eventual successes would raise the arithmetic upper bound to {100*(k+h)/n:.1f}%. That upper bound illustrates how little the pass says about the true prevalence of eclipses among holds.",'',
            f"The cohort contained 335 two-minute apertures and 67 full-frame apertures. {overall['extra_followup']} received at least one additional follow-up recorded in the adjudications. Selective follow-up affects which systems can clear the catalogue threshold. These estimates apply to the remainder of Fable’s selected shortlist. The 45 earlier cases informed the existing priority cut and were excluded from every comparison.",'',
            'The accompanying tables give separate confirmed, probable, prior-signal, directly refuted and unresolved counts, the two observing streams at equal relative budgets, and subgroup Wilson intervals. The composite adds one point for each of the first four indicators and breaks ties by Fable rank. See [the original analysis plan](analysis-plan.md).']
    lane_summary={r["value"]:r for r in features if r["feature"]=="stream"}
    ffi,spoc=lane_summary["ffi"],lane_summary["2min"]
    eligible=[r for r in budgets if r["stream"]=="ffi" and r["budget_all_lanes"]==100]
    high=ftab[("source_clock_score","4")];low=ftab[("source_clock_score","0")]
    cp=ftab[("clock_agrees","False")];ne=ftab[("zero_capable_neighbours","True")];with_ne=ftab[("zero_capable_neighbours","False")]
    interpret=[
        "## What this suggests for the next queue", "",
        f"The observing stream had the largest observed yield difference. The full-frame stream produced {ffi['accepted_unique']} additions from {ffi['n']} apertures and the two-minute stream produced {spoc['accepted_unique']} from {spoc['n']}. Additional follow-up reached {ffi['extra_followup']}/{ffi['n']} full-frame apertures and {spoc['extra_followup']}/{spoc['n']} two-minute apertures. The difference mixes the candidate populations, data available and review effort.",
        "",
        f"Within the full-frame stream alone, the first {eligible[0]['n']} apertures produced {eligible[0]['accepted_unique']} additions under Fable rank, {eligible[1]['accepted_unique']} under existing priority and {eligible[2]['accepted_unique']} under the composite. The pooled comparison therefore cannot establish a generally superior ranking.",
        "",
        f"The original blind period check failed to agree for {cp['accepted_unique']} of the {k} eventual additions. A score of zero still yielded {low['accepted_unique']} additions among {low['n']} apertures, while all four indicators together yielded {high['accepted_unique']} among {high['n']}. An initial clock disagreement merits another period search when independent event times support one.",
        "",
        f"The absence of a flux-capable neighbour showed a possible enrichment ({ne['accepted_unique']}/{ne['n']} versus {with_ne['accepted_unique']}/{with_ne['n']}). With {k} additions total, differences of one or two systems can change the apparent ranking. The composite can prioritize earlier eclipse signals as well as new hosts, so keep both yields visible when comparing another cohort.", ""]
    ff=[r for r in frozen if r["stream"]=="ffi"]
    nf=counts([r for r in ff if r["zero_capable_neighbours"]=="True"])
    cf=counts([r for r in ff if r["zero_capable_neighbours"]=="False"])
    interpret[-2]+=f" In the full-frame stream the corresponding counts were {nf['accepted_unique']}/{nf['n']} without a capable neighbour and {cf['accepted_unique']}/{cf['n']} with one."
    resolved=n-h
    interpret.extend([f"Among the {resolved} apertures with a resolved endpoint, {k} contributed a new host ({100*k/resolved:.1f}%). The full-queue yield remains {100*k/n:.1f}%. Dropping holds from the denominator selects the systems for which the team could resolve the signal and attribute a source.", ""])
    if k:
        cs=read(dest/'cumulative-yield.csv')
        all_depths={label:next(r["review_count"] for r in cs if r["order"]==label and int(r["cumulative_additions"])==k) for label in ORDERS}
        interpret.extend([f"To reach every eventual addition in this cohort required {all_depths['Fable']} reviews under Fable rank, {all_depths['Existing priority']} under existing priority and {all_depths['Source and clock']} under the composite.", ""])
    idx=lines.index("## Individual preliminary indicators")
    lines[idx:idx]=interpret
    lines+=["", "The initial pass added eight hosts. A later inspection of the saved fold depths led to further observations and the ninth admission, probable TIC 247999198. The ranking inputs and their order were already fixed. The final set of proved outcomes reflects that additional effort, particularly for the retrospective fold-depth comparison."]
    if (HERE/'exploratory-fold-discrepancy.md').exists():
        lines+=["","A [separate exploratory comparison](exploratory-fold-discrepancy.md) tests a clue noticed after the recovered clocks were inspected."]
    (dest/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    (dest/'analysis-receipt.json').write_text(json.dumps(dict(n=n,decisions_file=src.name,decisions_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),features_sha256=hashlib.sha256((HERE/'frozen-features.csv').read_bytes()).hexdigest(),results={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dest.iterdir()) if p.name in ['feature-yield.csv','feature-yield-by-stream.csv','review-budget-yield.csv','cumulative-yield.csv','triage-yield.png','README.md']}),indent=2)+'\n')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('endpoints',type=Path);parser.add_argument('--out',type=Path,default=HERE);args=parser.parse_args();report(args.endpoints,args.out)
