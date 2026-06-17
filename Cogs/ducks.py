from discord.ext import commands
from Cogs.media import send_fixed_media

class DuckCog(commands.Cog, name="Ducks Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "thursday",description = "its thursday")
    async def thursday(self, ctx):
        print("Thursday command called")
        await send_fixed_media(ctx, "thursday", "./days/duck_thursday.mp4")


async def setup(bot:commands.Bot):
    await bot.add_cog(DuckCog(bot))
