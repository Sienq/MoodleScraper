

import calendar_event
import scrap

def calculateNewEvents(old_events, new_events):

    diff = []

    for event in new_events:

        if event not in old_events:
            diff.append(event)
    
    return diff


def email(events, address):
    pass


def checkNewEventsAndNotifyUser(credentials, user_file, user_email):

    old_events = calendar_event.loadEvents(user_file)
    current_events = scrap.scrap(credentials)
    calendar_event.saveEvents(current_events, user_file)

    new_events = calculateNewEvents(old_events, current_events)

    if new_events != []:
        email(new_events, address)