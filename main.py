# discord bot
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
client = commands.Bot(command_prefix = '.', intents = discord.Intents.all())
# run
client.run(os.getenv('TOKEN'))