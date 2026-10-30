import requests,sys
q="""SELECT source_id,nss_solution_type,period,period_error,t_periastron,t_periastron_error,eccentricity,eccentricity_error,arg_periastron,arg_periastron_error,
center_of_mass_velocity,semi_amplitude_primary,semi_amplitude_primary_error,bit_index,corr_vec,goodness_of_fit,significance
FROM gaiadr3.nss_two_body_orbit WHERE source_id IN (2202301453777953024,6363985915889785856)"""
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q),timeout=120)
print(r.status_code); open('s06_gaia_nss.csv','w').write(r.text); print(r.text)
q2="""SELECT source_id,phot_g_mean_mag,bp_rp,parallax,ruwe,radial_velocity,rv_amplitude_robust,rv_nb_transits,teff_gspphot,logg_gspphot,phot_variable_flag,non_single_star FROM gaiadr3.gaia_source WHERE source_id IN (2202301453777953024,6363985915889785856)"""
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q2),timeout=120)
open('s06_gaia_source.csv','w').write(r.text); print(r.text)
