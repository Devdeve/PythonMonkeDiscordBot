import discord
from discord.ext import commands

class SaturdayCog(commands.Cog, name="Saturday"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "saturday",description = "its Saturday")
    async def saturday(self, ctx):
        print("Saturday command called")
        file = discord.File(f"./days/saturday.mp4")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(SaturdayCog(bot))