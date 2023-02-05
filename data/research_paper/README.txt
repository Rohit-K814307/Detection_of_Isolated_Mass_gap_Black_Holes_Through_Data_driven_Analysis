Table of contents:
* Overview 
* Files in this repository
  - MOA lightcurves
  - OGLE lightcurves
  - HST lightcurves and astrometry
  - Microlensing parameter posterior samples
  - Microlensing simulation
* Documentation and data formats
  - MOA and OGLE lightcurves
  - HST lightcurves and astrometry
  - Microlensing parameter posterior samples
  - Microlensing simulation


###########################################################
                         Overview      
###########################################################

This repository contains data, models, and simulations associated with 
"An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJL 
and
"Supplement: An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJS 

The data and models are for the following 5 microlensing events:
* MOA-2009-BLG-260 (MB09260)
* MOA-2010-BLG-364 (MB10364)
* OGLE-2011-BLG-0037/MOA-2011-BLG-039 (OB110037)
* OGLE-2011-BLG-0310/MOA-2011-BLG-332 (OB110310)
* OGLE-2011-BLG-0462/MOA-2011-BLG-191 (OB110462)

The simulations were generated using the PopSyCLE software.


###########################################################
                 Files in this repository      
###########################################################

There are 25 files total.

-------------------
MOA lightcurves (5)
-------------------
* MOA-2009-BLG-260.dat
* MOA-2010-BLG-364.dat
* MOA-2011-BLG-039.dat
* MOA-2011-BLG-332.dat
* MOA-2011-BLG-191.dat

--------------------
OGLE lightcurves (3)
--------------------
If you make use of any of the OGLE data in publication, please cite:
"OGLE-IV: Fourth Phase of the Optical Gravitational Lensing Experiment", 
Udalski, A., Szymanski, M.K., and Szymanski, G. 2015 Acta Astron. 65, 1.
(https://ui.adsabs.harvard.edu/abs/2015AcA....65....1U/abstract)

* OGLE-2011-BLG-0037.dat
* OGLE-2011-BLG-0310.dat
* OGLE-2011-BLG-0462.dat

-----------------------------------
HST lightcurves and astrometry (10)
-----------------------------------
If you make use of any of the HST data in publication, please cite:
"An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJL
and
"Supplement: An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJS

* MB09260_HST_F606W.dat
* MB09260_HST_F814W.dat 
* MB10364_HST_F606W.dat
* MB10364_HST_F814W.dat 
* OB110037_HST_F606W.dat
* OB110037_HST_F814W.dat 
* OB110310_HST_F606W.dat
* OB110310_HST_F814W.dat 
* OB110462_HST_F606W.dat
* OB110462_HST_F814W.dat 

--------------------------------------------
Microlensing parameter posterior samples (6)
--------------------------------------------
If you make use of any of these posterior samples in publication, please cite:
"An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJL
and
"Supplement: An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJS

* MB09260_post.fits
* MB10364_post.fits
* OB110037_post.fits 
* OB110310_post.fits
* OB110462_DW_post.fits
* OB110462_EW_post.fits

---------------------------
Microlensing simulation (1)
---------------------------
If you make use of this simulation in publication, please cite:
"An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJL
and
"Supplement: An isolated mass gap black hole or neutron star detected with 
astrometric microlensing", Lam, C. Y., et al. 2022 ApJS

* popsycle_sim.fits


###########################################################
               Documentation and data formats
###########################################################

------------------------
MOA and OGLE lightcurves
------------------------
The MOA and OGLE lightcurves are provided as ascii tables.
There are three columns: 
* time in HJD (hjd);
* magnitude (mag);
* magnitude errors (mag_err).

The magnitudes for OGLE lightcurves are OGLE-IV I band.
The magnitudes for MOA lightcurves are calibrated to OGLE-III band.

------------------------------
HST lightcurves and astrometry
------------------------------
The HST data are provided as ascii tables.
There are two tables for each target, one associated with the F814W 
measurements, and one for the F606W measurements.

There are 7 columns: 
* time in UTC (t);
* RA relative position in mas (x);
* RA position errors in mas (x_err);
* Dec relative position in mas (y); 
* Dec position errors in mas (y_err); 
* Vega magnitude (mag);
* Vega magnitude errors (mag_err).

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