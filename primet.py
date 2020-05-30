#!/usr/bin/python

def factors( anint ) :
    facs = []
    for test in range( 2, anint ) :
        #print( test, anint % test )
        if (0 == (anint % test)) :
            facs.append( test )
    return facs
        
#print( factors( 10 ), len( factors( 11 ) ) )

if __name__ == "__main__" :

    first = 41003
    while (len( factors( first ) ) > 0) :
        print( first, end=', ' )
        first += 1