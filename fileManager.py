from datetime import date as DATE
from event import Event

class FileManager(object):
    def __init__(self, filename):
        self.filename = filename
    
    def readEvents(self):
        events = []
        with open(self.filename, 'r') as file:
            for line in file:
                values = line.split(';')
                dateValues = values[1].split('.')
                eventDate = DATE(day = int(dateValues[0]), month = int(dateValues[1]), year = int(dateValues[2]))
                
                if eventDate >= DATE.today():
                    event = Event(values[0], eventDate, float(values[2]))
                    events.append(event)
        return events

    def rewriteEvents(self, events):
        with open(self.filename, 'w') as file:
            for event in events:
                file.write(event.name + ';' + str(event.date.day) + '.' + str(event.date.month) + '.' + str(event.date.year) + ';' + str(event.hours) + '\n')
