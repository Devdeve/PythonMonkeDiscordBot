from discord.ext import commands
from media import send_fixed_media

class postFoogCog(commands.Cog, name="Foog cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "foog", aliases = ["2st"], description = "lord foog the 2st")
    async def foog(self, ctx):
        await send_fixed_media(ctx, "foog", "./foog/foog.mp4")

async def setup(bot:commands.Bot):
    await bot.add_cog(postFoogCog(bot))
