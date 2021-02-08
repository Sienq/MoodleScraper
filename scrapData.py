from bs4 import BeautifulSoup
import datetime
import calendarEvent
import calendarSourceDownloader
import getCredentials


def formatDate(mystr):

    today = datetime.datetime.today()
    today = today.replace(second=0, microsecond=0)

    splitted = mystr.split(',')
    if(splitted[0] == "Dziś"):
        today = today.replace(hour = int(splitted[1][1:3]),minute = int(splitted[1][4:6]))
        return today
    elif(splitted[0] == "Jutro"):
        tommorow = today + datetime.timedelta(days = 1)
        tommorow= tommorow.replace(hour = int(splitted[1][1:3]),minute = int(splitted[1][4:6]))
        return tommorow
    else:
        dayMonth = splitted[1].split(".")
        taskDate = datetime.datetime(year = today.year, month = int(dayMonth[1]),day = int(dayMonth[0]), hour = int(splitted[2][1:3]),minute = int(splitted[2][4:6]))
        return taskDate



def scrap(cridentials):

    text = calendarSourceDownloader.getEventsPageSource(cridentials)
    html_soup = BeautifulSoup(text, 'html.parser')
    quiz_container = html_soup.findAll('div',attrs={"data-event-component" : ["mod_quiz","mod_assign"]})
    first = quiz_container[0]
    first = first.div.find('div',class_ = "col-11")

    events = []

    for element in quiz_container:

        name = element.div.h3.text
        dateSub = element.div.findAll('div',class_="col-11")
        dateOfTask = formatDate(dateSub[0].text)
        subject = dateSub[2].text
        event = calendarEvent.CalendarEvent(name,subject,dateOfTask)
        events.append(event)

    return events
