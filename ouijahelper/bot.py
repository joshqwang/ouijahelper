# bot.py
import os

import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#Variables and lists
ouijiProgress = False
promptList = ["Test1","Test2", "Test3"]

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


        
#Gets called automatically whenever a message is sent and is used to call other functions as well as fitting conditional statements
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == '.ouiji':
        await ouiji_start(message)
    elif message.content.lower() == '.end':
        await ouiji_end()      
    elif message.content.lower() == '.help':
        await message.channel.send('Info about commands and stuff')
    
    if await len(message) == 1 && ouijiProgess == True
        await addOuiji(message)
    
    
#Starts the ouiji board with a question
async def ouiji_start(startingChannel):
    randomPrompt = await prompt()
    await startingChannel.channel.send(randomPrompt)
    ouijiProgress = True

    #Gives a random prompt from a list
def prompt():
    newPrompt = promptList[random.randrange(len(promptList))]
    return newPrompt

def addOuiji(letter):
    

async def ouiji_end():
    ouijiProgress = False


    

        

client.run(TOKEN)
