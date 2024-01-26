import discord
from discord.ext import commands
import random
from os import listdir
from os.path import isfile, join

# generic emotes used
FlinkerMirror = "<:FlinkerMirror:625448790932979725>"
monkePog = "<:monkePog:818852117409955882>"
monke = "<:monke:726507355029897216>"
monkeggenosse = "<:monkeggenosse:802488703897436160>"
monkesalute = "<:monkesalute:802487166869176330>"

onlyfiles = [f for f in listdir("./monkeys") if isfile(join("./monkeys", f))]
monkeyImagesList = onlyfiles

class postMonkeyCog(commands.Cog, name="Monke cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "monkey",aliases = ["monki", "monke", "ape", "gorilla", "monkei", "chimp"], description = "mmm monke")
    async def monkey(self, ctx):
        imageNumber = random.randint(0, len(monkeyImagesList))
        ChimpEvent = random.randint(0,200)
        if (ChimpEvent == 69):
            await ctx.send(f"{monkePog} {monkePog} {monkePog} {monkePog} {monkePog} RANDOM CHIMP EVENT {monkePog} {monkePog} {monkePog} {monkePog} {monkePog}")
            i = 0
            while i <= 10:
                chimpEventMonkey = random.randint(0,len(monkeyImagesList))
                file = discord.File(f"./monkeys/{monkeyImagesList[chimpEventMonkey]}")
                await ctx.send(file=file)
                i += 1
        file = discord.File(f"./monkeys/{monkeyImagesList[imageNumber]}")
        await ctx.send(file=file)


async def setup(bot:commands.Bot):
    await bot.add_cog(postMonkeyCog(bot))