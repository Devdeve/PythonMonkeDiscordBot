import discord
from discord.ext import commands

class SquidCog(commands.Cog, name="Squid Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "sunday",description = "its squid sunday")
    async def squid(self, ctx):
        print("Squid command called")
        file = discord.File(f"./days/squid_sunday.mp4")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(SquidCog(bot))