from discord.ext import commands
import random
from media import send_random_media

# generic emotes used
FlinkerMirror = "<:FlinkerMirror:625448790932979725>"
monkePog = "<:monkePog:818852117409955882>"
monke = "<:monke:726507355029897216>"
monkeggenosse = "<:monkeggenosse:802488703897436160>"
monkesalute = "<:monkesalute:802487166869176330>"

class postMonkeyCog(commands.Cog, name="Monke cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "monkey",aliases = ["monki", "monke", "ape", "gorilla", "monkei", "chimp", "bonobo", "monkee", "monk", "baboon", "rasmus"], description = "mmm monke")
    async def monkey(self, ctx):
        print("Monkey command called")
        ChimpEvent = random.randint(0,200)
        if (ChimpEvent == 69):
            print("Chimp event rolled succesfully")
            await ctx.send(f"{monkePog} {monkePog} {monkePog} {monkePog} {monkePog} RANDOM CHIMP EVENT {monkePog} {monkePog} {monkePog} {monkePog} {monkePog}")
            i = 0
            while i <= 10:
                await send_random_media(ctx, "monkeys", "./monkeys")
                i += 1
        await send_random_media(ctx, "monkeys", "./monkeys")


async def setup(bot:commands.Bot):
    await bot.add_cog(postMonkeyCog(bot))
