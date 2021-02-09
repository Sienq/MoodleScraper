
import sendMail
import calendarEvent
import scrapData
import datetime
import dscBot
import time
import asyncio


DEADLINE_INTERVAL = datetime.timedelta(hours=60)

def calculateNewEvents(old_events, new_events):

    diff = []

    for event in new_events:

        if event not in old_events:
            diff.append(event)
    
    return diff


def getIntervalIfClose(event):

    now = datetime.datetime.now()
    time_till_deadline = event.date - now

    if time_till_deadline < DEADLINE_INTERVAL and time_till_deadline > datetime.timedelta(hours=1):
           return time_till_deadline
    
    return None


# async def awaitUpdate(new_events, user_id):
#     await dscBot.update(new_events, user_id)

def checkNewEventsAndNotifyUser(credentials, user_file, user_email, user_id):

    old_events = calendarEvent.loadEvents(user_file) # saved ones
    current_events = scrapData.scrap(credentials) # one line ones

    # notify about new events
    new_events = calculateNewEvents(old_events, current_events)
    if new_events != []:

        sendMail.newTasksEmail(new_events, user_email)
        # dscBot.client.loop.run(awaitUpdate(new_events, user_id))
        

    updated_events = old_events + new_events # to save

    # alert about upcoming deadlines
    for i in range(len(updated_events)):
        
        interval = getIntervalIfClose(updated_events[i])
        if interval and updated_events[i].alert_sent == False:

            sendMail.deadlineAlert(updated_events[i], str(interval), user_email)
            updated_events[i].alert_sent = True

    calendarEvent.saveEvents(updated_events, user_file)