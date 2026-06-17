from discord.ext import commands
from media import send_fixed_media

class WednesdayCog(commands.Cog, name="Wednesday Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "wednesday",description = "its wednesday")
    async def wednesday(self, ctx):
        print("Wednesday command called")
        await send_fixed_media(ctx, "wednesday", "./days/wednesday.mp4")


async def setup(bot:commands.Bot):
    await bot.add_cog(WednesdayCog(bot))
