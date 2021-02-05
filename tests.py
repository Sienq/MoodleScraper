
from getCredentials import getCredentials
import calendarEvent import *
import calendarSourceDownloader
from datetime import datetime

TEST_CRIDENTIALS_FILE = "config/test_cridentials.txt"
TEST_EVENTS_FILE = "config/test_events.json"

def calendaSourceDownladTest():

    cridentials = getCridentials(TEST_CRIDENTIALS_FILE)

    try:
        print(calendarSourceDownloader.getEventsPageSource(cridentials))
        print("CRIDENTIALS DOWNLOAD TEST PASSED")
    
    except:
        print("CRIDENTIALS DOWNLOAD TEST FAILED")


def calendarEventSerialisationTest():

    date1 = datetime(year=2020, month=10, day=2, hour=14, minute=20)
    date2 = datetime(year=2021, month=11, day=2, hour=12, minute=10)
    date3 = datetime(year=2022, month=11, day=1, hour=14, minute=20)

    event1 = calendarEvent.CalendarEvent("event1", "eng", date1)
    event2 = calendarEevent.CalendarEvent("event2", "fiz", date2)
    event3 = calendarEvent.CalendarEvent("event3", "elc", date3)

    org_events = [event1, event2, event3]
    
    calendarEvent.saveEvents(org_events, TEST_EVENTS_FILE)
    loaded_events = calendarEvent.loadEvents(TEST_EVENTS_FILE)

    if len(org_events) != len(loaded_events):
        print("CALENDAR EVENT SERIALISATION TEST FAILED")

    for i in range(len(org_events)):

        if org_events[i] != loaded_events[i]:
            print("CALENDAR EVENT SERIALISATION TEST FAILED")

    print("CALENDAR EVENT SERIALISATION TEST PASSED")


if __name__ == "__main__":

    calendaSourceDownladTest()
    calendarEventSerialisationTest() 