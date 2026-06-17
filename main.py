import asyncio
import discord
from discord.ext import commands
import json
import os

def get_config():
    data = {}
    if os.path.exists("configuration.json"):
        with open("configuration.json", "r") as config:
            data = json.load(config)

    token = os.environ.get("DISCORD_TOKEN") or data.get("token")
    prefix = os.environ.get("DISCORD_PREFIX") or data.get("prefix", "!")
    owner_id = int(os.environ.get("DISCORD_OWNER_ID") or data.get("owner_id", 0))

    if not token:
        raise RuntimeError("Set DISCORD_TOKEN or add token to configuration.json")

    return token, prefix, owner_id

token, prefix, owner_id = get_config()

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# The bot
bot = commands.Bot(command_prefix=prefix, intents = intents, owner_id = owner_id)
client = bot

# cogs
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="monkeys"))
    print('Logged in as {0.user}'.format(client))    # Lets you know when the bot is online
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.command(name='load', description='Loads the given cog')
async def load(ctx:commands.Context, extension: str):
    await client.load_extension(f"Cogs.{extension}")
    await ctx.send(f"Loaded {extension}.")
    print(f"Loaded {extension}.py")

@client.command(name='unload', description='Unloads the given cog')
async def unload(ctx:commands.Context, extension: str):
    await client.unload_extension(f"Cogs.{extension}")
    await ctx.send(f"Unloaded {extension}.")
    print(f"Unloaded {extension}.py")

@client.command(name='reload', description='Re-loads the given cog')
async def reload(ctx:commands.Context, extension: str):
    await client.reload_extension(f"Cogs.{extension}")
    await ctx.send(f"Re-loaded {extension}.")
    print(f"Re-loaded {extension}.py")

async def load_extensions():
    for filename in os.listdir("./Cogs"):
        print(f"loading cog {filename}")
        if filename.endswith(".py"):
            await client.load_extension(f"Cogs.{filename[:-3]}")


@bot.hybrid_command(name = "sync")
async def sync(ctx):
    if ctx.author.id == owner_id:
        await bot.tree.sync()
        print('Command tree synced.')
    else:
        await ctx.author.response.send_message('You must be the owner to use this command!')

async def main():
    async with client:
        await load_extensions()
        await client.start(token)

asyncio.run(main())
