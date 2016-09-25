#!/usr/bin/python3

import csv

# symbol -> (name, atomic number, boiling pt.)
symbol_to_properties = {
    'H':  ('hydrogen',	1,	20.28),
    'He': ('helium',	2,	4.22),
    'Li': ('lithium',	3,	1615.0),
    'Be': ('beryllium',	4,	2742.0),
    'B':  ('boron',	5,	4200.0),
    'C':  ('carbon',	6,	5100.0),
    'N':  ('nitrogen',	7,	77.36),
    'O':  ('oxygen',	8,	90.20),
    'F':  ('fluorine',	9,	85.03),
    'Ne': ('neon',	10,	27.07),
    'Na': ('sodium',	11,	1156.0),
    'Mg': ('magnesium',	12,	1363.0),
    'Al': ('aluminium',	13,	2792.0),
    'Si': ('silicon',	14,	3538.0),
    'P':  ('phosphorus',	15,	553.0),
    'S':  ('sulphur',	16,	717.8),
    'Cl': ('chlorine',	17,	239.11),
    'Ar': ('argon',	18,	87.30),
    'K':  ('potassium',	19,	1032.0),
    'Ca': ('calcium',	20,	1757.0),
    'Sc': ('scandium',	21,	3109.0),
    'Ti': ('titanium',	22,	3560.0),
    'V':  ('vanadium',	23,	3680.0),
    'Cr': ('chromium',	24,	2944.0),
    'Mn': ('manganese',	25,	2334.0),
    'Fe': ('iron',	26,	3134.0),
    'Co': ('cobalt',	27,	3200.0),
    'Ni': ('nickel',	28,	3186.0),
    'Cu': ('copper',	29,	2835.0),
    'Zn': ('zinc',	30,	1180.0),
    'Ga': ('gallium',	31,	2477.0),
    'Ge': ('germanium',	32,	3106.0),
    'As': ('arsenic',	33,	887.0),
    'Se': ('selenium',	34,	958.0),
    'Br': ('bromine',	35,	332.0),
    'Kr': ('krypton',	36,	119.93),
    'Rb': ('rubidium',	37,	961.0),
    'Sr': ('strontium',	38,	1655.0),
    'Y':  ('yttrium',	39,	3609.0),
    'Zr': ('zirconium',	40,	4682.0),
    'Nb': ('niobium',	41,	5017.0),
    'Mo': ('molybdenum',	42,	4912.0),
    'Tc': ('technetium',	43,	5150.0),
    'Ru': ('ruthenium',	44,	4423.0),
    'Rh': ('rhodium',	45,	3968.0),
    'Pd': ('palladium',	46,	3236.0),
    'Ag': ('silver',	47,	2435.0),
    'Cd': ('cadmium',	48,	1040.0),
    'In': ('indium',	49,	2345.0),
    'Sn': ('tin',	50,	2875.0),
    'Sb': ('antimony',	51,	1860.0),
    'Te': ('tellurium',	52,	1261.0),
    'I':  ('iodine',	53,	457.4),
    'Xe': ('xenon',	54,	165.03),
    'Cs': ('caesium',	55,	944.0),
    'Ba': ('barium',	56,	2170.0),
    'La': ('lanthanum',	57,	3737.0),
    'Ce': ('cerium',	58,	3716.0),
    'Pr': ('praesodymium',	59,	3793.0),
    'Nd': ('neodymium',	60,	3347.0),
    'Pm': ('promethium',	61,	3273.0),
    'Sm': ('samarium',	62,	2067.0),
    'Eu': ('europium',	63,	1802.0),
    'Gd': ('gadolinium',	64,	3546.0),
    'Tb': ('terbium',	65,	3503.0),
    'Dy': ('dysprosium',	66,	2840.0),
    'Ho': ('holmium',	67,	2993.0),
    'Er': ('erbium',	68,	3503.0),
    'Tm': ('thulium',	69,	2223.0),
    'Yb': ('ytterbium',	70,	1469.0),
    'Lu': ('lutetium',	71,	3675.0),
    'Hf': ('hafnium',	72,	4876.0),
    'Ta': ('tantalum',	73,	5731.0),
    'W':  ('tungsten',	74,	5930.0),
    'Re': ('rhenium',	75,	5900.0),
    'Os': ('osmium',	76,	5285.0),
    'Ir': ('iridium',	77,	4701.0),
    'Pt': ('platinum',	78,	4098.0),
    'Au': ('gold',	79,	3129.0),
    'Hg': ('mercury',	80,	630.0),
    'Tl': ('thallium',	81,	1746.0),
    'Pb': ('lead',	82,	2022.0),
    'Bi': ('bismuth',	83,	1837.0),
    'Po': ('polonium',	84,	1235.0),
    'At': ('astatine',	85,	610.0),
    'Rn': ('radon',	86,	211.3),
    'Fr': ('francium',	87,	950.0),
    'Ra': ('radium',	88,	2010.0),
    'Ac': ('actinium',	89,	3471.0),
    'Th': ('thorium',	90,	5061.0),
    'Pa': ('protactinium',	91,	4300.0),
    'U':  ('uranium',	92,	4404.0),
    }


output_file = open('atomic_props.csv', 'w', newline='')

data = csv.writer(output_file)

for symbol in symbol_to_properties:
    (name, anum, boil) = symbol_to_properties[symbol]
    data.writerow([symbol, name, anum, boil])
del symbol, name, anum, boil

del data

output_file.close()
del output_file
