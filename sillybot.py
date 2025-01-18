import discord
from discord.ext import commands
import time



 with open('insults.txt', 'r') as file:
    possible_reply = file.readlines()
    possible_reply = [line.strip() for line in possible_reply]  # Remove newline characters


# Define the bot and its command prefix
bot = commands.Bot(command_prefix='!')
intents = discord.Intents.default()
intents.message_content = True

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    while True:
        channel = bot.get_channel(1011428840062582785)  # Replace with your channel ID
        
        members = channel.members
        if members:
            member = random.choice(members)
            await channel.send(f'{member.mention} {random.choice(possible_reply)}')
        await asyncio.sleep(900)  # Sleep for 15 minutes (900 seconds)

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot with the token
with open('token.txt') as f:
    input
bot.run(input)