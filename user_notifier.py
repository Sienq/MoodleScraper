
import user_calendar
import get_credentials

def email(events, address):
    pass

def checkNewEventsAndNotifyUser(credentials_file, user_file, user_email):

    credentials = get_credentials.getCredentials(credentials_file)
    new_events = user_calendar.updateEventsAndResolveNew(credentials, user_file)
    email(new_events, address)