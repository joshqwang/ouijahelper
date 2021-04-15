# bot.py
import os

import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#Variables and lists
ouijiProgress = False
promptList = ["What is the objectively best movie?","What is the meaning of life?", "Who in this server is the most likely to trip on their own foot?", "What was the first thing you did this morning?", "Who in this server is the most likely to be in bed right now?", "What will the weather tomorrow be like?", "What would you wait in line for a really long time for?"]
letterList = []
randomPrompt = ""
customOuiji = False
customPrompt = ""
ouijiChannel = ""

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


        
#Gets called automatically whenever a message is sent and is used to call other functions as well as fitting conditional statements
@client.event
async def on_message(message):
    global letterList
    global customOuiji
    global customPrompt
    global ouijiProgress
    global ouijiChannel
    
    if message.author == client.user:
        return
    
    if message.content.lower() == '.ouiji':
        ouijiChannel = message.channel
        letterList = []
        await ouiji_start(message)
    elif message.content.lower() == '.ouijiend' or message.content.lower() == 'goodbye':
        if message.channel == ouijiChannel:
            await ouiji_end(message)      
    elif message.content.lower() == '.ouijihelp':
        await message.channel.send('Commands: .ouiji: Starts the ouiji board   .ouijiEnd: Ends the ouiji board .customOuiji: Lets the next message sent become the prompt usesRules: Only accepts one letter at a time, use - as spaces if needed. Users string these letters to make words to find a funny or unexpected answer to the prompt given')
    elif message.content.lower() == '.ouijicustom': 
        ouijiChannel = message.channel
        letterList = []
        customOuiji = True
        await message.channel.send('What prompt would you like to have?')
    elif len(message.content) == 1 and ouijiProgress == True and message.channel == ouijiChannel:
        await message.add_reaction('\N{THUMBS UP SIGN}')
        addOuiji(message)
    elif customOuiji == True and message.channel == ouijiChannel and ouijiProgress == False:
        customPrompt = message.content
        await message.add_reaction('\N{THUMBS UP SIGN}')
        await custom_start(message)
        
    
#Starts the ouiji board with a question determined by the function 'prompt'
async def ouiji_start(startingChannel):
    global ouijiProgress
    global randomPrompt
    randomPrompt = prompt()
    await startingChannel.channel.send(randomPrompt)
    ouijiProgress = True

#Gives a custom prompt based upon a user's input
async def custom_start(customChannel):
    global ouijiProgress
    global customPrompt
    await customChannel.channel.send(customPrompt)
    ouijiProgress = True

#Gives a random prompt from a list
def prompt():
    global promptList
    newPrompt = promptList[random.randrange(len(promptList))]
    return newPrompt

#Adds a letter or symbol to the Ouiji board determined by user input
def addOuiji(letter):
    global letterList
    if letter != '-':
        letterList.append(letter)
    else:
        letterList.append(" ")
    
#Ends the ouiji as well as sending what the overall message was and stuff
async def ouiji_end(startingChannel):
    global ouijiProgress
    ouijiProgress = False
    global randomPrompt
    global customOuiji
    global customPrompt
    global letterList
    convertedLetterList = ""
    for element in letterList:
        convertedLetterList += element.content
    if customOuiji == False:
        await startingChannel.channel.send(randomPrompt + ' The spirits say: ' +  convertedLetterList)
    else:
        await startingChannel.channel.send(customPrompt + ' The spirits say: ' +  convertedLetterList)
        customOuiji = False


    

        

client.run(TOKEN)
