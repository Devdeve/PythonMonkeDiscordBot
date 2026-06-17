from discord.ext import commands
from media import send_fixed_media

# generic emotes used
FlinkerMirror = "<:FlinkerMirror:625448790932979725>"
monkePog = "<:monkePog:818852117409955882>"
monke = "<:monke:726507355029897216>"
monkeggenosse = "<:monkeggenosse:802488703897436160>"
monkesalute = "<:monkesalute:802487166869176330>"

async def postFridayCali(ctx):
    await ctx.send(f"{FlinkerMirror} {monkePog} {monke} {monkeggenosse} {monkePog} {monkesalute} {monkePog} {monkeggenosse} {monke} {monkePog} {FlinkerMirror} {monkePog} {monke} {monkeggenosse} {monkePog} {monkesalute} {monkePog} {monkeggenosse} {monke} {monkePog} {FlinkerMirror}")


class FridayCog(commands.Cog, name="Friday In Cali Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "cali",description = "its Friday")
    async def cali(self, ctx):
        print("Cali command called")
        await send_fixed_media(ctx, "friday_cali", "./days/Today_is_Friday_in_California.mp4")


async def setup(bot:commands.Bot):
    await bot.add_cog(FridayCog(bot))
