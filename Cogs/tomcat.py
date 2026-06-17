from discord.ext import commands
from media import send_fixed_media

class TomcatCog(commands.Cog, name="Tomcat Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "tuesday",description = "its tuesday")
    async def tomcat(self, ctx):
        print("Tomcat command called")
        await send_fixed_media(ctx, "tuesday", "./days/Tomcat_Tuesday.mp4")

    @commands.hybrid_command(name = "chewsday",description = "its chewsday")
    async def chewsday(self, ctx):
        print("chewsday command called")
        await send_fixed_media(ctx, "chewsday", "./days/chewsday.mp4")


async def setup(bot:commands.Bot):
    await bot.add_cog(TomcatCog(bot))
