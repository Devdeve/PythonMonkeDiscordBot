import discord
from discord.ext import commands

class DuckCog(commands.Cog, name="Ducks Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "thursday",description = "its thursday")
    async def thursday(self, ctx):
        print("Thursday command called")
        file = discord.File(f"./days/duck_thursday.mp4")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(DuckCog(bot))