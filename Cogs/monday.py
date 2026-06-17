from discord.ext import commands
from Cogs.media import send_fixed_media

class MondayCog(commands.Cog, name="Monday Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "monday",description = "its monday")
    async def monday(self, ctx):
        print("Monday command called")
        await send_fixed_media(ctx, "monday", "./days/monday.png")
    
    @commands.hybrid_command(name = "old_monday",description = "its monday")
    async def old_monday(self, ctx):
        print("Old Monday command called")
        await send_fixed_media(ctx, "old_monday", "./days/old_monday.png")


async def setup(bot:commands.Bot):
    await bot.add_cog(MondayCog(bot))
