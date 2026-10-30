import requests, io
q="""SELECT source_id, nss_solution_type, period, period_error, t_periastron, t_periastron_error, eccentricity, eccentricity_error,
arg_periastron, arg_periastron_error, semi_amplitude_primary, semi_amplitude_primary_error, center_of_mass_velocity, bit_index, corr_vec,
goodness_of_fit, significance, flags FROM gaiadr3.nss_two_body_orbit WHERE source_id IN (53541096672533120, 2964506347485091072)"""
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q),timeout=120)
print(r.status_code); print(r.text)
open('s9_gaia_nss.csv','w').write(r.text)
q2="""SELECT source_id, ra, dec, phot_g_mean_mag, bp_rp, parallax, ruwe, radial_velocity, rv_amplitude_robust, phot_variable_flag, teff_gspphot, non_single_star
FROM gaiadr3.gaia_source WHERE source_id IN (53541096672533120, 2964506347485091072)"""
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q2),timeout=120)
print(r.text); open('s9_gaia_source.csv','w').write(r.text)
q3="""SELECT * FROM gaiadr3.vari_summary WHERE source_id IN (53541096672533120, 2964506347485091072)"""
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q3),timeout=120)
print(r.text[:3000]); open('s9_gaia_varisum.csv','w').write(r.text)
