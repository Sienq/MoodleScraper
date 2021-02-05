
import sendMail
import calendarEvent
import scrapData

def calculateNewEvents(old_events, new_events):

    diff = []

    for event in new_events:

        if event not in old_events:
            diff.append(event)
    
    return diff

def checkNewEventsAndNotifyUser(credentials, user_file, user_email):

    old_events = calendarEvent.loadEvents(user_file)
    current_events = scrapData.scrap(credentials)
    calendarEvent.saveEvents(current_events, user_file)

    new_events = calculateNewEvents(old_events, current_events)

    if new_events != []:
        sendMail.email(new_events, user_email)