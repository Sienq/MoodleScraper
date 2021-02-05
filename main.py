
import calendar_source_downloader
from get_cridentials import getCridentials
import tests

CRIDENTIALS_FILE = "cridentials.txt"
EVENTS_FILE = "events.json"

if __name__ == "__main__":

    tests.calendaSourceDownladTest()
    tests.calendarEventSerialisationTest()