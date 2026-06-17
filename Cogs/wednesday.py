import discord
from discord.ext import commands

class WednesdayCog(commands.Cog, name="Wednesday Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "wednesday",description = "its wednesday")
    async def wednesday(self, ctx):
        print("Wednesday command called")
        file = discord.File(f"./days/wednesday.mp4")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(WednesdayCog(bot))