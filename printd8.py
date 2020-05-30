#!/usr/bin/python

import time

def printdate( date ) :
    localized = time.localtime( date )
    printd8 = time.strftime( "%m/%d/%Y %H:%M:%S", localized )
    print( printd8 )

if __name__ == '__main__' :
    for d8 in range( 10 ) :
        checkd8 = 1000000000 + (1000000 * d8)
        print( checkd8 )
        printdate( checkd8 )
    print( '11 days, 13 hours, 46 minutes is ', 11*24*60*60 + 13*60*60 + 46*60, 'seconds' )
    st = time.localtime()
    print( time.time() )
    secs = st.tm_sec
    secs += (st.tm_min*60)
    secs += (st.tm_hour*3600)
    secs += (st.tm_yday*24*3600)
    print( secs, 'seconds since the New Year (w/o accounting for DST)' )
    printdate( time.time() )
    printdate( time.time() - secs )