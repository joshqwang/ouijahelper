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


#The function "on_message" automatically gets called whenever a message gets sent by a user. The class "message" in discord is the input type of the variable message.
#The output of this function is dependent on the message but most results call a function

@client.event
async def on_message(message):
    global letterList
    global customOuiji
    global customPrompt
    global ouijiProgress
    global ouijiChannel
    
    if message.author == client.user:
        return
    
    if message.content.lower() == '.ouiji' and ouijiProgress == False and customOuiji == False:
        ouijiChannel = message.channel
        letterList = []
        await ouiji_start(message)
    elif message.content.lower() == '.ouijiend' or message.content.lower() == 'goodbye':
        if message.channel == ouijiChannel:
            await ouiji_end(message)      
    elif message.content.lower() == '.ouijihelp':
        await message.channel.send('Commands: .ouiji: Starts the ouiji board   .ouijiEnd: Ends the ouiji board .customOuiji: Lets the next message sent become the prompt usesRules: Only accepts one letter at a time, use - as spaces if needed. Users string these letters to make words to find a funny or unexpected answer to the prompt given')
    elif message.content.lower() == '.ouijicustom' and ouijiProgress == False: 
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
#The input of the function is the startingChannel which is determined by what channel the message was sent in
#The output of this function is that it starts the ouiji, giving a prompt and making ouijiProgress true.
async def ouiji_start(startingChannel):
    global ouijiProgress
    global randomPrompt
    randomPrompt = prompt()
    await startingChannel.channel.send(randomPrompt)
    ouijiProgress = True

#Gives a custom prompt based upon a user's input
#The output of this function is that it sends the user's message in the channel to signify the program is working 
async def custom_start(customChannel):
    global ouijiProgress
    global customPrompt
    await customChannel.channel.send(customPrompt)
    ouijiProgress = True

#Gives a random prompt from a list
#The output of this function is that random prompt provided 
def prompt():
    global promptList
    newPrompt = promptList[random.randrange(len(promptList))]
    return newPrompt

#Adds a letter or symbol to the Ouiji board determined by user input
#The output of this function is adding on to the list of letters allowing for a correct ouiji
def addOuiji(letter):
    global letterList
    letterList.append(letter)
    
#Ends the ouiji and sends a message giving information about it
#The input of this function is the channel the message was sent in (startingChannel)
#The outputs of this function are that it ends the ouiji (ouijiProgress = false) and sends a message about the ouiji
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
