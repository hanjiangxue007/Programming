#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 11, 2016
# Last update :
#

# Imports
import scipy
from scipy.constants import codata as cd


e = cd.value('elementary charge')
print(e)  #     1.602176487e-019

m_alpha = cd.value('alpha particle mass')
print(m_alpha)  #     6.64465675e-27 kg

lookup = scipy.constants.find("light")
print(lookup)

lookup = scipy.constants.find("alpha")
print(lookup)

# alpha particle mass    6.64465675e-27 kg
# alpha particle mass energy equivalent  5.97191967e-10 J
# alpha particle mass energy equivalent in MeV   3727.37924 MeV
# alpha particle mass in u   4.00150617913 u
# alpha particle molar mass  0.00400150617912 kg mol^-1
# alpha particle-electron mass ratio 7294.2995361
# alpha particle-proton mass ratio   3.97259968933
#  Angstrom star  1.00001495e-10 m
#  atomic mass constant   1.660538921e-27 kg
#  atomic mass constant energy equivalent 1.492417954e-10 J
#  atomic mass constant energy equivalent in MeV  931.494061 MeV
#  atomic mass unit-electron volt relationship    931494061.0 eV
#  atomic mass unit-hartree relationship  34231776.845 E_h
#  atomic mass unit-hertz relationship    2.2523427168e+23 Hz
#  atomic mass unit-inverse meter relationship    7.5130066042e+14 m^-1
#  atomic mass unit-joule relationship    1.492417954e-10 J
#  atomic mass unit-kelvin relationship   1.08095408e+13 K
#  atomic mass unit-kilogram relationship 1.660538921e-27 kg
#  atomic unit of 1st hyperpolarizability 3.206361449e-53 C^3 m^3 J^-2
#  atomic unit of 2nd hyperpolarizability 6.23538054e-65 C^4 m^4 J^-3
#  atomic unit of action  1.054571726e-34 J s
#  atomic unit of charge  1.602176565e-19 C
#  atomic unit of charge density  1.081202338e+12 C m^-3
#  atomic unit of current 0.00662361795 A
#  atomic unit of electric dipole mom.    8.47835326e-30 C m
#  atomic unit of electric field  5.14220652e+11 V m^-1
#  atomic unit of electric field gradient 9.717362e+21 V m^-2
#  atomic unit of electric polarizability 1.6487772754e-41 C^2 m^2 J^-1
#  atomic unit of electric potential  27.21138505 V
#  atomic unit of electric quadrupole mom.    4.486551331e-40 C m^2
#  atomic unit of energy  4.35974434e-18 J
#  atomic unit of force   8.23872278e-08 N
#  atomic unit of length  5.2917721092e-11 m
#  atomic unit of mag. dipole mom.    1.854801936e-23 J T^-1
#  atomic unit of mag. flux density   235051.7464 T
#  atomic unit of magnetizability 7.891036607e-29 J T^-2
#  atomic unit of mass    9.10938291e-31 kg
#  atomic unit of mom.um  1.99285174e-24 kg m s^-1
#  atomic unit of permittivity    1.11265005605e-10 F m^-1
#  atomic unit of time    2.4188843265e-17 s
#  atomic unit of velocity    2187691.26379 m s^-1
#  Avogadro constant  6.02214129e+23 mol^-1
#  Bohr magneton  9.27400968e-24 J T^-1
#  Bohr magneton in eV/T  5.7883818066e-05 eV T^-1
#  Bohr magneton in Hz/T  13996245550.0 Hz T^-1
#  Bohr magneton in inverse meters per tesla  46.6864498 m^-1 T^-1
#  Bohr magneton in K/T   0.67171388 K T^-1
#  Bohr radius    5.2917721092e-11 m
#  Boltzmann constant 1.3806488e-23 J K^-1
#  Boltzmann constant in eV/K 8.6173324e-05 eV K^-1
#  Boltzmann constant in Hz/K 20836618000.0 Hz K^-1
#  Boltzmann constant in inverse meters per kelvin    69.503476 m^-1 K^-1
#  characteristic impedance of vacuum 376.730313462 ohm
#  classical electron radius  2.8179403267e-15 m
#  Compton wavelength 2.4263102389e-12 m
#  Compton wavelength over 2 pi   3.86159268e-13 m
#  conductance quantum    7.7480917346e-05 S
#  conventional value of Josephson constant   4.835979e+14 Hz V^-1
#  conventional value of von Klitzing constant    25812.807 ohm
#  Cu x unit  1.00207697e-13 m
#  deuteron g factor  0.8574382308
#  deuteron mag. mom. 4.33073489e-27 J T^-1
#  deuteron mag. mom. to Bohr magneton ratio  0.0004669754556
#  deuteron mag. mom. to nuclear magneton ratio   0.8574382308
#  deuteron mass  3.34358348e-27 kg
#  deuteron mass energy equivalent    3.00506297e-10 J
#  deuteron mass energy equivalent in MeV 1875.612859 MeV
#  deuteron mass in u 2.01355321271 u
#  deuteron molar mass    0.00201355321271 kg mol^-1
#  deuteron rms charge radius 2.1424e-15 m
#  deuteron-electron mag. mom. ratio  -0.0004664345537
#  deuteron-electron mass ratio   3670.4829652
#  deuteron-neutron mag. mom. ratio   -0.44820652
#  deuteron-proton mag. mom. ratio    0.307012207
#  deuteron-proton mass ratio 1.99900750097
#  electric constant  8.85418781762e-12 F m^-1
#  electron charge to mass quotient   -1.758820088e+11 C kg^-1
#  electron g factor  -2.00231930436
#  electron gyromag. ratio    1.760859708e+11 s^-1 T^-1
#  electron gyromag. ratio over 2 pi  28024.95266 MHz T^-1
#  electron mag. mom. -9.2847643e-24 J T^-1
#  electron mag. mom. anomaly 0.00115965218076
#  electron mag. mom. to Bohr magneton ratio  -1.00115965218
#  electron mag. mom. to nuclear magneton ratio   -1838.2819709
#  electron mass  9.10938291e-31 kg
#  electron mass energy equivalent    8.18710506e-14 J
#  electron mass energy equivalent in MeV 0.510998928 MeV
#  electron mass in u 0.00054857990946 u
#  electron molar mass    5.4857990946e-07 kg mol^-1
#  electron to alpha particle mass ratio  0.000137093355578
#  electron to shielded helion mag. mom. ratio    864.058257
#  electron to shielded proton mag. mom. ratio    -658.2275971
#  electron volt  1.602176565e-19 J
#  electron volt-atomic mass unit relationship    1.07354415e-09 u
#  electron volt-hartree relationship 0.03674932379 E_h
#  electron volt-hertz relationship   2.417989348e+14 Hz
#  electron volt-inverse meter relationship   806554.429 m^-1
#  electron volt-joule relationship   1.602176565e-19 J
#  electron volt-kelvin relationship  11604.519 K
#  electron volt-kilogram relationship    1.782661845e-36 kg
#  electron-deuteron mag. mom. ratio  -2143.923498
#  electron-deuteron mass ratio   0.00027244371095
#  electron-helion mass ratio 0.00018195430761
#  electron-muon mag. mom. ratio  206.7669896
#  electron-muon mass ratio   0.00483633166
#  electron-neutron mag. mom. ratio   960.9205
#  electron-neutron mass ratio    0.00054386734461
#  electron-proton mag. mom. ratio    -658.2106848
#  electron-proton mass ratio 0.00054461702178
#  electron-tau mass ratio    0.000287592
#  electron-triton mass ratio 0.00018192000653
#  elementary charge  1.602176565e-19 C
#  elementary charge over h   2.417989348e+14 A J^-1
#  Faraday constant   96485.3365 C mol^-1
#  Faraday constant for conventional electric current 96485.3321 C_90 mol^-1
#  Fermi coupling constant    1.166364e-05 GeV^-2
#  fine-structure constant    0.0072973525698
#  first radiation constant   3.74177153e-16 W m^2
#  first radiation constant for spectral radiance 1.191042869e-16 W m^2 sr^-1
#  Hartree energy 4.35974434e-18 J
#  Hartree energy in eV   27.21138505 eV
#  hartree-atomic mass unit relationship  2.9212623246e-08 u
#  hartree-electron volt relationship 27.21138505 eV
#  hartree-hertz relationship 6.57968392073e+15 Hz
#  hartree-inverse meter relationship 21947463.1371 m^-1
#  hartree-joule relationship 4.35974434e-18 J
#  hartree-kelvin relationship    315775.04 K
#  hartree-kilogram relationship  4.85086979e-35 kg
#  helion g factor    -4.255250613
#  helion mag. mom.   -1.074617486e-26 J T^-1
#  helion mag. mom. to Bohr magneton ratio    -0.001158740958
#  helion mag. mom. to nuclear magneton ratio -2.127625306
#  helion mass    5.00641234e-27 kg
#  helion mass energy equivalent  4.49953902e-10 J
#  helion mass energy equivalent in MeV   2808.391482 MeV
#  helion mass in u   3.0149322468 u
#  helion molar mass  0.0030149322468 kg mol^-1
#  helion-electron mass ratio 5495.8852754
#  helion-proton mass ratio   2.9931526707
#  hertz-atomic mass unit relationship    4.4398216689e-24 u
#  hertz-electron volt relationship   4.135667516e-15 eV
#  hertz-hartree relationship 1.519829846e-16 E_h
#  hertz-inverse meter relationship   3.33564095198e-09 m^-1
#  hertz-joule relationship   6.62606957e-34 J
#  hertz-kelvin relationship  4.7992434e-11 K
#  hertz-kilogram relationship    7.37249668e-51 kg
#  inverse fine-structure constant    137.035999074
#  inverse meter-atomic mass unit relationship    1.3310250512e-15 u
#  inverse meter-electron volt relationship   1.23984193e-06 eV
#  inverse meter-hartree relationship 4.55633525276e-08 E_h
#  inverse meter-hertz relationship   299792458.0 Hz
#  inverse meter-joule relationship   1.986445684e-25 J
#  inverse meter-kelvin relationship  0.01438777 K
#  inverse meter-kilogram relationship    2.210218902e-42 kg
#  inverse of conductance quantum 12906.4037217 ohm
#  Josephson constant 4.8359787e+14 Hz V^-1
#  joule-atomic mass unit relationship    6700535850.0 u
#  joule-electron volt relationship   6.24150934e+18 eV
#  joule-hartree relationship 2.29371248e+17 E_h
#  joule-hertz relationship   1.509190311e+33 Hz
# joule-inverse meter relationship   5.03411701e+24 m^-1
# joule-kelvin relationship  7.2429716e+22 K
# joule-kilogram relationship    1.11265005605e-17 kg
# kelvin-atomic mass unit relationship   9.2510868e-14 u
# kelvin-electron volt relationship  8.6173324e-05 eV
# kelvin-hartree relationship    3.1668114e-06 E_h
# kelvin-hertz relationship  20836618000.0 Hz
# kelvin-inverse meter relationship  69.503476 m^-1
# kelvin-joule relationship  1.3806488e-23 J
# kelvin-kilogram relationship   1.536179e-40 kg
# kilogram-atomic mass unit relationship 6.02214129e+26 u
# kilogram-electron volt relationship    5.60958885e+35 eV
# kilogram-hartree relationship  2.061485968e+34 E_h
# kilogram-hertz relationship    1.356392608e+50 Hz
# kilogram-inverse meter relationship    4.52443873e+41 m^-1
# kilogram-joule relationship    8.98755178737e+16 J
# kilogram-kelvin relationship   6.5096582e+39 K
# lattice parameter of silicon   5.431020504e-10 m
# Loschmidt constant (273.15 K, 100 kPa) 2.6516462e+25 m^-3
# Loschmidt constant (273.15 K, 101.325 kPa) 2.6867805e+25 m^-3
# mag. constant  1.25663706144e-06 N A^-2
# mag. flux quantum  2.067833758e-15 Wb
# Mo x unit  1.00209952e-13 m
# molar gas constant 8.3144621 J mol^-1 K^-1
# molar mass constant    0.001 kg mol^-1
# molar mass of carbon-12    0.012 kg mol^-1
# molar Planck constant  3.9903127176e-10 J s mol^-1
# molar Planck constant times c  0.119626565779 J m mol^-1
# molar volume of ideal gas (273.15 K, 100 kPa)  0.022710953 m^3 mol^-1
# molar volume of ideal gas (273.15 K, 101.325 kPa)  0.022413968 m^3 mol^-1
# molar volume of silicon    1.205883301e-05 m^3 mol^-1
# muon Compton wavelength    1.173444103e-14 m
# muon Compton wavelength over 2 pi  1.867594294e-15 m
# muon g factor  -2.0023318418
# muon mag. mom. -4.49044807e-26 J T^-1
# muon mag. mom. anomaly 0.00116592091
# muon mag. mom. to Bohr magneton ratio  -0.00484197044
# muon mag. mom. to nuclear magneton ratio   -8.89059697
# muon mass  1.883531475e-28 kg
# muon mass energy equivalent    1.692833667e-11 J
# muon mass energy equivalent in MeV 105.6583715 MeV
# muon mass in u 0.1134289267 u
# muon molar mass    0.0001134289267 kg mol^-1
# muon-electron mass ratio   206.7682843
# muon-neutron mass ratio    0.1124545177
# muon-proton mag. mom. ratio    -3.183345107
# muon-proton mass ratio 0.1126095272
# muon-tau mass ratio    0.0594649
# natural unit of action 1.054571726e-34 J s
# natural unit of action in eV s 6.58211928e-16 eV s
# natural unit of energy 8.18710506e-14 J
# natural unit of energy in MeV  0.510998928 MeV
# natural unit of length 3.86159268e-13 m
# natural unit of mass   9.10938291e-31 kg
# natural unit of mom.um 2.73092429e-22 kg m s^-1
# natural unit of mom.um in MeV/c    0.510998928 MeV/c
# natural unit of time   1.28808866833e-21 s
# natural unit of velocity   299792458.0 m s^-1
# neutron Compton wavelength 1.3195909068e-15 m
# neutron Compton wavelength over 2 pi   2.1001941568e-16 m
# neutron g factor   -3.82608545
# neutron gyromag. ratio 183247179.0 s^-1 T^-1
# neutron gyromag. ratio over 2 pi   29.1646943 MHz T^-1
# neutron mag. mom.  -9.6623647e-27 J T^-1
# neutron mag. mom. to Bohr magneton ratio   -0.00104187563
# neutron mag. mom. to nuclear magneton ratio    -1.91304272
# neutron mass   1.674927351e-27 kg
# neutron mass energy equivalent 1.505349631e-10 J
# neutron mass energy equivalent in MeV  939.565379 MeV
# neutron mass in u  1.008664916 u
# neutron molar mass 0.001008664916 kg mol^-1
# neutron to shielded proton mag. mom. ratio -0.68499694
# neutron-electron mag. mom. ratio   0.00104066882
# neutron-electron mass ratio    1838.6836605
# neutron-muon mass ratio    8.892484
# neutron-proton mag. mom. ratio -0.68497934
# neutron-proton mass difference 2.30557392e-30
# neutron-proton mass difference energy equivalent   2.0721465e-13
# neutron-proton mass difference energy equivalent in MeV    1.29333217
# neutron-proton mass difference in u    0.00138844919
# neutron-proton mass ratio  1.00137841917
# neutron-tau mass ratio 0.52879
# Newtonian constant of gravitation  6.67384e-11 m^3 kg^-1 s^-2
# Newtonian constant of gravitation over h-bar c 6.70837e-39 (GeV/c^2)^-2
# nuclear magneton   5.05078353e-27 J T^-1
# nuclear magneton in eV/T   3.1524512605e-08 eV T^-1
# nuclear magneton in inverse meters per tesla   0.02542623527 m^-1 T^-1
# nuclear magneton in K/T    0.00036582682 K T^-1
# nuclear magneton in MHz/T  7.62259357 MHz T^-1
# Planck constant    6.62606957e-34 J s
# Planck constant in eV s    4.135667516e-15 eV s
# Planck constant over 2 pi  1.054571726e-34 J s
# Planck constant over 2 pi in eV s  6.58211928e-16 eV s
# Planck constant over 2 pi times c in MeV fm    197.3269718 MeV fm
# Planck length  1.616199e-35 m
# Planck mass    2.17651e-08 kg
# Planck mass energy equivalent in GeV   1.220932e+19 GeV
# Planck temperature 1.416833e+32 K
# Planck time    5.39106e-44 s
# proton charge to mass quotient 95788335.8 C kg^-1
# proton Compton wavelength  1.32140985623e-15 m
# proton Compton wavelength over 2 pi    2.1030891047e-16 m
# proton g factor    5.585694713
# proton gyromag. ratio  267522200.5 s^-1 T^-1
# proton gyromag. ratio over 2 pi    42.5774806 MHz T^-1
# proton mag. mom.   1.410606743e-26 J T^-1
# proton mag. mom. to Bohr magneton ratio    0.00152103221
# proton mag. mom. to nuclear magneton ratio 2.792847356
# proton mag. shielding correction   2.5694e-05
# proton mass    1.672621777e-27 kg
# proton mass energy equivalent  1.503277484e-10 J
# proton mass energy equivalent in MeV   938.272046 MeV
# proton mass in u   1.00727646681 u
# proton molar mass  0.00100727646681 kg mol^-1
# proton rms charge radius   8.775e-16 m
# proton-electron mass ratio 1836.15267245
# proton-muon mass ratio 8.88024331
# proton-neutron mag. mom. ratio -1.45989806
# proton-neutron mass ratio  0.99862347826
# proton-tau mass ratio  0.528063
# quantum of circulation 0.0003636947552 m^2 s^-1
# quantum of circulation times 2 0.0007273895104 m^2 s^-1
# Rydberg constant   10973731.5685 m^-1
# Rydberg constant times c in Hz 3.28984196036e+15 Hz
# Rydberg constant times hc in eV    13.60569253 eV
# Rydberg constant times hc in J 2.179872171e-18 J
# Sackur-Tetrode constant (1 K, 100 kPa) -1.1517078
# Sackur-Tetrode constant (1 K, 101.325 kPa) -1.1648708
# second radiation constant  0.01438777 m K
# shielded helion gyromag. ratio 203789465.9 s^-1 T^-1
# shielded helion gyromag. ratio over 2 pi   32.43410084 MHz T^-1
# shielded helion mag. mom.  -1.074553044e-26 J T^-1
# shielded helion mag. mom. to Bohr magneton ratio   -0.001158671471
# shielded helion mag. mom. to nuclear magneton ratio    -2.127497718
# shielded helion to proton mag. mom. ratio  -0.761766558
# shielded helion to shielded proton mag. mom. ratio -0.7617861313
# shielded proton gyromag. ratio 267515326.8 s^-1 T^-1
# shielded proton gyromag. ratio over 2 pi   42.5763866 MHz T^-1
# shielded proton mag. mom.  1.410570499e-26 J T^-1
# shielded proton mag. mom. to Bohr magneton ratio   0.001520993128
# shielded proton mag. mom. to nuclear magneton ratio    2.792775598
# speed of light in vacuum   299792458.0 m s^-1
# standard acceleration of gravity   9.80665 m s^-2
# standard atmosphere    101325.0 Pa
# standard-state pressure    100000.0 Pa
# Stefan-Boltzmann constant  5.670373e-08 W m^-2 K^-4
# tau Compton wavelength 6.97787e-16 m
# tau Compton wavelength over 2 pi   1.11056e-16 m
# tau mass   3.16747e-27 kg
# tau mass energy equivalent 2.84678e-10 J
# tau mass energy equivalent in MeV  1776.82 MeV
# tau mass in u  1.90749 u
# tau molar mass 0.00190749 kg mol^-1
# tau-electron mass ratio    3477.15
# tau-muon mass ratio    16.8167
# tau-neutron mass ratio 1.89111
# tau-proton mass ratio  1.89372
# Thomson cross section  6.652458734e-29 m^2
# triton g factor    5.957924896
# triton mag. mom.   1.504609447e-26 J T^-1
# triton mag. mom. to Bohr magneton ratio    0.001622393657
# triton mag. mom. to nuclear magneton ratio 2.978962448
# triton mass    5.0073563e-27 kg
# triton mass energy equivalent  4.50038741e-10 J
# triton mass energy equivalent in MeV   2808.921005 MeV
# triton mass in u   3.0155007134 u
# triton molar mass  0.0030155007134 kg mol^-1
# triton-electron mass ratio 5496.9215267
# triton-proton mass ratio   2.9937170308
# unified atomic mass unit   1.660538921e-27 kg
# von Klitzing constant  25812.8074434 ohm
# weak mixing angle  0.2223
# Wien frequency displacement law constant   58789254000.0 Hz K^-1
# Wien wavelength displacement law constant  0.0028977721 m K
# {220} lattice spacing of silicon   1.920155714e-10 m
