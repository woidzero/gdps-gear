"""
GDPSGear
~~~~~~~~~~~~~~~~~~~
Discord bot for managing Geometry Dash IOCore based private servers

:copyright: (c) 2023 woidzero
:license: MIT, see LICENSE for more details.
"""
import os

import discord
from discord.ext import bridge

from misc.config import CONFIG
from misc.errorHandler import handle

bot = bridge.Bot(
    command_prefix=CONFIG["prefix"],
    owner_id=CONFIG["owner_id"],
    activity=discord.Game(name="GDPS"),
)


@bot.event
async def on_command_error(ctx: bridge.Context, error) -> None:
    message = handle(error)
    await ctx.respond(message)


@bot.event
async def on_ready() -> None:
    print(f"Logged in as: {bot.user.name}")


@bot.bridge_command(name="load")
async def load(ctx, ext) -> None:
    bot.load_extension(f"cogs.{ext}")
    await ctx.send(f"`{ext} loaded.`")


@bot.bridge_command(name="unload")
async def unload(ctx, ext) -> None:
    bot.unload_extension(f"cogs.{ext}")
    await ctx.send(f"`{ext} unloaded.`")


@bot.bridge_command(name="reload")
async def reload(ctx, ext) -> None:
    bot.reload_extension(f"cogs.{ext}")
    await ctx.send(f"`{ext} reloaded.`")


for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(CONFIG["token"])
