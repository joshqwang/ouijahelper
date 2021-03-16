# bot.py
import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(testing)
    if message.content.lower() == 'hello':
        await message.channel.send('Yeet!')

client.run(TOKEN)
