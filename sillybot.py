    import discord
from discord.ext import commands, tasks
import random
import asyncio

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to read message content

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Read possible replies from insults.txt
with open('insults.txt', 'r') as file:
    possible_reply = file.readlines()
    possible_reply = [line.strip() for line in possible_reply]  # Remove newline characters

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


def sendmessage():
    channel = bot.get_channel(1011428840062582785)  # Replace with your channel ID
    return f'{random.choice(possible_reply)}'

def senddual():
    

@bot.command()
async def insult(ctx):
    await ctx.send(sendmessage(), reference=ctx.message)

#dual
@bot.command()



# Run the bot with the token
with open('token.txt') as f:
    token = f.read().strip()  # Read the token correctly
bot.run(token)

