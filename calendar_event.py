
from datetime import datetime
import json

class CalendarEvent:

    DATE_FORMAT = '%Y-%m-%d %H:%M'

    def __init__(self, name, course, date):

        self.name = name
        self.course = course
        self.date = date

    def __repr__(self):

        print(
            self.name,
            self.course,
            self.date
            )

    @classmethod
    def initFromDict(cls, _dict):

        name = _dict['name']
        course = _dict['course']
        date = datetime.strptime(_dict['date'], cls.DATE_FORMAT)
        
        return cls(name, course, date)
    

    def toDict(self):

        _dict = dict()

        _dict['name'] = self.name
        _dict['course'] = self.course
        _dict['date'] = self.date.strftime(self.DATE_FORMAT)

        return _dict

    def __eq__(self, other):

        if self.name == other.name and self.course == other.course and self.date == other.date:
            return True
        
        else:
            return False


def saveEvents(events, file_name):

    dicted_events = []

    for event in events:
        dicted_events.append(event.toDict())

    with open(file_name, "w") as f:
        f.write(json.dumps(dicted_events))


def loadEvents(file_name):

    events = []

    with open(file_name, "r") as f:

        file_contents = f.read()
        dicted_events = json.loads(file_contents)
    
    for dicted in dicted_events:
        events.append(CalendarEvent.initFromDict(dicted))
    
    return events
