import discord
from discord.ext import commands

bot = discord.Bot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
  print('Hello world')
  
bot.run("Your discord bot token here")
