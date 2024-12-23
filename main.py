# discord bot
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
client = commands.Bot(command_prefix = '.', intents = discord.Intents.all())
# on ready
@client.event
async def on_ready():
    # status
    await client.change_presence(activity=discord.Game(name="我成功上線了!!!!"))

# on message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.hello'):
        await message.channel.send('Hello!')
# run
client.run(os.getenv('TOKEN'))