import discord
from discord.ext import commands

from utils import get_env

ascii = """
               __        ___.           __
  ____   _____/  |_  ____\\_ |__   _____/  |_
 /  _ \\_/ ___\\   __\\/  _ \\| __ \\ /  _ \\   __\\
(  <_> )  \\___|  | (  <_> ) \\_\\ (  <_> )  |
 \\____/ \\___  >__|  \\____/|___  /\\____/|__|
            \\/                \\/
"""

bot = commands.Bot(command_prefix="octo", intents=discord.Intents.all())

bot.run(get_env("TOKEN"))
