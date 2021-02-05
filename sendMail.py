import smtplib
import scrapData
import get_credentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    subject = "NEW ASSIGNMENT"

    body = ""
    for event in events:
        body = body + "Course: " + event.course +"    Name: " + event.name + "    Deadline: " + str(event.date) + "\n"

    msg.attach(MIMEText(body,'plain'))
    emailText = msg.as_string()    
    server.sendmail(sender, address, emailText)
    server.quit()

