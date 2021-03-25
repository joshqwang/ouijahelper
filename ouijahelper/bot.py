# bot.py
import os

import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#Variables and lists
ouijiProgress = False
promptList = ["Test1","Test2", "Test3"]
letterList = []
randomPrompt = "Test17"

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
        await ouiji_end(message)      
    elif message.content.lower() == '.help':
        await message.channel.send('Info about commands and stuff')
    
    if len(message.content) == 1 and ouijiProgress == True:
        await message.add_reaction(":ghost:message.id")
        addOuiji(message)
    
    
#Starts the ouiji board with a question determined by the function 'prompt'
async def ouiji_start(startingChannel):
    global ouijiProgress
    global randomPrompt
    randomPrompt = prompt()
    await startingChannel.channel.send(randomPrompt)
    ouijiProgress = True

#Gives a random prompt from a list
def prompt():
    global promptList
    newPrompt = promptList[random.randrange(len(promptList))]
    return newPrompt

#Adds a letter or symbol to the Ouiji board determined by user input
def addOuiji(letter):
    global letterList
    letterList.append(letter)
    
#Ends the ouiji as well as sending what the overall message was 
async def ouiji_end(startingChannel):
    global ouijiProgress
    ouijiProgress = False
    global randomPrompt
    global letterList
    convertedLetterList = ""
    for element in letterList:
        convertedLetterList += element.content
    
    await startingChannel.channel.send(randomPrompt + 'The spirits say: ' +  convertedLetterList)


    

        

client.run(TOKEN)
