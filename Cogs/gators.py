from discord.ext import commands
from media import send_fixed_media

class FlatFuckFridayCog(commands.Cog, name="Flat Fuck Friday Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "fff",description = "its Flat Fuck Friday")
    async def flatFuckFriday(self, ctx):
        print("Flat Fuck Friday command called")
        await send_fixed_media(ctx, "fff", "./gator/FFF.mp4")

    @commands.hybrid_command(name = "ffc",description = "its Flat Fuck Christmas")
    async def flatFuckChristmas(self, ctx):
        print("Flat Fuck Christmas command called")
        await send_fixed_media(ctx, "ffc", "./gator/flat_fuck_christmas.mov")


async def setup(bot:commands.Bot):
    await bot.add_cog(FlatFuckFridayCog(bot))
