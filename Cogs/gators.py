import discord
from discord.ext import commands

class FlatFuckFridayCog(commands.Cog, name="Flat Fuck Friday Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "fff",description = "its Flat Fuck Friday")
    async def flatFuckFriday(self, ctx):
        print("Flat Fuck Friday command called")
        file = discord.File(f"./gator/FFF.mp4")
        await ctx.send(file=file)

    @commands.hybrid_command(name = "ffc",description = "its Flat Fuck Christmas")
    async def flatFuckChristmas(self, ctx):
        print("Flat Fuck Christmas command called")
        file = discord.File(f"./gator/flat_fuck_christmas.mov")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(FlatFuckFridayCog(bot))