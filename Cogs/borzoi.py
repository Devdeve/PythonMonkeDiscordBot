import discord
from discord.ext import commands
import random
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("./borzoi") if isfile(join("./borzoi", f))]
borzoiImagesList = onlyfiles

class postBorzoiCog(commands.Cog, name="Borzoi cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "borzoi", aliases = ["long","snoopa","longboi","anteater","idoitforyou","nose","skinwalker","schnozer"], description = "borzoi skinwalkers")
    async def borzoi(self, ctx):
        imageNumber = random.randint(0, len(borzoiImagesList))
        BorzoiEvent = random.randint(0,200)
        if (BorzoiEvent == 69):
            i = 0
            while i <= 10:
                borzoiEventBorzoi = random.randint(0,len(borzoiImagesList))
                file = discord.File(f"./borzoi/{borzoiImagesList[borzoiEventBorzoi]}")
                await ctx.send(file=file)
                i += 1
        file = discord.File(f"./borzoi/{borzoiImagesList[imageNumber]}")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(postBorzoiCog(bot))