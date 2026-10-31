"""Zoomed look at s80 (and s79) q0 SAP with bkg, to vet census hits. python -X utf8 s80look.py"""
import sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
sys.path.insert(0, '.'); import vetlib as v
fig, ax = plt.subplots(4, 1, figsize=(18, 12))
for j, s in enumerate((79, 80)):
    d = [v.load_qlp(f) for f in v.qlp_files(275065610) if f'_s0{s}' in f][0]; g = d['q'] == 0
    ax[2*j].plot(d['t'][~g], d['f'][~g], '.', c='.7', ms=2); ax[2*j].plot(d['t'][g], d['f'][g], '.', ms=2); ax[2*j].set_ylim(.985, 1.008); ax[2*j].set_title(f's{s} SAP (grey flagged)')
    ax[2*j+1].plot(d['t'], d['bkg'], '.', ms=2); ax[2*j+1].set_ylim(np.percentile(d['bkg'], 1) - 200, np.percentile(d['bkg'], 90) * 2 + 200); ax[2*j+1].set_title('bkg')
    for a in ax[2*j:2*j+2]:
        for tb in (3469.52, 3497.57): a.axvline(tb, c='purple', ls='--')
plt.tight_layout(); plt.savefig('s7980.png', dpi=60)
