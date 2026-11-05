"""Record bounded alias evidence independent of Gaia-prior period ranking."""
import json
from pathlib import Path
B=Path(__file__).resolve().parent
t12=json.loads((B/'323458448/lead-timing.json').read_text())['kinds'];p=t12['deep']['period_days'];deep=t12['deep']['mid_btjd'];shallow=t12['shallow']['mid_btjd'];
out={'tic':'323458448','deep_times_btjd':deep,'shallow_times_btjd':shallow,'deep_to_next_shallow_days':shallow[1]-deep[0], 'shallow_to_next_deep_days':deep[1]-shallow[1], 'fractional_spacing':[ (shallow[1]-deep[0])/p,(deep[1]-shallow[1])/p ],'comparison':'S37 deep, S64 shallow, S65 deep provide distinct consecutive kinds over nearly two half cycles. S12/S93 reproduce shallow kind and S37/S65 reproduce deep kind. P/2 timestamps alone would alternate ~90 and ~60 ppt eclipse depths, whereas Gaia SB1 period and two-kind geometry favor the full P. The partial S11 and distorted S38 are not clock anchors.','limitation':'This excludes a simple same-kind P/2 interpretation, not all exotic alternation mechanisms; no exhaustive harmonic search.'}
(B/'323458448/lead-alias.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['fractional_spacing'])
