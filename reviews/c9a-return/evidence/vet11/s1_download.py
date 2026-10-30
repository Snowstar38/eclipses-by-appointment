# Download QLP + TESS-SPOC light curves for the five vet11 stars
import lightkurve as lk, sys, os
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet11'
for tic in sys.argv[1:]:
    d=f'{D}/{tic}'; os.makedirs(d,exist_ok=True)
    sr=lk.search_lightcurve(f'TIC {tic}',author=['QLP','TESS-SPOC','SPOC'])
    print(tic, len(sr)); print(sr)
    sr.download_all(download_dir=d)
