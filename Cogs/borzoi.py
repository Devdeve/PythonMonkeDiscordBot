from discord.ext import commands
import random
from Cogs.media import send_random_media

class postBorzoiCog(commands.Cog, name="Borzoi cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "borzoi", aliases = ["long","snoopa","longboi","anteater","idoitforyou","nose","skinwalker","schnozer"], description = "borzoi skinwalkers")
    async def borzoi(self, ctx):
        BorzoiEvent = random.randint(0,200)
        if (BorzoiEvent == 69):
            i = 0
            while i <= 10:
                await send_random_media(ctx, "borzoi", "./borzoi")
                i += 1
        await send_random_media(ctx, "borzoi", "./borzoi")


async def setup(bot:commands.Bot):
    await bot.add_cog(postBorzoiCog(bot))
