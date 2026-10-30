from pathlib import Path
p=Path('[local working path omitted]');s=p.read_text().replace("(80,3498.424)]","(80,3498.424),(80,3500.8637),(80,3503.2989),(80,3505.734)]").replace("0,.18,.25]","0,.18,.25]")
s=s.replace(".2,.7,.5]", ".2,1.2,.5]")
s=s.replace("p=ev[1]['tc']-ev[0]['tc'];epoch=ev[0]['tc'];", "p=ev[1]['tc']-ev[0]['tc'];epoch=ev[0]['tc'];\n if tic=='9396327':\n  cyc=np.array([round((e['tc']-epoch)/p) for e in ev]);p,epoch=np.polyfit(cyc,[e['tc'] for e in ev],1)\n if tic=='183994341':\n  p,epoch=np.polyfit(np.arange(4),[e['tc'] for e in ev],1)")
s=s.replace("n_events=2,note='Direct interval between representative consecutive primary events in same sector; cross-sector phase stability checked separately; no formal period error.'", "n_events=len(ev),note='Representative local event timing regression for939/183; direct consecutive event interval for431/222; no formal period error.'")
p.with_name('refine_final.py').write_text(s)
