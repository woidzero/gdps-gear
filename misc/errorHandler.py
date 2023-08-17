"""
GDPSGear
~~~~~~~~~~~~~~~~~~~
Discord bot for managing Geometry Dash IOCore based private servers

:copyright: (c) 2023 woidzero
:license: MIT, see LICENSE for more details.
"""
import discord
from discord.ext import commands


def handle(error: discord.DiscordException) -> str | type[str]:
    message = str

    if isinstance(error, commands.InvalidEndOfQuotedStringError):
        message = "`[error] Invalid end of quoted string.`"
    elif isinstance(error, commands.NSFWChannelRequired):
        message = "`[error] NSFW Required.`"
    elif isinstance(error, commands.CheckFailure):
        message = "`[error] Check failure.`"
    elif isinstance(error, commands.CommandRegistrationError):
        message = "`[error] Command cannot been registered.`"

    elif isinstance(error, commands.MissingPermissions):
        message = "`[error] You don't have required permissions.`"
    elif isinstance(error, commands.BotMissingPermissions):
        message = "`[error] Bot missing permissions.`"

    elif isinstance(error, commands.BadArgument):
        message = "`[error] Bad argument provided.`"
    elif isinstance(error, commands.MissingRequiredArgument):
        message = "`[error] Missing required argument.`"
    elif isinstance(error, commands.BadUnionArgument):
        message = "`[error] Bad union argument.`"
    elif isinstance(error, commands.ArgumentParsingError):
        message = "`[error] Invalid end of quoted string.`"

    elif isinstance(error, commands.CommandOnCooldown):
        message = f"`[error] This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.`"
    elif isinstance(error, commands.CommandNotFound):
        message = "`[error] Command not found.`"
    elif isinstance(error, commands.PrivateMessageOnly):
        message = "`[error] This commands used only in private messages.`"
    elif isinstance(error, commands.NoPrivateMessage):
        message = "`[error] This commands used only in guilds.`"
    elif isinstance(error, commands.NotOwner):
        message = "`[error] Your'e not a bot owner.`"

    elif isinstance(error, discord.ExtensionNotLoaded):
        message = "`[error] Extension not loaded.`"
    elif isinstance(error, discord.ExtensionError):
        message = "`[error] Extension error.`"
    elif isinstance(error, discord.ExtensionNotFound):
        message = "`[error] Extension not found.`"

    return message
