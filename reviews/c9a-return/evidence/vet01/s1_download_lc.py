# s1: download all QLP / TESS-SPOC / SPOC light curves for both targets
import lightkurve as lk, sys, warnings
warnings.filterwarnings('ignore')
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
for tic in ['195865529','468181994']:
    sr=lk.search_lightcurve(f'TIC {tic}')
    print(tic); print(sr.table['mission','author','exptime','target_name'])
    sel=sr[[a in ('QLP','TESS-SPOC','SPOC') for a in sr.author]]
    lcs=sel.download_all(download_dir=f'{D}/{tic}')
    print('downloaded',len(lcs))
