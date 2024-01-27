import discord
from discord.ext import commands

class postFoogCog(commands.Cog, name="Foog cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "foog", aliases = ["2st"], description = "lord foog the 2st")
    async def food(self, ctx):
        file = discord.File(f"./foog/foog.mp4")
        await ctx.send(file=file)

async def setup(bot:commands.Bot):
    await bot.add_cog(postFoogCog(bot))