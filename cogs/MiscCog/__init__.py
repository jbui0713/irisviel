import random
from discord.ext import commands

class MiscCog(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.guilds = {}

  @commands.command(aliases=['hi', 'hey', 'konnichiwa', 'こんにちは'])
  async def hello(self, ctx):
    guildID = ctx.guild.id
    return await ctx.send("こんにちは！")

