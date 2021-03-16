# bot.py
import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def hello_world(message):
    if message.author == client.user:
        return
    if message.content.lower() == '.hello':
        await message.channel.send('World!')
        
##Prints out information about the bot and how to use its functions
@client.event
async def ouija_help(message):
    if message.author == client.user:
        return
    if message.content.lower() == '.help':
        await message.channel.send('Info about commands and stuff')

        

client.run(TOKEN)
