from discord.ext import commands
import discord
import os
from dotenv import load_dotenv


load_dotenv()
intent=discord.Intents.all()
bot = commands.Bot(command_prefix='gm2!',intents=intent)

bot.run(os.environ["TOKEN"])
