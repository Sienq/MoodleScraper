
import get_cridentials
import calendar_event
import calendar_source_downloader
from datetime import datetime

TEST_CRIDENTIALS_FILE = "cridentials.txt"
TEST_EVENTS_FILE = "events.json"

def calendaSourceDownladTest():

    cridentials = get_cridentials.getCridentials(TEST_CRIDENTIALS_FILE)

    try:
        print(calendar_source_downloader.getEventsPageSource(cridentials))
        print("CRIDENTIALS DOWNLOAD TEST PASSED")
    
    except:
        print("CRIDENTIALS DOWNLOAD TEST FAILED")


def calendarEventSerialisationTest():

    date1 = datetime(year=2020, month=10, day=2, hour=14, minute=20)
    date2 = datetime(year=2021, month=11, day=2, hour=12, minute=10)
    date3 = datetime(year=2022, month=11, day=1, hour=14, minute=20)

    event1 = calendar_event.CalendarEvent("event1", "eng", date1)
    event2 = calendar_event.CalendarEvent("event2", "fiz", date2)
    event3 = calendar_event.CalendarEvent("event3", "elc", date3)

    org_events = [event1, event2, event3]
    
    calendar_event.saveEvents(org_events, TEST_EVENTS_FILE)
    loaded_events = calendar_event.loadEvents(TEST_EVENTS_FILE)

    if len(org_events) != len(loaded_events):
        print("CALENDAR EVENT SERIALISATION TEST FAILED")

    for i in range(len(org_events)):

        if org_events[i] != loaded_events[i]:
            print("CALENDAR EVENT SERIALISATION TEST FAILED")

    print("CALENDAR EVENT SERIALISATION TEST PASSED")
