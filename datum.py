import calendar
import sys

if len(sys.argv) != 4:
    print "usage: "+sys.argv[0]+" <year> <month> <days>"
    print "   where days is a comma-separated list and monday is 0"
    print "   so for example tue+thurs in feb 2012 would be"
    print "   "+sys.argv[0]+" 2012 2 1,3"
    exit(0)
c = calendar.Calendar()

day_names = ['mon','tue','wed','thu','fri','sat','sun']
month_names = ['error','jan','feb','mar','apr','may','june','july','aug','sept',
        'oct','nov','dec']
year = int(sys.argv[1])
month = int(sys.argv[2])
days = map(int,sys.argv[3].split(","))


print 'showing all '+str(map(lambda x: day_names[x],days))+" in "\
        +month_names[month]+" of "+str(year)+":"

for x,y in c.itermonthdays2(year, month):
    if x > 0:
        if y in days:
            print x
