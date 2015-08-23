import calendar as cal
from datetime import date as dt, timedelta as td

def main():
    newCal = cal.Calendar()
    
    newCal.draw()
    '''zzz = [[" " for i in xrange(50)] for i in xrange(50)]
    for d in newCal.events:
        x = (d.date - dt.today()).days
        y = d.importance
        zzz[5*y][x] = d.name
    
    print("------------------------------------------>days")
    for zz in zzz:
        sys.stdout.write('|')
        for z in zz:
            sys.stdout.write(' '+z+' ')
        print
    print('v')
    print('importance')'''
main()

