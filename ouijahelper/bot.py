# bot.py
import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#Variables and lists
ouijiProgress = False
promptList = ["Test1","Test2", "Test3"]

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
    elif message.content.lower() == '.end':
        ouiji_end()
        
    if message.content.lower() == '.help':
        await message.channel.send('Info about commands and stuff')
    elif message.content.lower() == 'hello':
        await message.channel.send('World!')
  
#Starts the ouiji board with a question
def ouiji_start():
    randomPrompt = prompt()
    message.channel.send(randomPrompt)
    ouijiProgress = True

def prompt():
    newPrompt = promptList[random.randrange(len(promptList))]
    return newPrompt

def ouiji_end():
    ouijiProgress = False


    

        

client.run(TOKEN)
