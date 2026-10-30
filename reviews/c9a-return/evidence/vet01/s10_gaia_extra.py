# s10: Gaia DR3 extra columns (Heidelberg TAP mirror) for both targets and the 2.85" neighbour of 468181994
import requests, time
def post(q):
    for i in range(5):
        try: return requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q),timeout=180)
        except Exception as e: print('retry',e); time.sleep(5)
Q="""SELECT source_id, phot_g_mean_mag, bp_rp, parallax, parallax_error, ruwe, astrometric_excess_noise, astrometric_excess_noise_sig,
ipd_frac_multi_peak, ipd_gof_harmonic_amplitude, ipd_frac_odd_win, duplicated_source, non_single_star, phot_variable_flag,
radial_velocity, radial_velocity_error, rv_nb_transits, rv_amplitude_robust, rv_chisq_pvalue, rv_renormalised_gof, teff_gspphot, logg_gspphot, radius_gspphot? 
FROM gaiadr3.gaia_source WHERE source_id IN (2066587801542354176, 6342991943947141376, 6342991943947141504)"""
Q=Q.replace(', radius_gspphot?','')
r=post(Q)
print(r.status_code); print(r.text)
Q2="""SELECT source_id, period, period_error, eccentricity, arg_periastron, semi_amplitude_primary, goodness_of_fit, significance, flags, conf_spectro_period, mass_ratio
FROM gaiadr3.nss_two_body_orbit WHERE source_id IN (2066587801542354176, 6342991943947141376)"""
r=post(Q2)
print(r.status_code); print(r.text)
Q3="""SELECT source_id, radius_flame, lum_flame, mass_flame, teff_gspphot, ag_gspphot, distance_gspphot FROM gaiadr3.astrophysical_parameters WHERE source_id IN (2066587801542354176, 6342991943947141376)"""
r=post(Q3)
print(r.status_code); print(r.text)
