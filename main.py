import os
import discord
from discord.ext import commands
from cogs.MiscCog import MiscCog

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix='?')
bot.add_cog(MiscCog(bot))

client = discord.Client()

@client.event
async def on_ready():
  print("アイリスは起きます")

bot.run(TOKEN)