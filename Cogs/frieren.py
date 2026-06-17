from discord.ext import commands
from Cogs.media import send_fixed_media

class FrierenCog(commands.Cog, name="Frieren Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "frieren", description = "its Frieren Friday")
    async def frierenFriday(self, ctx):
        print("Frieren Friday Command")
        await ctx.send("It's Frieren Friday")
        await send_fixed_media(ctx, "frieren", "./days/frieren.png")


async def setup(bot:commands.Bot):
    await bot.add_cog(FrierenCog(bot))
