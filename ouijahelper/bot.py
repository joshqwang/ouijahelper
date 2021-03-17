# bot.py
import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


        
#Gets called automatically whenever a message is sent and is used to call other functions
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == '.ouiji':
        ouiji_start()
    if message.content.lower() == '.help':
        await message.channel.send('Info about commands and stuff')
    elif message.content.lower() == 'hello':
        await message.channel.send('World!')
  
#Starts the ouiji board with a question
def ouiji_start():
    randomPrompt = prompt()
    await message.channel.send(randomPrompt)

def prompt():
    return 'yeetus beetus'

        

client.run(TOKEN)
