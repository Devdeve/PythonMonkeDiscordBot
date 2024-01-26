import discord
from discord.ext import commands

# generic emotes used
FlinkerMirror = "<:FlinkerMirror:625448790932979725>"
monkePog = "<:monkePog:818852117409955882>"
monke = "<:monke:726507355029897216>"
monkeggenosse = "<:monkeggenosse:802488703897436160>"
monkesalute = "<:monkesalute:802487166869176330>"

async def postFunkyMonkeyFriday(ctx):
	await ctx.send(f"{FlinkerMirror} {monkePog} {monke} {monkeggenosse} {monkePog} {monkesalute} {monkePog} {monkeggenosse} {monke} {monkePog} {FlinkerMirror} {monkePog} {monke} {monkeggenosse} {monkePog} {monkesalute} {monkePog} {monkeggenosse} {monke} {monkePog} {FlinkerMirror}")
	await ctx.send(f"{monkePog} {monkePog} {monkePog} {monkePog} {monkePog} ITS FUNKY MONKEY FRIDAY {monkePog} {monkePog} {monkePog} {monkePog} {monkePog}")
	await ctx.send("https://cdn.discordapp.com/attachments/555708248519344159/822418848216121424/cooling_off.webm https://cdn.discordapp.com/attachments/555708248519344159/835065295089303572/image0-9.jpg https://cdn.discordapp.com/attachments/555708248519344159/817324459933302784/fonky_monky_friday_1.mp4 https://cdn.discordapp.com/attachments/555708248519344159/817324659149635605/funky-monkey-friday-4k-remaster.mp4 https://cdn.discordapp.com/attachments/722811898919125083/912898503213199421/MonkeTime.mov")
	await ctx.send("https://cdn.discordapp.com/attachments/555708248519344159/822419168677593098/RsXgyHyG-Q_7L4fc.mp4 https://cdn.discordapp.com/attachments/555708248519344159/824927029815279616/chillin.webm . https://tenor.com/view/monkey-gif-18612587 https://tenor.com/view/monke-monkey-friday-gif-20298992")
	await ctx.send(f"{FlinkerMirror} {monkePog} {monke} {monkeggenosse} {monkePog} {monkesalute} {monkePog} {monkeggenosse} {monke} {monkePog} {FlinkerMirror} {monkePog} {monke} {monkeggenosse} {monkePog} {monkesalute} {monkePog} {monkeggenosse} {monke} {monkePog} {FlinkerMirror}")


class FMFCog(commands.Cog, name="Funky Monkey Friday Cog"):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name = "fmf",description = "its Funky Monkey Friday")
    async def fmf(self, ctx):
        await postFunkyMonkeyFriday(ctx)


async def setup(bot:commands.Bot):
    await bot.add_cog(FMFCog(bot))