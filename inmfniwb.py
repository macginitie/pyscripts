import sys
from datetime import datetime as dt
from datetime import timedelta as td

now = dt.now()
#print(now.date())

"""
inmfniwb = 
In N Minutes From Now It Will Be
"""


if __name__ == '__main__':
    try:   
        mfn = int(sys.argv[1])
    except:
        print('please provide a # of minutes as arg #1')
        exit(0)
        
    print('in {0} minutes it will be {1}'.format(mfn, (now + td(minutes=mfn))))

