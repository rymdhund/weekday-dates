import calendar
import sys

if len(sys.argv) != 4:
    print "usage: "+sys.argv[0]+" <year> <month> <days>"
    print "   where days is a comma-separated list and monday is 0"
    print "   so for example tue+thurs in feb 2012 would be"
    print "   "+sys.argv[0]+" 2012 2 1,3"
    exit(0)
c = calendar.Calendar()

days = map(int,sys.argv[3].split(","))
for x,y in c.itermonthdays2(int(sys.argv[1]), int(sys.argv[2])):
    if x > 0:
        if y in days:
            print x
