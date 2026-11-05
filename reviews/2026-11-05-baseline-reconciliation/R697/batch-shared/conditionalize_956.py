"""Retain the rejected-assumption numerical fit without advertising a secure ephemeris."""
import json
from pathlib import Path
B=Path(__file__).resolve().parent;p=B/'95623701'/'measurements.json'
m=json.loads(p.read_text(encoding='utf-8'))
mapping={'period_days':'conditional_112_cycle_period_days','period_error_days':'conditional_112_cycle_formal_period_error_days','reference_epoch_btjd':'conditional_112_cycle_reference_epoch_btjd','epoch_error_days':'conditional_112_cycle_formal_epoch_error_days','reference_cycle':'conditional_112_cycle_reference_cycle','reduced_chi_square':'conditional_112_cycle_reduced_chi_square','timing_residual_days':'conditional_112_cycle_residual_days','depth_ppt':'median_selected_event_realized_depth_ppt'}
for a,b in mapping.items():
 if a in m:m[b]=m.pop(a)
m['conditional_alias_warning']='The 112-cycle linear fit is conditional on assigning sector-12/103 deep events and sector-39 weak event to one clock. A fully covered sector-65 window is a same-branch clean null; source ownership and alternative integer aliases are unresolved. These formal errors are not ephemeris uncertainties and must not populate generic result fields.'
p.write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
