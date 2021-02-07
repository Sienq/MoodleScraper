import os
from sys import prefix
import discord
from discord import message
from dotenv import load_dotenv
import calendarEvent
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connectedn to Discord')

@client.event
async def on_message(message,userID,events):
    user = await client.fetch_user(userID)
    if message.author == client.user:
        return
    if message.content.startswith("!Tasks") and message.author == user:
        for event in events:
            await user.send(event.name + " " + event.course + " " + event.date)
        await asyncio.sleep(10)

async def update(events,userID):
    await client.wait_until_ready()
    user = await client.fetch_user(userID)
    for event in events:
        await user.send("Name : " + event.name + "    " + "Course: " + event.course + "    " + "Date: " + str(event.date))
    await asyncio.sleep(10)

# events = [calendarEvent.CalendarEvent("pierwszy","jakis","25-02-2020"),calendarEvent.CalendarEvent("drugi","jakis","22-02-2020")]
# client.loop.create_task(update(events,302525505783988226))
client.run(TOKEN)
