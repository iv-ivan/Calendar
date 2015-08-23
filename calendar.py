from datetime import date as DATE
import sys

class Event(object):
    def __init__(self, name, date, hours):
        self.hours = hours
        self.date = date
        self.name = name
        
    def __str__(self):
        return self.name + " " + str(self.hours) + " " + str(self.date)

class Calendar(object):
    def __init__(self):
        fManager = FileManager('data.txt')
        self.events = fManager.events
        self.painter = Painter()
        fManager.rewriteEvents()
        
    def draw(self):
        self.painter.draw(self.events)
        
class FileManager(object):
    def __init__(self, filename):
        self.events = []
        file = open(filename, 'r')
        self.filename = filename
        
        for line in file:
            values = line.split(';')
            dateValues = values[1].split('.')
            eventDate = DATE(day = int(dateValues[0]), month = int(dateValues[1]), year = int(dateValues[2]))
            
            if eventDate >= DATE.today():
                event = Event(values[0], eventDate, float(values[2]))
                self.events.append(event)
        file.close()

    def rewriteEvents(self):
        file = open(self.filename, 'w')
        
        for event in self.events:
            file.write(event.name + ';' + str(event.date.day) + '.' + str(event.date.month) + '.' + str(event.date.year) + ';' + str(event.hours) + '\n')
        file.close()
            
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
        