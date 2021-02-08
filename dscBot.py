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
from userslist import loadUserList, getUserWithID


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
DATE_FORMAT = '%Y-%m-%d %H:%M'


USERS_FILE = None


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):

    author = message.author
    if author == client.user:
        return
    
    user_id = author.name
    users = loadUserList(USERS_FILE)
    user = getUserWithID(users, user_id)

    if message.content.startswith("!Tasks") and user != None:
        
        events = calendarEvent.loadEvents(user['events_file_name'])
        await author.send("Oooo CHOOLLEEERRRA")
        await author.send(file = discord.File('qLjgGQ3ZCSVhT0D1veRSpFwk-2019-07-04 20_46_56.gif'))
        for event in events:
            await author.send(event.name + " " + event.course + " " + str(event.date))
       
        await asyncio.sleep(10)


async def update(events,userID):
    await client.wait_until_ready()
    user = await client.fetch_user(userID)
    print(user)
    for event in events:
        await user.send("Name : " + event.name + "    " + "Course: " + event.course + "    " + "Date: " + str(event.date))
    await asyncio.sleep(10)

if __name__ == "__main__":

    USERS_FILE = argv[1]
    client.run(TOKEN)

