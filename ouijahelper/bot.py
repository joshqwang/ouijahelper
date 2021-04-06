# bot.py
import os

import discord
import random

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

#Variables and lists
ouijiProgress = False
promptList = ["What is the objectively best movie?","What is the meaning of life?", "Who in this server is the most likely to trip on their own foot?"]
letterList = []
randomPrompt = ""
customOuiji = False
customPrompt = ""

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


        
#Gets called automatically whenever a message is sent and is used to call other functions as well as fitting conditional statements
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == '.ouiji':
        letterList = []
        await ouiji_start(message)
    elif message.content.lower() == '.ouijiend':
        await ouiji_end(message)      
    elif message.content.lower() == '.ouijihelp':
        await message.channel.send('Commands: .ouiji: Starts the ouiji board   .ouijiEnd: Ends the ouiji board. Rules: Only accepts one letter at a time, use - as spaces if needed. Users string these letters to make words to find a funny or unexpected answer to the prompt given')
    elif message.content.lower() == '.ouijicustom': 
        letterList = []
        customOuiji = True
        await message.channel.send('What prompt would you like to have?')
    elif len(message.content) == 1 and ouijiProgress == True:
        await message.add_reaction('\N{THUMBS UP SIGN}')
        addOuiji(message)
    elif customOuiji == True:
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
async def custom_start(startingChannel):
    global ouijiProgress
    global customPrompt
    await startingChannel.channel.send(customPrompt)
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
    global customOuiji
    global customPrompt
    global letterList
    convertedLetterList = ""
    for element in letterList:
        convertedLetterList += element.content
    if customOuiji == False:
        await startingChannel.channel.send(randomPrompt + 'The spirits say: ' +  convertedLetterList)
    else:
        await startingChannel.channel.send(customPrompt + 'The spirits say: ' +  convertedLetterList)
        customOuiji = False


    

        

client.run(TOKEN)
