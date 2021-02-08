from asyncio import events
import os
from sys import prefix
import discord
from discord import message
from dotenv import load_dotenv
import calendarEvent
import asyncio
import periodicScraper
from sys import argv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
DATE_FORMAT = '%Y-%m-%d %H:%M'


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!Tasks"): #!MESSAGE AUTHOR IN USERLIST
        user = message.author
        print(user)
        events = calendarEvent.loadEvents('hubert_events.json')
        #!LOAD USER TASKS
        await user.send("Oooo CHOLLEEERRA")
        await user.send(file = discord.File('qLjgGQ3ZCSVhT0D1veRSpFwk-2019-07-04 20_46_56.gif'))
        for event in events:
            await user.send(event.name + " " + event.course + " " + str(event.date))
        await asyncio.sleep(10)

async def update(events,userID):
    await client.wait_until_ready()
    user = await client.fetch_user(userID)
    print(user)
    for event in events:
        await user.send("Name : " + event.name + "    " + "Course: " + event.course + "    " + "Date: " + str(event.date))
    await asyncio.sleep(10)

# events = [calendarEvent.CalendarEvent("pierwszy","jakis","25-02-2020"),calendarEvent.CalendarEvent("drugi","jakis","22-02-2020")]
# client.loop.create_task(update(events,302525505783988226))


client.run(TOKEN)
user_list_file_name = argv[1]
users = periodicScraper.loadUserList(user_list_file_name)
    
