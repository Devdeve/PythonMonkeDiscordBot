import discord
from discord.ext import commands

class FrierenCog(commands.Cog, name="Frieren Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "frieren", description = "its Frieren Friday")
    async def frierenFriday(self, ctx):
        print("Frieren Friday Command")
        file = discord.File(f"./days/Frieren.png")
        await ctx.send("It's Frieren Friday")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(FrierenCog(bot))