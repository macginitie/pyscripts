#!/usr/bin/python

import os

#f1 = open( 'd:/src/py/rb7mfi.cpp' )
#f1 = open( 'd:/src/py/rb6mfi.cpp' )
f1 = open( 'd:/src/py/rb6mfmm.cpp' )

sortedlines = f1.readlines()
sortedlines.sort()
for line in sortedlines:
    print( line[:-1] )
    
    