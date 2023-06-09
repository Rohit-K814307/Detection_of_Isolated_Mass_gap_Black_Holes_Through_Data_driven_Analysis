"An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJL 
and
"Supplement: An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJS
##############################################################################
----------------------------------------
Microlensing parameter posterior samples
----------------------------------------
The microlensing parameter posteriors are provided as FITS tables.

There are 19 columns:
* log likelihood (logLike); 
* time of closest approach in MJD (t0); 
* impact parameter (u0_amp); 
* Einstein crossing time in days (tE);
* log10 of Einstein radius in mas (log10_thetaE);
* source parallax in mas (piS);
* microlensing parallax vector (piE_E, piE_N);
* source position vector at t0 in arcsec (xS0_E, xS0_N);
* source proper motion vector in mas/yr (muS_E, muS_N); 
* lens mass in solar masses (mL);
* lens parallax in mas (piL);
* lens-source relative parallax in mas (piRel);
* lens proper motion vector in mas/yr (muL_E, muL_N);
* source-lens relative proper motion vector in mas/yr (muRel_E, muRel_N).

Each row of the table corresponds to a random sample of the posterior.
Vector components are given as East (increasing RA), North (increasing Dec).
Please refer to Section 5 of the Supplement for additional details.

-----------------------
Microlensing simulation
-----------------------
The PopSyCLE microlensing simulation is provided as FITS tables.
There are 26 columns total.

For each microlensing lensing event, 9 columns correspond to properties 
of the lens (_L suffix), and 9 columns to the source (_S suffix):
* Object type where 0 = star, 101 = white dwarf, 
  102 = neutron star, 103 = black hole (rem_id);
* Mass of the object in solar masses (mass);
* Galactic radial distance in kpc (rad); 
* Galactic latitude in deg (glat); 
* Galactic longitude in deg (glon);
* Galactic radial velocity in km/s (vr);
* Galactic proper motion vector long/lat components in mas/yr (mu_b, mu_lcosb); 
* I-band magnitude (Imag).

8 columns correspond to properties of the lensing event, 
so they do not have a _L or _S suffix:
* Einstein radius in mas (theta_E);
* impact parameter (u0);
* source-lens relative proper motion in mas/yr (mu_rel);
* time of closest approach in days (t0);
* Einstein crossing time in days (t_E);
* lens-source relative parallax in mas (pi_rel);
* microlensing parallax (pi_E);
* source flux fraction in I-band (bsff_I).

Additional information about the PopSyCLE simulation can be found in
"PopSyCLE: A New Population Synthesis Code for Compact Object Microlensing Events", 
Lam, C. Y. et al. 2020 ApJ 889 31.
(https://ui.adsabs.harvard.edu/abs/2020ApJ...889...31L/abstract)
or the github repository for the code at https://github.com/jluastro/PopSyCLE.