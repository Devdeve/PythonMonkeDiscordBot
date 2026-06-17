import discord
from discord.ext import commands

class MondayCog(commands.Cog, name="Monday Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "monday",description = "its monday")
    async def monday(self, ctx):
        print("Monday command called")
        file = discord.File(f"./days/monday.png")
        await ctx.send(file=file)
    
    @commands.hybrid_command(name = "old_monday",description = "its monday")
    async def old_monday(self, ctx):
        print("Old Monday command called")
        file = discord.File(f"./days/old_monday.png")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(MondayCog(bot))