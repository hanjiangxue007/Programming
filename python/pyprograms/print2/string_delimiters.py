#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 24, 2016
# Last update : 
#
# Inputs      : none
# Outputs     : 
#
# Info:
# 1. break a long string separated by delimiters and print them.
#

# Imports
import re 


dan = 'dan|warrior|54'
print(*dan.split('|'), sep='\n')



# example
commands= " " +\
"cd ~/jedisim/imcat_analysis/galshear; " +\
"catcats galshear_[0123456789].cat galshear_[1234][0123456789].cat > galshear_big.cat"

print(*commands.split(';'), sep='\n')



# example
commands = " " +\
"cd ~/jedisim/imcat_analysis/galshear; " +\
"lc -c < galshear_big.cat ; " +\
"lc -i '%rg 1.5 > %ce %ce dot 1 < and' < galshear_big.cat > galshear_cut.cat ;  " +\
"lc -b +all 'x = %rg %ce[0] 2 vector' 'cPg0 = %cPg[0][0]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 cPg0 > galshear_cpg0.par ;  " +\
"lc -b +all 'x = %rg %ce[1] 2 vector' 'cPg1 = %cPg[1][1]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 cPg1 > galshear_cpg1.par "


print(*commands.split(';'), sep='\n')

