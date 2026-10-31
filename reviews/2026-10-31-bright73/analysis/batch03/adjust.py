from pathlib import Path
b=Path('[local path omitted]')
p=b/'review_measure.py'; s=p.read_text().replace("('48752905','351335839')","('16809274',)"); s=s.replace("summary['timing_event_count']=len(good)","if tic=='16809274':summary['epoch_kind']='Shallower repeating eclipse, even historical half-period cycles; not asserted to be deeper primary'\n summary['timing_event_count']=len(good)"); p.write_text(s)
p=b/'alias_audit.py';p.write_text(p.read_text().replace("('48752905','351335839')","('16809274',)"))
