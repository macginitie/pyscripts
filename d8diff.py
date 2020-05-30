import sys

reqd_args = 7   # later[m/d/y] earlier[m/d/y] (+ py script name)
month_days = 30.44

print
print('------- d8 diff approxim8r --------')
# print(len(sys.argv))
if len(sys.argv) < reqd_args :
    print('later_month, later_day, later_year, earlier_month, earlier_day, earlier_year')
    exit()

l_mo = int(sys.argv[1])
l_day = int(sys.argv[2])
l_yr = int(sys.argv[3])
e_mo = int(sys.argv[4])
e_day = int(sys.argv[5])
e_yr = int(sys.argv[6])
    
# approxim8
earlier = e_yr*365.25 + e_mo*month_days + e_day
later = l_yr*365.25 + l_mo*month_days + l_day

print('approxim8ly ' + str(later - earlier) + ' days')



