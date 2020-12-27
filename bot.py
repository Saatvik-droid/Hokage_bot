import discord
import os
import dotenv

from discord.ext import commands
from datetime import datetime
from dotenv.main import load_dotenv

"""
    Loads environment variables from .env.
    Initializes TOKEN as bot token.
"""
load_dotenv()
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    """
        Sends a message in terminal with start time.
        Primary use is just for logging.
    """
    launch_time = datetime.now()
    print(f"Started at {launch_time}")

# maintaining cogs


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


<<<<<<< HEAD
@bot.command()
async def unload(ctx, extension):
    bot.unload_exntension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


# ping it and it returns your latency
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
=======
@bot.command(hidden=True)
@commands.is_owner()
async def reload(ctx, cog=None):
    """
        Hot reloading of cogs.
    """
    if cog is None:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
                bot.load_extension(f'cogs.{filename[:-3]}')
                cog1 = 'all cogs'

    else:
        bot.unload_extension(f'cogs.{cog}')
        bot.load_extension(f'cogs.{cog}')
        cog1 = f'cog `{cog}`'

    await ctx.send(f"Successfully reloaded {cog}")


"""
    Loads cogs from ./cogs directory.
    Make sure your file name starts with '_' if you dont want it to load just yet. 
"""
for cog in os.listdir(r"./cogs"):
    if cog.endswith(".py") and not cog.startswith("_"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded\n{e}")
>>>>>>> main


bot.run(DISCORD_TOKEN)
