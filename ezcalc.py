#!/usr/bin/python
#
# use Python 3.0

minutesperhour = 60
workhoursperday = 8
minutesperworkday = (minutesperhour * workhoursperday)
print( "minutes per workday = %d" % minutesperworkday )

minutesperfilediff = 10
diffsperday = minutesperworkday / minutesperfilediff
print( "diffs per workday = %d" % diffsperday )
numfilediffs = 5123
daysrequired = numfilediffs / diffsperday
print( "days required = %d" % daysrequired )

