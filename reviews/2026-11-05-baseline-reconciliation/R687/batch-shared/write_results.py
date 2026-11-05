"""Write exact fixed-queue physical rows; root catalogue gate stays pending."""
import csv, json
from pathlib import Path
W=Path(__file__).resolve().parent
queue=list(csv.DictReader((W/'queue.csv').open(newline='',encoding='utf-8')))
assert [r['tic'] for r in queue]==['167197264','155346713']
ep=json.loads((W/'ephemeris-167197264.json').read_text())
m=json.loads((W/'measurements-155346713.json').read_text())
assert ep['tic']==167197264 and m['tic']==155346713
rows=[
 dict(tic='167197264',gaia_dr3_source_id='1868634515521921152',physical_verdict='probable',
      full_review_completion='COMPLETE_LEAD_HELPER_ROOT_CATALOGUE_PENDING',count_eligible_now='false',
      period_days=f"{ep['shared_period_days_descriptive']:.9f}",period_error_days='',
      period_error_meaning='No calibrated error; descriptive seven-center two-kind cycle fit; >=0.02 d per-center systematic allowance',
      gaia_period_days='41.804020454205606',primary_epoch_btjd=f"{ep['B_reference_btjd']:.6f}",
      epoch_kind='fitted B-like reference epoch near observed deeper s76 event; stellar-component primary identity unassigned',depth_ppt='30.14',
      depth_meaning='sector-76 QLP Q0 raw-SAP local realized central trapezoid loss; aperture diluted',
      limitations='G15.32/G15.35 neighbors at 22-24 arcsec near maximum blended-loss bound; s76 centroid favors target but uncertainty uncalibrated; no calibrated photometric period error',
      next_check='calibrated crowded-field pixel attribution; root catalogue novelty gate',
      report='167197264/REPORT.md'),
 dict(tic='155346713',gaia_dr3_source_id='5694314546391164032',physical_verdict='plausible',
      full_review_completion='COMPLETE_LEAD_HELPER_ROOT_CATALOGUE_PENDING',count_eligible_now='false',
      period_days='',period_error_days='',
      period_error_meaning='No photometric same-kind period; Gaia catalog period is only a conditional hypothesis',
      gaia_period_days='33.63348396287843',primary_epoch_btjd='3702.328988',
      epoch_kind='observed sector-88 A-like eclipse; stellar-component primary identity unassigned',depth_ppt='136.59',
      depth_meaning='sector-88 QLP Q0 raw-SAP local realized central trapezoid loss; aperture diluted',
      limitations='One complete event per kind; sector-7 A ingress truncated; sector-61 B central forecast in Q0 core gap; Gaia period uncertainty projects to days across long baselines',
      next_check='complete same-kind repeat and alias test; root catalogue novelty gate',
      report='155346713/REPORT.md')]
assert [r['tic'] for r in rows]==[r['tic'] for r in queue]
with (W/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
print('wrote',len(rows),'exact-queue rows')
