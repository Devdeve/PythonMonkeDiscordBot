from discord.ext import commands
from Cogs.media import send_fixed_media

class SquidCog(commands.Cog, name="Squid Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "sunday",description = "its squid sunday")
    async def squid(self, ctx):
        print("Squid command called")
        await send_fixed_media(ctx, "sunday", "./days/squid_sunday.mp4")


async def setup(bot:commands.Bot):
    await bot.add_cog(SquidCog(bot))
