import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    helpful_tips = [
       
        ' if you are minning dont forget to bring a light source.',
        'If you are going camping dont forget to bring shelter',
        'dont forget a life vest if you are going camping',
        'A common mistake that people make is getting to close to wildlife',
     ]
    if message.content == '!tips':
    #if message.content.startswith('$towel'):
        response = random.choice(helpful_tips)
        await message.channel.send(response)

client.run(TOKEN)