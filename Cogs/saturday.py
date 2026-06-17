from discord.ext import commands
from Cogs.media import send_fixed_media

class SaturdayCog(commands.Cog, name="Saturday"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "saturday",description = "its Saturday")
    async def saturday(self, ctx):
        print("Saturday command called")
        await send_fixed_media(ctx, "saturday", "./days/saturday.mp4")


async def setup(bot:commands.Bot):
    await bot.add_cog(SaturdayCog(bot))
