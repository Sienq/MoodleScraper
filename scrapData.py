from bs4 import BeautifulSoup
import datetime
import calendar_event
import calendar_source_downloader
import get_credentials

def formatDate(mystr):
    
    today = datetime.datetime.today()
    splitted = mystr.split(',')
    dayMonth = splitted[1].split(".")
    taskDate = datetime.datetime(year = today.year, month = int(dayMonth[1]),day = int(dayMonth[0]), hour = int(splitted[2][1:3]),minute = int(splitted[2][4:6]))
    return taskDate



def scrap(cridentials):

    text = calendar_source_downloader.getEventsPageSource(cridentials)
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
        event = calendar_event.CalendarEvent(name,subject,dateOfTask)
        events.append(event)

    return events


