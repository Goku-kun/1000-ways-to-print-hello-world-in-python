import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
  print('Hello world')
  
bot.run("Your discord bot token here")
