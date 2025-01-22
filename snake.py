import discord
import random
import asyncio
import datetime
# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to read message content
number = random.randint(1, 100)

client = discord.Client(intents=intents)

#some global variables
startingdate = datetime.datetime(2022, 12, 25)
jackpots = 0
channel = 1011428840062582785
#list of snake images
sillysnake = [
    "https://cdn.discordapp.com/attachments/1011428840062582785/1279631628070551622/IMG_7709.png?ex=6791abd2&is=67905a52&hm=2bd65bf62ae3737f23a9790a0c665f017b053d7d8da065535e836c0140c878c4&",
"https://cdn.discordapp.com/attachments/1011428840062582785/1330400050378965154/IMG_8924.jpg?ex=6791cb99&is=67907a19&hm=7aa938aaf94b9cbea1f0ba6be2b9cbc8a8e55b6b4bcd87d673d40a24cea21242&",
"https://cdn.discordapp.com/attachments/1011428840062582785/1325652892102688892/IMG_7744.png?ex=6791a9f6&is=67905876&hm=923a610fd40c684336e4a1b933a9e8fc7c273498cc07660af325bcf76d30fa3c&",
"https://cdn.discordapp.com/attachments/1011428840062582785/1330289772404670484/ezgif-6-96646ae2e0.gif?ex=679164e5&is=67901365&hm=4a30d0341fa5948198d578a887c1b12efa3c6004c8ef70b70d139500f0a56f15&",
"https://media.discordapp.net/attachments/1011428840062582785/1288204234332049549/bounce.gif?ex=6791e06f&is=67908eef&hm=669f4813914942d9f338468773ad2b5c81815c6af1e7294b18be6f9b7c92821f&",
"https://cdn.discordapp.com/attachments/1011428840062582785/1298453809747726418/bounce.gif?ex=67919758&is=679045d8&hm=8e3bba0359747997c6c2ed392e260c387820204f503e48c86a25fe1478ba523f&",
"https://tenor.com/view/dimden-dimdem-discord-rules-discord-meme-gif-22604752",
"https://cdn.discordapp.com/attachments/1011428840062582785/1269871020639125565/1269870822101745666remix-1722831243213.png?ex=6791c20c&is=6790708c&hm=e497df52c659cc502309f8a0d9f90ef072b05eef1da54732661fd33f3b8fe69c&",
"https://cdn.discordapp.com/attachments/1150684690412474450/1331549915129839637/fearofsnake.png?ex=679205fe&is=6790b47e&hm=3826a55955a21166299bf365bb4dc7d9484b2c387c1d528f7a0105b260286c3d&"



]

@client.event
async def on_message(message):
    global jackpots  # Declare jackpots as global so we can modify it

    # Avoid bot responding to its own messages
    if message.author == client.user:
        return

    # Randomly check if it's a jackpot event (1 in 500 chance)
    randint = random.randint(1, 500)
    if randint == 1:
        jackpots += 1  # Increment the jackpot counter
        print(f"Jackpot! Current jackpot count: {jackpots}")
        # Send a reply with a random silly snake message
        await message.reply(random.choice(sillysnake), mention_author=True)

    # Check if "test" is in the message content (case-insensitive)
   # if "test" in message.content.lower():
      #  print("Test message received.")
        # Send a random silly snake message
     #   await message.channel.send(random.choice(sillysnake), reference=message)





with open('token.txt') as f:
    token = f.read().strip()  # Read the token correctly
client.run(token)

