import discord
from discord.ext import commands

class TomcatCog(commands.Cog, name="Tomcat Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "tuesday",description = "its tuesday")
    async def tomcat(self, ctx):
        print("Tomcat command called")
        file = discord.File(f"./days/Tomcat_Tuesday.mp4")
        await ctx.send(file=file)

    @commands.hybrid_command(name = "chewsday",description = "its chewsday")
    async def chewsday(self, ctx):
        print("chewsday command called")
        file = discord.File(f"./days/chewsday.mp4")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(TomcatCog(bot))