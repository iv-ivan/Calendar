from datetime import date as DATE
import sys

class Painter(object):
    def __init__(self):
        x = 60
        y = 8
        self.x = x
        self.y = y
        
        self.field = [[' ' for i in xrange(2*x + 2)] for i in xrange(5*y + 2)]
        
        for i in xrange(2*x + 1):
            if (i % 2 == 1):
                self.field[0][i] = '-'
            else:
                self.field[0][i] = '+'
            if (i % 10 == 0):
                self.field[0][i] = str(i / 2)
        self.field[0][-1] =  '>'
        
        for i in xrange(5*y + 1):
            self.field[i][0] = '|'
            if (i % 5 == 0):
                self.field[i][0] = str(i / 5)
        self.field[-1][0] =  '^'
        
    def placeEvent(self, event):
        self.field[int(5*event.hours)][2*((event.date - DATE.today()).days)] = event.name[0]
    
    def buildInformation(self, events):
        width = 15
        self.information = ["" for i in xrange(5*self.y + 2)]
        for i, event in enumerate(events):
            self.information[i] = event.name + " " + str(event.hours) + " " + str(event.date)
            
    def draw(self, events):
        for event in events:
            self.placeEvent(event)
        self.buildInformation(events)
        
        print
        for i, row in enumerate(reversed(self.field)):
            for cell in row:
                sys.stdout.write(cell)
            if len(self.information[i]) > 0:
                sys.stdout.write('(' + self.information[i][0] + ') - ' + self.information[i])
            print
  