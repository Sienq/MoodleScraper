import smtplib
import scrapData
import get_credentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import calendar_event


def email(events,address):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('moodlemajor@gmail.com','japodatkiplace')

    sender = "MoodleMajor@gmail.com"
    msg = MIMEMultipart()

    msg['From'] = sender
    msg['To'] = address
    msg['Subject'] = "NEW ASSIGNMENT"

    body = ""
    for event in events:
        body = body + "Course: " + event.course +"    Name: " + event.name + "    Deadline: " + str(event.date) + "\n"

    msg.attach(MIMEText(body,'plain'))
    emailText = msg.as_string()    
    server.sendmail(sender, address, emailText)
    server.quit()

def alert(event,timeleft,address):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('moodlemajor@gmail.com','japodatkiplace')
    sender = "MoodleMajor@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = address
    msg['Subject'] = "24H ALERT"
    body = "Time left for: " + event.name + " is " + timeleft
    msg.attach(MIMEText(body,'plain')) 

    emailText = msg.as_string()    
    server.sendmail(sender, address, emailText)
    server.quit()

def checkTime(address):
    print("siema")
    now = datetime.datetime.now()
    events = calendar_event.loadEvents('events.json')
    for event in events:
        if event.date - now < datetime.timedelta(hours=24):
            alert(event,str(event.date-now),address)        

