import os
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
async def on_message(message):
    channel = client.get_channel(807332645137547274)
    if message == "on jest olkoholik":
        await channel.send("Ja nie zaden olkoholik, ja podatki place")
        

async def update(events):
    await client.wait_until_ready()
    msg_sent = False
    channel = client.get_channel(807332645137547274)
    for event in events:
        await channel.send("Name : " + event.name + "    " + "Course: " + event.course + "    " + "Date: " + str(event.date))
    await asyncio.sleep(10)
events = calendarEvent.loadEvents("events.json")
client.loop.create_task(update(events))
client.run(TOKEN)

# channel = client.get_channel('807332645137547274')
# await channel.send('hello')